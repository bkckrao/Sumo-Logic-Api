import pandas as pd, shutil, os, fnmatch
import Sumo_Library as library
import chenna_confidential as ckkeys

basepath = "C:\\CloudOps\\sumo\\NON_GA"
workbookname = "\\commands_collectors1.xlsx"
sheetname = "QAIds"
columnname = "QAPrefixandserver" 

df = pd.read_excel(basepath + workbookname, sheet_name=sheetname) # can also index sheet by name or fetch all sheets
NonGA_PrefixList = df[columnname].tolist()

print("total count of Prefixes : " + str(len(NonGA_PrefixList)))

# NonGA_PrefixList.clear()
# NonGA_PrefixList.append("INFORBCBUS1#want2bthere#170652797")

custprefix = "custprefix"   # string to replace with the customer prefix
servername = "servername"    # string to replace with the customer server 

template = "Sun_QA_Template"
outputfolder = "Sun_Paths_QA"
outputfile = "QA_output.txt"

accessid = ckkeys.accessid
accesskey = ckkeys.accesskey
f = open(basepath + "\\" + outputfile,'w')

for i in NonGA_PrefixList:
    # INFORBCBUS1#want2bthere#170652797

    NonGAValues = i.split('#')
    replace = NonGAValues[0]
    server = NonGAValues[1]
    id = NonGAValues[2]
    
    library.copyfolder(basepath + '\\' + template, basepath + '\\' + outputfolder + '\\temp') # created folder as temp and copies the folders from template
    library.renamefolder(basepath + '\\' + outputfolder + '\\temp', basepath + '\\' + outputfolder + '\\' +replace)  # renames the folder to value provided in replace variable
    library.findReplace(basepath + '\\' + outputfolder + '\\' +replace, custprefix, replace,'*.json')  # function call to perform replace in all the files
    library.findReplace(basepath + '\\' + outputfolder + '\\' +replace, servername, server, '*.json')
    
    print("curl -u \"" + (accessid) + ":" + (accesskey) + "\" -X POST -H \"Content-Type: application/json\" -T \"" + basepath + '\\' + outputfolder + '\\' +replace + "\\QA1.json\" https://api.sumologic.com/api/v1/collectors/" + id + "/sources", file=f)
    print("curl -u \"" + (accessid) + ":" + (accesskey) + "\" -X POST -H \"Content-Type: application/json\" -T \"" + basepath + '\\' + outputfolder + '\\' +replace + "\\QA1.json\" https://api.sumologic.com/api/v1/collectors/" + id + "/sources")
