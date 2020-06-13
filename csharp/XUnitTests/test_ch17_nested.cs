using Newtonsoft.Json.Linq;
using Xunit;
using Xunit.Abstractions;
using FluentAssertions;

/* Notes
1. Two JSON libraries, Json.net and ?
2. C# for Programmers Deitel 2016 does not cover Json.net
   C# 8.0 In a Nutshell does not cover Json.net
   C# DotNetCore does discuss Json.net
3. https://weblog.west-wind.com/posts/2012/aug/30/using-jsonnet-for-dynamic-json-parsing 08/30/2012
4. https://www.c-sharpcorner.com/UploadFile/manas1/json-serialization-and-deserialization-using-json-net-librar/ 11/20/2018
5. https://hub.packtpub.com/json-jsonnet/
6. http://codingsonata.com/how-to-dump-object-for-debugging-purposes-in-csharp/
*/
namespace XUnitTests
{
    public class test_ch17_nested
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_ch17_nested(ITestOutputHelper output) { this.output = output;  }
        [Fact]
        public void test_string_formatting(){
            // This string comes from python, but JValue.Parse fails if using @ formatting
            // because @ formatting causes \n to be interpreted literally
            var a_string = @"\n\n\n{\n ""resultCount"":25,\n ""results"": [\n{""wrapperType"":""track"", ""kind"":""podcast"", ""collectionId"":10892}]}";
            output.WriteLine($"a: {a_string}");
            // We can convert any \n into a real line break
            var b_string = @"
{
 ""resultCount"":25,
 ""results"": [
   {""wrapperType"":""track"",
    ""kind"":""podcast"",
    ""collectionId"":10892}]}
";
            output.WriteLine($"b: {b_string}");
            // After removing the \ns, they work
            var c_string = @"{""resultCount"":25,""results"":[{""wrapperType"":""track"",""kind"":""podcast"",""collectionId"":10892}]}";
            output.WriteLine($"c: {c_string}");
            // Or just use the string without @ formatting
            var d_string = "\n\n\n{\n \"resultCount\":25,\n \"results\": [\n{\"wrapperType\":\"track\", \"kind\":\"podcast\", \"collectionId\":10892}]}";
            output.WriteLine($"d: {d_string}");
        }
        [Fact]
        public void test_1731_json_loads() // For Json.Net, it is JValue.Parse
        {
                //// test_string_formatting shows which strings can parse, which do not
                //// This string comes from python, but JValue.Parse fails if using @ formatting
#pragma warning disable CS0219 // Variable is assigned but its value is never used
            var b_string = @"\n\n\n{\n ""resultCount"":25,\n ""results"": [\n{""wrapperType"":""track"", ""kind"":""podcast"", ""collectionId"":10892}]}";
                //// After removing the \ns, they work
            var c_string = @"{""resultCount"":25,""results"":[{""wrapperType"":""track"",""kind"":""podcast"",""collectionId"":10892}]}";
#pragma warning restore CS0219 // Variable is assigned but its value is never used
                //// Or just use the string without @ formatting
            // 1. Start with a json encoded string, including \n
            var a_string = "\n\n\n{\n \"resultCount\":25,\n \"results\": [\n{\"wrapperType\":\"track\", \"kind\":\"podcast\", \"collectionId\":10892}]}";
            output.WriteLine($"1 a_string:\n{a_string}\n:a_string");
            // 2. Use JValue.Parse
            dynamic d = JValue.Parse(a_string);
            string s = d.GetType().ToString();
            output.WriteLine($"2 type: {s}");
                //// d.GetType().ToString().Should().Be("Newtonsoft.Json.Linq.JObject"); d is dynamic, so its elements needs to be assigned to concrete type
            s.Should().Be("Newtonsoft.Json.Linq.JObject");
            // 3. d is dynamic, cannot access dictionary keys directly
            output.WriteLine($"3 d: {d.ToString()}");
            // 4. each data is considered as a JToken
            JContainer jc = d;
            var ejc = jc.AsJEnumerable();
            foreach (var k in ejc)
            {
                output.WriteLine($"4 {k}");
            }
            // 5. access results dictionary
            JContainer results = d.results;
            for(int i=0; i < results.Count; ++i)
            {
                output.WriteLine($"5 {i} -> {results[i]}");
            }
            // 6. access dictionary element
            int r = d.resultCount;
            int r2 = d["resultCount"];
            output.WriteLine($"6 resultCount: {r}");
            r.Should().Be(25);
            r2.Should().Be(25);
        }// fact
        [Fact]
        public void test_1732_json_dumps(){
        /* In python, json.dumps can be used to show the structure of a nested collection.
           http://codingsonata.com/how-to-dump-object-for-debugging-purposes-in-csharp/ gives 3 ways to do the same
           in c#
           1. Object Dumper library
           2. JSON serializer, and an extension method
           3. YAML
           However, JSON.net has its own ToString that already works very well.
         */
            string sd = "{\"key1\": {\"c\": true, \"a\": 90, \"5\": 50}, \"key2\":{\"b\": 3, \"c\": \"yes\"}}"; // string of dictionary
            dynamic d= JValue.Parse(sd);
            string formatted = d.ToString();
            output.WriteLine($"d == > {formatted} <");
            var expected = @"{
  ""key1"": {
    ""5"": 50,
    ""a"": 90,
    ""c"": true
  },
  ""key2"": {
e    ""b"": 3,
    ""c"": ""yes""
  }
}";
            formatted.Should().Equals(expected);
        }
    }// class
}// namespace
