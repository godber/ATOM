Testing Python
==============
Understanding testing in the Python World

* Austin Godber
* Mail: godber@uberhip.com
* Twitter: @godber
* Source: http://github.com/godber/Python-Testing-Presentation

.. raw:: pdf

  PageBreak oneColumn


Motivation for Testing
======================

* Does your code behave correctly to begin with?
* How about when you fix a bug?
* After you refactor?
* After everyone who wrote it is gone, how do you know what it was supposed to do
  in the first place?


Testing Topics
==============

* Unit Testing 
* Fixtures and Mocks
* Code Coverage and Code Quality
* Fuzz Testing
* Web Testing
* Acceptance/Functional Testing
* Regression Tests


Unit Testing - Description
==========================

* Testing the functionality of a small piece of application.

  * Does ``MyInteger.add(2)`` return what it is supposed to?
* Test Coverage

  * How much of the code is covered by existing tests?

    * Are all branches or code paths covered?
    * Are all functions/methods covered?


Unit Testing - Concepts
=======================

test fixture
  setup and teardown for a collection of tests
test case
  the code that actually implements the tests
test suite
  a collection of test cases
test runner
  interface for running test cases or suites


Unit Testing - Options
======================

* Built In Solutions

  * ``doctest``, ``unittest``, ``unittest2``

.. doctest can be used on Restructured Text Documents, but are not recommended
   for full coverage since it would clutter the source, I mainly use for simple
   examples included in documentation.
.. unittest2 is an extension of unittest and is standard in Python 2.7+

* 3rd Party Alternatives

  * ``py.test``, ``PyUnit``

* Testing Related Utils

  * ``nose`` - Helps run tests
  * ``coverage``, ``figleaf`` - Testing Coverage
  * ``pythonscope`` - Test generation

  
Unit Testing - Example
======================

An example using ``unittest2``, ``nose``, ``coverage``, and ``pythonscope``::

  cd src/unittesting
  nosetests --with-doctest -v


Running manually, without help from nose::

  python -m doctest -v myinteger.py
  PYTHONPATH=. python tests/test_myinteger.py


Unit Testing - Example
======================

.. code-block:: python

  import myinteger, unittest2

  class TestMyInteger(unittest2.TestCase):
      def test_add_simple(self):
          """Make sure single digit addition works"""
          i = myinteger.MyInteger(4)
          self.assertEqual(i.add(2), 6)

  if __name__ == '__main__':
      unittest2.main()

.. The class should have a name that begins with Test and inherit from
   unittest2.TestCase.  Class methods define the various setup, teardown and
   tests to permform and will get executed by the runner.
.. The assertEqual is where the action is at.
.. The last bit allows tests to be executed when called directly.


Unit Testing - Assertions
=========================

The python unittest library is built around the set of assertions_::

  assertTrue, assertEqual, assertAlmostEqual, assertGreater, assertIn,
  assert***Equal, assertRaises, assertIsNone, assertIs, assertIsInstance,
  assertFalse

They take the arguments you would expect, plus a message.

.. code-block:: python

  assertTrue(i_return_true(), "I should return True")
  assertEqual(two(), 2, "I should return two")

Remember Greg's Python Koans_.

.. _assertions: http://docs.python.org/release/2.7/library/unittest.html#unittest.TestCase
.. There is no separate documentation for unitest2 since it is backported from
   2.7.
.. _koans: http://bitbucket.org/gregmalcolm/python_koans/wiki/Home

Example - Coverage
==================

So how well does our existing test cover the MyInteger class?

::

  PYTHONPATH=. coverage run --source=myinteger.py \
    tests/test_myinteger.py
  coverage html

There is a nose plugin for coverage that probably simplifies this.


Example - Pythoscope
====================

Lets generate the remaining tests::

  pythoscope --init
  pythoscope myinteger

.. LIVECODING!!! Refactor the generated code to use a setUp() fixture, showing
   the coverage increasing as we do.  Point out that coverage doesn't
   necessarily mean you are doing a good job testing.


