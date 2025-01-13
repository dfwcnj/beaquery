#! env python
#
import argparse
import json
import os
import sys
import time
import xml


class BEAQueryITA():
    def __init__(self):

        self.bsurl = 'https://apps.bea.gov/api/signup/'
        self.bdurl = 'https://apps.bea.gov/api/data/'
        if 'BEA_API_KEY' in os.environ:
                self.api_key = os.environ['BEA_API_KEY']
        else:
            print('BEA api_key required: %s' % (self.bsurl), file=sys.stderr)
            print('assign this key to BEA_API_KEY env variable',
                              file=sys.stderr)
            sys.exit()

        self.burl = '%s?&UserID=%s' % (self.bdurl, self.api_key)

    def getitatbls(self, ind, area, fq, yr, fmt):
        params = ('&method=GetData&'
                  'DatasetName=ITA&'
                  'Indicator=%s&'
                  'AreaorCountry=%s&'
                  'Frequency=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ind, area, fq, yr, fmt) )
        url = self.burl % params

    def getparamvals(self, dsn, prm, fmt):
        params = ('&method=GetParameterValue&'
                  'DatasetName=%s&'
                  'ParameterName=%s&'
                  'ResultFormat=%s' %
                  (dsn, prm, fmt) )
        url = self.burl % params

    def getparams(self, dsn, fmt):
        params = ('&method=getparameterlist&'
                  'DatasetName=%s&'
                  'ResultFormat=%s' %
                  (dsn, fmt) )
        url = self.burl % params

    def getdatasets(self, fmt):
        params = ('&method=GETDATASETLIST&'
                  'ResultFormat=%s' % fmt)
        url = self.burl % params
#
def main():
    argp = argparse.ArgumentParser(description='explore BEA structure')

    argp.add_argument('--indicator', help='type of transaction indicator')
    argp.add_argument('--area', default = 'AllCountries',
                     help='area or country or ALL')
    argp.add_argument('--freq', default = 'A',
                     choices=['A', 'QSA', 'QNSA'],
                     help='frequency QSA, QNSA, A ')
    argp.add_argument('--yr', default = 'ALL',
                      help='year 1929-2025 or ALL ')
    argp.add_argument('--format', default='json',
                      choices=['json', 'XML'], help='result format')

    argp.add_argument('--hierarchy', action='store_true', default=False,
        help='display BEA data organization hierarchy')
    argp.add_argument('--datasets', action='store_true', default=False,
        help='display datasets')
    argp.add_argument('--params', action='store_true', default=False,
        help='display parameters for a dataset')
    argp.add_argument('--paramvals', action='store_true', default=False,
              help='show values for a parameter of a dataset')
    args=argp.parse_args()

    BITA = BEAQueryITA()

    argp.print_help()




if __name__ == '__main__':
    main()
