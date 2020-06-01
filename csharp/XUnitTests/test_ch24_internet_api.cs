using System;
using System.Collections.Generic;
using Xunit;
using Xunit.Abstractions;
using RestSharp;
using System.Linq;
using Newtonsoft.Json.Linq;
using FluentAssertions;
using System.Text.RegularExpressions;
using FluentAssertions.Execution;

namespace XUnitTests
{ /* Q) R there any books on RestSharp?
        Library Genesis search - nothing
        Amazon serach - nothing
        Manning - Microservices in .NET Core
        Apress - nothing
        Pragmatic Programmer - nothing
     1) Articles
        a) https://stackify.com/restsharp/
        b) https://groups.google.com/forum/#!forum/restsharp
     2) Extracting results from Response is a good application for LinqToJson
        https://www.newtonsoft.com/json/help/html/LINQtoJSON.htm is the basis for some tests to
        learn usage of Linq to Json.
        The basic class is JObject. The inheritance hierarchy shows that
           System.Object
              Newtonsoft.Json.Linq.JToken
                 Newtonsoft.Json.Linq.JContainer
                    Newtonsoft.Json.Linq.JArray
                    Newtonsoft.Json.Linq.JConstructor
                    Newtonsoft.Json.Linq.JObject
                    Newtonsoft.Json.Linq.JProperty
         a) JObject has same functionality as JArray
  */
    public class test_ch24_internet_api
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        private readonly string flickr_key = "464b86270211da70af8a940c0ed6c219";
        public test_ch24_internet_api(ITestOutputHelper output) { this.output = output;  }
    #region internet
        [Fact]
        public void test_2461_get()
        {
            var client = new RestClient("https://api.datamuse.com");
            var request = new RestRequest("/words?rel_rhy=funny", DataFormat.Json);
            IRestResponse response = client.Get(request);
            output.WriteLine($"type of response: {response.GetType()}");
            var first50chars = new String(response.Content.Take(50).ToArray());
            output.WriteLine($"first 50 chars: {first50chars}");
            output.WriteLine($"url: {response.ResponseUri}");
            var eUri = "https://api.datamuse.com/words?rel_rhy=funny";
            response.ResponseUri.Should().Be(eUri);

            JArray x = JArray.Parse(response.Content);
            string firstItem = x[0].ToString();
            firstItem = firstItem.Replace("\r", "").Replace("\n", "");
            output.WriteLine($"first item in list: {firstItem}");
            string efirstItem = "{  \"word\": \"money\",  \"score\": 4415,  \"numSyllables\": 2}";
            firstItem.Should().Be(efirstItem);
            var numItems = x.Count;
            numItems.Should().Be(84);
            // skip dumping the entire list because its values changes all the time?
        }// fact
        [Fact]
        public void test_2463_get()
        { // using params
            var client = new RestClient("https://api.datamuse.com");
            var request = new RestRequest("/words", DataFormat.Json);
            request.AddParameter("rel_rhy", "funny");
            IRestResponse response = client.Get(request);
            output.WriteLine($"url: {response.ResponseUri}");
            var eUri = "https://api.datamuse.com/words?rel_rhy=funny";
            response.ResponseUri.Should().Be(eUri);
        }
        IEnumerable<string> get_rhymes(string word)
        {
            var baseurl = "https://api.datamuse.com/words";
            var client = new RestClient(baseurl);
            var request = new RestRequest()
                .AddParameter("rel_rhy", word)
                .AddParameter("max", 3);
            var resp = client.Get(request);
            IEnumerable<JToken> listDict = JArray.Parse(resp.Content);
            var z = listDict.Select(dict => dict["word"].ToString());
            /* Just to show the types in a loop
            var z = new List<string>();
            foreach(JToken j in x)
            {
                z.Add(j["word"].ToString());
            }
            */
            return z;
        }
        [Fact]
        public void test_2482_test_get_rhymes()
        {
            var rhymes = get_rhymes("funny");
            var erhymes = new List<string> { "money", "honey", "sunny" };
            rhymes.Should().Equal(erhymes);
        }
        [Fact]
        public void test_2411_itunes()
        {
            var baseurl = "https://itunes.apple.com";
            var client = new RestClient(baseurl);
            var request = new RestRequest("/search", DataFormat.Json)
                .AddParameter("term", "Ann Arbor")
                .AddParameter("entity", "podcast");
            var resp = client.Get(request);
            var dict = JContainer.Parse(resp.Content); // resp.Content is dictionary, not array
            var resultsDict = dict["results"];
            // resultsDict.Count().Should().Be(34); // same as Python, this is unreliable
            // for visual check
            foreach(var trackDict in resultsDict) {
                output.WriteLine($"{trackDict["trackName"]}");
            }
        }
         JToken get_flickr_data(string tags_string){
            var baseurl = "https://api.flickr.com/services";
            var client = new RestClient(baseurl);
            var request = new RestRequest("/rest", DataFormat.Json)
                .AddParameter("api_key", flickr_key)
                .AddParameter("tags", tags_string)
                .AddParameter("tag_mode", "all")
                .AddParameter("method", "flickr.photos.search")
                .AddParameter("per_page", 5)
                .AddParameter("media", "photos")
                .AddParameter("format", "json")
                .AddParameter("nojsoncallback", 1);
            var resp = client.Get(request);
            output.WriteLine($"statuscode = {resp.StatusCode}");
            resp.StatusCode.Should().Be(System.Net.HttpStatusCode.OK);
            output.WriteLine($"url: {resp.ResponseUri}");
            JToken dict = JToken.Parse(resp.Content);
            return dict;
        }
        [Fact]
        public void test_2412_flickr(){
            var result_river_mts = get_flickr_data("river,mountains");
            // Some code to open up a few photos that are tagged with the mountains and river tags...
            var photos = result_river_mts["photos"]["photo"];
            photos.Count().Should().Be(5);
            foreach(var photo in photos){
                var owner = photo["owner"];
                var photo_id = photo["id"];
                var url = $"https://www.flickr.com/photos/{owner}/{photo_id}";
                output.WriteLine(url);
            }
        }
    #endregion internet
    #region Linq to Json
        [Fact]
        public void test_0001_l2j()
        {
            JObject o = JObject.Parse(@"{
  'CPU': 'Intel',
  'Drives': [
    'DVD read/writer',
    '500 gigabyte hard drive'
  ]
}");
            output.WriteLine($"o.GetType == {o.GetType()}");
            JContainer jA = o as JContainer;
            output.WriteLine($"jA.GetType == {jA.GetType()}");
            JToken jT = o as JToken;
            output.WriteLine($"jT.GetType == {jT.GetType()}");

            // Start with plain one liner
            string cpu = (string)o["CPU"]; // Intel
            // Check out the types
            JToken jt = o["CPU"];
            string cpu2 = jt.ToString();
            cpu.Should().Be(cpu2);

            // plain
            string firstDrive = (string)o["Drives"][0]; // DVD read/writer
            // typed
            var jt2 = o["Drives"][0]; // Why does o also show up as JToken, not JArray or JContainer?
            // JArray : JContainer, IList<JToken>, ICollection<JToken>, IEnumerable<JToken>, IEnumerable
            string firstDrive2 = jt2.ToString();
            firstDrive.Should().Be(firstDrive2);

            // plain
            IList<string> allDrives = o["Drives"].Select(t => (string)t).ToList(); 
            IEnumerable<string> listDrives = o["Drives"].Select(t => (string)t);
            allDrives.Should().Equal(listDrives);
        }
    #endregion Linq to Json
    }// class
}// namespace
