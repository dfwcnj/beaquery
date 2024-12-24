#! env python
#
import os
import sys
import json
import time
import argparse
import beaapi
import pandas as pd


class BEAQuery():
    def __init__(self):

        self.burl = 'https://apps.bea.gov/api/signup/'
        if 'BEA_API_KEY' in os.environ:
                self.api_key = os.environ['BEA_API_KEY']
        else:
            print('BEA api_key required: %s' % (self.burl), file=sys.stderr)
            print('assign this key to BEA_API_KEY env variable',
                              file=sys.stderr)
            sys.exit()

        # self.datasetdict = {}

        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)


    def dsparamvals(self, dataset_name, parameter_name):
        print('Values for dataset %s parameter %s' % (dataset_name,
                                                      parameter_name))
        try:
            pvals = beaapi.get_parameter_values(self.api_key,
                                                     dataset_name,
                                                     parameter_name)
        except Exception as e:
            print('dsparamvals get_parameter_values %s' % e)
            sys.exit()

        return pvals


    def dsparams(self, dataset_name):
        print('Parameters for %s dataset' % dataset_name)
        try:
            paramframe = beaapi.get_parameter_list(self.api_key,
                                                       dataset_name)
        except Exception as e:
            print('dsparams get_parameter_list %s' % e)
            sys.exit()

        return paramframe

    def datasets(self):
        try:
            datasetsframe = beaapi.get_data_set_list(self.api_key)
        except Exception as e:
            print('hierarchy get_data_set_list %s' % e)
            sys.exit()

        return datasetsframe

    def datasetdictparamval(self, i, pvdict):
        pvd = {}
        for k in pvdict.keys():
            pvd[k] = pvdict[k][i]
        return pvd

    def datasetdictparamvals(self, dsdict, dn):
        dsdict['datasets'][dn]['ParameterValues'] = []
        for pd in dsdict['datasets'][dn]['Parameters']:
            pn =  pd['ParameterName']
            pvals = self.dsparamvals(dn, pn)
            pvalsdict = pvals.to_dict()
            ks = [k for k in pvalsdict.keys()]
            for k in ks:
                ix = [i for i in pvalsdict[k].keys()]
            for k in ks:
                for i in ix:
                   pvdict = self.datasetdictparamval(i, pvalsdict)
                   dsdict['datasets'][dn]['ParameterValues'].append(pvdict)

    def datasetdictparam(self, i, pdict):
        pd = {}
        for k in pdict.keys():
                pd[k] = pdict[k][i]
        return pd

    def datasetdictparams(self, dsdict, dn):
        params = self.dsparams(dn)
        paramsdict = params.to_dict()
        dsdict['datasets'][dn]['Parameters'] = []
        ks = [k for k in paramsdict.keys()]
        for k in ks:
            ix = [i for i in paramsdict[k].keys()]
        for k in ks:
            for i in ix:
                pdict = self.datasetdictparam(i, paramsdict)
                dsdict['datasets'][dn]['Parameters'].append(pdict)

    def initdatasetdict(self, dsf):
        dsr = dsf.to_dict()
        dsdict = {}
        dsdict['datasets'] = {}
        for i in dsr['DatasetName'].keys():
            n = dsr['DatasetName'][i]
            d = dsr['DatasetDescription'][i]
            dsdict['datasets'][n] = {}
            dsdict['datasets'][n]['DatasetDescription'] = d
        return dsdict

    def dicthierarchy(self):
        datasetsframe = self.datasets()
        dsdict = self.initdatasetdict(datasetsframe)

        # datasetsframe.to_excel('beahierarchy.xlsx', sheet_name='datasets')

        for n in dsdict['datasets'].keys():
            self.datasetdictparams(dsdict, n)
            self.datasetdictparamvals(dsdict, n)

        return dsdict
#
def main():
    argp = argparse.ArgumentParser(description='explore BEA structure')

    argp.add_argument('--dataset', help='specify the dataset',
                      choices=['NIPA', 'NIUnderlyingDetail', 'MNE',
                      'FixedAssets', 'ITA', 'IIP', 'InputOutpus',
                      'IntlServTrade', 'GDPbyIndustry', 'Regional',
                      'UnderlyingGDPbyIndustry', 'APIDatasetMetaData'])

    argp.add_argument('--param', help='specify a  parameter for a dataset')

    argp.add_argument('--hierarchy', action='store_true', default=False,
        help='display BEA data organization hierarchy')
    argp.add_argument('--datasets', action='store_true', default=False,
        help='display datasets')
    argp.add_argument('--params', action='store_true', default=False,
        help='display parameters for a dataset')
    argp.add_argument('--paramvals', action='store_true', default=False,
              help='show values for a parameter of a dataset')

    argp.add_argument('--json', action='store_true', default=False,
        help='display json')
    args=argp.parse_args()

    BQ = BEAQuery()
    if args.hierarchy:
        dsdict = BQ.dicthierarchy()
        if args.json:
            dsjson = json.JSONEncoder().encode(dsdict)
            print(dsjson)
        else:
            print(dsdict)
    elif args.datasets:
        ds = BQ.datasets()
        if args.json:
            dsjson = json.JSONEncoder().encode(ds)
            print(dsjson)
        else:
            print(ds)
    elif args.params:
        if args.dataset == None:
            print('a dataset must be provided')
            argp.print_help()
            sys.exit()
        ps = BQ.dsparams(args.dataset)
        if args.json:
            psjson = json.JSONEncoder().encode(ps)
            print(psjson)
        else:
            print(ps)
    elif args.paramvals:
        if args.dataset == None and args.param == None:
            print('a dataset and parameter must be provided')
            argp.print_help()
            sys.exit()
        pvs = BQ.dsparamvals(args.dataset, args.param)
        print(pvs)




if __name__ == '__main__':
    main()
