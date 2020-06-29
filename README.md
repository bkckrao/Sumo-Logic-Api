# Sumo-Logic-Api  :  Creation and Deletion of multiple sources through Sumo-Logic-Api 
This repository is used to manage the Sumo Logic api. Currently this repo is focused on creation of multiple sources and deletion of multiple sources.

### Prerequisites to Creation or Deletion

- Create list of collectors and the corresponding Ids in an Excel, For example see the [file](https://github.com/bkckrao/Sumo-Logic-Api/blob/master/commands_collectors1.xlsx) 
- Create keys from Sumo Logic, For detailed steps, follow the [link](https://help.sumologic.com/Manage/Security/Access-Keys)

[Creation of sources:](#Creation-of-sources:)  
[Deletion of Sources:](#Deletion-of-Sources:)


## Creation of sources:

### Prerequisites for sources creation

- Create list of collectors and the corresponding Ids in an Excel, For example see the Sheet **WEB_Ids** and column **WebPrefix_Id** in the [file](https://github.com/bkckrao/Sumo-Logic-Api/blob/master/commands_collectors1.xlsx) 
- Create a template of sources with a variable that differentiates each customer
- Create keys from Sumo Logic, For detailed steps, follow the [link](https://help.sumologic.com/Manage/Security/Access-Keys)

### Description:
Sumo Logic recommended way of creating sources is through Curl command as below:

    curl -u '<accessId>:<accessKey>' -X POST -H "Content-Type: application/json" -T host_metrics.json https://api.sumologic.com/api/v1/collectors/10/sources

But Sumo Logic does not have option to push multiple sources at a single go. so we have created a Python script **Sumo_Singles_create.py** for the purpose.

 Here we can create bunch of same sources to the multiple customers. For example 10 sources to be created for a 100 customers. we will create a template of 10 sources and copies the template and replace the required parameters in the template copy that match to the particular customer and then push to the Sumo Logic API. Similarly we can do for any number of customers in few minutes.

 -  User has to enter the AccessId, Accesskey in a separate file as **chenna_confidential**.
 -  variables to pass before execution:
    -  basepath
    -  workbookname
    -  sheetname
    -  columnname

 Also note that, we are taking variables template, outputfolder dynamically based on our requirement. If you have consistenat fodler, I would suggest write the varaibles after the line **accesskey = ckkeys.accesskey**.

 you are ready to execure your script. Post execution, you will observe a text file **output.txt**. Please veriry the requests carefully and update the file extension as .sh instead of .txt and hit enter the file. You will see respective sources creation.




## Deletion of Sources:

### Prerequisites for sources creation

- Create list of collectors and the corresponding Ids in an Excel, For example see the Sheet **WEB_Ids** and column **WEB_Collectors**
 in the [file](https://github.com/bkckrao/Sumo-Logic-Api/blob/master/commands_collectors1.xlsx) 

Sumo Logic recommended way of deleting sources is through Curl command as below:

    curl -u '<accessId>:<accessKey>' -X DELETE https://api.sumologic.com/api/v1/collectors/<CollectorId>/sources/<SourceId>

Incase we have to delete multiple sources at a time, we have to frame multiple requests just like above one. To create multiple sources , we have written a simple python code **Sumo_sources_deletion.py** that generates the requests based on the criteria mentioned by the user.

we have to select a criteria based on the deletion like:
- category
- sourceType
- name
- id

Make sure only that field is not null and filled with correct value based on which sources will be selected for deletion.

You are set to execute the script. Post execution you will see an output.txt file with the list of sources targeted for deletion. make sure all sources are appropriate and update the extension to .sh instead of .txt and hit enter. You can observe the sources getting deleted.


