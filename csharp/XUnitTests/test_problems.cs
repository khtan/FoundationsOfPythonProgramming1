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
          If using Lookup, will output as per problem spec
    */
    /* Notes:
       1. C# String does not have sort implemented. Sorting by characters typically involve converting to array char, sort and back or Linq operators
       2. test_0002_anagrams is 2x faster than test_0003_anagramsB, difference being the SortString vs SortStringB
       3. https://hryniewski.net/2017/04/25/lookup-class-in-c-have-you-ever-tried-it discuss Lookup class. This is a readonly class that allows 1 to many
          mapping. Also, if key does not exist, it won't thrown an exception, merely return an empty collection
          The Lookup class itself is the Enumerable<Item> while it has a method .Key
          Hence, outputing the Lookup will just produce a list of Enumerables, matching the problem spec output.
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
        private IDictionary<string, IEnumerable<string>> GenerateAnagramsSortString(IEnumerable<string> list)
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
        private IDictionary<string, IEnumerable<string>> GenerateAnagramsSortStringLinq(IEnumerable<string> list)
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
        private IDictionary<string, IEnumerable<string>> GenerateAnagramsByLookup(IEnumerable<string> list){
            ILookup<string, string> lookup = list.ToLookup(word => SortString(word), word => word);
            //    .ToDictionary( g => g.Key);
            output.WriteLine(JsonConvert.SerializeObject(lookup));
            /* to print the ILookup */
            foreach(IGrouping<string, string> x in lookup)
            {
                output.WriteLine($"key={x.Key} values={x.ToString("list")}");
            }
            return lookup.ToDictionary(item => item.Key, item => item.AsEnumerable());
        }
        private IDictionary<string, IEnumerable<string>> GenerateAnagramsByGrouping(IEnumerable<string> list)
        {
            IEnumerable<IGrouping<string, string>> lookup = list.GroupBy(word => SortString(word));
            output.WriteLine(JsonConvert.SerializeObject(lookup));
            /* to print the IEnumerable<IGrouping>> */
            foreach(IGrouping<string, string> x in lookup)
            {
                output.WriteLine($"key={x.Key} values={x.ToString("list")}");
            }

            return lookup.ToDictionary(item => item.Key, item => item.AsEnumerable());
        }
        #endregion helpers
#region testhelpers
        private void TestAnagrams(Func<IEnumerable<string>, IDictionary<string, IEnumerable<string>>> generateAnagrams /* list to dictionary */,
            IEnumerable<string> list /* list of words */, 
            IDictionary<string, IEnumerable<string>> edict /* expected dictionary */)
        {
            var dict = generateAnagrams(list);
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
            var dict = GenerateAnagramsSortString(list);
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
            TestAnagrams(GenerateAnagramsSortString, list, edict);
        }// test
        [Fact]
        public void test_0003_anagramsSortStringLinq()
        {
            var list = new List<string> { "eat", "tea", "tan", "ate", "nat", "bat" };
            list.Reverse(); // Order to values in map will be different, but this does not matter
            IDictionary<string, IEnumerable<string>> edict = new Dictionary<string, IEnumerable<string>>() // expected dictionary
            {
                { "aet" , new List<string>(){"eat", "tea", "ate"} },
                { "ant" , new List<string>(){"tan", "nat"} },
                { "abt" , new List<string>(){"bat" } }
            };
            TestAnagrams(GenerateAnagramsSortStringLinq, list, edict);
        }// test
        [Fact]
        public void test_0004_anagramsByLookup()
        {
            var list = new List<string> { "eat", "tea", "tan", "ate", "nat", "bat" };
            list.Reverse(); // Order to values in map will be different, but this does not matter
            IDictionary<string, IEnumerable<string>> edict = new Dictionary<string, IEnumerable<string>>() // expected dictionary
            {
                { "aet" , new List<string>(){"eat", "tea", "ate"} },
                { "ant" , new List<string>(){"tan", "nat"} },
                { "abt" , new List<string>(){"bat" } }
            };
            TestAnagrams(GenerateAnagramsByLookup, list, edict);
        }// test
        [Fact]
        public void test_0005_anagramsByGrouping()
        {
            var list = new List<string> { "eat", "tea", "tan", "ate", "nat", "bat" };
            list.Reverse(); // Order to values in map will be different, but this does not matter
            IDictionary<string, IEnumerable<string>> edict = new Dictionary<string, IEnumerable<string>>() // expected dictionary
            {
                { "aet" , new List<string>(){"eat", "tea", "ate"} },
                { "ant" , new List<string>(){"tan", "nat"} },
                { "abt" , new List<string>(){"bat" } }
            };
            TestAnagrams(GenerateAnagramsByGrouping, list, edict);
        }// test
        [Fact(Skip = "Manual test only")]
        public void test_0005_ManualTestGenerateAnagramsC()
        {
            var list = new List<string> { "eat", "tea", "tan", "ate", "nat", "bat" };
            var dict = GenerateAnagramsByGrouping(list);
        }
#endregion tests
    }// class
}// namespace
