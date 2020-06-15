package kwee.learn;
import java.util.logging.Logger;
import java.util.List;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import io.restassured.RestAssured;
import io.restassured.response.Response;
import io.restassured.response.ResponseBody;
import io.restassured.common.mapper.TypeRef;
import io.restassured.path.json.JsonPath;

// static imports
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
// import static io.restassured.path.json.JsonPath.with;
import static io.restassured.RestAssured.get;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;


/* 1. While it is nice to have a common definition of Http status codes, the fact that they are non
   standard means it is not as useful as we think.
   2. Also enums are not first class citizens in most languages
   3. For Java, the choices are javax.ws.rs.core.Response.Status, HttpUrlConnection and org.apache.http.HttpStatus
   https://stackoverflow.com/questions/730283/does-java-have-a-complete-enum-for-http-response-codes
   4. restassured has its own JsonPath builtin, so no need to use Jayway's JsonPath in github.com/json-path/JsonPath
*/
class PhotoItem {
    public String id;
    public String owner;
    public String secret;
    public String server;
    public String farm;
    public String title;
    public String ispublic;
    public String isfriend;
    public String isfamily;
    public PhotoItem(){id="uninitialized"; owner=""; secret=""; server=""; farm=""; title=""; ispublic="0"; isfriend="0"; isfamily="0";};
}
class RhymeItem { // single line because plain data type
    public String word;
    public Integer score;
    public Integer numSyllables;
    public RhymeItem(){word="uninitialized"; score= -1; numSyllables= -1;};    
    public RhymeItem(final String w, final Integer s, final Integer n) { word = w; score = s; numSyllables = n; }
}

public class TestCh24InternetApi {
    private Logger logger;
    private String flickr_key = "464b86270211da70af8a940c0ed6c219";
    @BeforeEach
    public void setUp(){
       logger = Logger.getLogger(TestCh24InternetApi.class.getName());
    }
    // #region Postman examples
    // http://www.projectdebug.com/send-get-request-using-rest-assured/
    @Test
    public void test_PostmanEcho_statuscode() { // non standard name, but clear, easy to read
        final String ROOT_URI = "https://postman-echo.com";
        get(ROOT_URI + "/GET").then().statusCode(200);
    }

    @Test
    public void test_PostmanEcho_body() {
        final String ROOT_URI = "https://postman-echo.com";
        get(ROOT_URI + "/GET").then().assertThat().body("headers.host", equalTo("postman-echo.com"));
    }

    @Test
    public void test_PostmanEcho_header() {
        final String ROOT_URI = "https://postman-echo.com";
        // Postman shows "gzip, deflate, br" but not sure why only 2 token match
        get(ROOT_URI + "/GET").then().assertThat().body("headers.accept-encoding", equalTo("gzip,deflate"));
    }

