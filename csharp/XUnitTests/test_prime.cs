﻿using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;
using Xunit;
using Xunit.Abstractions;
using System.Runtime.CompilerServices;
using Newtonsoft.Json;
using System.ComponentModel;

namespace XUnitTests
{
    public static class Extensions1
    {
        // IEnumerable does not have count before 4.7.1
        public static string ToString<T>(this IEnumerable<T> list, string desc = "list")
        {
            StringBuilder returnString = new StringBuilder(desc + "<" + typeof(T).Name + ">{");
            int numElements = list.Count();
            if (numElements == 0) returnString.Append("empty");
            else
            {
                for (int i = 0; i < numElements - 1; i++) { returnString.Append(list.ElementAt(i) + ","); }
                returnString.Append(list.ElementAt(numElements - 1));
            }
            returnString.Append("}");
            return returnString.ToString();
        }
    } // class Extensions

    public class test_prime
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_prime(ITestOutputHelper output) { this.output = output; }
        private IEnumerable<int> Primes(int upTo = 10000)
        {
            var ints = Enumerable.Range(2, upTo);
            return ints.Where(
                x => !ints.TakeWhile(y => y < x)
                .Any(y => x % y == 0)
            );
        }
        [Fact]
        public void test_0001_helloworld()
        {
            output.WriteLine("hello world");
        }// fact
        [Fact]
        public void test_0002_xxxx()
        {
            var maxNum = 9;
            var ints = Enumerable.Range(2, maxNum);
            var list1 = ints.ToList();
            // output.WriteLine(list1.ToString("list1"));
            var list2 = list1.Select(x => ints.TakeWhile(y => y < x)).ToList();
            // var list2 = list1.Where(x => !ints.TakeWhile(y => y < x).Any(y => x % y == 0));
            foreach (var listX in list2)
            {
                output.WriteLine(listX.ToString("listX"));
                if (listX.Count() == 0) {
                    output.WriteLine("empty");
                } else {
                    var x = listX.Max();
                    var xb = !listX.Any(y => {
                        var b1 = (x % y == 0);
                        output.WriteLine($"   any: x={x} y={y} b1={b1}");
                        return b1;
                    });
                    output.WriteLine($"x={x} xb={xb}");
                }
            }
            /*
            var list3 = list1.Where(x => {
                var rb = !ints.TakeWhile(y => {
                    var rc = y < x;
                    output.WriteLine($"    tw:       x={x} y={y} b1={rc}");
                    return rc;
                }).Any(y => {
                    var rd = x % y == 0;
                    output.WriteLine($"    an:       x={x} y={y} b2={rd}");
                    return rd;
                });
                if (x == 2) { output.WriteLine($"--- x={x} b0={rb}"); } else { output.WriteLine($"    x={x} b0={rb}"); }
                return rb;  
            });
            output.WriteLine(list3.ToString("list3"));
            */
        }
        [Fact]
        public void test_0003_two_ways_to_print_listOflist()
        {
            var maxNum = 4;
            var ints = Enumerable.Range(2, maxNum);
            var list1 = ints.ToList();
            // output.WriteLine(list1.ToString("list1"));
            var list2 = list1.Select(x => ints.TakeWhile(y => y < x)).ToList();
            // var list2 = list1.Where(x => !ints.TakeWhile(y => y < x).Any(y => x % y == 0));
            output.WriteLine("1. Using JsonConvert");
            output.WriteLine(JsonConvert.SerializeObject(list2));
            output.WriteLine("2. Loop with listX.ToString");
            foreach (var listX in list2)
            {
                output.WriteLine(listX.ToString("listX"));
            }
        }
        [Fact]
        public void test_0004_xxxx()
        {
            /*  Range(start=2,count=4) generates 2, 3, 4, 5
                ints.Where( x => !ints.TakeWhile(y => y < x).Any(y => x % y == 0));
                ints.TakeWhile( y => y < x )
                   x = 2, 2 < 2, no => {}
                   x = 3, 2 < 3, 3 < 3, no => {2}
                   x = 4, 2 < 4, 3 < 4, 4 < 4, no => {2,3}
                   x = 5,                        => {2,3,4}

                 {}.Any => false
                 {2}.Any => true
                 {2,3}.Any => true
                 {2,3,4}.Any => false

            So, the !Any will return List of falses, ie 5, 3, 2
             */
            var upTo = 4;
            var ints = Enumerable.Range(2, upTo);


            var x1 = new List<int> { 2, 3, 4 };
            var b1 = x1.Any(y => 5 % y == 0);
            output.WriteLine($"x1={x1.ToString("x1")} b1={b1}"); // 5 == false
            var x2 = new List<int> { 2, 3 };
            var b2 = x2.Any(y => 4 % y == 0);
            output.WriteLine($"x2={x2.ToString("x2")} b2={b2}"); // 4 == true
            var x3 = new List<int> { 2 };
            var b3 = x3.Any(y => 3 % y == 0);
            output.WriteLine($"x3={x3.ToString("x3")} b3={b3}"); // 3 == false
            var x4 = new List<int> {};
            var b4 = x4.Any(y => 2 % y == 0);
            output.WriteLine($"x4={x4.ToString("x4")} b4={b4}"); // 2 == false
            var primes = ints.Where(
                              x => !ints.TakeWhile(y => y < x) // creates lists of elements
                              .Any(y => x % y == 0) // true if any element pass the criteria, false if all elements fail criteria
                              );
            output.WriteLine(primes.ToString("primes"));
        }// fact
        [Fact]
        public void test_0005_xxxx()
        {
            var upTo = 4;
            var ints = Enumerable.Range(2, upTo);
            var primes = ints.Where(
               x => {
                   var b = !ints.TakeWhile(y => {
                       var b2 = y < x;
                       output.WriteLine($"   takewhile: y:{y} x:{x} b2:{b2}");
                       return b2;
                   }).Any(y => {
                       var b1 = x % y == 0;
                       output.WriteLine($"      any: y:{y} x:{x} b1:{b1}");
                       return b1;
                   });
                   output.WriteLine($"where: x={x} b={b}");
                   return b;
               }
            ).ToList(); // otherwise calling Primes in output will run code again
            output.WriteLine(primes.ToString("primes"));
        }// fact
        [Fact]
        public void test_0006_xxxx()
        {
/* Transcript
   Test Name:	XUnitTests.test_prime.test_0006_xxxx
   Test Outcome:	Passed
   Result StandardOutput:

   takewhile: y:2 x:2 b2:False
   whereA: li<Int32>{empty}
   whereB: x=2 b=True

   takewhile: y:2 x:3 b2:True
   takewhile: y:3 x:3 b2:False
   whereA: li<Int32>{2}
   any: y:2 x:3 b1:False
   whereB: x=3 b=True

   takewhile: y:2 x:4 b2:True
   takewhile: y:3 x:4 b2:True
   takewhile: y:4 x:4 b2:False
   whereA: li<Int32>{2,3}
   any: y:2 x:4 b1:True
   whereB: x=4 b=False

   takewhile: y:2 x:5 b2:True
   takewhile: y:3 x:5 b2:True
   takewhile: y:4 x:5 b2:True
   takewhile: y:5 x:5 b2:False
   whereA: li<Int32>{2,3,4}
   any: y:2 x:5 b1:False
   any: y:3 x:5 b1:False
   any: y:4 x:5 b1:False
   whereB: x=5 b=True

   primes<Int32>{2,3,5}
*/
            var upTo = 4;
            var ints = Enumerable.Range(2, upTo);
            var primes = ints.Where(
                x =>
                {
                    IEnumerable<int> li = ints.TakeWhile(y =>
                    {
                        var b2 = y < x;
                        output.WriteLine($"   takewhile: y:{y} x:{x} b2:{b2}");
                        return b2;
                    }).ToList(); // this is needed
                    output.WriteLine($"whereA: {li.ToString("li")}");
                    var b = !li.Any(y =>
                    {
                        var b1 = x % y == 0;
                        output.WriteLine($"      any: y:{y} x:{x} b1:{b1}");
                        return b1;
                    });
                    output.WriteLine($"whereB: x={x} b={b}");
                    return b;
                }
                ).ToList(); // also needed, otherwise calling Primes in output will run code again
            output.WriteLine(primes.ToString("primes"));
        }// fact
    }// class
}// namespace
