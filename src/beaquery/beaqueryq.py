
#! env python
#
import argparse
import json
import os
import sys
import time
import webbrowser
import xml
import xml.etree.ElementTree as ET

try:
    import beaquery.ebquery
except Exception as e:
    import ebquery


class BEAQueryQ():
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

        self.trurl = 'https://apps.bea.gov/national/Release/TXT/TablesRegister.txt'

        self.uq = ebquery._EBURLQuery()

    def getNIPAregister(self):
        """ getNIPAregister()
        retrieve and return the register of BEA NIPA tables
        """
        resp = self.uq.query(self.trurl)
        if resp == None:
            print('getNIPAregister: no response', file=sys.stderr)
            return resp
        rstr = resp.read().decode('utf-8')
        return rstr

    # not using TableID Parameter
    def NIPAParams(self, tn, fq, yr, fmt,
                   ds='NIPA', shm='N'):
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TableName=%s&'
                  'ShowMillions=%s&'
                  'Frequency=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, tn, shm, fq, yr, fmt) )
        return params

    def NIUnderlyingDetailParams(self, tn, fq, yr, fmt):
        return self.NIPAParams(tn.  fq, yr, fmt,
                               'NIUnderlyingDetail',shm)

    def MNEParameters(self, doi, cl, fmt,
                      ds='MNE', cnt='000', ind='000', yr='all'):
        params = ('&method=GetData&'
                  'DirectionOfInvestment=%s&'
                  'Classification=%s&'
                  'Country=%s&'
                  'Industry=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, doi, cl, cnt, ind, yr, fmt) )
        return params

    def FixedAssetsParameters(self, tn, fmt, ds='FixedAssets', yr='X'):
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TableName=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, tn, yr, fmt) )
        return params

    def ITAParameters(self, ind, fmt,
                      ds='ITA', area='ALL', fq='ALL', yr='ALL'):
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'Indicator=%s&'
                  'AreaOrCountry=%s&'
                  'Frequency=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, ind, area, fq, yr, fmt) )
        return params

    def IIPParameters(self, toi, fmt, ds='IIP', cmp='ALL', fq='ALL', yr='ALL'):
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TypeOfInvestment=%s&'
                  'Component=%s&'
                  'Frequency=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, toi, cmp, fq, yr, fmt) )
        return params

    def InputOutputParameters(self, tid, fmt, ds='InputOutput', yr='ALL'):
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TableID=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, tid, yr, fmt) )
        return params

    def IntlServTradeParameters(self, fmt,
                                ds='IntlServTrade', tos='ALL', td='ALL',
                                aff='All', area='All', year='ALL'):
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TypeOfService=%s&'
                  'TradeDirection=%s&'
                  'Affiliation=%s&'
                  'AreaOrCountry=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, tos, td, aff, area, yr, fmt) )
        return params

    def IntlServSTAParameters(self, fmt, ds='IntlServSTA', ch='ALL',
                              dst='ALL', ind='ALL', area='ALL', year='ALL'):
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'Channel=%s&'
                  'Destination=%s&'
                  'Industry=%s&'
                  'AreaOrCountry=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, ch, dst, ind, area, yr, fmt) )
        return params

    def GDPbyIndustryParameters(self, fmt,
                                tid='ALL', ind='ALL', fq='ALL', yr='ALL'):
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TableID=%s&'
                  'Industry=%s&'
                  'Frequency=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, tid, ind, fq, yr, fmt) )
        return params

    def RegionalParameters(self, tn, lc, fmt,
                           ds='Regional', fips='STATE', yr='ALL'):
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'GeoFIPS=%s&'
                  'TableName=%s&'
                  'LineCode=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, fips, tn, lc, yr, fmt) )
        return params

    def UnderlyingGDPbyIndustryParameters(self, fmt,
                                          ds='UnderlyingGDPbyIndustry',
                                          tid='ALL', ind='All',
                                          fq='ALL', yr='ALL'):
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TableID=%s&'
                  'Industry=%s&'
                  'Frequency=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, tid, ind, fq, yr, fmt) )
        return params



    # NIPA NIUnderlyingDetail
    def gettfydata(self, ds, tn, fq, yr, fmt):
        """ gettfydata(ds, tn, fq, yr, fmt)
        ds - dataset name
        tn - table name
        fq - frequency
        yr - year
        fmt - result format
        retrieve BEA table for BEA dataset
        """
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TableName=%s&'
                  'Frequency=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, tn, fq, yr, fmt) )
        url = self.burl + params
        resp = self.uq.query(url)
        if resp == None:
            print('gettfydata: no response', file=sys.stderr)
            return resp
        rstr = resp.read().decode('utf-8')
        jsd = json.loads(rstr)
        return jsd['BEAAPI']['Results']

    # FixedAssets
    def gettydata(self, ds, tn, yr, fmt):
        """ gettydata(ds, tn, fq, yr, fmt)
        ds - dataset name
        tn - table name
        yr - year
        fmt - result format
        retrieve BEA table for BEA dataset
        """
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TableName=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, tn, fq, yr, fmt) )
        url = self.burl + params
        resp = self.uq.query(url)
        if resp == None:
            print('gettydata: no response', file=sys.stderr)
            return resp
        rstr = resp.read().decode('utf-8')
        jsd = json.loads(rstr)
        return jsd['BEAAPI']['Results']

    # MNE
    def getdcydata(self, ds, doi, cl, yr, fmt):
        """ getdcydata(ds, doi, cl, yr, fmt)
        ds - dataset name
        doi - direction of investment
        cl - classification
        yr - year
        fmt - result format
        retrieve BEA table for BEA dataset
        """
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'DirectionofInvestmane=%s&'
                  'Claѕsification=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, doi, cl, yr, fmt) )
        url = self.burl + params
        resp = self.uq.query(url)
        if resp == None:
            print('getdcydata: no response', file=sys.stderr)
            return resp
        rstr = resp.read().decode('utf-8')
        jsd = json.loads(rstr)
        return jsd['BEAAPI']['Results']

    # ITA
    def getiafydata(self, ds, ind, area, fq, yr, fmt):
        """ getiafydata(ind, area, fq, yr, fmt)
        ds - dataset name
        ind - indicator
        area - area or country
        fq - frequency
        yr - year
        fmt - retult format
        """
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'Indicator=%s&'
                  'AreaorCountry=%s&'
                  'Frequency=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, ind, area, fq, yr, fmt) )
        url = self.burl + params
        resp = self.uq.query(url)
        if resp == None:
            print('getdcydata: no response', file=sys.stderr)
            return resp
        rstr = resp.read().decode('utf-8')
        jsd = json.loads(rstr)
        return jsd['BEAAPI']['Results']

    # IIP
    def gettcfydata(self, ds, toi, cmp, fq, yr, fmt):
        """ gettcfydata(ind, area, fq, yr, fmt)
        ds - dataset name
        toi - type of investment
        cmp - component
        fq - frequency
        yr - year
        fmt - retult format
        """
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TypeOfInvestment=%s&'
                  'Component=%s&'
                  'Frequency=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, ind, area, fq, yr, fmt) )
        url = self.burl + params
        resp = self.uq.query(url)
        if resp == None:
            print('gettcfydata: no response', file=sys.stderr)
            return resp
        rstr = resp.read().decode('utf-8')
        jsd = json.loads(rstr)
        return jsd['BEAAPI']['Results']

    # InputOutput
    def getiodata(self, ds, tid, yr, fmt):
        """ getiodata(ind, area, fq, yr, fmt)
        ds - dataset name
        toi - type of investment
        cmp - component
        fq - frequency
        yr - year
        fmt - retult format
        """
        params = ('&method=GetData&'
                  'DatasetName=%s&'
                  'TableID=%s&'
                  'Year=%s&'
                  'ResultFormat=%s' %
                  (ds, tid, yr, fmt) )
        url = self.burl + params
        resp = self.uq.query(url)
        if resp == None:
            print('getiodata: no response', file=sys.stderr)
            return resp
        rstr = resp.read().decode('utf-8')
        jsd = json.loads(rstr)
        return jsd['BEAAPI']['Results']



    def dd2csv(self, jsd):
        """ dd2csv(jsd)
        jsd - restults from BEA table query
        return csv text for table data
        """
        aa = self.dd2aa(jsd, 'Data')
        csv = self.aa2csv(aa)
        return csv

    def aa2table(self, cap, aa):
       """ aa2table(aa)

       convert array of arrays to an html table
       aa - array of arrays
       """
       tbla = []
       # table
       tbla.append('<table border="1">')
       # table header
       hdra = aa[0]
       hdr = '</th><th>'.join(hdra)
       tbla.append('<tr><th scope="col">%s</th></tr>' % (hdr) )
       cap = '<caption>%s</caption>' % cap
       tbla.append(cap)
       # table rows
       for i in range(1, len(aa) ):
           rowa = aa[i]
           for j in range(len(rowa)):
               if rowa[j] == None:
                   rowa[j] = ''
               elif type(rowa[j]) == type(1):
                   rowa[j] = '%d' % rowa[j]
           row = '</td><td>'.join(rowa)
           tbla.append('<tr><td>%s</td></tr>' % (row) )

       # close
       tbla.append('</table>')
       return tbla


    def x2aa(self, dss, jsk):
        """ x2dict(dss)
        dss - string containing XML
        convert string result to array of arrays
        """
        root = ET.fromstring(dss)
        keys = []
        aa = []
        for c in root:
            for gc in c:
                if c.tag == 'Results':
                    print(c.tag, c.attrib, gc.tag, gc.attrib)
                    if len(aa) == 0:
                        keys = [k for k in gc.attrib.keys()]
                        aa.append(keys)
                    a = []
                    for k in keys:
                        a.append(gc.attrib[k])
                    aa.append(a)
        return aa


    def dd2aa(self, dsd, jsk):
        """ dd2aa(dss)
        dss - string containing json
        convert string result to array of arrays
        """
        keys = [k for k in dsd[jsk][0].keys()]
        aa = []
        for d in dsd[jsk]:
            if len(aa) == 0:
                aa.append(keys)
            a = []
            for k in keys:
                if k not in d:
                    a.append('')
                else:
                    a.append(d[k])
            aa.append(a)
        return aa

    def js2aa(self, dss, jsk):
        """ js2aa(dss)
        dss - string containing json
        convert string result to array of arrays
        """
        dsd = json.loads(dss)

        if type(dsd['BEAAPI']['Results'][jsk]) != type([]):
            keys = [k for k in dsd['BEAAPI']['Results'][jsk].keys()]
            aa = []
            aa.append(keys)
            a = []
            for k in keys:
                a.append(dsd['BEAAPI']['Results'][jsk][k])
            aa.append(a)
            return aa


        keys = [k for k in dsd['BEAAPI']['Results'][jsk][0].keys()]
        aa = []
        for d in dsd['BEAAPI']['Results'][jsk]:
            if len(aa) == 0:
                aa.append(keys)
            a = []
            for k in keys:
                if k not in d:
                    a.append('')
                else:
                    if d[k].endswith(' '):
                        d[k] = d[k][0:-1]
                    a.append(d[k])
            aa.append(a)
        return aa

    def aa2csv(self, aa):
        csva = []
        for a in aa:
            csva.append('"%s"' % '","'.join(a))
        return '\n'.join(csva)

    def dsparamvals(self, ds, param, fmt):
        """ dsparamvale(ds, param, fmt)
        ds - dataset name
        param - parameter name
        fmt - result format
        retrieve parameter values for BEA dataset parameter
        """
        params = ('&method=GetParameterValues&'
                  'Datasetname=%s&'
                  'ParameterName=%s&'
                  'ResultFormat=%s' % (ds, param, fmt))
        url = self.burl + params
        resp = self.uq.query(url)
        if resp == None:
            print('dsparamvale: no response', file=sys.stderr)
            return resp
        rstr = resp.read().decode('utf-8')
        return rstr

    def dsparams(self, ds, fmt):
        """ dsparams(ds, fmt)
        ds - dataset name
        fmt - result format
        retrieve parameter list for a BEA dataset
        """
        params = ('&method=GetParameterList&'
                  'Datasetname=%s&'
                  'ResultFormat=%s' % (ds, fmt))
        url = self.burl + params
        resp = self.uq.query(url)
        if resp == None:
            print('dsparams: no response', file=sys.stderr)
            return resp
        rstr = resp.read().decode('utf-8')
        return rstr

    def datasets(self, fmt):
        """ datasets(fmt)
        fmt - result format
        retrieve BEA datasets list
        """
        params = ('&method=GetDatasetList&'
                  'ResultFormat=%s' % fmt)
        url = self.burl + params
        resp = self.uq.query(url)
        if resp == None:
            print('datasets: no response', file=sys.stderr)
            return resp
        rstr = resp.read().decode('utf-8')
        return rstr

    def hierarchyhtml(self, hier):
        """ hierarchyhtml(hier)
        hier - dictionary of BEA data model
        return html page for BEA data model
        """
        htmla = []
        htmla.append('<html>')
        ttl = 'BEA Dataset Data Hierarchy'
        htmla.append('<head><h1>%s</h1></head>' % (ttl) )
        dsaa = hier['Datasets']
        tbl = self.aa2table('Datasets', dsaa)
        htmla.extend(tbl)
        for i in range(1, len(dsaa)):
            dsn = dsaa[i][0]
            paa = hier[dsn]['Parameter']
            tbl = self.aa2table('%s Parameters' % dsn, paa)
            htmla.extend(tbl)
            for j in range(1, len(paa)):
                pn = paa[j][0]
                pvaa = hier[dsn]['ParameterValue'][pn]
                tbl = self.aa2table('%s Parameter %s Values' % (dsn, pn), pvaa)
                htmla.extend(tbl)
        htmla.append('</html>')
        return ''.join(htmla)

    def showhtml(self, fn, html):
        with open(fn, 'w') as fp:
            fp.write(html)
        webbrowser.open('file://%s' % fn)

    def hierarchy(self, fmt):
        """ hierarchy(fmt)
        fmt - result format
        retrieve BEA data model
        """
        hier = {}
        dss = self.datasets(fmt)
        if fmt == 'json':
            dsaa = self.js2aa(dss, 'Dataset')
        else:
           dsaa = self.x2aa(dss, 'Dataset')
        hier['Datasets'] = dsaa
        for i in range(1, len(dsaa)):
            dsn = dsaa[i][0]
            hier[dsn] = {}
            pss = self.dsparams(dsn, fmt)
            if fmt == 'json':
                paa = self.js2aa(pss, 'Parameter')
            else:
                paa = self.x2aa(pss, 'Parameter')
            hier[dsn]['Parameter'] = paa
            hier[dsn]['ParameterValue'] = {}
            for j in range(1, len(paa)):
                pn = paa[j][0]
                psv = self.dsparamvals(dsn, pn, fmt)
                if fmt == 'json':
                    vaa = self.js2aa(psv, 'ParamValue')
                else:
                    vaa = self.x2aa(psv, 'ParamValue')
                hier[dsn]['ParameterValue'][pn] = vaa
        return hier

