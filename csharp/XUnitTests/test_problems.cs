using Newtonsoft.Json;
using System.Text;
using System.Collections.Generic;
using System.Collections.Immutable;
using Xunit;
using Xunit.Abstractions;
using System.Linq;
using FluentAssertions;

namespace XUnitTests
{
    public class test_problems
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_problems(ITestOutputHelper output) { this.output = output;  }
        // private IDictionary<string, IEnumerable<string>> GenerateAnagrams(IEnumerable<string> list)
        private Dictionary<string, List<string>> GenerateAnagrams(IEnumerable<string> list)
        {
            var dict = new Dictionary<string, List<string>>();
            foreach (string word in list)
            {
                var listChars = new List<char>(word.ToCharArray());
                listChars.Sort();
                var canonicalKey = new string(listChars.ToArray());
                if (dict.ContainsKey(canonicalKey))
                {
                    dict[canonicalKey].Add(word);
                } else
                {
                    dict[canonicalKey] = new List<string>() { word };
                }
            }
            return dict;
        }
        /*
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
         */
        [Fact]
        public void test_0001_empty_anagrams()
        {
            var list = new List<string>();
            var dict = GenerateAnagrams(list);
            output.WriteLine(JsonConvert.SerializeObject(dict));
        }
        [Fact]
        public void test_0002_some_anagrams()
        {
            var list = new List<string> { "eat", "tea", "tan", "ate", "nat", "bat" };
            var dict = GenerateAnagrams(list);
            output.WriteLine(JsonConvert.SerializeObject(dict));
            Dictionary<string, List<string>> edict = new Dictionary<string, List<string>>() // expected dictionary
            {
                { "aet" , new List<string>(){"eat", "tea", "ate"} },
                { "ant" , new List<string>(){"tan", "nat"} },
                { "abt" , new List<string>(){"bat" } }
            };
            output.WriteLine(JsonConvert.SerializeObject(edict));
            // Note: edict.Should().Equal(dict) 
            // fails because List comparison is by reference despite documentation
            // that says comparison is via the Equals, while below works
            // edict["aet"].Should().Equal(dict["aet"]);
            edict.Should().BeEquivalentTo(dict);
        }// test
    }// class
}// namespace
