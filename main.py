from lib.utils import *

###
### step 1 - trigger LCM export job
###

# parameters
jobType = "Export Metadata"
jobName = "Scenario_Export"

runJob(jobType, jobName)

###
### step 2 - Download snapshot, save & unzip it
###

# parameters
pbcsFile = 'Scenario_export.zip'
savedFile = 'Scenario.zip'

downloadFile(pbcsFile, savedFile)

# set a new forecast start period
setStartPeriod(savedFile, 'May')

###
### step 3 - delete file from PBCS
###

# parameters
file = 'scenario_import.csv'

deleteFile(file)

###
### step 4 - upload new file to PBCS
###

# parameters
file = 'Scenario_import.csv'

uploadFile(file)

###
### step 5 - trigger LCM import job
###

# parameters
jobType = "Import Metadata"
jobName = "Scenario_import"

runJob(jobType, jobName)
