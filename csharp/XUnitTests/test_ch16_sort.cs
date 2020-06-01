using System;
using System.Collections.Generic;
using Xunit;
using Xunit.Abstractions;
using FluentAssertions;
using System.Collections.Immutable;
using System.Linq;

namespace XUnitTests
{
    public class test_ch16_sort
    {
        /*  1. Unlike Python, C# Sort is dependent on the class/superclass.
            For example, arrays can be sorted with the global ArraySort while lists are sorted
            with ListSort. These are mutable. For immutable sorts, consider the Immutable collections
            2. For collections like List<T>, the class method .Sort works mutably as well.
               Only Immutable collection Sort will return a sorted copy
            3. https://devblogs.microsoft.com/dotnet/please-welcome-immutablearrayt/
            4. Sort takes either a Comparison<T> or IComparer<T>
               delegate int Comparison<in T>(T x, T y), similar to Python's cmp function
               IComparer<T> is an object that implments the int Compare(T x, T y) function
            5. C# Sort currently does not have a function that extracts the comparison key from each element,
               in Python called key function
        */
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_ch16_sort(ITestOutputHelper output) { this.output = output; }

        [Fact]
        public void test_1611_List_Sort_is_mutable()
        {
            var L1 = new List<int> { 1, 7, 4, -2, 3 };
            var L2 = new List<string> { "Cherry", "Apple", "Blueberry" };

            L1.Sort(); // returns void
            var sortedL1 = new List<int> { -2, 1, 3, 4, 7 };
            L1.Should().Equal(sortedL1);

            L2.Sort();
            var sortedL2 = new List<string> { "Apple", "Blueberry", "Cherry" };
            L2.Should().Equal(sortedL2);
        }// fact
        [Fact]
        public void test_1611_ArraySort_is_mutable()
        {
            var L1 = new int[] { 1, 7, 4, -2, 3 };
            string[] L2 = new string[] { "Cherry", "Apple", "Blueberry" };

            Array.Sort(L1); // returns void
            output.WriteLine(L1.ToString());
            var sortedL1 = new int[] { -2, 1, 3, 4, 7 };
            L1.Should().Equal(sortedL1);

            Array.Sort(L2);
            output.WriteLine(L2.ToString());
            var sortedL2 = new string[] { "Apple", "Blueberry", "Cherry" };
            L2.Should().Equal(sortedL2);
        }// fact
        [Fact]
        public void test_1611_ImmutableArraySort()
        {
            var L1 = ImmutableArray.Create(1, 7, 4, -2, 3);
            var L2 = ImmutableArray.Create("Cherry", "Apple", "Blueberry");

            var sortedL1 = L1.Sort();
            var esortedL1 = new int[] { -2, 1, 3, 4, 7 };
            sortedL1.Should().Equal(esortedL1);

            var sortedL2 = L2.Sort();

            var esortedL2 = new string[] { "Apple", "Blueberry", "Cherry" };
            sortedL2.Should().Equal(esortedL2);
        }// fact
        [Fact]
        public void test_1621_reverse_parameter()
        { /* Both ImmutableArray.Sort and ImmutableList.Sort does not provide a reverse parameter
            The reversal has to be implemented with an IComparer or IComparison
            Similarly List<T>.Sort does not have reverse parameter.
            One solution is to use the .Reverse()
          */
            var L1 = ImmutableArray.Create("c", "a", "b");
            var sorted1 = L1.Sort();
            var sorted2 = L1.Sort().Reverse();
            var esorted1 = new List<string> { "a", "b", "c" };
            var esorted2 = new List<string> { "c", "b", "a" };
            sorted1.Should().Equal(esorted1);
            sorted2.Should().Equal(esorted2);
        }
        public class AbsoluteComparer: IComparer<int>
        {
            public int Compare(int x, int y)
            {
               return Math.Abs(x)-Math.Abs(y);
            }
        }
        [Fact]
        public void test_1631_Comparer()
        {
            var L1 = ImmutableList.Create(1, 7, 4, -2, 3);
            var sortedL1 = L1.Sort(new AbsoluteComparer());
            var esortedL1 = new List<int> { 1, -2, 3, 4, 7 };
            sortedL1.Should().Equal(esortedL1);
        }
        [Fact]
        public void test_1631_Comparison(){
            var L1 = ImmutableList.Create(1, 7, 4, -2, 3);
            var sortedL1 = L1.Sort((x, y) => Math.Abs(x) - Math.Abs(y));
            var esortedL1 = new List<int> { 1, -2, 3, 4, 7 };
            sortedL1.Should().Equal(esortedL1);
        }
    }// class
}// namespace
