using System;
using System.Collections.Generic;
using Xunit;

namespace XUnitTests
{
    public class test_ch09
    {
        #region slice
        [Fact]
        public void test_index1_string()
        {
            string s = "hello";
            // using System.Index
            var firstIndex = new System.Index(0, false);
            var lastIndex = new System.Index(1, true); // long for ^1
            Assert.Equal('h', s[firstIndex]);
            Assert.Equal('o', s[lastIndex]);
            // using array index
            Assert.Equal('h', s[0]);
            Assert.Equal('o', s[^1]);
        }
        [Fact]
        public void test_range1_string()
        {
            string s = "hello";
            Assert.Equal(s, s[..]);      // empty range
            Assert.Equal(s, s[0..^0]);   // specify start and end
            Assert.Equal(s, s[..^0]);    // specify end only
            var start = new System.Index(1, false);
            var stop = new System.Index(1, true); // long for ^1
            Assert.Equal("ell", s[start..stop]);
            Assert.Equal("ell", s[1..^1]);
        }
        [Fact]
        public void test_slice_string()
        {
            string s = "hello";
            // string r = "olleh";
            Assert.Equal(s, s[..]);
            Assert.Equal('h', s[0]); // single index returns char, not string
            Assert.Equal("h", s[0..1]);
            Assert.Equal('o', s[^1]);
            Assert.Equal("o", s[^1..]);
            var stop = new System.Index(1, true);
            var start = new System.Index(1, false);
            Assert.Equal("ell", s[start..stop]);
            Assert.Equal("ell", s[1..^1]);
            // 
            var story = "C# is going to be great";
            var e = story[^6..^0];
            Assert.Equal("great", story[^5..^0]);
        }
        [Fact]
        public void test_slice_arrayString()
        {
            var s = new string[] { "a", "b", "c", "d", "e" };
            Assert.Equal("a", s[0]);
            Assert.Equal("e", s[^1]);
            Assert.Equal(new string[] { "b", "c" }, s[1..3]);
        }
        [Fact]
        public void test_slice_listString()
        {
            var s = new List<string> { "a", "b", "c", "d", "e" };
            Assert.Equal("a", s[0]);
            Assert.Equal("e", s[^1]);
            // CollectionAssert.Equal(new List<string>{ "b", "c" }, s[1..3]); // List<string> does not have indexers?
            // CollectionAssert.Equal(new List<string> { "b", "c" }, s.Slice());
        }
        [Fact]
        public void test_slice_enumerableString()
        {
            String[] s = new String[] { "a", "b", "c", "d", "e" };
            var ss = new ArraySegment<String>(s, 0, 1);
            Assert.Equal(new String[] { "a" }, (new ArraySegment<String>(s, 0, 1)));
            // var tt = new ArraySegment<String>(s, 1, 2);
            // Console.WriteLine(tt.Array.ToString());
            // Assert.Equal("b", new ArraySegment<String>(s, 1, 2).Array[0]);
            Assert.Equal(new String[] { "e" }, new ArraySegment<String>(s, s.Length - 1, 1));
            Assert.Equal(new List<string> { "b", "c" }, s[1..3]);
            Assert.Equal(new List<string> { "b", "c" }, new ArraySegment<string>(s, 1, 2));
        }
        [Fact]
        public void test_slice_arraySegmentString()
        {
            String[] s = new String[] { "a", "b", "c", "d", "e" };
            var seg = new ArraySegment<string>(s, 0, s.Length);
            Assert.Equal(new List<string>{"a"}, seg.Slice(0, 1));
            Assert.Equal(new List<string>{"e"}, seg.Slice(s.Length - 1, 1));
            Assert.Equal(new List<string> { "b", "c" }, seg.Slice(1, 2));
        }
        #endregion slice
    }// class test_ch09
}// namespace XUnit
