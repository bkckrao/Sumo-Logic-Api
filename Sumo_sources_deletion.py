'''import Sumo_sources_deletion_Library as obj '''
import Sumo_Library as obj
import chenna_confidential as ckkeys
import sys  


''' category field is the category of a source like "configuration", "application/sunsystems/QueryAnalysis"'''
# category = "application/sunsystems/QueryAnalysis"
# Ex: category = "configuration"
# category = "NULL" 
category = "application.AGENT"

''' sourceType field is the source type of a source like "Local File", "Local Windows Event Log" '''
# sourceType = "Local File"
sourceType = "NULL" 

''' Id field is the source id like 1234567'''
# id = "NULL"
#  Ex: id = "1234567"
id = "NULL1"

''' Name field is the source name '''
# Ex : name = "api"
name = "NULL"

# Initiating the counter to check only a single field is assigned to process
counter = 0

if (category != "NULL"):
    counter += 1
if  (sourceType != "NULL"):
    counter += 1
if  (id != "NULL"):
    counter += 1
if  (name != "NULL"):
    counter += 1

if (counter != 1):
    print("Counter Value :" + str(counter))
    print("Either you have declared multiple variables as or no varaibles declared. \n  Please check the below values : \n 1. category = " + category + "\n 2. sourceType = " + sourceType + " \n 3. id = "+ id + "\n 4. name = " + name + "EOF.")
    sys.exit("Exception : Either you have declared multiple variables as or no varaibles declared")
    

 
    
datapath = "C:\\CloudOps\\sumo\\NON_GA\\commands_collectors1.xlsx"

# sheetname = "APP and Web Collectors"
# columnheading = "app_Web_GA_Collectors"

# QA Info
# sheetname = "APP and Web Collectors"
# columnheading = "app_Web_GA_Collectors"
# columnheading = "testing"

sheetname = "QAIds"
columnheading = "QA_collectors"

accessid = ckkeys.accessid
accesskey = ckkeys.accesskey


''' Below line of code gets the list of collectors from the Excel sheet and the column provided '''
collectorlist = obj.getcollectorsfromExcel(datapath,sheetname,columnheading)
# count=len(collectorlist)

print("Count of collectors :  %d" %(len(collectorlist)))

# for j in range(len(collectorlist)):
#  obj.getsourceinfo(accessid, accesskey, obj.getcollectorsfromExcel(datapath,sheetname,columnheading)[j], searchstring)
    # obj.getsourceinfo(accessid, accesskey, collectorlist[j], searchstring, outputfile)

if(name != "NULL"):
    for collector in range(len(collectorlist)):
        obj.getsourceinfo_by_name(accessid, accesskey, obj.getcollectorsfromExcel(datapath,sheetname,columnheading)[collector], name)
elif(category != "NULL"):
    for collector in range(len(collectorlist)):
        obj.getsourceinfo_by_category(accessid, accesskey, obj.getcollectorsfromExcel(datapath,sheetname,columnheading)[collector], category)
elif(sourceType != "NULL"):
    for collector in range(len(collectorlist)):
         obj.getsourceinfo_by_sourceType(accessid, accesskey, obj.getcollectorsfromExcel(datapath,sheetname,columnheading)[collector], sourceType)
elif(id != "NULL"):
    for collector in range(len(collectorlist)):
        obj.getsourceinfo_by_id(accessid, accesskey, obj.getcollectorsfromExcel(datapath,sheetname,columnheading)[collector], id)

