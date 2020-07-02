using System;
using System.Collections.Generic;
using System.Linq;
using Xunit;
using Xunit.Abstractions;
using Newtonsoft.Json;
using FluentAssertions;

namespace XUnitTests
{
    public class PetOwner
    {
        public string Name { get; set; }
        public List<string> Pets { get; set; }
    }
    public class PetOwnerAndName
    {
        public PetOwner petOwner { get; set; }
        public string petName { get; set; }
    }
    public class StringPetOwner
    {
        public string Owner { get; set; }
        public string Pet { get; set; }
    }
    public class test_SelectMany
    {
/* 1. https://docs.microsoft.com/en-us/dotnet/api/system.linq.enumerable.selectmany?view=netcore-3.1
2. There are 4 extension methods for SelectMany, two of which are the indexed version of the other
   SMa:          public static IEnumerable<TResult> SelectMany<TSource, TResult>(this IEnumerable<TSource> source, Func<TSource, int, IEnumerable<TResult>> selector);
   SMaWithIndex: public static IEnumerable<TResult> SelectMany<TSource, TResult>(this IEnumerable<TSource> source, Func<TSource, IEnumerable<TResult>> selector);
   SMb:          public static IEnumerable<TResult> SelectMany<TSource, TCollection, TResult>(this IEnumerable<TSource> source, Func<TSource, IEnumerable<TCollection>> collectionSelector, Func<TSource, TCollection, TResult> resultSelector);
   SMbWithIndex: public static IEnumerable<TResult> SelectMany<TSource, TCollection, TResult>(this IEnumerable<TSource> source, Func<TSource, int, IEnumerable<TCollection>> collectionSelector, Func<TSource, TCollection, TResult> resultSelector);

   So, SMa and SMb are the 2 signatures to study
*/
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        public test_SelectMany(ITestOutputHelper output) { this.output = output;  }

        // data in testclass as context
        private readonly PetOwner[] petOwners =
            { new PetOwner { Name="Higa", Pets = new List<string>{ "Scruffy", "Sam" } },
                  new PetOwner { Name="Ashkenazi", Pets = new List<string>{ "Walker", "Sugar" } },
                  new PetOwner { Name="Price", Pets = new List<string>{ "Scratches", "Diesel" } },
                  new PetOwner { Name="Hines", Pets = new List<string>{ "Dusty" } }
        };
        [Fact]
        public void test_0001_SelectManySMa()
        {
            // template disambiguated: var query = petOwners.SelectMany<PetOwner, string>(Func<PetOwner, IEnumerable<string>)
            var query = petOwners.SelectMany(petOwner => petOwner.Pets);
            output.WriteLine(JsonConvert.SerializeObject(query));
            var expectedResult = new[] { "Scruffy", "Sam", "Walker", "Sugar", "Scratches", "Diesel", "Dusty" };
            expectedResult.Should().BeEquivalentTo(query);
        }// fact
        [Fact]
        public void test_0002_SelectManySMaWithIndex()
        {
            // Project the pet owner's name and the pet's name.
            // template disambiguated: var query = petOwners.SelectMany<PetOwner, string>(Func<PetOwner, int, IEnumerable<string>)
            var query = petOwners.SelectMany((petOwner, index) => petOwner.Pets.Select(pet => index + "-" + pet));
            output.WriteLine(JsonConvert.SerializeObject(query));
            var expectedResult = new[] { "0-Scruffy", "0-Sam", "1-Walker", "1-Sugar", "2-Scratches", "2-Diesel", "3-Dusty" };
            expectedResult.Should().BeEquivalentTo(query);
        }// fact
        [Fact]
        public void test_0003_SelectManySMbWithNamedClass()
        {
            // Project the pet owner's name and the pet's name. Instead of anonymous class, use PetOwnerAndName
            // This allows the SelectMany to be disambiguated clearly
            // SMb: public static IEnumerable<TResult> SelectMany<TSource, TCollection, TResult>(
            //    this IEnumerable<TSource> source,
            //    Func<TSource, IEnumerable<TCollection>> collectionSelector,
            //    Func<TSource, TCollection, TResult> resultSelector
            // );
            // template disambiguated: IEnumerable<PetOwnerAndName> sm = petOwners.SelectMany<PetOwner, string, PetOwnerAndName>(
            var sm = petOwners.SelectMany(
                petOwner => petOwner.Pets, // collector selector
                (petOwner, petName) => new PetOwnerAndName { petOwner = petOwner, petName = petName } // result selector
            );
            IEnumerable<StringPetOwner> query = sm.Where(ownerAndPet => ownerAndPet.petName.StartsWith("S"))
                .Select(ownerAndPet => new StringPetOwner
                {
                    Owner = ownerAndPet.petOwner.Name,
                    Pet = ownerAndPet.petName
                }
            );
            IEnumerable<StringPetOwner> expectedResult = new List<StringPetOwner>() {
                new StringPetOwner{Owner = "Higa", Pet = "Scruffy"},
                new StringPetOwner{Owner = "Higa", Pet = "Sam"},
                new StringPetOwner{Owner = "Ashkenazi", Pet = "Sugar"},
                new StringPetOwner{Owner = "Price", Pet = "Scratches"},
            };
            output.WriteLine(JsonConvert.SerializeObject(query));
            expectedResult.Should().BeEquivalentTo(query);
        }// fact
        [Fact]
        public void test_0004_SelectManySMbWithAnonClasses()
        {
            // Project the pet owner's name and the pet's name.
            // Original code with SelectMany templates are <petOwner, string, `a> where `a is the anonymous class new {petOwner, petName}
            // But in order to instantiate the templates, PetOwnerAndName class has to be declared.
            var query = petOwners.SelectMany(
                petOwner => petOwner.Pets,
                (petOwner, petName) => new { petOwner, petName }
            ).Where(ownerAndPet => ownerAndPet.petName.StartsWith("S"))
                .Select(ownerAndPet => new
                        {
                            Owner = ownerAndPet.petOwner.Name,
                            Pet = ownerAndPet.petName
                        }
            );
            output.WriteLine(JsonConvert.SerializeObject(query));
            var expectedResult = new []{ // array of anonymous class
                new {Owner = "Higa", Pet = "Scruffy"},
                new {Owner = "Higa", Pet = "Sam"},
                new {Owner = "Ashkenazi", Pet = "Sugar"},
                new {Owner = "Price", Pet = "Scratches"}
            };
            expectedResult.Should().BeEquivalentTo(query);
        }// fact
    }// class
}// namespace
