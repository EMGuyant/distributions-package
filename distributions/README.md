# Probability Distribution Package
A probability distribution package that was built while expanding my working
knowledge of developing and consuming Python packages, Python classes, and OOP
programing fundamentals.

The `distributions` package has a `Gaussian` and `Binomial` distribution classes
which both inherit attributes and actions from a generic `Distribution` class.

# Contents
* `distributions-package` it the project directory for the Python package.
  * `data` contains two text files containing test data that can be read with
    the Gaussian and Binomial classes
    * `numbers.txt`
    * `numbers_binomial.txt`
  * `testing` contains the `test.py` file used to verify the package is working
    as expected
    * `test.py`
  * `distributions` is the package
    * `__init__.py`
    * `Binomialdistribution.py`
    * `Gaussiandistribution.py`
    * `Generaldistribution.py`
    * `README.md`
    * `setup.cfg`

# Use of the Package

### Import the package
```python
from distributions import Gaussian
from distributions import Binomial
```
### Distribution  Methods
* `read_data_file`
  * Arguments
    * `file_name` (string)

### Gaussian Methods
* `calculate_mean`
* `calculate_stdev`
  * Arguments
    * *Optional* `sample`
      * `True`: sample standard deviation
      * `False`: population standard deviation
* `plot_histogram`
* `pdf`
  * Arguments
    * `x` (float)
* `plot_histogram_pdf`
  * Arguments
    * `n_spaces` (int)
### Binomial Methods
* `calculate_mean`
* `calculate_stdev`
  * Arguments
    * *Optional* `sample`
      * `True`: sample standard deviation
      * `False`: population standard deviation
* `replace_stats_with_data`
* `plot_bar`
* `pdf`
  * Arguments
    * `k` (float)
* `plot_bar_pdf`


