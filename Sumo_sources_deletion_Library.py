import requests
import json
import dictor
import pandas as pd
"""
# import getpass
# from builtins import input
# from datetime import datetime
# import argparse
import os
import re
import json
import time

from terminaltables import AsciiTable

def print_sources_table(collectors, headings):
    '''
    Given a set of headings and a list of Collectors, prints the attributes
    of sources for each Collector (one per row) specified in the headings
    in a nice ASCII table. If an attribute is empty, a dash is printed
    in the column instead.
    Args:
        collectors (list): The list of Collectors to be printed.
        headings (list): The list of headings for the table.
    '''
    table_data = []
    table_data.append(headings)
    table_rows = 0

    if collectors:
        for collector in collectors:
            for source in collector['sourcejson']:
                    row = []
                    row.append(collector['id'])
                    for col in headings[1:]:
                        if col == 'category' and 'category' not in source:
                            row.append('-')
                        else:
                            row.append(source[col])
                    table_data.append(row)
        table_rows = len(table_data) - 1
        print("table_rows : "+table_rows)
    else:
        table_data.append(['-'] * len(headings))   # prints blanks if table has no entries

table = AsciiTable(table_data)
log('[INFO] %d total sources\n%s' % (table_rows, table.table))

source_table_headings = ['collectorid', 'name', 'id', 'category']
collectorslist = ['saas.aws.st.app.cloudsuite-SunSystems-6-3-0.mettaprd-sun.INFORBCAPP01', 'saas.aws.st.app.cloudsuite-SunSystems-6-3-0.mettaprd-sun.INFORBCWEB01']
"""


"""
collecid = parsed["collector"]["links"][0]
print("collector id : "+ str(collecid))


print("\n")
id = parsed["sources"]["id"]
print("id value : ")
print(id)

# print(int(r['sources']['id']))
print("response url : " + str(r.url))
print("source headers Date : " + str(r.headers['Date']))
print("response id : \n" + (parsed["sources"]["id"]))
"""
# searchstring = "SunSystems"
# searchstring = "searchstring"
# hostName = "hostName"
# category = "category"
# id = "id"
# name = "name"
# sourceType = "sourceType"


# datapath = "C:\\Users\\kbachu\\OneDrive - Infor\\Desktop\\CloudOps\\sumo\\commands_collectors1.xlsx"
# sheetname = "APP and Web Collectors"
# columnheading = "app_Web_GA_Collectors"

# datapath = "Default"
# sheetname = "Default"
# columnheading = "Default"
# outputfile = "Default"
# accessid = "Have to pass the Access Id"
# accesskey = "Have to pass the Access Key"
# accessid = "suelYBY3VuU4tR"
# accesskey = "V9CnJM9DNMjLyke4k1j3hSvtpCKY4BZoL4JXA6TMCFW6tkzG5KGIE131JvrqWE1h"

# f = open('CollectorSources_to_Delete.txt','w')

f = open("Output_to_Delete_Sources.txt",'w')

def getcollectorsfromExcel(path, sheet, columnname):
    '''
    This method is used to get the daat from Excel by passing the path of excel workbook, sheet name and the column name.
    This method takes the following input: 
    1. Path = Excel workbookpath
    2. Sheet = Name of the sheet
    3. Columnname = heading of the column to get the data.
    In this case data is list of collectors and return the collectots in the List
    '''
    df = pd.read_excel(path, sheet_name=sheet) # can also index sheet by name or fetch all sheets
    mylist = df[columnname].tolist()
    # print("Number of collectors : ",  len(mylist))
    return mylist
 
def getsourceinfo_by_name(accessid, accesskey, collector, name):
 '''
this method gets the sources id based on the name provided and search with contains and creates .sh file with list of curl requests for deletion.
After the file got generated. Simply have to click the .sh file that executes one by one and performs the deletion.

 Note: Please cross verify the output file genearted before execution. shell file is very powerful and sensitive. It will direcly executes on double click.
 '''

 # Content type as application/json
 header = {'Content-Type': 'application/json'}
 auth = (accessid,accesskey)
 r = requests.get(collector,headers=header,auth=auth)
 # print("type of response : " + str(type(r.text)))

