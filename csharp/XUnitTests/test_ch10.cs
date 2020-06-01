using System;
using System.IO;
using System.Globalization;
using System.Collections.Generic;
using System.Text;
using Xunit;
using Xunit.Abstractions;

namespace XUnitTests
{
    public class test_ch10
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_ch10(ITestOutputHelper output) { this.output = output;  }

        [Fact]
        public void test_1031_num_char_ReadAllText()
        {
            string s = File.ReadAllText("../../../../../data/school_prompt2.txt");
            string noReturns = s.Replace("\r\n", "").Replace("\n", "");
            var num_char = noReturns.Length;
            Assert.Equal(527, num_char);
            output.WriteLine($"num_char: {num_char}");
        }
        [Fact]
        public void test_1031_num_char_ReadAllLines()
        {
            string[] lines = File.ReadAllLines("../../../../../data/school_prompt2.txt");
            int num_char = 0;
            foreach (var line in lines)
            {
                num_char += line.Length;
            }
            Assert.Equal(527, num_char);
        }
        [Fact]
        public void test_1031_num_char_StreamReader()
        {

            using (FileStream fs = File.OpenRead("../../../../../data/school_prompt2.txt"))
            using (StreamReader reader = new StreamReader(fs))
            {
                int num_char = 0;
                string line;
                while ((line = reader.ReadLine()) != null)
                {
                    num_char += line.Length;
                }
                Assert.Equal(527, num_char);
            }

        }
    }
}
