using System;
// using System.Collections.Generic;
using System.Linq;
using Xunit;
using Xunit.Abstractions;
using LanguageExt.Common;
// using Newtonsoft.Json;
// using FluentAssertions;

namespace XUnit_LanguageExt
{
    public class Test_langext
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public Test_langext(ITestOutputHelper output) { this.output = output; }
        static Result<int> Divide(int numerator, int denominator)
        {
            if (denominator == 0)
            {
                return new Result<int>(new Exception("Division by zeron"));
            }
            return new Result<int>(numerator / denominator);
        }
        static void ExerciseDivide(ITestOutputHelper output, int numerator, int denominator)
        {
            Result<int> res = Divide(numerator, denominator);
            var m = res.Match<int>(
                Succ: (value) => {
                    output.WriteLine($"Result {value}");
                    return value;
                },
                Fail: (ex) => {
                    output.WriteLine($"Error: {ex.Message}");
                    return 0;
                }
            );
            output.WriteLine($"m: {m}");
        }
        [Fact]
        public void Test_0001()
        {
            ExerciseDivide(this.output, 10, 2);
        }
        [Fact]
        public void Test_0002()
        {
            ExerciseDivide(this.output, 10, 0);
        }
    }// class
}// namespace

