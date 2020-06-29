package kwee.learn;

import java.util.logging.Logger;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.AbstractMap;
import java.util.Collections;
import java.util.stream.Collectors;
import java.util.stream.Stream;
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

/*
1. Dictionary was deprecated in Java 1.2, so use Map
2. Parameterized tests in JUnit5 is tedious compared with Pytest and Xunit
The CsvSource format is hokey, ie does not map into any language construct, even like a list or array
Good thing CsvSource has a delimiter specifier ( default is comma )that I made good use of, and this is
my first try at parameterized tests
3. The multitude of ways to initialize and merge lists, maps shows that there is no single vision in Java
hence the diversity. This is much different from Python and C#
*/
public class TestCh11Dictionaries {
    @SuppressWarnings("unused")
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
    public void test_0001_initializeList(){ // https://www.geeksforgeeks.org/initializing-a-list-in-java/
        List<Integer> listDoubleBraces = new ArrayList<Integer>(){ // anonymous class
            { // initializer block
                add(1);
                add(2);
                add(4);
            }
        };
        List<Integer> listAsListImmutable = Arrays.asList(1,2,4); // immutable
        List<Integer> listAsListMutable = new ArrayList<>(Arrays.asList(1,2,4));
        // List<Integer> listCollectionsAddAll = Collections.EMPTY_LIST; // Type safety: The expression of type List needs unchecked conversion to conform to List<Integer>
        List<Integer> listCollectionsAddAll = new ArrayList<Integer>();
        Collections.addAll(listCollectionsAddAll = new ArrayList<Integer>(), 1, 2, 4);
        List<Integer> listCollectionsUnmodifiableList = Collections.unmodifiableList(Arrays.asList(1,2,4));
        // Java 8 stream
        List<Integer> listStreamOf1 = Stream.of(1,2,4).collect(Collectors.toList());
        List<Integer> listStreamOf2 = Stream.of(1,2,4).collect(Collectors.toCollection(ArrayList::new));
        List<Integer> listStreamOf3 = Stream.of(1,2,4).collect(Collectors.collectingAndThen(Collectors.toList(), Collections::unmodifiableList));
        // Java 9 of, up to 10 elements
        List<Integer> listOfImmutable = List.of(1,2,4);
        // series of transitive asserts
        assertEquals(listDoubleBraces, listAsListImmutable);
        assertEquals(listAsListImmutable, listAsListMutable);
        assertEquals(listAsListMutable, listCollectionsAddAll);
        assertEquals(listCollectionsAddAll, listCollectionsUnmodifiableList);
        assertEquals(listCollectionsUnmodifiableList, listStreamOf1);
        assertEquals(listStreamOf1, listStreamOf2);
        assertEquals(listStreamOf2, listStreamOf3);
        assertEquals(listStreamOf3, listOfImmutable);
    }
    @Test
    public void test_0002_initializeMap(){ // https://www.baeldung.com/java-initialize-hashmap
        // 1. double braces
        Map<Integer, String> mapDoubleBrace = new HashMap<Integer, String>(){{
            put(1, "one");
            put(2, "two");
            put(3, "three");
        }};
        // 2. Java 8 Stream.of() Collectors.toMap
        Map<Integer, String> mapStreamOf = Stream.of(new Object[][]{
            {1, "one"},
            {2, "two"},
            {3, "three"}
        }).collect(Collectors.toMap(data -> (Integer) data[0], data -> (String) data[1]));
        // 3. Java 8 Stream.of() Map.SimpleEntry
        Map<Integer, String> mapStreamOfEntry = Stream.of(
        new AbstractMap.SimpleEntry<>(1, "one"),
        new AbstractMap.SimpleEntry<>(2, "two"),
        new AbstractMap.SimpleEntry<>(3, "three")
        ).collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
        // 4. Java 8 Stream.of() Map.SimpleImmutableEntry
        Map<Integer, String> mapStreamOfImmutableEntry = Stream.of(
        new AbstractMap.SimpleImmutableEntry<>(1, "one"),
        new AbstractMap.SimpleImmutableEntry<>(2, "two"),
        new AbstractMap.SimpleImmutableEntry<>(3, "three")
        ).collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
        // 5 Java 8 Stream.of() unmodifiableMap -- likely to have performance hit and garbage objects
        Map<Integer, String> mapStreamOfUnmodifiableMap = Stream.of(
        new Object[][]{
            {1, "one"},
            {2, "two"},
            {3, "three"}
        }).collect(Collectors.collectingAndThen(
        Collectors.toMap(data -> (Integer)data[0], data -> (String)data[1]),
        Collections::<Integer, String> unmodifiableMap
        ));
        // 6. Java 9 Map.of()
        Map<Integer, String> mapImmutableOf = Map.of(1,"one", 2, "two", 3, "three"); // limit of 10 items, lexically dumb bec no indication of which pairs
        // 7. Java 9 Map.ofEntries()
        Map<Integer, String> mapImmutableOfEntries = Map.ofEntries(
        new AbstractMap.SimpleEntry<Integer, String>(1, "one"),
        new AbstractMap.SimpleEntry<Integer, String>(2, "two"),
        new AbstractMap.SimpleEntry<Integer, String>(3, "three")
        );
        // 7. Guava Iterables (skip)
        // 8. Apache Commons Collections (skip)
        // series of asserts
        assertEquals(mapDoubleBrace, mapImmutableOf);
        assertEquals(mapImmutableOf, mapImmutableOfEntries);
        assertEquals(mapImmutableOfEntries, mapStreamOf);
        assertEquals(mapStreamOf, mapStreamOfEntry);
        assertEquals(mapStreamOfEntry, mapStreamOfImmutableEntry);
        assertEquals(mapStreamOfImmutableEntry, mapStreamOfUnmodifiableMap);
    }
    @Test
    public void test_0003_mergeLists(){ // https://www.techiedelight.com/join-two-lists-java/
        List<Integer> listA = List.of(1,2,4);
        List<Integer> listB = List.of(3,7,11);
        List<Integer> eMergedList = List.of(1,2,4,3,7,11);
        // 1. List.add()
        List<Integer> list1 = new ArrayList<>();
        list1.addAll(listA);
        list1.addAll(listB);
        assertEquals(eMergedList, list1);
        // 2. List .add() 
        List<Integer> list2 = new ArrayList<>(listA);
        list2.addAll(listB);
        assertEquals(eMergedList, list2);
        // 3. Double brace initialization
        List<Integer> list3 = new ArrayList<Integer>(){{ // wasteful because anonymous class created
            addAll(listA);
            addAll(listB);
        }};
        assertEquals(eMergedList, list3);
        // 4. Collections.allAll
        List<Integer> list4 = new ArrayList<>();
        Collections.addAll(list4, listA.toArray(new Integer[0]));
        Collections.addAll(list4, listB.toArray(new Integer[0]));
        assertEquals(eMergedList, list4);
        // 5. Java8 Stream.of() + flatMap() + Collector
        List<Integer> list5 = Stream.of(listA, listB).flatMap(x -> x.stream()).collect(Collectors.toList());
        assertEquals(eMergedList, list5);
        // 6. Java8 Steam.of() + Stream.forEach()
        List<Integer> list6 = new ArrayList<>();
        Stream.of(listA, listB).forEach(list6::addAll);
        assertEquals(eMergedList, list6);
        // 7. Java8 Stream.concat() + Collector
        List<Integer> list7 = Stream.concat(listA.stream(), listB.stream()).collect(Collectors.toList());
        assertEquals(eMergedList, list7);
        // 8. stream, collect, addAll
        List<Integer> list8 = listA.stream().collect(Collectors.toList());
        list8.addAll(listB);
        assertEquals(eMergedList, list8);
    } // test