Fixtures and Mocks
==================

Fixtures
  Help setup testing environment for a set of tests with similar requirements.
  Create test objects, load test data into db. A simple setup fixture is seen
  in the MyInteger example.  The third party module, fixture_, loads multiple
  database backends.  There are also `Django fixtures`__.

Mocks
  Emulate actions or objects that are too expensive or disruptive to perform
  during every test run.  e.g. ``rocket.launch()`` See the module Mock_, mox_

.. _Mock: http://www.voidspace.org.uk/python/mock/
.. _fixture: http://farmdev.com/projects/fixture/
.. _djangofixture: http://docs.djangoproject.com/en/dev/topics/testing/#fixture-loading
__ djangofixture_
.. _mox: http://code.google.com/p/pymox/

Example - Code Quality
======================

pylint_
  Checks for errors, duplication, complexity and adherance to convention.
  Reports statistics on code composition and other metrics.  Provides an overall
  rating.  Very opinionated.

.. Show example on MyInteger

pep8_
  Does the code follow the PEP 8 style guide?  Basic code style checking.

.. Show example on something else I find.

.. _pylint: http://www.logilab.org/project/pylint
.. _pep8: http://pypi.python.org/pypi/pep8


Fuzz Testing
============

Fuzz Testing
  Throws garbage at your interfaces to see if it breaks.


Web Testing
===========

* Standard Tools Apply: unittest, doctest

.. Note that Django currently bundles unittest2 as unittest

* Web Specific Tools

  * Browser Emulation

    * `Django Test Client <http://docs.djangoproject.com/en/dev/topics/testing/#testing-tools>`_

  * Browser Drivers

    * `Windmill <http://www.getwindmill.com/>`_, `Selenium <http://seleniumhq.org/>`_

  * Acceptance Test Frameworks, ATDD, BDD, Not strictly web related.

    * `Lettuce <http://lettuce.it/>`_, `Pyccuracy <https://github.com/heynemann/pyccuracy/wiki/>`_


Django Testing - Basic
======================

The built in Django test runner looks for doctests or unittests in:

* ``models.py`` - Runs docstrings and any subclass of unittest.TestCase.
* ``tests.py`` - Runs docstrings and any subclass of unittest.TestCase.

Rather than one huge ``tests.py`` file, you can make a ``tests`` directory,
place your tests in that directory and then load the tests in
``tests/__init__.py``.  This is what I have done in the example application.


Django Testing - Run
====================

How to run?::

  cd src/djangoblog
  python ./manage.py test blog
  # or test all with
  python ./manage.py test

.. Open a terminal and do that, look at:
   src/djangoblog/blog/models.py - See the doctest
   src/djangoblog/blog/tests/simple.py - See the unittests


Django Testing - Test Client
============================

``django.test.client`` emulates browser actions but can peek within the app
itself.

* Does ``get``, ``post``, ``put``, ``delete``, ``head``, ``options`` plus django auth
  ``login`` and ``logout``.
* The response contains

  * Standard HTTP Stuff: ``content``, ``status_code`` and dictionary of HTTP headers.
  * App Internal Stuff: ``context``, ``template``

.. Look at src/djangoblog/blog/tests/client_example.py


Testing with Lettuce
====================

This just a brief introduction as I know my understanding is severly
lacking. ``src/djangoblog/blog/features/`` contains a basic example with the
following issues.

* ``world`` is a global and I don't understand its scope
* Avoid repetitious and brittle code by using page_objects_
* Browser drivers can be used in place of the django client, and thus can test
  non-django apps.

Run with::

  python manage.py harvest

.. _page_objects: http://www.cheezyworld.com/2010/11/09/ui-tests-not-brittle/



Continuous Integration
======================

A CI system will build a project and run tests against it after every commit.
This provides continuous feedback on the quality of your code.

* http://buildbot.net/trac
* http://greatbigcrane.com/
* http://hudson-ci.org/ (Java)


.. footer::

        Testing Python - © Austin Godber (@godber), 2010
