.. highlight:: shell

============
Installation
============

Setup Python Environment
------------------------------

TCRA depends on a number of packages.  For more information on Python package
dependencies, see :ref:`Dependencies`.

Installation
------------

To install TCRA, run this command in your terminal:

.. code-block:: console

    $ pip install tcra

Importing TCRA
---------------------

Once installed, you can import TCRA into your Python scripts or Jupyter notebooks. Here's a simple example:

.. code-block:: python

   import tcra

   # Now you can use the tcra functions and classes in your code


This is the preferred method to install tcra, as it will always install the
most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From Sources (for developers)
-----------------------------

The sources for TCRA can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/rxm562/TCRA

Or download the `tarball`_:


Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/rxm562/TCRA

.. _Dependencies:

Dependencies
------------

Requirements for TSNet include Python (3.5, 3.6, or 3.7) along with several Python packages.

The following Python packages are required::

1.  Numpy : the fundamental package needed for scientific computing with Python
    included in Anaconda distribution
    http://www.numpy.org/

2.  Matplotlib : Python 2D plotting library
    included in Anaconda distribution
    http://matplotlib.org/

3.  Pandas : pandas is a fast, powerful, flexible and easy to use open source data analysis 
    and manipulation tool, built on top of the Python programming language.
    https://pandas.pydata.org/

4.  Scipy : SciPy is a free and open-source Python library used for scientific 
    computing and technical computing.
    https://scipy.org/

5.  Folium : Folium builds on the data wrangling strengths of the Python ecosystem and the mapping 
    strengths of the Leaflet.js library.
    https://python-visualization.github.io/folium/latest/#

