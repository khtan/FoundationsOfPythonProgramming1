package kwee.learn;

import java.util.logging.Logger;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.AbstractMap;
import java.util.Collections;
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
   3. https://www.geeksforgeeks.org/initializing-a-list-in-java/
   4. https://www.baeldung.com/java-initialize-hashmap
   5. https://www.baeldung.com/java-merge-maps merging 2 maps in Java 8
*/
public class TestCh11Dictionaries {
    private Logger logger;

    @BeforeEach
    public void setUp(){
       logger = Logger.getLogger(test_template.class.getName());
    }
// #region helpers
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
        Map<String, String> English2Pirate = new HashMap<String,String>(){{
            put("sir","matey");
            put("hotel","fleabag inn");
            put("student","swabbie");
            put("boy","matey");
            put("madam","proud beauty");
            put("professor","foul blaggart");
            put("restaurant","galley");
            put("your","yer");
            put("excuse","arr");
            put("students","swabbies");
            put("are","be");
            put("lawyer","foul blaggart");
            put("the","th’");
            put("restroom","head");
            put("my","me");
            put("hello","avast");
            put("is","be");
            put("man","matey");
        }};
        var CapEnglish2Pirate=new HashMap<String,String>();
        English2Pirate.forEach((k,v) -> {
            CapEnglish2Pirate.put(Capitalize(k), Capitalize(v));
        });
        CapEnglish2Pirate.forEach((k,v) -> {
                English2Pirate.put(k, v);
        });
        return English2Pirate;
    }
    String TranslateEnglish2Pirate(Map<String,String> English2Pirate, String englishSentence){
        List<String> pirateLine = new ArrayList<String>();
        for(String word : englishSentence.split(" ")){
            String filteredWord = word.replaceAll("\\W+", "");
            if(English2Pirate.containsKey(filteredWord)){
                String replacedWord = word.replace(filteredWord, English2Pirate.get(filteredWord));
                pirateLine.add(replacedWord); // Append returns new sequence
            }
            else{
                pirateLine.add(word);
            }
        }
        return String.join(" ", pirateLine);
    }
// #endregion helpers
// #region exploratory
    @Test
    public void test_0001_initializeList(){
        List<Integer> listDoubleBraces = new ArrayList<Integer>(){ // anonymous class
            { // initializer block
               add(1);
               add(2);
               add(4);
            }
        };
        List<Integer> listAsListImmutable = Arrays.asList(1,2,4); // immutable
        List<Integer> listAsListMutable = new ArrayList<>(Arrays.asList(1,2,4));
        List<Integer> listCollectionsAddAll = Collections.EMPTY_LIST;
        Collections.addAll(listCollectionsAddAll = new ArrayList<Integer>(), 1, 2, 4);
        // series of asserts
        assertEquals(listDoubleBraces, listAsListImmutable);
        assertEquals(listAsListImmutable, listAsListMutable);
        assertEquals(listAsListMutable, listCollectionsAddAll);
    }
    @Test
    public void test_0002_initializeMap(){
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
    public void test_0003_CsvSourceTwoStringInputs(String input, String expected) {
        assertEquals(expected, input.toUpperCase());
    }
// #endregion exploratory
// #region tests for ch11
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
    }
// #endregion tests for ch11
}
