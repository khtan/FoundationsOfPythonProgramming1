using System;
using System.Collections.Generic;
using NUnit.Framework;
using System.Threading.Tasks;


namespace tests
{
    public class Program
    {
        private static string result;
        public static void ExecuteWithoutAwait()
        {
            DoSomething(); // 1. not called with async 2. return not used
            Console.WriteLine("executeWithoutAwait: result = {0}", result);
        }
        public static async Task ExecuteWithAwait()
        {
            var s = await DoSomething(); // 1. not called with async 2. return not used
            Console.WriteLine("executeWithAwait: result = {0}", result);
        }
        static async Task<string> DoSomething()
        {
            await Task.Delay(5000); // 5 ms is too fast, result gets set before WriteLine runs
            result = "Hello FA!";
            return "FA is located in Santa Ana";
        }
    }

    public class FirstAmInterview
    {
        [Test]
        public void Test_withoutAwait()
        {
            Program.ExecuteWithoutAwait();
        }
        [Test]
        public async Task Test_withAwait()
        {
            await Program.ExecuteWithAwait();
        }
    }
}