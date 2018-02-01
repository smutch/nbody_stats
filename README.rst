nbody_stats
===========

    Calculate the number of particles, particle mass, or volume of a cosmological N-body simulation given two of the three values.

* Free software: MIT license

Installation
------------

**nbody_stats** can be installed using:

.. code-block:: sh

    pip install git+https://github.com/smutch/nbody_stats.git


Usage
-----

.. code-block:: sh

    Usage: nbody-stats [OPTIONS] COMMAND [ARGS]...

    Options:
      --help  Show this message and exit.

    Commands:
        mass    Calculate the particle mass given the number...
        npart   Calculate the number of particles given the...
        volume  Calculate the simulation volume (in h^-1 Mpc)...


Credits
-------

Code written by Simon Mutch (smutch).

This package was created with Cookiecutter_ and the 
`audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