# parsing the ouput sources to json
 parsed = json.loads(r.text)


 for i in parsed["sources"]:
    # print(i)
    # if(i["category"]) == "application.AGENT": 
    # if(i["sourceType"]) == "LocalFile":
        # if(i["name"]) == "LocalFile":  
    if name in i["name"]:
        # print("Source id : " + str(i["id"]) , "Source url is : " + str(Collectorurl) + "/" + str(i["id"]) , "SourceType is : " + str(i["sourceType"]), "category is : " + str(i["category"]))
        print("Source id : " + str(i["id"]) + " | ", "Source url is : " + str(collector) + "/" + str(i["id"]) + " | ", "SourceType is : " + str(i["sourceType"]) + " | ", "category is : " + str(i["category"]))
        print("curl -u " + (accessid) + ":" + (accesskey) + " -X DELETE " + str(collector) + "/" + str(i["id"]), file=f)

def getsourceinfo_by_category(accessid, accesskey, collector, category):
 '''
this method gets the sources category based on the category provided and search with contains and creates .sh file with list of curl requests for deletion.
After the file got generated. Simply have to click the .sh file that executes one by one and performs the deletion.

 Note: Please cross verify the output file genearted before execution. shell file is very powerful and sensitive. It will direcly executes on double click.
 '''

 # Content type as application/json
 header = {'Content-Type': 'application/json'}
 auth = (accessid,accesskey)
 r = requests.get(collector,headers=header,auth=auth)
 # print("type of response : " + str(type(r.text)))

# parsing the ouput sources to json
 parsed = json.loads(r.text)

 for i in parsed["sources"]:
    if category in i["category"]:
        # print("Source id : " + str(i["id"]) , "Source url is : " + str(Collectorurl) + "/" + str(i["id"]) , "SourceType is : " + str(i["sourceType"]), "category is : " + str(i["category"]))
        print("Source id : " + str(i["id"]) + " | ", "Source url is : " + str(collector) + "/" + str(i["id"]) + " | ", "SourceType is : " + str(i["sourceType"]) + " | ", "category is : " + str(i["category"]))
        print("curl -u " + (accessid) + ":" + (accesskey) + " -X DELETE " + str(collector) + "/" + str(i["id"]), file=f)


def getsourceinfo_by_sourceType(accessid, accesskey, collector, sourceType):
 '''
this method gets the sources based on the sourceType provided and search with contains and creates .sh file with list of curl requests for deletion.
After the file got generated. Simply have to click the .sh file that executes one by one and performs the deletion.

 Note: Please cross verify the output file genearted before execution. shell file is very powerful and sensitive. It will direcly executes on double click.
 '''

 # Content type as application/json
 header = {'Content-Type': 'application/json'}
 auth = (accessid,accesskey)
 r = requests.get(collector,headers=header,auth=auth)
 # print("type of response : " + str(type(r.text)))

# parsing the ouput sources to json
 parsed = json.loads(r.text)

 for i in parsed["sources"]:
    if sourceType in i["sourceType"]:
        # print("Source id : " + str(i["id"]) , "Source url is : " + str(Collectorurl) + "/" + str(i["id"]) , "SourceType is : " + str(i["sourceType"]), "category is : " + str(i["category"]))
        print("Source id : " + str(i["id"]) + " | ", "Source url is : " + str(collector) + "/" + str(i["id"]) + " | ", "SourceType is : " + str(i["sourceType"]) + " | ", "category is : " + str(i["category"]))
        print("curl -u " + (accessid) + ":" + (accesskey) + " -X DELETE " + str(collector) + "/" + str(i["id"]), file=f)

def getsourceinfo_by_id(accessid, accesskey, collector, id):
 '''
this method gets the sources id based on the id provided and search with contains and creates .sh file with list of curl requests for deletion.
After the file got generated. Simply have to click the .sh file that executes one by one and performs the deletion.

 Note: Please cross verify the output file genearted before execution. shell file is very powerful and sensitive. It will direcly executes on double click.
 '''

 # Content type as application/json
 header = {'Content-Type': 'application/json'}
 auth = (accessid,accesskey)
 r = requests.get(collector,headers=header,auth=auth)
 # print("type of response : " + str(type(r.text)))

# parsing the ouput sources to json
 parsed = json.loads(r.text)


 for i in parsed["sources"]:
    if id in i["id"]:
        # print("Source id : " + str(i["id"]) , "Source url is : " + str(Collectorurl) + "/" + str(i["id"]) , "SourceType is : " + str(i["sourceType"]), "category is : " + str(i["category"]))
        print("Source id : " + str(i["id"]) + " | ", "Source url is : " + str(collector) + "/" + str(i["id"]) + " | ", "SourceType is : " + str(i["sourceType"]) + " | ", "category is : " + str(i["category"]))
        print("curl -u " + (accessid) + ":" + (accesskey) + " -X DELETE " + str(collector) + "/" + str(i["id"]), file=f)