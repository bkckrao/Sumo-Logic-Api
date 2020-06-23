import pandas as pd
import shutil, os, fnmatch

import requests
import json
import dictor
import shutil, os, fnmatch
import sys

f = open("Output.txt",'w')

''' This is WIP '''
def verifyFields(fieldslist):
    counter = 0
    for fields in fieldslist:
        field = fields.split('#')
    if (field[1] != 'NULL') :
        counter += 1
        print(" We wille be checking with field " + field[0] + "and value as " + field[1])

    if counter != 1 :
        print("Either you have declared multiple variables as or no varaibles declared")
        sys.exit("Exception : Either you have declared multiple variables as or no varaibles declared")


'''   Function to find and replace text '''
def findReplace(directory, find, replace, filePattern):
    
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

''' Function to replace text '''
def renamefolder(source, destination):
    os.rename(source, destination)

''' Function to create copy '''
def copyfolder(source, destination):
    shutil.copytree(source, destination)





    ''' Deletion Library functions'''

    # f = open("Output_to_Delete_Sources.txt",'w')

def getcollectorsfromExcel(path, sheet, columnname):
    '''
    This method is used to get the data from Excel by passing the path of excel workbook, sheet name and the column name.
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
    
    if name in i["name"]:
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
