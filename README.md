# BEAquery

[![PyPI - Version](https://img.shields.io/pypi/v/beaquery.svg)](https://pypi.org/project/beaquery)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/beaquery.svg)](https://pypi.org/project/beaquery)

-----

## Table of Contents

BEA query is a set of commands to investigate, retrieve, or view
datasets provided by BEA. 

beaillustrated collects information about all of the BEA datasets, their
parameters, and parameter values. It then displays this information in
your browser

The remaining commands retrieve and either store data in CSV files or
display the data along with interactive plots in your browser.

beaqueryq can be used to do all that the commands above do.

- [Installation](#installation)
- [License](#license)

## Installation
<br>
```console<br>
pip&nbsp;install&nbsp;beaquery<br>
```<br>
<br>
##&nbsp;License<br>
<br>
`beaquery`&nbsp;is&nbsp;distributed&nbsp;under&nbsp;the&nbsp;terms&nbsp;of&nbsp;the&nbsp;[MIT](https://spdx.org/licenses/MIT.html)&nbsp;license.<br>
<br>
<p><br>
<br/>

<br/>
##<br/>
## beaillustrated<br/>
##<br/>
usage: beaillustrated [-h] [--format {json,XML}] [--directory DIRECTORY]<br/>
<br/>
display BEA data model<br/>
<br/>
options:<br/>
-h, --help            show this help message and exit<br/>
--format {json,XML}   requested BEA result format(json)<br/>
--directory DIRECTORY<br/>
where to store the generated html<br/>
<br/>
<br/>
##<br/>
## beafixedassets<br/>
##<br/>
usage: beafixedassets [-h] --tn TN --yr YR [--format {json,XML}]<br/>
[--csvfn CSVFN] [--splitkey SPLITKEY] [--xkey XKEY]<br/>
[--ykey YKEY] [--unitskey UNITSKEY] [--htmlfn HTMLFN]<br/>
<br/>
get BEA FixedAssets data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--tn TN              FixedAssets table name<br/>
--yr YR              year YYYY or X for all years<br/>
--format {json,XML}  result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(LineDescription) to use to split the<br/>
plots<br/>
--xkey XKEY          table column name(TimePeriod) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  table column name(METRIC_NAME) to use to label the data<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beagdpbyind<br/>
##<br/>
usage: beagdpbyind [-h] --tid TID --indstry INDSTRY --freq FREQ --yr YR<br/>
[--format {json,XML}] [--csvfn CSVFN]<br/>
[--splitkey SPLITKEY] [--xkey XKEY] [--ykey YKEY]<br/>
[--unitskey UNITSKEY] [--htmlfn HTMLFN]<br/>
<br/>
get BEA GDPbyIndustry data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--tid TID            table id<br/>
--indstry INDSTRY    industry<br/>
--freq FREQ          frequency M, Q, A or comma separated list<br/>
--yr YR              year YYYY or ALL<br/>
--format {json,XML}  query result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(IndustrYDescription) to use to split<br/>
the plots<br/>
--xkey XKEY          table column name(Year) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  y key units(Billions?) to use to label the plotdata<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beaiip<br/>
##<br/>
usage: beaiip [-h] --toi TOI --comp COMP --freq FREQ --yr YR<br/>
[--format {json,XML}] [--csvfn CSVFN] [--splitkey SPLITKEY]<br/>
[--xkey XKEY] [--ykey YKEY] [--unitskey UNITSKEY]<br/>
[--htmlfn HTMLFN]<br/>
<br/>
get BEA IIP data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--toi TOI            type of investment<br/>
--comp COMP          composition<br/>
--freq FREQ          frequency M, Q, A or comma separated list<br/>
--yr YR              year YYYY or ALL<br/>
--format {json,XML}  result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(Component) to use to split the plots<br/>
--xkey XKEY          table column name(TimePeriod) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  table column name(CL_UNIT) to use to label the data<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beainputoutput<br/>
##<br/>
usage: beainputoutput [-h] --tid TID --yr YR [--format {json,XML}]<br/>
[--csvfn CSVFN] [--splitkey SPLITKEY] [--xkey XKEY]<br/>
[--ykey YKEY] [--unitskey UNITSKEY] [--htmlfn HTMLFN]<br/>
<br/>
get BEA InputOutput data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--tid TID            table id<br/>
--yr YR              year YYYY or ALL<br/>
--format {json,XML}  request result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(ColDescr) to use to split the plots<br/>
--xkey XKEY          table column name(Year) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  table column name(ColType) to y label the plot<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beaissta<br/>
##<br/>
usage: beaissta [-h] --chan CHAN --dest DEST --indstry INDSTRY --aoc AOC<br/>
--yr YR [--format {json,XML}] [--csvfn CSVFN]<br/>
[--splitkey SPLITKEY] [--xkey XKEY] [--ykey YKEY]<br/>
[--unitskey UNITSKEY] [--htmlfn HTMLFN]<br/>
<br/>
get BEA IntlServSTA data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--chan CHAN          channel<br/>
--dest DEST          destination<br/>
--indstry INDSTRY    industry<br/>
--aoc AOC            area or country<br/>
--yr YR              year YYYY or ALL<br/>
--format {json,XML}  query result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(TimeSeriesDescription) to use to<br/>
split the plots<br/>
--xkey XKEY          table column name(Year) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  table column name({'option_strings': ['--unitskey'],<br/>
'dest': 'unitskey', 'nargs': None, 'const': None,<br/>
'default': 'CL_UNIT', 'type': None, 'choices': None,<br/>
'required': False, 'help': 'table column name(%s) to y<br/>
label the plot', 'metavar': None, 'container':<br/>
<argparse._ArgumentGroup object at 0x105401c70>,<br/>
'prog': 'beaissta'}) to y label the plot<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beaistrade<br/>
##<br/>
usage: beaistrade [-h] --tos TOS [--tdir TDIR] [--affl AFFL] [--aoc AOC]<br/>
--yr YR [--format {json,XML}] [--csvfn CSVFN]<br/>
[--splitkey SPLITKEY] [--xkey XKEY] [--ykey YKEY]<br/>
[--unitskey UNITSKEY] [--htmlfn HTMLFN]<br/>
<br/>
get BEA IntlServTrade data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--tos TOS            type of service<br/>
--tdir TDIR          trade direction<br/>
--affl AFFL          affiliation<br/>
--aoc AOC            area or country<br/>
--yr YR              year YYYY or ALL<br/>
--format {json,XML}  query result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(TimeSeriesDescription) to use to<br/>
split the plots<br/>
--xkey XKEY          table column name(Year) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  table column name(CL_UNIT) to use to label the data<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beaita<br/>
##<br/>
usage: beaita [-h] --indctr INDCTR --aoc AOC --freq FREQ --yr YR<br/>
[--format {json,XML}] [--csvfn CSVFN] [--splitkey SPLITKEY]<br/>
[--xkey XKEY] [--ykey YKEY] [--unitskey UNITSKEY]<br/>
[--htmlfn HTMLFN]<br/>
<br/>
get BEA ITA data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--indctr INDCTR      ITA indicator<br/>
--aoc AOC            ITA area or country<br/>
--freq FREQ          frequency M, Q, A or comma separated list<br/>
--yr YR              year YYYY or ALL<br/>
--format {json,XML}  query result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(TimeSeriesDescription) to use to<br/>
split the plots<br/>
--xkey XKEY          table column name(Year) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  table column name({'option_strings': ['--unitskey'],<br/>
'dest': 'unitskey', 'nargs': None, 'const': None,<br/>
'default': 'CL_UNIT', 'type': None, 'choices': None,<br/>
'required': False, 'help': 'table column name(%s) to y<br/>
label the plot', 'metavar': None, 'container':<br/>
<argparse._ArgumentGroup object at 0x1037e8380>,<br/>
'prog': 'beaita'}) to y label the plot<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beamne<br/>
##<br/>
usage: beamne [-h] [--sid SID] --doi DOI --cls CLS [--cnt CNT]<br/>
[--indstry INDSTRY] --yr YR [--format {json,XML}]<br/>
[--csvfn CSVFN] [--splitkey SPLITKEY] [--xkey XKEY]<br/>
[--ykey YKEY] [--unitskey UNITSKEY] [--htmlfn HTMLFN]<br/>
<br/>
get BEA MNE data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--sid SID            MNE series id<br/>
--doi DOI            direction of investment<br/>
--cls CLS            classification<br/>
--cnt CNT            country<br/>
--indstry INDSTRY    industry<br/>
--yr YR              year YYYY or all<br/>
--format {json,XML}  query result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(SeriesName) to use to split the plots<br/>
--xkey XKEY          table column name(Year) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  table column name(TableScale) to to y label the plot<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beanipa<br/>
##<br/>
usage: beanipa [-h] --tn TN [--showm SHOWM] --freq FREQ --yr YR<br/>
[--format {json,XML}] [--csvfn CSVFN] [--splitkey SPLITKEY]<br/>
[--xkey XKEY] [--ykey YKEY] [--unitskey UNITSKEY]<br/>
[--htmlfn HTMLFN]<br/>
<br/>
get BEA NIPA data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--tn TN              NIPA table name<br/>
--showm SHOWM        NIPA show millions<br/>
--freq FREQ          frequency M, Q, A or comma separated list<br/>
--yr YR              year YYYY or X for all<br/>
--format {json,XML}  query result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(LineDescription) to use to split the<br/>
plots<br/>
--xkey XKEY          table column name(TimePeriod) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  table column name(METRIC_NAME) to y label the plot<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beaniud<br/>
##<br/>
usage: beaniud [-h] --tn TN --freq FREQ --yr YR [--format {json,XML}]<br/>
[--csvfn CSVFN] [--splitkey SPLITKEY] [--xkey XKEY]<br/>
[--ykey YKEY] [--unitskey UNITSKEY] [--htmlfn HTMLFN]<br/>
<br/>
get BEA NIUnderlyingDetail data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--tn TN              NIUnderlyingDetail table name<br/>
--freq FREQ          frequency M, Q, A or comma separated list<br/>
--yr YR              year YYYY or X or all<br/>
--format {json,XML}  query result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name({'option_strings': ['--splitkey'],<br/>
'dest': 'splitkey', 'nargs': None, 'const': None,<br/>
'default': 'LineDescription', 'type': None, 'choices':<br/>
None, 'required': False, 'help': 'table column name(%s)<br/>
to use to split the plots', 'metavar': None,<br/>
'container': <argparse._ArgumentGroup object at<br/>
0x1038858e0>, 'prog': 'beaniud'}) to use to split<br/>
the plots<br/>
--xkey XKEY          table column name(TimePeriod) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  table column name(METRIC_NAME) to y label the plot<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## bearegional<br/>
##<br/>
usage: bearegional [-h] --tn TN --fips FIPS --lncd LNCD --yr YR<br/>
[--format {json,XML}] [--csvfn CSVFN]<br/>
[--splitkey SPLITKEY] [--xkey XKEY] [--ykey YKEY]<br/>
[--unitskey UNITSKEY] [--htmlfn HTMLFN]<br/>
<br/>
get BEA Regional data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--tn TN              table name<br/>
--fips FIPS          geo fips<br/>
--lncd LNCD          line code<br/>
--yr YR              year YYYY or ALL<br/>
--format {json,XML}  query result format(json)<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(GeoName) to use to split the plots<br/>
--xkey XKEY          table column name(TimePeriod) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  table column name(CL_UNIT) to y label the plot<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beaugdpbyind<br/>
##<br/>
usage: beaugdpbyind [-h] --tid TID --indstry INDSTRY --freq FREQ --yr YR<br/>
[--format {json,XML}] [--csvfn CSVFN]<br/>
[--splitkey SPLITKEY] [--xkey XKEY] [--ykey YKEY]<br/>
[--unitskey UNITSKEY] [--htmlfn HTMLFN]<br/>
<br/>
get BEA UnderlyingGDPbyIndustry data<br/>
<br/>
options:<br/>
-h, --help           show this help message and exit<br/>
--tid TID            table id<br/>
--indstry INDSTRY    industry<br/>
--freq FREQ          frequency M, Q, A or comma separated list<br/>
--yr YR              year YYYY or ALL<br/>
--format {json,XML}  result format<br/>
--csvfn CSVFN        name of file to store dataset CSV result<br/>
--splitkey SPLITKEY  table column name(IndustrYDescription) to split the<br/>
plots<br/>
--xkey XKEY          table column name(Year) to use to plot the data<br/>
--ykey YKEY          table column name(DataValue) to use to plot the data<br/>
--unitskey UNITSKEY  name(Billions?) to y label the plot<br/>
--htmlfn HTMLFN      name of file to store dataset HTML result<br/>
<br/>
<br/>
##<br/>
## beaqueryq<br/>
##<br/>
usage: beaqueryq [-h]<br/>
[--dataset {NIPA,NIUnderlyingDetail,MNE,FixedAssets,ITA,IIP,InputOutput,IntlServTrade,IntlServSTA,GDPbyIndustry,Regional,UnderlyingGDPbyIndustry,APIDatasetMetaData}]<br/>
[--tn TN] [--tid TID] [--sid SID] [--showm SHOWM]<br/>
[--freq FREQ] [--yr YR]<br/>
[--doi {inward,outward,parent,state}] [--cls CLS]<br/>
[--indstry INDSTRY] [--cnt CNT] [--indctr INDCTR]<br/>
[--aoc AOC] [--toi TOI] [--comp COMP] [--tos TOS]<br/>
[--tdir TDIR] [--affl AFFL] [--chan CHAN] [--dest DEST]<br/>
[--fips FIPS] [--lncd LNCD] [--csvfn CSVFN]<br/>
[--splitkey SPLITKEY] [--xkey XKEY] [--ykey YKEY]<br/>
[--unitskey UNITSKEY] [--htmlfn HTMLFN]<br/>
[--format {json,XML}] [--hierarchy] [--tableregister]<br/>
<br/>
get BEA data<br/>
<br/>
options:<br/>
-h, --help            show this help message and exit<br/>
--dataset {NIPA,NIUnderlyingDetail,MNE,FixedAssets,ITA,IIP,InputOutput,IntlServTrade,IntlServSTA,GDPbyIndustry,Regional,UnderlyingGDPbyIndustry,APIDatasetMetaData}<br/>
dataset name<br/>
--tn TN               NIPA NIUnderlyingDetail FixedAssets Regional table<br/>
name<br/>
--tid TID             InputOutput GDPbyIndustry UnderlyingGDPbyIndustry<br/>
table id<br/>
--sid SID             MNE series id<br/>
--showm SHOWM         NIPA show millions<br/>
--freq FREQ           frequency M, Q, A or comma separated list<br/>
--yr YR               year YYYY X or all<br/>
--doi {inward,outward,parent,state}<br/>
MNE direction of investment<br/>
--cls CLS             MNE classification<br/>
--indstry INDSTRY     MNE IntlServSTA GDPbyIndustry UnderlyingGDPbyIndustry<br/>
Industry<br/>
--cnt CNT             MNE country<br/>
--indctr INDCTR       ITA indicator<br/>
--aoc AOC             ITA IntlServTrade IntlServSTA area or country<br/>
--toi TOI             IIP type of investment<br/>
--comp COMP           IIP component<br/>
--tos TOS             IntlServTrade type of service<br/>
--tdir TDIR           IntlServTrade trade direction<br/>
--affl AFFL           IntlServTrade affiliation<br/>
--chan CHAN           IntlServSTA channel<br/>
--dest DEST           IntlServSTA destination<br/>
--fips FIPS           Regional geo FIPS<br/>
--lncd LNCD           Regional line code<br/>
--csvfn CSVFN         name of file to store dataset CSV result<br/>
--splitkey SPLITKEY   table column name to use to split the table<br/>
--xkey XKEY           table column name to use to plot the data<br/>
--ykey YKEY           table column name to use to plot the data<br/>
--unitskey UNITSKEY   table column name to use to label the data<br/>
--htmlfn HTMLFN       name of file to store dataset HTML result<br/>
--format {json,XML}   query result format<br/>
--hierarchy           BEA data model<br/>
--tableregister       get NIPA table register<br/>
<br/>
