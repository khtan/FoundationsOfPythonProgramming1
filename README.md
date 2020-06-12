[![CircleCI Status](https://circleci.com/gh/khtan/FoundationsOfPythonProgramming1.svg?style=shield)](https://circleci.com/gh/khtan/FoundationsOfPythonProgramming1)
# Software Kata Environment
# Introduction
When I first read about [Code Kata](http://codekata.com/), it was appealing as a way to keep my programming chops honed and active.
At the expense of simplicity, Code Kata, is based on the martial arts practice of Kata, where the practitioner
goes through a series of ritualized movements. The goal is to reinforce muscle memory and reflex. While the general
idea is that "Practice makes Perfect", it gained momentum from the ["10 Thousand Hours Rule"](https://www.newyorker.com/sports/sporting-scene/complexity-and-the-ten-thousand-hour-rule), popularized by Malcolm Galwell in his book ["Outliers"](https://en.wikipedia.org/wiki/Outliers_(book)). Although recent research have debunked the 10 Thousand Hours Rule, it remained as an ideal for many.

# Why a software kata environment
When I first tried Code Kata, the experience was nice but I did not do it very often. When I reflected on this, I realized there were several issues that the Code Kata did not address but I needed to.

The first concern was computing environment variability. I would create a project on my desktop, and later, decide
to do the kata, when I'm travelling with my laptop. In addition, I sometimes work in Linux, and sometimes in Windows.
There are a lot of languages that can work in both platorms - Java, C# (DotNet), Python, to mention 3. Without a good system in place, I had been creating projects in many places and then forgetting about them.

Secondly, while Code Kata had a set of programming problems that could be used for the katas, I felt that they were based on small problems while I had a different goal. I wanted to be able to learn/review basic programming utilizing all the languages that I've been familiar with. For example, OOP languages such as C#, Java, Scripting languages such as Perl, Python, functional languages like Haskell and also Functional extensions of common languages such as RxJava, RxNet, RxPython. As each language and book tends to introduce its material in its own sequence and content, I sometimes forget or get lost when I try to implement something, simply because I hadn't covered that topic with that specific language. What I needed was a system to keep programming snippets in an organized way as I worked on the practice sessions. Instead of the standard code kata's practice of writing the same code again and again, I find I learn more if I try to implement the same snippet in each of the languages I was interested in. The snippets would ideally be runnable so that both learning and doing are enhanced.

Closely related is the method of running the snippets. The Code Kata is based on running some command line execution of a program. This does not scale well if there are lots of snippets. It also missed a key weakness in most programming curriculum - they introduce testing way too late, and force the learner to unlearn some bad practices in the process. It dawned on me that every language has at least one unit testing framework, and every testcase is an executable snippet, achieving the earlier goal of making them executable. Once set up, a unit framework allows me to concentrate only on the testcase, and the test manager has a convenient way to organize and run many testcases.

Coincidentally at this time, I had decided to re-learn Python in a more systematic way. I had signed up for the University of Michigan Coursera [Python 3 Programming Specialization track](https://www.coursera.org/specializations/python-3-programming) using the free audit only option. It consisted of 5 courses that covering Python Basics to Python Classes, and a Python project course at the end. As I worked through the course,
I found that the MOOC was based on an electronic textbook opened sourced and called [Runestone Academy Foundations of Python Programming](https://runestone.academy/runestone/books/published/fopp/index.html).
As an audit student, I could not make use of the graded assignment feature of the course. Since the MOOC was a repackaging ( reordering ) of material in this Runestone book, I decided to study directly from this book instead. 
Thus, implementing each of the little programming exercises as a testcase in Python provided the basis for the initial set of problem snippets. 

A final problem I wanted to deal with is that many times, when I pick up an old project to reuse or add more snippets, I would find that the compiler or libraries have updated and they no longer work. I knew I had to keep
the source code in version control, and equally important, I needed some continuous integration system so that whenever I make updates, I would know that the code still work on both Linux and Windows.

# Open Implementation
Fortunately, a software environment based on GitHub and CircleCi would able to form the basis of a viable solution. This repo would consist of several folders, one for each language, with Python as my first language. This allows me to clone the repository on any platform I wish and pick up from there, complete with the version history of all my changes. As I work on one machine, the CircleCi will run regressions on both Linux and Windows. Below is a table that shows my current progress. It details which language maps to what platforms the tests are running on CircleCi.

The current preponderance of Linux Docker machines is due to the fact that Windows Docker is not yet available in
CircleCi. There is a noticeable execution time increase when using a Windows VM vs a Docker file. When CircleCi makes Windows Docker available, I will update my testing suite.

The IDEs listed are what I use in my development as examples. Since they are just source repositories, any environment
will do, so long as you know how to set things up. 

  | Language | CircleCi     | Unit Testing Framework | IDE               |
  |----------|--------------|------------------------|-------------------|
  | Python   | Linux Docker | Pytest                 | VS Code           |
  | C#       | Linux Docker | XUnit, dotnet          | VS Code           |
  | C#       | Windows VM   | XUnit, dotnet          | VS 2019 Community |
  | Java     | Linux Docker | Junit4/5 on Maven      | VS Code, IntelliJ |

# Best Practices
## Pedagogical emphasis
The first pedagogical device I implemented is to name the snippets such that there is an indication of meaning and
the order in which the snippets were written. Since my first implementation was in Python, the convention was 
'[test]\_[nnn]\_[functionality]' where [test] is a Pytest convention, [nnn] is an increasing index to help remember
the order of testcase, and [functionality] gives an idea of what's covered.
The same convention was also adopted for the file names, for example, test_ch06_sequences.py.

This pedagogical device would immediately clash with the standard coding convention of any language other than Python.
However by carrying the same naming convention to CSharp and other languages, it allowed me to indicate which testcase in CSharp matches the same testcase in Python. Thus the file naming and test naming convention was adopted from Python and carried through into CSharp and Java.

## Running the tests
The tests can all be run from within the IDE and in the command line. The command line invocations are the same used by CircleCi. 
As the table above shows, I have chosen to always pick the unit test environment that runs on both Windows and Linux. For example, Visual Studio 2019 Community comes with the default Microsoft Unit Test framework but I have chosen to use Xunit instead.

## Learn wide, then deep
As this project progressed I learned that it is not sufficient just to know a language and its syntax. It is important
to learn the libraries available so as to not reinvest the wheel. In particular, the unit testing framework and the assertion libraries are two pieces that should be used as early as possible. Only when all the supporting pieces are in place does it make sense to go deeper into each area, either library or language.

# References
* [Live Github](https://github.com/khtan/FoundationsOfPythonProgramming1)
* [Live CircleCi](https://circleci.com/gh/khtan/FoundationsOfPythonProgramming1)
