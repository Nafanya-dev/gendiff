### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nafanya-dev/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Nafanya-dev/python-project-50/actions)

<a href="https://codeclimate.com/github/Nafanya-dev/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/71297dd3d7b98aa9c6f8/maintainability" /></a>

<a href="https://codeclimate.com/github/Nafanya-dev/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/71297dd3d7b98aa9c6f8/test_coverage" /></a>


# Difference generator
### Compares documents in *.json, *.yml, *.yaml formats containing a dictionary of dictionaries. Finds differences in keys and their values and outputs them in a given format.


## Output Formats

* stylish - used by default. Outputs the result as multi-line text with a tree-like dictionary structure.
* plain - outputs the result as multiline text in the form:
  * Property... has been added...
  * Property... has been removed...
  * Property... has been updated...
* json - Outputs the result as a json object.


### Package installation:

```bash
>> git clone https://github.com/Nafanya-dev/gendiff.git && cd gendiff
```

Then you have to build the package and install it:

```bash
>> make build
>> make package-install
```


### Options:
* -h, --help - show help message.
* -f, --format - ability to specify format selection.


---

### Example

<a href="https://asciinema.org/a/UKfQbDdDlAKjhWLrgF7SH8Sf9" target="_blank"><img src="https://asciinema.org/a/UKfQbDdDlAKjhWLrgF7SH8Sf9.svg" /></a>

<a href="https://asciinema.org/a/MZOFkbD5MV7q0ufNw1CXrGn7C" target="_blank"><img src="https://asciinema.org/a/MZOFkbD5MV7q0ufNw1CXrGn7C.svg" /></a>

<a href="https://asciinema.org/a/HxG4GPmr8avoGUMYOz8cBf7Ha" target="_blank"><img src="https://asciinema.org/a/HxG4GPmr8avoGUMYOz8cBf7Ha.svg" /></a>

<a href="https://asciinema.org/a/oTDeLSpCu91dr7BjkLlNYsyKU" target="_blank"><img src="https://asciinema.org/a/oTDeLSpCu91dr7BjkLlNYsyKU.svg" /></a>