    @Test
    public void test_0004_mergeMaps(){ // https://www.baeldung.com/java-merge-maps
        Map<Integer, String> mapA = Map.of(1,"one", 2, "two", 3, "three");
        Map<Integer, String> mapB = Map.of(4,"four", 5, "five", 6, "six");
        Map<Integer, String> eMergedMap = Map.of(1,"one", 2, "two", 3, "three",4,"four", 5, "five", 6, "six"); // expected merged map
        // 1. Map.merge https://www.nurkiewicz.com/2019/03/mapmerge-one-method-to-rule-them-all.html
        Map<Integer, String> map1 = new HashMap<>(mapA);
        mapB.forEach((k,v) -> map1.merge(k, v, (v1, v2) -> v1));
        assertEquals(eMergedMap, map1);
        // 2. Stream.concat()
        Map<Integer, String> map2 = Stream.concat(mapA.entrySet().stream(), mapB.entrySet().stream()).
        collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (v1, v2) -> v1));
        assertEquals(eMergedMap, map2);
        // 3. Stream.of()
        Map<Integer, String> map3 = Stream.of(mapA, mapB).
        flatMap(map -> map.entrySet().stream()).
        collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue,(v1, v2) -> v1));
        assertEquals(eMergedMap, map3);
        // 4. Simple streaming
        Map<Integer, String> map4 = mapA.entrySet().stream().
        collect(
        Collectors.toMap(
        Map.Entry::getKey,
        Map.Entry::getValue,
        (v1, v2) -> v1,
        () -> new HashMap<>(mapB))
        );
        assertEquals(eMergedMap, map4);
        // 5. StreamEx library (skipped)
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
    
