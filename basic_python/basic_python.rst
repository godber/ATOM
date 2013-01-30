Basic Python
----------------

ATOM - Austin's Thing of the Month
++++++++++++++++++++++++++++++++++
Learning Python

* Austin Godber
* Mail: godber@uberhip.com
* Twitter: @godber
* Source: http://github.com/godber/ATOM

.. image:: P5M1-vertical.png
    :height: 2.5cm
    :align: right

.. raw:: pdf

  PageBreak oneColumn


Online Resources
----------------

* `Official Python Documentation 3.3 <http://docs.python.org/3/>`_

  * Tutorial, Library Ref, Language Ref

* `Official Python Documentation 2.7 <http://docs.python.org/2.7/>`_

  * Tutorial, Library Ref, Language Ref

* `Hitchhiker's Guide to Python <http://docs.python-guide.org/en/latest/>`_
* `Learn Python the Hard Way <http://learnpythonthehardway.org/>`_


Books
-----

* Learning Python - Lutz
* Programming Python - Lutz
* Python Pocket Reference - Lutz
* Think Python - Downey

Tools & Utilities
-----------------

* `pip <http://www.pip-installer.org/en/latest/>`_ (easy_install) - package install
* `fabric <http://docs.fabfile.org/en/1.5/>`_ - system management
* ipython & python - Interactive shells
* `Sphinx <http://sphinx-doc.org/>`_ & `Restructured Text <http://docutils.sourceforge.net/rst.html>`_

  * `Tinkerer <tinkerer.me>`_ - Static Site/Blog Generation

Programming Style
-----------------

* `pep8 <http://www.python.org/dev/peps/pep-0008/>`_ (autopep8)
* `pylint <http://www.pylint.org/>`_
* The zen of Python

.. sourcecode:: python

  import this

* pythonic - `Code Like a Pythonista <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html>`_


Testing
-------

* doctests - usage examples only
* unittest/unittest2 - unit testing
* web testing

  * django client
  * lettuce
  * selenium


Other Topics
------------

* Math & Science

  * Matplotlib
  * PANDAS
  * Scipy & NumPy

Other Topics
------------

* Web

  * `Flask <http://flask.pocoo.org/>`_
  * `Django <https://www.djangoproject.com/>`_
  * `CherryPy <http://cherrypy.org/>`_
  * `Web2Py <http://www.web2py.com/>`_


Other Topics
------------

* Database interactions
* Report Generation (PDF, XLS)
* Web Scraping (Scrapy, Requests, Pattern)

Gotchas - Understand Imports
----------------------------

Bad

.. sourcecode:: python

  from os import *
  mkdir('/tmp/foo')

Better

.. sourcecode:: python

  from os import mkdir
  mkdir('/tmp/foo')

Best

.. sourcecode:: python

  import os
  os.mkdir('/tmp/foo')



.. footer::

        © Austin Godber (@godber), 2013
