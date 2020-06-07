package kwee.learn;
import java.util.logging.Logger;
import java.util.List;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import io.restassured.response.Response;
import io.restassured.response.ResponseBody;
import io.restassured.common.mapper.TypeRef;
import io.restassured.path.json.JsonPath;

// static imports
import static org.junit.jupiter.api.Assertions.assertEquals;
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

class RhymeItem { // single line because plain data type
    public String word;
    public Integer score;
    public Integer numSyllables;
    public RhymeItem(final String w, final Integer s, final Integer n) { word = w; score = s; numSyllables = n; }
}

public class test_ch24_internet_api {
    private Logger logger;

    @BeforeEach
    public void setUp(){
       logger = Logger.getLogger(test_ch24_internet_api.class.getName());
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
        var items = r1.as(new TypeRef<List<Object>>(){});
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
//#endregion chapter 24 tests    
}
