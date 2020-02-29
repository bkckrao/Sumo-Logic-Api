import Sumo_sources_deletion as obj 

category = "category"
# Ex: category = "configuration"

sourceType = "sourceType" #"LocalWindowsEventLog"
# Ex: sourceType = "sourceType"

id = "id"
#  Ex: id = "1234567"

name = "name"
# Ex : name = "api"



datapath = ""
sheetname = "APP and Web Collectors"
columnheading = "app_Web_GA_Collectors"
accessid = "ACCESSID"
accesskey = "ACCESSKEY"
# outputfile = "outputfile_to_delete.txt"


collectorlist = obj.getcollectorsfromExcel(datapath,sheetname,columnheading)

print("Count of collectors : ")
print(len(collectorlist))

# for j in range(len(collectorlist)):
#  obj.getsourceinfo(accessid, accesskey, obj.getcollectorsfromExcel(datapath,sheetname,columnheading)[j], searchstring)
    # obj.getsourceinfo(accessid, accesskey, collectorlist[j], searchstring, outputfile)

if(name != "name"):
    for collector in range(len(collectorlist)):
        obj.getsourceinfo_by_name(accessid, accesskey, obj.getcollectorsfromExcel(datapath,sheetname,columnheading)[collector], name)
elif(category != "category"):
    for collector in range(len(collectorlist)):
        obj.getsourceinfo_by_category(accessid, accesskey, obj.getcollectorsfromExcel(datapath,sheetname,columnheading)[collector], category)
elif(sourceType != "sourceType"):
    for collector in range(len(collectorlist)):
         obj.getsourceinfo_by_sourceType(accessid, accesskey, obj.getcollectorsfromExcel(datapath,sheetname,columnheading)[collector], sourceType)
elif(id != "id"):
    for collector in range(len(collectorlist)):
        obj.getsourceinfo_by_id(accessid, accesskey, obj.getcollectorsfromExcel(datapath,sheetname,columnheading)[collector], id)

