package kwee.learn;

import java.util.logging.Logger;
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

/* 1. Notes
*/
public class TestCh11Dictionaries {
    private Logger logger;

    @BeforeEach
    public void setUp(){
       logger = Logger.getLogger(test_template.class.getName());
    }
// #region xxx
    TranslateEnglish2Pirate(){}
// #endregion xxx
// #region tests
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
        assertEquals(expectedPirate, prirateLine);
    }
// #endregion tests
}
