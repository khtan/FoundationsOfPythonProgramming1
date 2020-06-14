
package kwee.learn;
import java.util.logging.Logger;
import java.util.List;
import java.util.Map;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

// static imports
import static io.restassured.path.json.JsonPath.with;
import static org.junit.jupiter.api.Assertions.assertEquals;
/*
import io.restassured.response.Response;
import io.restassured.response.ResponseBody;
import io.restassured.common.mapper.TypeRef;
import io.restassured.path.json.JsonPath;

import static io.restassured.RestAssured.get;
import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
*/

/* 1. https://restfulapi.net/json-jsonpath appears to be Jayway JsonPath
      It supports the $ array and the $ dot notation. They don't work for Rest Assured JsonPath
   2. https://www.javadoc.io/doc/io.rest-assured/json-path/3.0.0/io/restassured/path/json/JsonPath.html
      This is the Rest Assured Json Path documentation. It talks about the GPath notation
   3. http://docs.groovy-lang.org/latest/html/documentation/#_gpath
      The GPath notation uses a series of connected dots
*/
class BookItem{
    public String category;
    public String author;
    public String title;
    public String isbn;
    public float price;
}
public class test_ch17_jsonpath {
    private Logger logger;
    private static final String storeJson =
            "{ \"store\": {\n" +
            "    \"book\": [\n" +
            "        { \"category\": \"reference\",\n" +
            "                \"author\": \"Nigel Rees\",\n" +
            "                \"title\": \"Sayings of the Century\",\n" +
            "                \"price\": 8.95\n" +
            "                },\n" +
            "        { \"category\": \"fiction\",\n" +
            "                \"author\": \"Evelyn Waugh\",\n" +
            "                \"title\": \"Sword of Honour\",\n" +
            "                \"price\": 12.99\n" +
            "                },\n" +
            "        { \"category\": \"fiction\",\n" +
            "                \"author\": \"Herman Melville\",\n" +
            "                \"title\": \"Moby Dick\",\n" +
            "                \"isbn\": \"0-553-21311-3\",\n" +
            "                \"price\": 8.99\n" +
            "                },\n" +
            "        { \"category\": \"fiction\",\n" +
            "                \"author\": \"J. R. R. Tolkien\",\n" +
            "                \"title\": \"The Lord of the Rings\",\n" +
            "                \"isbn\": \"0-395-19395-8\",\n" +
            "                \"price\": 22.99\n" +
            "                }\n" +
            "     ],\n" +
            "       \"bicycle\": {\n" +
            "       \"color\": \"red\",\n" +
            "       \"price\": 19.95\n" +
            "        }\n" +
            "     }\n" +
            "}\n";

    @BeforeEach
    public void setUp(){
       logger = Logger.getLogger(test_ch17_jsonpath.class.getName());
    }
// #region xxx
// #endregion xxx
// #region tests
    @Test
    public void test_0001_listAllBookCategories() {
        List<String> categories = with(storeJson).get("store.book.category");
        List<String> expectedCategories = List.of("reference", "fiction","fiction", "fiction");
        assertEquals(expectedCategories, categories);
        // visual only
        for(String category: categories){
            logger.info(String.format("category = %s", category));
        }
    }
    @Test
    public void test_0002_firstBookCategory() {
        String category = with(storeJson).get("store.book[0].category");
        assertEquals("reference", category);
    }
    @Test
    public void test_0003_lastBookCategory() {
        String category = with(storeJson).get("store.book[-1].category");
        assertEquals("fiction", category);
    }
    @Test
    public void test_0004_allBooksPriced() {
        // Using get with container mapping
        List<Map<String, String>> books = with(storeJson).get("store.book.findAll {book -> book.price >=5 && book.price <=15 }");
        assertEquals(3, books.size());
        
        // visual only
        List<String> authors = new ArrayList<String>();        
        for(Map<String, String> book: books){
            logger.info("----- Book -----");
            for (Map.Entry<String, String> entry : book.entrySet()){
                String key = entry.getKey();
                if("author".equals(key)){ // warning "author" == key does not work, bec in Java, it compares the references, not content
                    String value = entry.getValue();                    
                    authors.add(value);
                }
                logger.info(String.format("\t%s -> %s", key, entry.getValue()));            
            }
        }
        List<String> expectedAuthors = List.of("Nigel Rees","Evelyn Waugh", "Herman Melville");
        assertEquals(expectedAuthors, authors);

    }// test
    @Test
    public void test_0005_allBooks() {
        // Using get with class mapping
        List<BookItem> books = with(storeJson).getList("store.book", BookItem.class);
        
        // visual only
        List<String> titles = new ArrayList<String>();
        for(BookItem book: books){
            titles.add(book.title);
            logger.info(String.format("Book: %s", book.title));
        }
        List<String> expectedTitles = List.of("Sayings of the Century", "Sword of Honour", "Moby Dick", "The Lord of the Rings");
        assertEquals(expectedTitles, titles);
    }// test
    // #endregion tests
}
