import requests                                 # python HTTP module
from requests.auth import HTTPBasicAuth         # generate BasicAuth credentials
import json                                     # JSON parser
import pandas as pd                             # data analysis module. used to manipulate files
import zipfile                                  # ZIP module
import time                                     # timeout

user = "a490304.IYehezkelov"
pw = "A0547780121b"

def url():
    """returns object 'url' which contains all Oracle PBCS URL's"""

    url = {
            "export":"https://planning-test-a490304.pbcs.em2.oraclecloud.com/HyperionPlanning/rest/v3/applications/DELPHI/jobs",
            "download":"https://planning-test-a490304.pbcs.em2.oraclecloud.com:443/interop/rest/11.1.2.3.600/applicationsnapshots/Scenario_export.zip/contents",
            "upload":"https://planning-test-a490304.pbcs.em2.oraclecloud.com:443/interop/rest/11.1.2.3.600/applicationsnapshots/Scenario_import.csv/contents?q={'isLast':true,'chunkSize':5522,'isFirst':true}",
            "import":"https://planning-test-a490304.pbcs.em2.oraclecloud.com/HyperionPlanning/rest/v3/applications/DELPHI/jobs",
            "delete":"https://planning-test-a490304.pbcs.em2.oraclecloud.com:443/interop/rest/11.1.2.3.600/applicationsnapshots/Scenario_import.csv"
            }
    return url
url = url()

def runJob(job_type, job_name):
    """
    runs a pre-defined job in a PBCS instance.
    accepts 2 parameters:
        job_type = PBCS job type
        job_name = PBCS job name
    """

    # payload & headers
    payload = json.dumps({"jobType":job_type, "jobName":job_name})
    headers = {"Content-Type":"application/json"}

    # send request
    res = requests.post(url=url['export'], auth=HTTPBasicAuth(user, pw), data=payload, headers=headers)
    res.raise_for_status()

    # print results
    print('triggered LCM export for Scenario dimension')
    print('request 1 status: ' + str(res.status_code))

    #return reponse object
    return res

def downloadSnapshot():
    """download a specific application snapshot"""

    # send request
    res = requests.get(url=url['download'], auth=HTTPBasicAuth(user, pw), stream=True)
    res.raise_for_status()

    # print results
    print('LCM file downloaded')
    print('request 2 status: ' + str(res.status_code))

    #return reponse object
    return res

def deleteFromInbox():
    """delete file from PBCS inbox"""

    # send request & error handling
    res = requests.delete(url=url['delete'],auth=HTTPBasicAuth(user, pw))
    res.raise_for_status()

    # print results
    print('deleted existing "scenario_import.csv" from PBCS inbox')
    print('request 3 status: ' + str(res.status_code))

    #return reponse object
    return res

def uploadSnapshot(payload):
    """uploads payload file to PBCX inbox"""

    # headers
    headers = {'Content-Type':'application/octet-stream'}

    # send request & error handling
    res = requests.post(url=url['upload'], auth=HTTPBasicAuth(user, pw),headers=headers, data=payload)
    res.raise_for_status()

    # print results
    print('uploaded LCM package to PBCS')
    print('request 4 status: ' + str(res.status_code))

    #return reponse object
    return res

def setStartPeriod(file, start_period):
    """set a new start period for the forecast scenario_import"""

    res = downloadSnapshot()

        # save response to 'responses' folder as 'content.zip'
    with open(file, 'wb') as handle:
        for chunk in res.iter_content(chunk_size=1024):
            handle.write(chunk)

        # extract 'scenario.zip'
    zf = zipfile.ZipFile(file)
    zf.extractall('./responses/content')

        # replace start period value with nPer
    df = pd.read_csv('./responses/content/IYehezkelov_ExportedMetadata_Scenario.csv',encoding='utf-8')
    df.iloc[2, 20] = start_period
    df[2:3].to_csv('./responses/content/Scenario_import.csv',encoding='utf-8', index=False)

    print('Forecast start period set to: ' + start_period)
