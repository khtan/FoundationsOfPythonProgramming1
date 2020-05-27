# region imports
import logging
import pytest
import requests
import json

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

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {}
    params_diction["rel_rhy"] = word
    params_diction["max"] = 3
    resp = requests.get(baseurl, params=params_diction)
    word_ds = resp.json()
    return [d['word'] for d in word_ds]

def test_2482_test_get_rhymes(): # 24.8.2
    rhymes = get_rhymes("funny")
    erhymes = ['money', 'honey', 'sunny']
    assert erhymes == rhymes

def test_2411_itunes(): # 24.11
    baseurl = "https://itunes.apple.com/search"
    parameters={"term":"Ann Arbor", "entity":"podcast"}
    response = requests.get(baseurl, params=parameters)
    py_data = json.loads(response.text)
    assert 34 == len(py_data['results'])
    # for visual check
    for r in py_data['results']:
        logger.info(r['trackName'])

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

def test_2412_flickr():
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

# endregion tests