    // #endregion Postman examples
    // #region ch24 tests
    @Test
    public void test_2461_get() {
        /*
        1. url not easy to get, so skip for now
        2. extraction makes use of other libraries, in this case, Jackson
        */
        String ROOT_URI = "https://api.datamuse.com";
        Response r1 = get(ROOT_URI + "/words?rel_rhy=funny");
        // Warning: ResponseBody is a raw type. References to generic type ResponseBody<T> should be parameterized
        ResponseBody<?> rb1 = r1.then().extract().response().body();
        logger.info(String.format("first 50 chars: %.50s", rb1.asString()));
        String word1 = rb1.path("[0].word");
        Integer score1 = rb1.path("[0].score");
        Integer numSyllables1 = rb1.path("[0].numSyllables");
        logger.info(String.format("%s %d %d", word1, score1, numSyllables1));

        r1.then().assertThat().body("[0].word", equalTo("money"));
        r1.then().assertThat().body("[0].score", equalTo(4415));
        r1.then().assertThat().body("[0].numSyllables", equalTo(2));
        // getList extracts word field across the array
        List<String> words = r1.jsonPath().getList("word");
        logger.info(String.format("lstring,size() = %d", words.size()));
        assertEquals(84, words.size());
        // get generic List<Object>
        var items = r1.as(new TypeRef<List<RhymeItem>>(){});
        logger.info(String.format("lo,size() = %d", items.size())); 
        assertEquals(84, items.size());
    }
    @Test
    public void test_2463_get(){
        /* The python code verifies the URL because it is useful in troubleshooting when things go wrong.
        For Java, RestAssured does not readily have a function for this.
        The accepted process is to turn logging on and look at the console.
        Ref: https://stackoverflow.com/questions/42015223/how-to-printout-the-url-that-restassured-trying-to-connect-with-to-the-web-servi
        */
        String ROOT_URI = "https://api.datamuse.com";
        // in-out indentation style to show given/when/then
        given().
            log().all().
            param("rel_rhy", "funny").
        when().
            get(ROOT_URI + "/words").
        then().
            statusCode(200);
    }
    private List<String> get_rhymes(String word){
        String ROOT_URI = "https://api.datamuse.com";
        ResponseBody<?> rb = given().
           log().all().
           param("rel_rhy", word).
           param("max", 3).
        when().
           get(ROOT_URI + "/words").
        then().
           statusCode(200)
           .extract().
           response()
           .body();

        return rb.jsonPath().getList("word");
    }
    @Test
    public void test_2482_test_get_rhymes(){
        List<String> rhymes = get_rhymes("funny");
        List<String> erhymes = List.of("money", "honey", "sunny");
        assertEquals(erhymes, rhymes);
    }
    @Test
    public void test_2411_itunes(){
        String baseurl = "https://itunes.apple.com/search";
        Response response = 
            given().
                param("term", "Ann Arbor").
                param("entity", "podcast").
            when().
                get(baseurl);
        
        JsonPath jp = response.jsonPath();
        List<String> tracks = jp.get("results.trackName");
        logger.info(String.format("size=%d", tracks.size()));        
        for( String track : tracks){
            logger.info(track.toString());
        }
    }
    Response get_flickr_data(String tags_string){
        String baseurl = "http://api.flickr.com/services/rest";
        Response r = given().
           log().all().
           param("api_key", flickr_key).
           param("tags", tags_string).
           param("tag_mode", "all").
           param("method", "flickr.photos.search").
           param("per_page", 5).
           param("media", "photos").
           param("format","json").
           param("nojsoncallback", 1).
           when().
              get(baseurl);
           /*   
           then().
              statusCode(200).extract().response().body();
              */
        return r;
    }
    @Test
    public void test_2412_flickr(){ // extract into PhotoItem
        ResponseBody<?> r1 = get_flickr_data("river,mountains").then().statusCode(200).extract().response().body();
        JsonPath result_river_mts = r1.jsonPath();
        // List<Object> photos = result_river_mts.getList("photos.photo"); // Q: Interesting q how to turn an Object format into some usable POD       
        List<PhotoItem> photos = result_river_mts.getList("photos.photo", PhotoItem.class);                
        assertEquals(5, photos.size());

        // visual use only
        for (PhotoItem photo : photos){
            String url = String.format("https://www.flickr.com/photos/%s/%s", photo.owner, photo.id);
            logger.info(url);
        }
    }//test
    @Test
    public void test_2413_flickr(){ // extract into Object, but unable to access fields in Object correctly
        ResponseBody<?> r1 = get_flickr_data("river,mountains").then().statusCode(200).extract().response().body();
        JsonPath result_river_mts = r1.jsonPath();
        List<Object> photos = result_river_mts.getList("photos.photo"); // Q: Interesting q how to turn an Object format into some usable POD       
        assertEquals(5, photos.size());

        // visual use only
        for (Object photoObj : photos){
            assertThrows(ClassCastException.class, () -> {
                String title = ((PhotoItem)photoObj).title;
                // String url = String.format("https://www.flickr.com/photos/%s/%s", photo.owner, photo.id);
                logger.info(title);
            });
        }
    }//test    
//#endregion chapter 24 tests    
}
