# BEAquery

[![PyPI - Version](https://img.shields.io/pypi/v/beaquery.svg)](https://pypi.org/project/beaquery)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/beaquery.svg)](https://pypi.org/project/beaquery)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install beaquery
```

## License

`beaquery` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

`
usage: beaquery.py [-h]
                   [--dataset {NIPA,NIUnderlyingDetail,MNE,FixedAssets,ITA,IIP,InputOutpus,IntlServTrade,GDPbyIndustry,Regional,UnderlyingGDPbyIndustry,APIDatasetMetaData}]
                   [--param PARAM] [--hierarchy] [--datasets] [--params]
                   [--paramvals]

explore BEA structure

options:
  -h, --help            show this help message and exit
  --dataset {NIPA,NIUnderlyingDetail,MNE,FixedAssets,ITA,IIP,InputOutpus,IntlServTrade,GDPbyIndustry,Regional,UnderlyingGDPbyIndustry,APIDatasetMetaData}
                        specify the dataset
  --param PARAM         specify a parameter for a dataset
  --hierarchy           display BEA data organization hierarchy
  --datasets            display datasets
  --params              display parameters for a dataset
  --paramvals           show values for a parameter of a dataset
`
