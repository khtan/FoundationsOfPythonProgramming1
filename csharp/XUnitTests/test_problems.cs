using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using Xunit;
using Xunit.Abstractions;
using System.Linq;
using FluentAssertions;

namespace XUnitTests
{
/* The problem:
   Given an array of strings, group the words that form ANAGRAMs together.
   - Anagragms are words that are made of same set of characters appearing in various order.
   Example:
   Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
   Output:
   [
   ["ate","eat","tea"],
   ["nat","tan"],
   ["bat"]
   ]
   Modifications:
   1. Output the entire map, instead of just the values

   Lessons:
   1. C# String does not have sort implemented. Sorting by characters typically involve converting to array char, sort and back or Linq operators
   2. test_0002_anagrams is 2x faster than test_0003_anagramsB, difference being the SortString vs SortStringB
*/
    public class test_problems
    {
#region internal
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_problems(ITestOutputHelper output) { this.output = output;  }
#endregion internal
#region helpers
        private string SortString(string word){
            var listChars = new List<char>(word.ToCharArray());
            listChars.Sort();
            var canonicalKey = new string(listChars.ToArray());
            return canonicalKey;
        }
        private string SortStringLinq(string word){
            return new string (word.OrderBy(c => c).ToArray());
        }
        private IDictionary<string, IEnumerable<string>> GenerateAnagrams(IEnumerable<string> list)
        {
            var dict = new Dictionary<string, IEnumerable<string>>();
            foreach (string word in list)
            {
                var canonicalKey = SortString(word);
                if (dict.ContainsKey(canonicalKey))
                {
                    dict[canonicalKey] = dict[canonicalKey].Append(word);
                } else
                {
                    dict[canonicalKey] = new List<string>() { word };
                }
            }
            return dict;
        }
        private IDictionary<string, IEnumerable<string>> GenerateAnagramsB(IEnumerable<string> list)
        { // Using SortStringLinq instead of SortString
            var dict = new Dictionary<string, IEnumerable<string>>();
            foreach (string word in list)
            {
                var canonicalKey = SortStringLinq(word);
                if (dict.ContainsKey(canonicalKey))
                {
                    dict[canonicalKey] = dict[canonicalKey].Append(word);
                } else
                {
                    dict[canonicalKey] = new List<string>() { word };
                }
            }
            return dict;
        }
        private IDictionary<string, IEnumerable<string>> GenerateAnagramsC(IEnumerable<string> list){
            var x = list.Select(word => Tuple.Create(SortString(word), word));
            return null;
        }
#endregion helpers
#region testhelpers
        private void TestAnagrams(IEnumerable<string> list /* list of words */, IDictionary<string, IEnumerable<string>> edict/* expected dictionary */){
            var dict = GenerateAnagrams(list);
            output.WriteLine(JsonConvert.SerializeObject(dict));
            output.WriteLine(JsonConvert.SerializeObject(edict));

            // Note: edict.Should().Equal(dict)
            // fails because List comparison is by reference despite documentation
            // that says comparison is via the Equals, while below works
            // edict["aet"].Should().Equal(dict["aet"]);
            edict.Should().BeEquivalentTo(dict);

        }
        private void TestAnagramsB(IEnumerable<string> list /* list of words */, IDictionary<string, IEnumerable<string>> edict/* expected dictionary */){
            var dict = GenerateAnagramsB(list);
            output.WriteLine(JsonConvert.SerializeObject(dict));
            output.WriteLine(JsonConvert.SerializeObject(edict));

            // Note: edict.Should().Equal(dict)
            // fails because List comparison is by reference despite documentation
            // that says comparison is via the Equals, while below works
            // edict["aet"].Should().Equal(dict["aet"]);
            edict.Should().BeEquivalentTo(dict);

        }
#endregion testhelpers
#region tests
        [Fact]
        public void test_0001_empty_anagrams()
        {
            var list = new List<string>();
            var dict = GenerateAnagrams(list);
            output.WriteLine(JsonConvert.SerializeObject(dict));
            dict.Should().BeEmpty();
        }
        [Fact]
        public void test_0002_anagrams()
        {
            var list = new List<string> { "eat", "tea", "tan", "ate", "nat", "bat" };
            IDictionary<string, IEnumerable<string>> edict = new Dictionary<string, IEnumerable<string>>() // expected dictionary
            {
                { "aet" , new List<string>(){"eat", "tea", "ate"} },
                { "ant" , new List<string>(){"tan", "nat"} },
                { "abt" , new List<string>(){"bat" } }
            };
            TestAnagrams(list, edict);
        }// test
        [Fact]
        public void test_0003_anagramsB()
        {
            var list = new List<string> { "eat", "tea", "tan", "ate", "nat", "bat" };
            list.Reverse(); // Order to values in map will be different, but this does not matter
            IDictionary<string, IEnumerable<string>> edict = new Dictionary<string, IEnumerable<string>>() // expected dictionary
            {
                { "aet" , new List<string>(){"eat", "tea", "ate"} },
                { "ant" , new List<string>(){"tan", "nat"} },
                { "abt" , new List<string>(){"bat" } }
            };
            TestAnagrams(list, edict);
        }// test
#endregion tests
    }// class
}// namespace
