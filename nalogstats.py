#!usr/bin/env python

import os
import os.path
import xlrd
import csv

YEARS = [2012, 2013, 2014, 2015, 2016, 2017, 2018]

FILEPATH_IP = 'process/IP/'
FILEPATH_UL = 'process/UL/'
ROSFED ='Российская Федерация'

def process_files():
    alldata = {}
    allregs = {}
    rfdata = []
    for y in YEARS:
        regdata = {}

        # Process IP data
        filename = FILEPATH_IP + str(y) + '.xls'
        print('Processing %s' % (filename))
        w = xlrd.open_workbook(filename)
        s2010 = w.sheet_by_name('2010')
        rf_val = s2010.row_values(10)
        row = [str(y), rf_val[1], str(int(rf_val[3])), str(int(rf_val[8])), str(round(rf_val[3]*100/rf_val[8], 2))]
        rowid = 11
        while True:
            try:
                val = s2010.row_values(rowid)
            except IndexError:
                break
            if len(val[1]) == 0: break
            regcode = None
            if type(val[0]) == float:
                regcode = str(int(val[0]))
            elif val[0].isdigit():
                regcode = val[0]
            if regcode:
                regdata[regcode] = [regcode, val[1], int(val[3]), int(val[8]), round(val[3]*100/val[8], 2)]
                if int(val[0]) not in allregs.keys():
                    allregs[regcode] = val[1]
            rowid += 1
        alldata[y] = regdata

        regdata_ul = {}
        # Process UL data
        filename = FILEPATH_UL + str(y) + '.xls'
        print('Processing %s' % (filename))
        wul = xlrd.open_workbook(filename)
        s2010ul = wul.sheet_by_name('2010')
        rf_ul_val = s2010ul.row_values(13)
        row.extend([str(int(rf_ul_val[3])), str(int(rf_ul_val[7])), str(round(rf_ul_val[3]*100/rf_ul_val[7], 2))])
        rfdata.append(row)
        rowid = 14
        while True:
            try:
                val = s2010ul.row_values(rowid)
            except IndexError:
                break
            if len(val[1]) == 0: break
            regcode = None
            if type(val[0]) == float:
                regcode = str(int(val[0]))
            elif val[0].isdigit():
                regcode = val[0]
            if regcode:
                regdata_ul[regcode] = [int(val[3]), int(val[7]), round(val[3]*100/val[7], 2)]
                if int(val[0]) not in allregs.keys():
                    allregs[regcode] = val[1]
                if regcode in alldata[y].keys():
                    alldata[y][regcode].extend(regdata_ul[regcode])
            rowid += 1


#    print('\t'.join(['year','region','ip_reg','ip_liq', 'ip_reg_liq_diff', 'ul_reg', 'ul_liq', 'ul_reg_liq_diff']))
#    for row in rfdata:
#        print('\t'.join(row))


    print('Writing nalog_rosfed.csv with Russian federation 2012-2018 stats')
    wr = csv.writer(open('nalog_rosfed.csv', 'w', encoding='utf8'), delimiter=',')
    wr.writerow(['year','region','ip_reg','ip_liq', 'ip_reg_liq_diff', 'ul_reg', 'ul_liq', 'ul_reg_liq_diff'])
    wr.writerows(rfdata)
    regcodes = list(allregs.keys())
    regcodes.sort()

    print('Writing nalog_regions.csv with regional 2012-2018 stats')
    wr = csv.writer(open('nalog_regions.csv', 'w', encoding='utf8'), delimiter=',')
    wr.writerow(['year','regcode','region','ip_reg','ip_liq', 'ip_reg_liq_diff', 'ul_reg', 'ul_liq', 'ul_reg_liq_diff'])
    for r in regcodes:
        for y in YEARS:
            if r not in alldata[y].keys(): continue
            wr.writerow([str(y), str(r), allregs[r], str(alldata[y][r][2]),
                             str(alldata[y][r][3]), str(alldata[y][r][4]),
                             str(alldata[y][r][5]),
                             str(alldata[y][r][6]), str(alldata[y][r][7])
                             ])

def run():
    process_files()
    pass

if __name__ == "__main__":
    run()