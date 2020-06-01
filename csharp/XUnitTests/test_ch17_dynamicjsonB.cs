using System;
using System.Collections.Generic;
using Xunit;
using Xunit.Abstractions;
using Newtonsoft.Json;
using FluentAssertions;

/* https://weblog.west-wind.com/posts/2012/aug/30/using-jsonnet-for-dynamic-json-parsing
   The tests here deal with reading/writing with any class information for Song and Album
 */
namespace XUnitTests
{
    public class Song{ public string SongName {get; set;} public string SongLength {get; set;} }
    public class Album {
        public DateTime Entered {get; set;}
        public string AlbumName {get; set;}
        public string Artist {get; set;}
        public int YearReleased {get; set;}
        public List<Song> Songs {get; set;}
    }
    public class test_ch17_dynamicjsonB
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_ch17_dynamicjsonB(ITestOutputHelper output) { this.output = output;  }

        [Fact]
        public void test_0004_StronglyTypedSerialization()
        {

            // Demonstrate deserialization from a raw string
            var album = new Album()
                {
                    AlbumName = "Dirty Deeds Done Dirt Cheap",
                    Artist = "AC/DC",
                    Entered = DateTime.Now,
                    YearReleased = 1976,
                    Songs =  new List<Song>() 
                    {
                        new Song()
                        {
                            SongName = "Dirty Deeds Done Dirt Cheap",
                            SongLength = "4:11"
                        },
                        new Song()
                        {
                            SongName = "Love at First Feel",
                            SongLength = "3:10"
                        }
                    }
                };
            // "{\r\n  \"Entered\": \"2020-05-19T16:50:23.6776358-07:00\",\r\n  \"AlbumName\": \"Dirty Deeds Done Dirt Cheap\",\r\n  \"Artist\": \"AC/DC\",\r\n  \"YearReleased\": 1976,\r\n  \"Songs\": [\r\n    {\r\n      \"SongName\": \"Dirty Deeds Done Dirt Cheap\",\r\n      \"SongLength\": \"4:11\"\r\n    },\r\n    {\r\n      \"SongName\": \"Love at First Feel\",\r\n      \"SongLength\": \"3:10\"\r\n    }\r\n  ]\r\n}"
            // serialize to string
            string json2 = JsonConvert.SerializeObject(album,Formatting.Indented);
            output.WriteLine("----- begin json2 -----");
            output.WriteLine(json2);
            output.WriteLine("----- end json2 -----");
            // make sure we can serialize back
            var album2 = JsonConvert.DeserializeObject<Album>(json2);

            album2.Should().NotBeNull();
            album2.AlbumName.Should().Equals("Dirty Deeds Done Dirt Cheap");
            album2.Songs.Count.Should().Be(2);
        }
    }// class
}// namespace
