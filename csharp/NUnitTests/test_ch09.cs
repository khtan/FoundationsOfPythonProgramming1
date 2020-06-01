using System;
using System.Collections.Generic;
using NUnit.Framework;


namespace tests
{
    public class Test_Ch09
    {
        [SetUp]
        public void Setup()
        {
        }
        #region slice
        /*  https://www.codejourney.net/2019/02/csharp-8-slicing-indexes-ranges/
        c# indexing and ranging is implemented very differently from python.
        The System.Index is a class that represents an index type.
        The Index constructor has a fromEnd boolean to indicate the direction of the index

        This allows [<index type variable>] to be easily implemented
        The System.Range represents a range. It contains a Start and Stop index.
        Range does not have a direction, ie Start is always less than Stop.
        There is no <step> variable that can be set negative to move backwards.

        In Python, -X is used to indicate reversal of index. For C#, instead of allowing -X,
        they introduced ^X. However, ^X cannot be entered because it does not have a type, so only 
        a cosmetic usage.

        While Python has only one splice function, C# has several but none has the step 
           Span<T>.Slice(Int32 start), (Int32 start, Int32 stop)
           System.ArraySegment<T>.Slice(Int32 start), (Int32 start, Int32 stop)
              IEnumerable<T> derives from ArraySegment<T>
           System.Memory<T>.Slice(Int32 start), (Int32 start, Int32 stop)
           System.Buffer.ReadOnlySequence<T>.Slice

        */
        [Test]
        public void test_index1_string()
        {
            string s = "hello";
            // using System.Index
            var firstIndex = new System.Index(0, false);
            var lastIndex = new System.Index(1, true); // long for ^1
            Assert.AreEqual('h', s[firstIndex]);
            Assert.AreEqual('o', s[lastIndex]);
            // using array index
            Assert.AreEqual('h', s[0]);
            Assert.AreEqual('o', s[^1]);
        }
        [Test]
        public void test_range1_string()
        {
            string s = "hello";
            Assert.AreEqual(s, s[..]);      // empty range
            Assert.AreEqual(s, s[0..^0]);   // specify start and end
            Assert.AreEqual(s, s[..^0]);    // specify end only
            var start = new System.Index(1, false);
            var stop = new System.Index(1, true); // long for ^1
            Assert.AreEqual("ell", s[start..stop]);
            Assert.AreEqual("ell", s[1..^1]);
        }
        [Test]
        public void test_cannot_delete_and_insert_string()
        { // This means that range will not produce a mutable string
          string s = "hello";
            string ss = s[1..^1];
            // s[1..^1] = ''; // LHS must be variable, property or indexer
        }
        [Test]
        public void test_slice_string()
        {
            string s = "hello";
            // string r = "olleh";
            Assert.AreEqual(s, s[..]);
            Assert.AreEqual('h', s[0]); // single index returns char, not string
            Assert.AreEqual("h", s[0..1]);
            Assert.AreEqual('o', s[^1]);
            Assert.AreEqual("o", s[^1..]);
            var stop = new System.Index(1, true);
            var start = new System.Index(1, false);
            Assert.AreEqual("ell", s[start..stop]);
            Assert.AreEqual("ell", s[1..^1]);
            // 
            var story = "C# is going to be great";
            var e = story[^6..^0];
            Assert.AreEqual("great", story[^5..^0]);
        }
        [Test]
        public void test_slice_arrayString()
        {
            var s = new string[] { "a", "b", "c", "d", "e" };
            Assert.AreEqual("a", s[0]);
            Assert.AreEqual("e", s[^1]);
            CollectionAssert.AreEqual(new string[] { "b", "c" }, s[1..3]);
        }
        [Test]
        public void test_slice_listString()
        {
            var s = new List<string> { "a", "b", "c", "d", "e" };
            Assert.AreEqual("a", s[0]);
            Assert.AreEqual("e", s[^1]);
            // CollectionAssert.AreEqual(new List<string>{ "b", "c" }, s[1..3]); // List<string> does not have indexers?
            // CollectionAssert.AreEqual(new List<string> { "b", "c" }, s.Slice());
        }
        [Test]
        public void test_slice_enumerableString()
        {
            String[] s = new String[] { "a", "b", "c", "d", "e" };
            var ss = new ArraySegment<String>(s, 0, 1);
            Assert.AreEqual(new String[] { "a" }, (new ArraySegment<String>(s, 0, 1)));
            // var tt = new ArraySegment<String>(s, 1, 2);
            // Console.WriteLine(tt.Array.ToString());
            // Assert.AreEqual("b", new ArraySegment<String>(s, 1, 2).Array[0]);
            Assert.AreEqual(new String[] { "e" }, new ArraySegment<String>(s, s.Length - 1, 1));
            CollectionAssert.AreEqual(new List<string> { "b", "c" }, s[1..3]);
            CollectionAssert.AreEqual(new List<string> { "b", "c" }, new ArraySegment<string>(s, 1, 2));
        }
        [Test]
        public void test_slice_arraySegmentString()
        {
            String[] s = new String[] { "a", "b", "c", "d", "e" };
            var seg = new ArraySegment<string>(s, 0, s.Length);
            CollectionAssert.AreEqual(new List<string>{"a"}, seg.Slice(0, 1));
            CollectionAssert.AreEqual(new List<string>{"e"}, seg.Slice(s.Length - 1, 1));
            CollectionAssert.AreEqual(new List<string> { "b", "c" }, seg.Slice(1, 2));
        }
        #endregion slice
    }
}