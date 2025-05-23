.. image:: https://img.shields.io/pypi/v/kustomize.svg
   :target: https://pypi.org/project/kustomize

.. image:: https://img.shields.io/pypi/pyversions/kustomize.svg

.. image:: https://github.com/coherent-oss/python-kustomize/actions/workflows/main.yml/badge.svg
   :target: https://github.com/coherent-oss/python-kustomize/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. .. image:: https://readthedocs.org/projects/PROJECT_RTD/badge/?version=latest
..    :target: https://PROJECT_RTD.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2025-informational
   :target: https://blog.jaraco.com/skeleton

Build your Kubernetes manifests for Kustomize in Python!

* PyPI: https://pypi.org/project/kustomize/
* Repository: https://github.com/coherent-oss/python-kustomize
* Documentation: https://python-kustomize.readthedocs.io/en/latest/

Overview
--------

The reason for this project to exist is to make it easier to create dynamic
manifests to be exported for usage in Kubernetes' "Kustomize" tool. And, by
using Python and supporting the "dataclasses" language feature, it also helps
reducing boilerplate by encouraging code reuse.

Kustomize, by itself, is already a very powerful tool, and it's possible to
deal with different apps and environments by using the "overlays" approach; but
it's not dynamic enough if you need to define manifests parameters through
environment variables, for example. So this project aims to cover that gap.

A complement for Kustomize
--------------------------

This project is by no means a replacement for Kustomize, but rather a
complement. The idea is to generate kustomization files from Python files, and
then use ``kubectl apply -k`` or ``kustomize build`` to transform them into
final manifests for Kubernetes (even applying them to the cluster).

In other words, the idea is to "compile" Python files into Kustomize files, then
just use Kustomize for the rest of the deployment.

Installing
----------

The only mandatory dependency to this project is ``PyYAML``. This library
supports a number of object definition types:

* ``dict``
* ``dataclasses``
* ``BaseModel`` (from Pydantic)
* ``attr`` (needs the library installed)
* ``kubernetes`` (needs the library installed)

This package will be available as ``kustomize``; you may install it with pip,
for example::

    $ pip install kustomize

This will also install ``PyYAML`` if it's not already installed.

Alternatively, you can use any other package manager capable of installing
packages from PyPI.

Usage
-----

The summary is:

1. You write a source directory with Python files representing the Kustomize
   files (see directories at ``python-kustomize/tests/fixtures/``);
2. You run::

   $ pykustomize <source-dir> <dest-dir>

   where ``<dest-dir>`` will be
   the directory where Kustomize YAML files will be put at;
3. Then you can apply the generated Kustomize files into your cluster::

   $ kubectl apply -f <dest-dir>

   and done!
