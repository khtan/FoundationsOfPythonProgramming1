﻿using System;
using System.Globalization;
using System.Threading.Tasks;
using System.Collections.Generic;
using System.Text;
using Xunit;
using Xunit.Abstractions;

namespace XUnitTests
{

    public class Program {
        private static string result;
        public static void ExecuteWithoutAwait(ITestOutputHelper output)
        {
            DoSomething(); // 1. not called with async 2. return not used
            output.WriteLine("executeWithoutAwait: result = {0}", result);
        }
        public static async Task ExecuteWithAwait(ITestOutputHelper output)
        {
            var s = await DoSomething(); // 1. not called with async 2. return not used
            output.WriteLine("executeWithAwait: result = {0}", result);
        }
        static async Task<string> DoSomething()
        {
            await Task.Delay(50);
            result = "Hello FA!";
            return "FA is located in Santa Ana";
        }
    }

    public class FirstAmInterview
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public FirstAmInterview(ITestOutputHelper output) { this.output = output; }

        [Fact]
        public void Test_withoutAwait()
        {
            Program.ExecuteWithoutAwait(this.output);
        }
        [Fact]
        public async void Test_withAwait()
        {
            await Program.ExecuteWithAwait(this.output);
        }
    }
}
