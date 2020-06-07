package kwee.learn;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;


public class test_ch08 {
    @Test
    public void test_1(){
        String rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85";
        var rainfall_string_array = rainfall_mi.split(",");
        var num_rainy_months = 0;
        for(String rain_string : rainfall_string_array){
            var rainfall = Float.parseFloat(rain_string);
            if (rainfall > 3.0) num_rainy_months++;
        }
        System.out.println(String.format("num_rainy_months = %d", num_rainy_months));
        assertEquals(5, num_rainy_months);
    }

}