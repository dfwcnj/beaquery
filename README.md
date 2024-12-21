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

<p>
usage: beaquery.py [-h]<br>
                   [--dataset
                   {NIPA,NIUnderlyingDetail,MNE,FixedAssets,ITA,<br>
                    IIP,InputOutpus,IntlServTrade,GDPbyIndustry,Regional,<br>
                    UnderlyingGDPbyIndustry,APIDatasetMetaData}]<br>
                   [--param PARAM]<br>
                   [--hierarchy]<br>
                   [--datasets]<br>
                   [--params]<br>
                   [--paramvals]<br>

explore BEA structure<br>

options:<br>
  -h, --help            show this help message and exit<br>
  --dataset {NIPA,NIUnderlyingDetail,MNE,FixedAssets,ITA,IIP,<br>
             InputOutpus,IntlServTrade,GDPbyIndustry,Regional,<br>
             UnderlyingGDPbyIndustry,APIDatasetMetaData}<br>
        specify the dataset<br>
  --param PARAM         specify a parameter for a dataset<br>
  --hierarchy           display BEA data organization hierarchy<br>
  --datasets            display datasets<br>
  --params              display parameters for a dataset<br>
  --paramvals           show values for a parameter of a dataset<br>
</p>
