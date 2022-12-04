# immatriculation
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Set of tools for D&D dice actions !


## Installation

Clone this repo with

```
$ git clone https://github.com/vdbma/immatriculation
```

Install with
```
$ pip install -e .
```
while in the repository directory (`-e` option will auto-update the package for your python environement when pulling newer versions).

## Usage

Given a python string formatted as `'XX-YYY-ZZ'` where
- XX are two letters
- YYY are thre numbers
- ZZ are two letters

`immatriculation.siv.computeValue('XX-YYY-ZZ')` returns the number corresponding to the ID. If the string is not valid, it returns `None`.

This follows the french SIV ID plate system (see [wikipedia page](https://fr.wikipedia.org/wiki/Plaque_d%27immatriculation_fran%C3%A7aise))
