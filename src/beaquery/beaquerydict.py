#! env python
#
import os
import sys
import json
import time
import argparse
import pandas as pd

import beaapi


class BEAQueryDict():
    def __init__(self):

        # BEA
        self.burl = 'https://apps.bea.gov/api/signup/'
        if 'BEA_API_KEY' in os.environ:
                self.api_key = os.environ['BEA_API_KEY']
        else:
            print('BEA api_key required: %s' % (self.burl), file=sys.stderr)
            print('assign this key to BEA_API_KEY env variable',
                              file=sys.stderr)
            sys.exit()

        self.delay = 2

        # pandas
        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)


    def dsparamvals(self, dataset_name, parameter_name):
        """ dsparamvals(dataset_name, parameter_name)
        dataset_name - name of the dataset
        parameter_name - name of the parameter
        return pandas dataframe for the values of the dataset parameter
        """
        print('Values for dataset %s parameter %s' % (dataset_name,
                          parameter_name), file=sys.stderr)
        try:
            pvalframe = beaapi.get_parameter_values(self.api_key,
                            dataset_name,
                                                     parameter_name)
        except Exception as e:
            print('dsparamvals get_parameter_values %s' % e)
            sys.exit()

        time.sleep(self.delay)
        return pvalframe


    def dsparams(self, dataset_name):
        """ dsparams(dataset_name)
        dataset_name = name of the dataset
        return pandas frame for the parameters of a dataset
        """
        print('Parameters for %s dataset' % dataset_name,
        file=sys.stderr)
        try:
            paramframe = beaapi.get_parameter_list(self.api_key,
                                                       dataset_name)
        except Exception as e:
            print('dsparams get_parameter_list %s' % e)
            sys.exit()

        time.sleep(self.delay)
        return paramframe

    def datasets(self):
        """ datasets()
        return pandas frame for BEA datasets
        """
        try:
            datasetsframe = beaapi.get_data_set_list(self.api_key)
        except Exception as e:
            print('hierarchy get_data_set_list %s' % e)
            sys.exit()

        time.sleep(self.delay)
        return datasetsframe

    def jsondatasetshtml(self, dict):
        """ jsondatasetshtml(dict)
        render BEA dataset names parameters and values to html
        dict = dictionary containing model data for datasets
        return array containing an html rendering
        """
        ka = [k for k in dict['dataset'].keys()]
        htmla = []
        htmla.append('<table border=1 >')
        hd = '</th><th scope="col">'.join(['DatasetName', 'DatasetDescription'])
        htmla.append('<tr><th scope="col">%s</th></tr>' % (hd) )
        cap = '<caption>%s</caption>' % ('BEA Datasets')
        htmla.append(cap)
        for k in ka:
            ra = [k, dict['dataset'][k]]
            rw = '</td><td scope="row">'.join(ra)
            htmla.append('<tr><td scope="row">%s</td></tr>' % (rw) )
        htmla.append('</table>')
        for k in ka:
            ht = self.jsonparametershtml(k, dict['dataset'][k])
            htmla.extend(ht)
            ht = self.jsonparametervalueshtml(k, dict['dataset'][k])
            htmla.extend(ht)

    def jsonparametershtml(self, ds, dict):
        """ jsonparametershtml(ds, dict)
        ds - dataset name
        dict - dict containing data model for a dataset
        return an html table rendering for the parameters of a dataset
        """
        ka = [k for k in dict['Parameters'][0].keys()]
        htmla = []
        htmla.append('<table border=1 >')
        hd = '</th><th scope="col">'.join(ka)
        htmla.append('<tr><th scope="col">%s</th></tr>' % (hd) )
        cap = '<caption>%s</caption>' % ('BEA Dataset %s Parameters' % ds)
        htmla.append(cap)
        for d in dict['Parameters']:
            ra = [d[k] for k in d.keys()]
            rw = '</td><td scope="row">'.join(ra)
            htmla.append('<tr><td scope="row">%s</td></tr>' % (rw) )
        htmla.append('</table>')
        return htmla

    def jsonparametervalueshtml(self, ds, param, dict):
        """ jsonparametervalueshtml(ds, param, dict)
        ds - dataset name
        param - parameter name
        dict - dictionary containing schema for values of a parameter of a dataset
        return an html table rendering for the values of the parameter
        """
        ka = [k for k in dict['ParameterValuess'][0].keys()]
        htmla = []
        htmla.append('<table border=1 >')
        hd = '</th><th scope="col">'.join(ka)
        htmla.append('<tr><th scope="col">%s</th></tr>' % (hd) )
        cap = '<caption>%s</caption>' % ('BEA Datasets')
        htmla.append(cap)
        cap = '<caption>%s</caption>' % ('BEA Dataset %s Parameter %v Values' % (ds, param))
        htmla.append(cap)
        for d in dict['ParameterValuess']:
            ra = [d[k] for k in d.keys()]
            rw = '</td><td scope="row">'.join(ra)
            htmla.append('<tr><td scope="row">%s</td></tr>' % (rw) )
        htmla.append('</table>')
        return htmla
        pass

    def datasetdictparamval(self, i, pvdict):
        pvd = {}
        for k in pvdict.keys():
            pvd[k] = pvdict[k][i]
        return pvd

    def datasetdictparamvals(self, dsdict, dn):
        dsdict['datasets'][dn]['ParameterValues'] = {}
        for i in range(1, len(dsdict['datasets'][dn]['Parameters'])):
            pn = dsdict['datasets'][dn]['Parameters'][1][0]
            pvalframe = self.dsparamvals(dn, pn)
            pvalsdict = pvalframe.to_dict()
            ks = [k for k in pvalsdict.keys()]
            ix = [i for i in pvalsdict[ks[0]].keys()]
            rows = []
            rows.append(ks)
            for i in ix:
                rw = [pvalsdict[k][i] for k in ks]
                rows.append(rw)
            dsdict['datasets'][dn]['ParameterValues'][pn]=rows

        return

    def datasetdictparams(self, dsdict, dn):
        paramsframe = self.dsparams(dn)
        paramsdict = paramsframe.to_dict()
        ks = [k for k in paramsdict.keys()]
        ix = [i for i in paramsdict[ks[0]].keys()]
        rows = []
        rows.append(ks)
        for i in ix:
            rw = [paramsdict[k][i] for k in ks]
            rows.append(rw)
        dsdict['datasets'][dn]['Parameters'] = rows
        return

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
    argp.add_argument('--html', action='store_true', default=False,
        help='display html')
    args=argp.parse_args()

    BQ = BEAQueryDict()
    if args.hierarchy:
        dsdict = BQ.dicthierarchy()
        if args.html:
            htmla = BQ.jsondatasetshtml(dsdict)
            print(''.join(htmla))
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
        if args.dataset == None or args.param == None:
            print('a dataset and parameter must be provided')
            argp.print_help()
            sys.exit()
        pvs = BQ.dsparamvals(args.dataset, args.param)
        print(pvs)
    else:
        argp.print_help()




if __name__ == '__main__':
    main()