#
def main():
    argp = argparse.ArgumentParser(description='get BEA data')

    argp.add_argument('--hierarchy',
                      action='store_true', default=False,
                      help='BEA data model ')

    argp.add_argument('--dataset', default='NIPA',
                      choices=['NIPA', 'NIUnderlyingDetail', 'MNE',
                      'FixedAssets', 'ITA', 'IIP', 'InputOutput',
                      'IntlServTrade', 'GDPbyIndustry', 'Regional',
                      'UnderlyingGDPbyIndustry', 'APIDatasetMetaData'],
                      help='dataset name')
    argp.add_argument('--table', help='dataset table name')
    argp.add_argument('--param', help='dataset parameter ')

    argp.add_argument('--tableregister',
                      action='store_true', default=False,
                      help='get NIPA table register ')

    # argp.add_argument('--freq', default = 'A',
    argp.add_argument('--freq',
                     help='frequency M, Q, A or comma separated list')
    argp.add_argument('--yr', default = 'X',
                      help='year 1929-2025 or X for all')
    # argp.add_argument('--doi', default = 'inward',
    argp.add_argument('--doi',
                      choices = ['inward', 'outward', 'parent', 'state'],
                      help='direction of investment ')
    argp.add_argument('--cls', default = 'inward',
                      help='classification country code or comma'
                      ' separated list or  000 for all')

    argp.add_argument('--format', default='json',
                      choices=['json', 'XML'], help='result format')

    args=argp.parse_args()

    BN = BEAQueryQ()

    if args.tableregister:
       txt = BN.getNIPAregister()
       print(txt)
    elif args.table:
        if args.doi:
            jsd = BN.getdcydata(args.dataset, args.doi, args.cls,
                                 args.yr, args.format)
            csvstr = BN.dd2csv(jsd)
            print(csvstr)
        elif args.freq:
            jsd = BN.gettfydata(args.dataset, args.table,
                                 args.freq, args.yr, args.format)
            csvstr = BN.dd2csv(jsd)
            print(csvstr)
        elif args.yr:
            jsd = BN.gettydata(args.dataset, args.table,
                                args.yr, args.format)
            csvstr = BN.dd2csv(jsd)
            print(csvstr)
        else:
            argp.print_help()
            sys.exit()
    elif args.hierarchy:
        hd = BN.hierarchy(args.format)
        htm = BN.hierarchyhtml(hd)
        BN.showhtml('/tmp/hierarchy.html', htm)
    else:
        argp.print_help()
        sys.exit()




if __name__ == '__main__':
    main()
