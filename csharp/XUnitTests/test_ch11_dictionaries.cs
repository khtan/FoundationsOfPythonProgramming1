using System;
using System.Collections;
using System.Text.RegularExpressions;
using System.Globalization;
using System.Collections.Generic;
using Xunit;
using Xunit.Abstractions;
using System.Linq;

namespace XUnitTests
{
    public class test_ch11_dictionaries
    {
        private readonly ITestOutputHelper output; // helper provides interface for WriteLine only, so not logging per se
        private String Capitalize(string input){
            if (!String.IsNullOrEmpty(input)) {
                if (input.Length == 1)
                {
                    return input.ToUpper();
                } else
                {
                    return char.ToUpper(input[0]) + input.Substring(1);
                }
            }
            else { return input; }
        }
        private Dictionary<string, string> GetEnglish2PirateDictionary(){
            var English2Pirate = new Dictionary<string,string>(){
                {"sir","matey"},{"hotel","fleabag inn"},{"student","swabbie"},{"boy","matey"},{"madam","proud beauty"},{"professor","foul blaggart"},{"restaurant","galley"},{"your","yer"},{"excuse","arr"},{"students","swabbies"},{"are","be"},{"lawyer","foul blaggart"},{"the","th’"},{"restroom","head"},{"my","me"},{"hello","avast"},{"is","be"},{"man","matey"}
            };
            var CapEnglishPirate=new Dictionary<string,string>();
            // Note: If TextInfo.ToTitleCase is used, then "proud beauty" becomes "Proud Beauty"
            //       while Capitalize returns "Proud beauty"
            // TextInfo TI = new CultureInfo("en-US", false).TextInfo;
            foreach (var entry in English2Pirate){
                // var capEnglish = TI.ToTitleCase(entry.Key);
                var capEnglish = Capitalize(entry.Key);
                // CapEnglishPirate[capEnglish]=TI.ToTitleCase(English2Pirate[entry.Key]);
                CapEnglishPirate[capEnglish] = Capitalize(English2Pirate[entry.Key]);
            }
            CapEnglishPirate.ToList().ForEach(x => English2Pirate.Add(x.Key, x.Value));
            return English2Pirate;
        }
        private String TranslateEnglish2Pirate(Dictionary<string, string> English2Pirate, string englishSentence)
        {
            var pirateLine = new List<string>();
            foreach(var word in englishSentence.Split()){
                var filteredWord = Regex.Replace(word, @"\W+", "");
                if(English2Pirate.ContainsKey(filteredWord)){
                    var replacedWord = word.Replace(filteredWord, English2Pirate[filteredWord]);
                    pirateLine.Add(replacedWord); // Append returns new sequence
                }
                else{
                    pirateLine.Add(word);
                }
            }
            return String.Join(" ", pirateLine);
        }
        public test_ch11_dictionaries(ITestOutputHelper output) { this.output = output;  }

        [Theory] // english sentece, pirate sentence
        [InlineData("Hello boy, how are you?","Avast matey, how be you?")]
        [InlineData("I saw the professor and his student entering the restaurant near the hotel this afternoon","I saw th’ foul blaggart and his swabbie entering th’ galley near th’ fleabag inn this afternoon")]
        [InlineData("Good morning Sir and Madam!","Good morning Matey and Proud beauty!")]
        [InlineData("Excuse me, where is the restroom?","Arr me, where be th’ head?")]
        public void test_111112_pirate(string english, string expectedPirate)
        {
            var English2Pirate = GetEnglish2PirateDictionary();
            var pirateLine = TranslateEnglish2Pirate(English2Pirate, english);
            Assert.Equal(expectedPirate, pirateLine);
        }// fact
    }// class
}// namespace
