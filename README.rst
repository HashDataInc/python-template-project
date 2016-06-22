template
--------
Python project template

=====
Tests
=====
To run all tests and PEP8, run tox, like so:

.. code-block:: bash

    $ tox

To run just the tests for Python 2.7, run:

.. code-block:: bash

    $ tox -epy27

To run just PEP8, run:

.. code-block:: bash

    $ tox -epep8

To generate a coverage report,run:

.. code-block:: bash

    $ tox -ecover

(note: on some boxes, the results may not be accurate unless you run it twice)

If you want to run only the tests in one file you can use py.test e.g.

.. code-block:: bash

    $ tox -e venv -- py.test src/tests/test_sample.py
