# taxonid - Get taxon id from NCBI taxonomy database

## Install
### From Conda
```sh
[sudo] conda install -c conda-forge taxonid

```

## Use
### CLI
```
python -m taxonid "Escherichia coli str. K-12 substr. MG1655"
```
### As a Python module
```python
from taxonid import get_from_label

taxon_id = get_from_label("Escherichia coli str. K-12 substr. MG1655")
```

## Tests
Please follow instructions below ti run tests:
```
cd tests
pytest -v
```
For further tests and development tools, a CI toolkit is provided in `ci` folder (see [ci/README.md](ci/README.md)). -->


## Authors

* **Joan Hérisson**

## Acknowledgments

* ChatGPT


## Licence
taxonid is released under the MIT licence. See the LICENCE file for details.
