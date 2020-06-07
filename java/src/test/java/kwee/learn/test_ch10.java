package kwee.learn;
import java.io.IOException;
import java.lang.IllegalStateException;
import java.util.NoSuchElementException;
import java.io.BufferedReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Scanner;
import java.util.logging.Logger;
import java.util.stream.Stream;
import java.util.Optional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

/*
Deitel 17.13 Stream<String> from a file
Deitel 15.7.2 InputStreamReader, StringReader, LineNumberReader

*/

public class test_ch10 {
    private Logger logger;

    @BeforeEach
    public void setUp(){
        logger = Logger.getLogger(test_ch10.class.getName());
    }
    @Test
    public void test_1031_num_char_read_scanner(){
        try(Scanner input = new Scanner(Paths.get("../../../data/school_prompt2.txt"))){
            var num_char = 0;
            // logger.info(String.format("delimiter: >%s<", input.delimiter()));
            while(input.hasNext()){
                var line = input.nextLine().strip();
                logger.info(String.format(">%s<", line));
                num_char += line.length();
            }
            // logger.info(String.valueOf(num_char));
            logger.info(String.format("num_char: %d", num_char));
            assertEquals(527, num_char);
        }
        catch(IOException | NoSuchElementException | IllegalStateException e){
            e.printStackTrace();
            fail("unforeseen Exception");            
        }
    }
    @Test
    public void test_1031_num_char_read_bufferedreader(){
        // try(BufferedReader input = new BufferedReader(new FileReader("../../../data/school_prompt2.txt"))){ // old style
        try(BufferedReader input = Files.newBufferedReader(Paths.get("../../../data/school_prompt2.txt"))){            
            var num_char = 0;
            String line;
            while((line = input.readLine()) != null){
                num_char += line.length(); // carriage-return is stripped out by readLine
            }
            // logger.info(String.valueOf(num_char));
            logger.info(String.format("num_char: %d", num_char));
            assertEquals(527, num_char);
        }
        catch(IOException | NoSuchElementException | IllegalStateException e){
            e.printStackTrace();
            fail("unforeseen Exception");                        
        }
    }
    @Test
    public void test_1031_num_char_read_filesreadalllines(){
        try{
            List<String> lines = Files.readAllLines(Paths.get("../../../data/school_prompt2.txt"));
            var num_char = 0;        
            for(String line : lines){
                num_char += line.length();
            }
            // logger.info(String.valueOf(num_char));
            logger.info(String.format("num_char: %d", num_char));
            assertEquals(527, num_char);
        } catch(IOException e){
            e.printStackTrace();
            fail("unforeseen IOException");                        
        }
    }    
    @Test
    public void test_1031_num_char_read_stream_of_string(){
        // functional in steps
        try(Stream<String> streamString = Files.lines(Paths.get("../../../data/school_prompt2.txt"))){
            Stream<Integer> streamInt = streamString.map( line -> line.length());
            Optional<Integer> num_char = streamInt.reduce((x,y) -> x + y);
            // logger.info(String.valueOf(num_char));
            if(num_char.isPresent()){
                logger.info(String.format("num_char: %d", num_char.get()));
                assertEquals(527, num_char.get());
            }else{
                fail("num_char does not have a value");
            }
        } catch(IOException e){
            e.printStackTrace();
            fail("unforeseen IOException");            
        }
    }    
    @Test
    public void test_1031_num_char_read_stream_of_string2(){
        // more canonically functional
        try(Stream<String> streamString = Files.lines(Paths.get("../../../data/school_prompt2.txt"))){
            int num_char = streamString
                .map( line -> line.length())
                .reduce((x,y) -> x + y)
                .get();
            logger.info(String.format("num_char: %d", num_char));
            assertEquals(527, num_char);
        } catch(IOException e){
            e.printStackTrace();
            fail("unforeseen IOException");                        
        }
    }    
}