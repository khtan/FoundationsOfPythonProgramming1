using System;
using System.Globalization;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace XUnitTests
{
    public class test_ch08
    {
        [Fact]
        public void test_1()
        {
            String rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85";
            var rainfall_string_array = rainfall_mi.Split(",");
            var num_rainy_months = 0;
            foreach(string rain_string in rainfall_string_array){
                var rainfall = float.Parse(rain_string, CultureInfo.InvariantCulture);
                if (rainfall > 3.0) num_rainy_months++;
            }
            Console.WriteLine(num_rainy_months);
            Assert.Equal(5, num_rainy_months);
        }
        [Fact]
        public void test_1a()
        { // Can use functional style?
            // String rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85";
        }
    }
}
