# region imports
import logging
import pytest
import requests
import json
import functools

''' Notes Ch24 Internet APIs
Meta
1. Need better handling of json
24.6.2
1. Because of auto-redirection, the efficiency of the call is impacted without knowing.
   This is potentially a performance problem, although hidden.
   Can mountebank can be used to detect and alert on this
2.Explanation does not cover the case of encryption bec sometimes we don't want to expose the parameters of the api
24.7 requests_with_caching
1. This module cannot be run outside Runestone environment
2. Sample code is good for study
3. File datamuse_cache.txt
24.9 Debugging calls to requests.get()
     makes distinction between Runestone and full python environment
     requestURL wrapper to return url shoudl things go wrong

24.13 unicode for non-english charactesr
    In Py3, all strings are unicode.
    Unicode is 1 to 4 bytes per symbol
    UTF-8
    content-type == application/json; charset=utf8
    string(s).encode('utf8') before writing string to file
'''
# from  pytest_mock import mocker
# endregion imports
# region globals
logger = logging.getLogger(__name__)
flickr_key = '464b86270211da70af8a940c0ed6c219'
# endregion globals
# region helpers
def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {}
    params_diction["rel_rhy"] = word
    params_diction["max"] = 3
    resp = requests.get(baseurl, params=params_diction)
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    # flickr_resp = requests_with_caching.get(baseurl, params = params_diction, permanent_cache_file="flickr_cache.txt")
    flickr_resp = requests.get(baseurl, params = params_diction)
    # Useful for debugging: print the url! Uncomment the below line to do so.
    # Add a assert check here
    assert flickr_resp.status_code == 200
    logger.info("get_flickr_data: url == {}".format(flickr_resp.url)) # Paste the result into the browser to check it out...
    return flickr_resp.json()

def extract_movie_titles(dic):
    return [d['Name'] for d in dic['Similar']['Results']]

def get_movies_from_tastedive(query, qtype, baseUrl='https://tastedive.com/api/similar', infonum=1, limit=5, key='382398-test-ZF54VD42' ):
    """
    The API is described in https://tastedive.com/read/api
    Adding a / at the end will cause "page not found" error

    Parameters
    - q: the search query; consists of a series (at least one) of bands, movies, TV shows, podcasts, books, authors and/or games, separated by commas. Sometimes it is useful to specify the type of a certain resource in the query (e.g. if a movie and a book share the same title). You can do this by using the "band:", "movie:", "show:", "podcast:", "book:", "author:" or "game:" operators, for example: "band:underworld, movie:harry potter, book:trainspotting". Don't forget to encode this parameter.
    - type: query type, specifies the desired type of results. It can be one of the following: music, movies, shows, podcasts, books, authors, games. If not specified, the results can have mixed types.
    - info: when set to 1, additional information is provided for the recommended items, like a description and a related Youtube clip (when available). Default is 0.
    - limit: maximum number of recommendations to retrieve. Default is 20.
    - k: Your API access key.
    - callback: add when using JSONP, to specify the callback function.

    This is the full rest calling function to encapsulate the api/similar endpoint with defaults for
    info, limit, key values
    """
    kval_pairs = {
        'info' : infonum, 'limit': limit, 'k': key,
        'q' : query, 'type': qtype
    }
    response = requests.get(baseUrl, params=kval_pairs)
    # response_map = response.json()
    # return [d['Name'] for d in response_map['Similar']['Results'] if d['Type'] == 'movie']
    return json.loads(response.text)

def get_movies_test_helper(artistOrMovie, qtype):
    ml = get_movies_from_tastedive(artistOrMovie, qtype)
    logger.info("len={}".format(len(ml)))
    for m in ml:
       logger.info(m)
    return ml

def get_related_titles(listOfMovies):
    setOfMovies = set()
    for movie in listOfMovies:
        extractedListTitles = extract_movie_titles(get_movies_from_tastedive(movie, "movies"))
        logger.info("{} => {}".format(movie, extractedListTitles))
        setOfMovies = setOfMovies.union(set(extractedListTitles))
    return list(setOfMovies)

