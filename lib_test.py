from Lib.funcs import *

    ### HTTP request 1 (GET) - trigger LCM export ###
job_type = "Export Metadata"
job_name = "Scenario_Export"
runJob(job_type, job_name)

    ### HTTP request 2 (GET) - Download snapshot & handle response ###
file = './responses/Scenario.zip'
startPeriod = 'Aug'

# set a new start period
setStartPeriod(file, startPeriod)


    ### HTTP request 3 (GET) - deleted file from PBCS inbox ###
deleteFromInbox()

    ### HTTP request 4 (POST) - upload modified snapshot to PBCS ###
payload = open('./responses/content/Scenario_import.csv', 'rb').read()
uploadSnapshot(payload)

    ### HTTP request 5 (POST) - trigger MD import ###
job_type = "Import Metadata"
job_name = "Scenario_import"
runJob(job_type, job_name)
