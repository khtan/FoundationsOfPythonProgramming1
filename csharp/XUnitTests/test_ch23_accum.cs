using System;
using System.Linq;
using System.Collections.Generic;
using Xunit;
using Xunit.Abstractions;
using FluentAssertions;
using FluentAssertions.Equivalency;
using System.Diagnostics.Tracing;
using System.ComponentModel;

namespace XUnitTests
{
    public class test_ch23_accum
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_ch23_accum(ITestOutputHelper output) { this.output = output; }

        [Fact]
        public void test_2321_map()
        {
            var lst = new List<int> { 2, 5, 9 };
            var lst3 = lst.Select(n => 3 * n);
            var elst3 = new List<int> { 6, 15, 27 };
            lst3.Should().Equal(elst3);
        }// fact
        [Fact]
        public void test_2321_lc()
        {
            var lst = new List<int> { 2, 5, 9 };
            var lst3 = from n in lst select 3 * n;
            var elst3 = new List<int> { 6, 15, 27 };
            lst3.Should().Equal(elst3);
        }// fact
        [Fact(Skip = "C# List of various types not well supported")]
        public void test_2322_map() { }
        [Fact]
        public void test_2323_map()
        {
            var abbrevs = new List<string> { "usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam" };
            var abbrevs_upper = abbrevs.Select(s => s.ToUpper());
            var eabbrevs = new List<string> { "USA", "ESP", "CHN", "JPN", "MEX", "CAN", "RUS", "RSA", "JAM" };
            abbrevs_upper.Should().Equal(eabbrevs);
        }
        [Fact]
        public void test_2323_lc()
        {
            var abbrevs = new List<string> { "usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam" };
            var abbrevs_upper = from s in abbrevs select s.ToUpper();
            var eabbrevs = new List<string> { "USA", "ESP", "CHN", "JPN", "MEX", "CAN", "RUS", "RSA", "JAM" };
            abbrevs_upper.Should().Equal(eabbrevs);
        }
        [Fact]
        public void test_2331_filter()
        {
            var lst = new List<int> { 3, 4, 6, 7, 0, 1 };
            var evens = lst.Select(n => n).Where(n => n % 2 == 0);
            var elst = new List<int> { 4, 6, 0 };
            evens.Should().Equal(elst);
        }
        [Fact]
        public void test_2331_lc()
        {
            var lst = new List<int> { 3, 4, 6, 7, 0, 1 };
            var evens = from n in lst where (n % 2 == 0) select (n);
            var elst = new List<int> { 4, 6, 0 };
            evens.Should().Equal(elst);
        }
        [Fact]
        public void test_2332_filter()
        {
            var lst_check = new List<string> { "plums", "watermelon", "kiwi", "strawberries", "blueberries", "peaches", "apples", "mangos", "papaya" };
            var filter_testing = lst_check.Where(w => w.Contains("w")).Select(w => w);
            var elst = new List<string> { "watermelon", "kiwi", "strawberries" };
            filter_testing.Should().Equal(elst);
        }
        [Fact]
        public void test_2332_lc()
        {
            var lst_check = new List<string> { "plums", "watermelon", "kiwi", "strawberries", "blueberries", "peaches", "apples", "mangos", "papaya" };
            var filter_testing = from w in lst_check where w.Contains("w") select w;
            var elst = new List<string> { "watermelon", "kiwi", "strawberries" };
            filter_testing.Should().Equal(elst);
        }
        [Fact]
        public void test_2341_mapfilter()
        {
            var things = new List<int> { 3, 4, 6, 7, 0, 1 };
            var lst = things.Where(n => n % 2 == 0).Select(n => n * 2);
            var elst = new List<int> { 8, 12, 0 };
            lst.Should().Equal(elst);
        }
        [Fact]
        public void test_2341_lc()
        {
            var things = new List<int> { 3, 4, 6, 7, 0, 1 };
            var lst = from n in things where n % 2 == 0 select n * 2;
            var elst = new List<int> { 8, 12, 0 };
            lst.Should().Equal(elst);
        }
        [Fact]
        public void test_2342_dict_mapfilter() {
            var tester = new Dictionary<string, List<Dictionary<string, string>>>{
                {"info", new List<Dictionary<string,string>>{
                    new Dictionary<string,string>{ { "name","Lauren" }, { "class standing", "Junior" }, { "major", "Information Science"}},
                    new Dictionary<string,string>{ {"name","Ayo" }, {"class standing","Bachelors" }, {"major", "Information Science"}},
                    new Dictionary<string,string>{ {"name","Kathryn" }, {"class standing","Senior" }, {"major", "Sociology"}},
                    new Dictionary<string,string>{ {"name", "Nick"}, {"class standing", "Junior"}, {"major", "Computer Science"}},
                    new Dictionary<string,string>{ {"name", "Gladys"}, {"class standing", "Sophomore"}, {"major", "History"}},
                    new Dictionary<string,string>{ {"name", "Adam"}, {"major", "Violin Performance"}, {"class standing", "Senior"}}
                }}
            };
            var compri = tester["info"].Where(x => x.ContainsKey("name")).Select(x => x["name"]);
            var ecompri = new List<string> { "Lauren", "Ayo", "Kathryn", "Nick", "Gladys", "Adam"};
            compri.Should().Equal(ecompri);
        }
        [Fact]
        public void test_2342_dict_lc()
        {
            var tester = new Dictionary<string, List<Dictionary<string, string>>>{
                {"info", new List<Dictionary<string,string>>{
                    new Dictionary<string,string>{ { "name","Lauren" }, { "class standing", "Junior" }, { "major", "Information Science"}},
                    new Dictionary<string,string>{ {"name","Ayo" }, {"class standing","Bachelors" }, {"major", "Information Science"}},
                    new Dictionary<string,string>{ {"name","Kathryn" }, {"class standing","Senior" }, {"major", "Sociology"}},
                    new Dictionary<string,string>{ {"name", "Nick"}, {"class standing", "Junior"}, {"major", "Computer Science"}},
                    new Dictionary<string,string>{ {"name", "Gladys"}, {"class standing", "Sophomore"}, {"major", "History"}},
                    new Dictionary<string,string>{ {"name", "Adam"}, {"major", "Violin Performance"}, {"class standing", "Senior"}}
                }}
            };
            var compri = from x in tester["info"] where x.ContainsKey("name") select x["name"];
            var ecompri = new List<string> { "Lauren", "Ayo", "Kathryn", "Nick", "Gladys", "Adam" };
            compri.Should().Equal(ecompri);
        }
        [Fact]
        public void test_2351_zip() {
            var L1 = new List<int> { 3, 4, 5 };
            var L2 = new List<int> { 1, 2, 3 };
            var L3 = new List<int>();
            var L4 = L1.Zip(L2);
            foreach( var (x1, x2)  in L4)
            {
                L3.Add(x1 + x2);
                // L3 = L3.Append(x1 + x2).ToList(); // inefficient to create a new List each time
            }
            var eL3 = new List<int> { 4, 6, 8 };
            L3.Should().Equal(eL3);
        }
        [Fact]
        public void test_2351_zip_map()
        {
            var L1 = new List<int> { 3, 4, 5 };
            var L2 = new List<int> { 1, 2, 3 };
            var L3 = L1.Zip(L2).Select(x => x.First + x.Second);
            var eL3 = new List<int> { 4, 6, 8 };
            L3.Should().Equal(eL3);
        }
        [Fact]
        public void test_2351_zip_lc()
        {
            var L1 = new List<int> { 3, 4, 5 };
            var L2 = new List<int> { 1, 2, 3 };
            var L3 = from x in L1.Zip(L2) select x.First + x.Second;
            var eL3 = new List<int> { 4, 6, 8 };
            L3.Should().Equal(eL3);
        }
        [Fact]
        public void test_extra_zip_resultselector()
        { // Zip takes a third argument that specifies how to put the elements together, Default is an Pair
            int[] numberSequence = { 10, 20, 30, 40, 50 };
            string[] wordSequence = { "Ten", "Twenty", "Thirty", "Forty" };
            var resultSequence = numberSequence.Zip(wordSequence, (first, second) => first + "-" + second);
            string[] expectedSequence = { "10-Ten", "20-Twenty", "30-Thirty", "40-Forty" };
            resultSequence.Should().Equal(expectedSequence);
        }
    }// class
}// namespace
