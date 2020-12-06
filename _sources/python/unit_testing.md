# Unit testing

Unit tests increase code quality and provide means to steer a project - they set objectives for next steps or help fix bugs. Unit tests mean writing more code and reviewing code under test, which takes time and effort. 

Below are a few links and my quick notes about unit testing in Python. I do not touch
frontend tests (eg [selenium][sel]), which I know little about.


[sel]: https://github.com/seleniumbase/SeleniumBase

<b>Favourite video about testing?</b><br>
[TDD, Where Did It All Go Wrong](https://www.youtube.com/watch?v=EZ05e7EMOLM) by [Ian Cooper](https://twitter.com/icooper) is very impactful. <!--Also advertised [here](https://twitter.com/unclebobmartin/status/1032405401009041409). -->

<b>A trivial test example?</b><br>

```python
def inc(x: int) -> int:
   return x + 1

assert inc(1) == 2
```

<b>Does the example show much?</b>

- Are there property guarantees?
- Does typing help?
- Not suited for dependency injection, right?

<b>Is unit test a proof?</b>
<br>Usually, no. You may try [property testing](https://hypothesis.works/articles/what-is-property-based-testing/) for more guarantees.

<!--b>Is code coverage a good metric?</b><br>
0% coverage means there are no tests. With 100% coverage you can have poorly written tests, so the metric is not exhaustive. -->

<b>What parts of code should I test?</b><br>

- At least public methods and bug fixes.
- The smallest parts (through unit tests) and the biggest (through end-to-end, integration tests).
- Beware of [dirty hybrids [Sanderson(2009)]][dh], the costly tests that attempt to target things in between.

[dh]: http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/

<b>Does typing help writing a more testable code?</b><br>
Yes, quite much. In Python we can then skip type-checking varieties of tests.

<!--b>A test setup (fixture) is getting big out of proportion, what is wrong?</b><br>

- Maybe a chance to reconsider program design and refactor, where possible.
- Testing the wrong part of program. -->

<b>Should one [mock or monkey-patch for testing?](https://twitter.com/gagliardi_vale/status/1318231202395004929)</b><br>
Only if you cannot use dependency injection.

<b>A continious integration (CI) for your projects?</b><br>
I was [a fan of Travis CI][tweet-travis], but now Github Actions seem a natural choice.

[tweet-travis]: https://twitter.com/PogrebnyakE/status/1323256976722305024

<b>pytest?</b><br>
Yes, [pytest](https://docs.pytest.org/en/stable/).

<b>Difficult questions for you about unit testing?</b><br>

- Testing with a database or ensuring a state
- [Test naming](https://github.com/mini-kep/guidelines/blob/master/testing.md)
- [Balancing test complexity and usefulness](https://twitter.com/PogrebnyakE/status/1230112605123076098)

<b>Anything about other types of tests?</b><br>
Unit tests are a part functional tests, there many more types of tests for a system
in or near production stage, depending on your release cylce sophistication and handling of incidents. See chaos engineering, or fault injection tests, for some frontier testing approaches.

**More links**

- [Stack Overflow on pytest](https://stackoverflow.com/questions/tagged/pytest?tab=Frequent)
- [Testing Flask](https://flask.palletsprojects.com/en/1.1.x/testing/)
- <https://raphael.codes/talks/>
- <https://testing.googleblog.com/>