def get_movie_from_omdb_by_title(title, mtype = "movie", baseUrl = "http://www.omdbapi.com", plottype = "short", returntype = "json", apiversion = "1", key = "4fc978d"):
    kval_pairs = {'t' : title, 'type' : mtype, 'plot' : plottype, 'r': returntype, 'v': apiversion, 'apikey' : key}
    response = requests.get(baseUrl, params=kval_pairs)
    return json.loads(response.text)

def get_movie_data(movieTitle):
    return get_movie_from_omdb_by_title(movieTitle)

def get_movie_rating(movieDb):
    # Is there a simpler way using json filtering?
    rList = movieDb["Ratings"]
    rating = 0
    for r in rList:
        if r["Source"] == 'Rotten Tomatoes':
            rating = float(r["Value"].strip('%'))/100
            break
    return rating

def movieCmp(a,b):
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    else:
        if a[0] < b[0]:
            return -1
        if a[0] > b[0]:
            return 1
        else:
            return 0

def get_sorted_recommendations(listOfMovies):
    mList = get_related_titles(listOfMovies)
    movieRatings = {}
    for m in mList:
        r = get_movie_rating(get_movie_data(m))
        movieRatings[m] = r
    logger.info("movieRatings: {}".format(movieRatings))
    # sortedRecommendations = sorted(movieRatings.items(), key = lambda item: item[1], reverse = True)
    sortedRecommendations = sorted(movieRatings.items(), key = functools.cmp_to_key(movieCmp), reverse = True)
    return [item[0] for item in sortedRecommendations]

# endregion helpers
# region tests for xx.x
def test_2461_get(): # 24.6.1
    response = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
    logger.info("type of response: {}".format(type(response)))
    logger.info("first 50 chars: {}".format(response.text[:50])) # logger.info, 50 chars is sufficient for inspection
    logger.info("url: {}".format(response.url)) # logger.info the url that was fetched

    x = response.json() # turn page.text into a python object
    logger.info("type of x returned from page.json(): {}".format(type(x)))
    firstItem = x[0]
    logger.info("--- first item in list: {}".format(x[0]))
    efirstItem = {'word': 'money', 'score': 4415, 'numSyllables': 2}
    assert firstItem == efirstItem

    numItems = len(x)
    assert numItems == 84
    # final dump just to view, not to validate
    # logger.info("---the whole list, pretty logger.infoed---")
    # logger.info(json.dumps(x, indent=2)) # pretty logger.info the results

def test_2463_get(): # 24.6.3

    kval_pairs = {'rel_rhy': 'funny'}
    page = requests.get("https://api.datamuse.com/words", params=kval_pairs)
    # Above equivalent to 
    # page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")

    logger.info(page.text[:150]) # print the first 150 characters
    logger.info(page.url) # print the url that was fetched
    eurl = "https://api.datamuse.com/words?rel_rhy=funny"
    assert eurl == page.url    

'''
pytest.mark.skip(reason="No module called requests_with_caching")
def test_2471_requests_with_caching():
    import requests_with_caching
    # it's not found in the permanent cache
    res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
    print(res.text[:100])
    # this time it will be found in the temporary cache
    res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=happy", permanent_cache_file="datamuse_cache.txt")
    # This one is in the permanent cache.
    res = requests_with_caching.get("https://api.datamuse.com/words?rel_rhy=funny", permanent_cache_file="datamuse_cache.txt")
'''

def test_2482_test_get_rhymes(): # 24.8.2
    rhymes = get_rhymes("funny")
    erhymes = ['money', 'honey', 'sunny']
    assert erhymes == rhymes

def test_2411_itunes(): # 24.11
    baseurl = "https://itunes.apple.com/search"
    parameters={"term":"Ann Arbor", "entity":"podcast"}
    response = requests.get(baseurl, params=parameters)
    py_data = json.loads(response.text)
    # assert 34 == len(py_data['results']) # unreliable and changes
    # for visual check
    for r in py_data['results']:
        logger.info(r['trackName'])

