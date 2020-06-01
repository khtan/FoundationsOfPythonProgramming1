using System;
using System.Linq;
using System.Collections.Generic;
using Xunit;
using Xunit.Abstractions;
using Microsoft.VisualStudio.TestPlatform.ObjectModel;

namespace XUnitTests
{
    static class Extensions
    {
        public static IEnumerable<(int, T)> Enumerate<T>(this IEnumerable<T> input, int start = 0)
        {
            int i = start;
            foreach (var t in input)
                yield return (i++, t);
        }
    }
    public class common{
        public static int GetSize(Type tuple){ // https://www.tabsoverspaces.com/233606-getting-the-size-of-a-tuple-number-of-items
            var genericArgs = tuple.GetGenericArguments();
            if(genericArgs.Length > 7) return 7 + GetSize(genericArgs[7]);
            else return genericArgs.Length;
        }
        public static Tuple<double,double> CircleInfo(double r)
        {
            double c = 2 * 3.14159 * r;
            double a = 3.14159 * r * r;
            return new Tuple<double, double>(c, a);
        }
    }
    public class test_ch13_tuple
    {
        /// <summary>
        /// 1. Unlike Python, C# tuples cannot be mixed if the base types are different
        /// 2. Unlkie Python, C# tuples does not have a good way of traversing
        /// </summary>
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_ch13_tuple(ITestOutputHelper output) { this.output = output;  }

        [Fact]
        public void test_1300_simple()
        {
            string s = "bob";
            int n = 23;
            var t = (s, n);
            output.WriteLine($"item1={t.Item1}, item2={t.Item2}");
            Assert.Equal(s, t.Item1);
            Assert.Equal(n, t.Item2);
        }// fact
        [Fact]
        public void test_1321_autopacking(){
            var julia1 = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia");
            // c# does not allow autopacking
            // var julia2 = "Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia";
            output.WriteLine($"julia1.Item5={julia1.Item5}");
            Assert.Equal(2009, julia1.Item5);
        }
        [Fact]
        public void test_1321b_autopacking()
        {
            var julia1 = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia");
            var s = julia1.ToString();

            output.WriteLine($"s={s}");
            // Assert.Equal(2009, julia1.Item5);
        }
        [Fact]
        public void test_1322a_creation() { // 2 tests to show difference between Tuple and ValueTuple underlying
            var practice = ('y','h','z','x'); // No simple builtin to get length of tuple
            output.WriteLine(practice.GetType().ToString()); // System.ValueTuple`4[System.Char,System.Char,System.Char,System.Char]
            Assert.Equal(4, common.GetSize(practice.GetType()));
        }
        [Fact]
        public void test_1322b_creation()
        {
            Tuple<char, char, char, char> practice = new Tuple<char, char, char, char>('y', 'h', 'z', 'x'); // No simple builtin to get lenght of tuple
            output.WriteLine(practice.GetType().ToString()); // System.Tuple`4[System.Char,System.Char,System.Char,System.Char]
            Assert.Equal(4, common.GetSize(practice.GetType()));
        }
        [Fact]
        public void test_1330_unpack()
        {
            var julia1 = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia");
            (string name, string surname, int birth_year, string movie, int movie_year, string profession, string birth_place) = julia1;
            Assert.Equal("Julia", name);
            Assert.Equal(2009, movie_year);
        }
        [Fact]
        public void test_1331a_swap()
        { // C# can swap tuples if types match
            int a = 321;
            int b = 123;
            (a, b) = (b, a);
            output.WriteLine($"a={a}, b={b}");
            Assert.Equal(123, a);
            Assert.Equal(321, b);
        }
        /* This cannot compile
        [Fact]
        public void test_1331b_swap()
        {
            string a = "hello";
            int b = 123;
            (a, b) = (b, a); // conversion type error here
            output.WriteLine($"a={a}, b={b}");
            Assert.Equal(123, a);
            Assert.Equal("hello" b);
        }
        */
        [Fact]
        public void test_1332_unpack_into_iterator(){
            // var authors = {("Paul", "Resnick"), ("Brad", "Miller"), ("Lauren", "Murphy")}; // without type info, C# parses differently from Python
            var authors = new List<Tuple<string,string>>{ 
                new Tuple<string,string>("Paul", "Resnick"), 
                new Tuple<string,string>("Brad", "Miller"), 
                new Tuple<string,string>("Lauren", "Murphy") 
            };
            foreach ((string first_name, string last_name) in authors)
            {
                output.WriteLine($"first name: {first_name}, last name: {last_name}");
            }
        }
        [Fact]
        public void test_1333_pythonic_enumerate_sequence()
        { /* 1. Keep same name so that can find in python code
            2. Python allows indexing into tuples, so the pythonic pattern includes a enumerate with index
            3. C# does not allow indexing into tuples, so this pattern does not work
 *             */
            // var fruits = { "apple", "pear", "apricot", "cherry", "peach" };
            var fruits = new List<string>{ "apple", "pear", "apricot", "cherry", "peach" };
            foreach(var item in fruits.Select((value, i) => (i, value)))
            {
                output.WriteLine($"{item.i} {item.value}");
            }
        }
        [Fact]
        public void test_1333_csharp_enumerate_sequence()
        { /* 
 *         */
            var fruits = new List<string> { "apple", "pear", "apricot", "cherry", "peach" };
            foreach (var(i,o) in fruits.Enumerate())
            {
                output.WriteLine($"{i} {o}");
            }
        }
        [Fact]
        public void test_1334_circleinfo()
        {
            (double area1, double circum1) = common.CircleInfo(10); // unpack into variables
            var ci2 = common.CircleInfo(100); // return as a tuple
            var area2 = ci2.Item1;
            var circum2 = ci2.Item2;
            output.WriteLine($"area1:{area1} circum1:{circum1}");
            output.WriteLine($"area2:{area2} circum2:{circum2}");
            Assert.Equal(area1*10, area2); // sorry xunit does not allow user message, consider FluentAssertions next time
            Assert.Equal(circum1*100, circum2);
        }
    }// class
}// namespace
