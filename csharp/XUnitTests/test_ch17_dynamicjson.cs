using System;
using Xunit;
using Xunit.Abstractions;
using Newtonsoft.Json.Linq;
using FluentAssertions;

/* https://weblog.west-wind.com/posts/2012/aug/30/using-jsonnet-for-dynamic-json-parsing
   The tests here deal with reading/writing without any class information for Song and Album
 */
namespace XUnitTests
{
    public class test_ch17_dynamicjson
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_ch17_dynamicjson(ITestOutputHelper output) { this.output = output;  }
        void PrintJObject(string desc, JObject jo)
        { // unused, keep for reference since JObject has good ToString()
            output.WriteLine(desc);
            foreach(var item in jo)
            {
                output.WriteLine($"\t{{{item.Key}:{item.Value.ToString()}}}");
            }
        }
        [Fact]
        public void test_0001_dynamic_type()
        {
            dynamic song = new JObject();
            song.SongName = "Love at First Feel";
            song.SongLength = "3:10";
            output.WriteLine($"song: {(song as JObject).ToString()}");
        }
        [Fact]
        public void test_0002_strong_type()
        {
            var song = new JObject();
            song.Add("SongName","Dirty Deeds Done Dirt Cheap");
            song.Add("SongLength", "4:11");
            PrintJObject("song", song);
        }
        [Fact]
        public void test_0003_valueparsing()
        {
            var jsonString = @"{""Name"":""Rick"",""Company"":""West Wind"", ""Entered"":""2012-03-16T00:03:33.245-10:00""}";
            dynamic json = JValue.Parse(jsonString);

            string name = json.Name;
            string company = json.Company;
            DateTime entered = json.Entered;
            name.Should().Be("Rick");
            company.Should().Be("West Wind");
            entered.Year.Should().Be(2012);
        }
        [Fact]
        public void test_0004_valueparsing()
        {
            var jsonString = "{\r\n  \"Entered\": \"2020-05-19T16:50:23.6776358-07:00\",\r\n  \"AlbumName\": \"Dirty Deeds Done Dirt Cheap\",\r\n  \"Artist\": \"AC/DC\",\r\n  \"YearReleased\": 1976,\r\n  \"Songs\": [\r\n    {\r\n      \"SongName\": \"Dirty Deeds Done Dirt Cheap\",\r\n      \"SongLength\": \"4:11\"\r\n    },\r\n    {\r\n      \"SongName\": \"Love at First Feel\",\r\n      \"SongLength\": \"3:10\"\r\n    }\r\n  ]\r\n}";
            dynamic json = JValue.Parse(jsonString);

            string albumname = json.AlbumName;
            string song0name = json.Songs[1].SongName;
            DateTime entered = json.Entered;
            albumname.Should().Be("Dirty Deeds Done Dirt Cheap");
            song0name.Should().Be("Love at First Feel");
            entered.Year.Should().Be(2020);

        }
        [Fact]
        public void test_0010_xxx()
        {
            var jsonObject = new JObject();
            jsonObject.Add("Entered", DateTime.Now);

            dynamic album = jsonObject;
            album.AlbumName = "Dirty Deeds Done Dirt Cheap";
            album.Artist = "AC/DC";
            album.YearReleased = 1976;

            album.Songs = new JArray() as dynamic;
            dynamic song = new JObject();
            song.SongName = "Dirty Deeds Done Dirt Cheap";
            song.SongLength = "4:11";
            album.Songs.Add(song);

            song = new JObject();
            song.SongName = "Love at First Feel";
            song.SongLength = "3:10";
            album.Songs.Add(song);

            output.WriteLine(album.ToString());
        }// fact
    }// class
}// namespace