def test_2412_flickr():
    # https://www.flickr.com/services/apps/about/ => app garden to showcase applications
    result_river_mts = get_flickr_data("river,mountains")
    # Some code to open up a few photos that are tagged with the mountains and river tags...
    photos = result_river_mts['photos']['photo']
    assert len(photos) == 5

    # visual usage only
    for photo in photos:
        owner = photo['owner']
        photo_id = photo['id']
        url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
        logger.info(url)
    # webbrowser.open(url)

def test_2414_black_panther():
    # movie list
    mlA = extract_movie_titles(get_movies_test_helper('black panther', 'movie'))
    mlB = extract_movie_titles(get_movies_test_helper('black panther', 'movies'))
    assert 5 == len(mlA)
    assert 5 == len(mlB)
    assert mlA == mlB
def test_2414_bridesmaids():
    ml = extract_movie_titles(get_movies_test_helper('Bridesmaids', 'movie'))
    assert 5 == len(ml)

def test_2421_related_titles_disjoint():
    ml = get_related_titles(["Black Panther", "Captain Marvel"])
    logger.info(ml)
    assert 9 == len(ml)

def test_2421_related_titles_overlap():
    ml = get_related_titles(["Black Panther", "Thor: Ragnarok"])
    logger.info(ml)
    # assert 7 == len(ml) # results are dynamic

def test_2422_rating():
    movieTitle = "Black Panther"
    rating = get_movie_rating(get_movie_data(movieTitle))
    logger.info("Rating for {0} = {1}".format(movieTitle, rating))
    assert 0.96 == rating

def test_243_sorted_recommendationsA():
    movieList=["Black Panther"]
    sRecom = get_sorted_recommendations(movieList)
    logger.info("Recommendations for {0}: {1}".format(movieList, sRecom))
    expectedList = ['Thor: Ragnarok', 'Spider-Man: Homecoming', 'Avengers: Infinity War', 'Deadpool 2', 'Ready Player One']
    # assert expectedList == sRecom # results are dynamic

def test_243_sorted_recommendationsB():
    movieList=["Black Panther", "Thor: Ragnarok"]
    sRecom = get_sorted_recommendations(movieList)
    logger.info("Recommendations for {0}: {1}".format(movieList, sRecom))
    expectedList = ['Thor: Ragnarok', 'Spider-Man: Homecoming', 'Guardians Of The Galaxy Vol. 2','Avengers: Infinity War', 'Deadpool 2', 'Ready Player One', 'Justice League']
    # assert expectedList == sRecom # results are dynamic

def test_xxx():
    movieRatings = {'Ready Player One': 0.72, 'Thor: Ragnarok': 0.93, 'Avengers: Infinity War': 0.85, 'Deadpool 2': 0.84, 'Spider-Man: Homecoming': 0.92}
    logger.info("movieRatings={}".format(movieRatings))
    sMovies = sorted(movieRatings.items(), key = lambda item: item[1], reverse = True)
    logger.info("sMovies={}".format(sMovies))

def test_sorted_recommendations():
    # Checks that if there is a tie, the movie title is in reverse alpha order
    movieRatings = {'Ready Player One': 0.72, 'Thor: Ragnarok': 0.92, 'Avengers: Infinity War': 0.85, 'Deadpool 2': 0.72, 'Spider-Man: Homecoming': 0.92}
    sortedRecommendations = sorted(movieRatings.items(), key = functools.cmp_to_key(movieCmp), reverse = True)
    logger.info("sortedRecommendations={}".format(sortedRecommendations))
    expectedRatings = [('Thor: Ragnarok', 0.92), ('Spider-Man: Homecoming', 0.92), ('Avengers: Infinity War', 0.85), ('Ready Player One', 0.72), ('Deadpool 2', 0.72)]
    assert expectedRatings == sortedRecommendations
# endregion tests for xx.x
