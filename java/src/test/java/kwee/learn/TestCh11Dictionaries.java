package kwee.learn;

import java.util.logging.Logger;
import java.util.Map;
import java.util.HashMap;
import java.util.AbstractMap;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
// static imports
import static org.junit.jupiter.api.Assertions.assertEquals;
/*
import java.util.List;
import io.restassured.response.Response;
import io.restassured.response.ResponseBody;
import io.restassured.common.mapper.TypeRef;
import io.restassured.path.json.JsonPath;

import static io.restassured.RestAssured.get;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
*/

/* 1. Dictionary was deprecated in Java 1.2, so use Map
   2. Parameterized tests in JUnit5 is tedious compared with Pytest and Xunit
      The CsvSource format is hokey, ie does not map into any language construct, even like a list or array
      Good thing CsvSource has a delimiter specifier ( default is comma )that I made good use of, and this is
      my first try at parameterized tests
   3. https://www.baeldung.com/java-initialize-hashmap
   4. https://www.baeldung.com/java-merge-maps merging 2 maps in Java 8
*/
public class TestCh11Dictionaries {
    private Logger logger;

    @BeforeEach
    public void setUp(){
       logger = Logger.getLogger(test_template.class.getName());
    }
// #region xxx
    String Capitalize(String input){
        if ( input != null &&  ! input.isEmpty() ){
            if (input.length() == 1){
                return input.toUpperCase();
            } else {
                return  input.substring(0,1).toUpperCase() + input.substring(1, input.length());
            }
        } else {
            return input;
        }
    }
    Map<String, String> GetEnglish2PirateDictionary(){
        Map<String, String> English2Pirate = new HashMap<String,String>(
           /*
           Map.of(
                  "sir","matey",
                  "hotel","fleabag inn",
                  "student","swabbie",
                  "boy","matey",
                  "madam","proud beauty",
                  "professor","foul blaggart",
                  "restaurant","galley",
                  "your","yer",
                  "excuse","arr",
                  "students","swabbies",
                  "are","be",
                  "lawyer","foul blaggart",
                  "the","th’",
                  "restroom","head",
                  "my","me",
                  "hello","avast",
                  "is","be",
                  "man","matey"
            )
            */
        );
        var CapEnglishPirate=new HashMap<String,String>();
        English2Pirate.forEach((k,v) -> {
            CapEnglishPirate.put(Capitalize(k), Capitalize(v));
        });



        
        return null;
    }
    String TranslateEnglish2Pirate(Map<String,String> English2Pirate, String englishSentence){
        return "";
    }
// #endregion xxx
// #region tests
    @Test
    public void test_0001_initializeMap(){
        Map<Integer, String> mapDoubleBrace = new HashMap<Integer, String>(){{
                put(1, "one");
                put(2, "two");
                put(3, "three");
        }};
        Map<Integer, String> mapImmutableOf = Map.of(1,"one", 2, "two", 3, "three"); // limit of 10 items, lexically dumb bec no indication of which pairs
        Map<Integer, String> mapImmutableOfEntries = Map.ofEntries(
           new AbstractMap.SimpleEntry<Integer, String>(1, "one"),
           new AbstractMap.SimpleEntry<Integer, String>(2, "two"),
           new AbstractMap.SimpleEntry<Integer, String>(3, "three")
        );
        // series of asserts
        assertEquals(mapDoubleBrace, mapImmutableOf);
        assertEquals(mapImmutableOf, mapImmutableOfEntries);
    }
    // Note: @ValueSource is only for functions with one argument. This is dumb, to create the mechanism for only one input
    @ParameterizedTest
    @CsvSource({
        "hello, HELLO",
        "world, WORLD"})
    public void test_0000_CsvSourceTwoStringInputs(String input, String expected) {
        assertEquals(expected, input.toUpperCase());
    }
    @ParameterizedTest
    @CsvSource(delimiter = '|', value = {
            "Hello boy, how are you?|Avast matey, how be you?",
            "I saw the professor and his student entering the restaurant near the hotel this afternoon|I saw th’ foul blaggart and his swabbie entering th’ galley near th’ fleabag inn this afternoon",
            "Good morning Sir and Madam!|Good morning Matey and Proud beauty!",
            "Excuse me, where is the restroom?|Arr me, where be th’ head?"
    })
    public void test_111112_pirate(String english, String expectedPirate){
        var English2Pirate = GetEnglish2PirateDictionary();
        var pirateLine = TranslateEnglish2Pirate(English2Pirate, english);
        assertEquals(expectedPirate, pirateLine);
        logger.info("hello");
    }
// #endregion tests
}
