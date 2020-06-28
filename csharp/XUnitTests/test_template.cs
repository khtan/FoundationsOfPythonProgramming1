using System;
using Xunit;
using Xunit.Abstractions;

namespace XUnitTests
{
    public class test_template
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_template(ITestOutputHelper output) { this.output = output;  }

        [Fact]
        public void test_0001_helloworld()
        {
            output.WriteLine("hello world");
        }// fact
    }// class
}// namespace
