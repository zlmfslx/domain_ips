# -*- coding: UTF-8 -*-
#__author__ = 'Administrator'

import os
import xlrd

def ip(path):
    domains = []
    ips = []
    domain_ips = []
    for file in os.listdir(path):
        #dtnz360.com_alidns_record
        sheet1 =file.split('_')[0]
        data=xlrd.open_workbook(path+file,encoding_override="cp1252")
        sheet_1_by_name=data.sheet_by_name(sheet1)
        n_of_rows=sheet_1_by_name.nrows#多少行

        for i in range(n_of_rows):
            if i != 0:
                arr = sheet_1_by_name.row_values(i)

                domain = str(arr[1])+'.'+sheet1
                domain = domain.strip('@.')
                ip = str(arr[3])
                domain_ip = domain+'   '+ip
                ips.append(ip)
                domains.append(domain)
                domain_ips.append(domain_ip)

    #u'去除重复'
    domains =list(set(domains))
    ips =list(set(ips))
    domain_ips =list(set(domain_ips))
    #print domains
    for i in ips:
        print i
    #print len(domains)



#print domains
if __name__ == '__main__':
    path='C:\\Users\\Administrator\\Downloads\\domain\\'
    ip(path)