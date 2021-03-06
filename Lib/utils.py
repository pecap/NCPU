# imported python modules #

import requests                                 # python HTTP module
from requests.auth import HTTPBasicAuth         # generate BasicAuth credentials
import json                                     # JSON parser
import pandas as pd                             # data analysis module. used to manipulate files
import zipfile                                  # ZIP module

# user credentials
user = ""
pw = ""

#####################################################################################################
###########                                    FUNCTIONS                                  ###########
#####################################################################################################


def url():
    """returns object 'url' which contains all Oracle PBCS URL's"""

    url =
    {
        "jobs":"https://planning-test-domain_name.pbcs.em2.oraclecloud.com/HyperionPlanning/rest/v3/applications/app_name/jobs",
        "files":"https://planning-test-domain_name.pbcs.em2.oraclecloud.com:443/interop/rest/11.1.2.3.600/applicationsnapshots"
    }

    return url
url = url()


def runJob(job_type, job_name):
    """
        runs a pre-defined job in a PBCS instance.
        accepts 2 parameters:
            1) job_type = PBCS job type
            2) job_name = PBCS job name
    """

    # payload & headers
    payload = json.dumps({"jobType":job_type, "jobName":job_name})
    headers = {"Content-Type":"application/json"}

    # send request
    res = requests.post(url=url['jobs'], auth=HTTPBasicAuth(user, pw), data=payload, headers=headers)
    res.raise_for_status()

    # print results
    print('triggered LCM export for Scenario dimension')
    print(res.status_code)

    #return reponse object
    return res


def downloadFile(pbcs_file, local_file):
    """
        download a file from PBCS inbox & unzip it
        accepts 2 parameters:
            1) file_dl = name of PBCS inbox file
            2) file_loc = name of local file
    """

    # send request
    res = requests.get(url=url['files']+'/'+pbcs_file+'/contents', auth=HTTPBasicAuth(user, pw), stream=True)
    res.raise_for_status()

    # print results
    print('file downloaded')
    print(res.status_code)

    with open('./data/'+local_file, 'wb') as handle:
        for chunk in res.iter_content(chunk_size=1024):
            handle.write(chunk)

    # extract 'scenario.zip'
    zf = zipfile.ZipFile('./data/'+local_file)
    zf.extractall('./data/content')
    #return reponse object
    return res


def uploadFile(file_name):
    """
        uploads payload file to PBCS inbox
        accepts 1 param:
        1) file_name = path of the file to be uploaded
    """

    payload = open('./data/content/'+file_name, 'rb').read()

    # headers & params
    headers = {'Content-Type':'application/octet-stream'}
    params = {'isLast':'true','chunkSize':'5522','isFirst':'true'}

    # send request & error handling
    res = requests.post(url=url['files']+'/'+file_name+'/contents', auth=HTTPBasicAuth(user, pw),headers=headers, data=payload, params=params)
    res.raise_for_status()

    # print results
    print('uploaded LCM package to PBCS')
    print(res.status_code)

    #return reponse object
    return res


def deleteFile(file_name):
    """
        delete file from PBCS inbox
        accepts 1 parameter:
            1) file_name = file to be deleted from PBCS inbox
    """

    # send request & error handling
    res = requests.delete(url=url['files']+'/'+file_name,auth=HTTPBasicAuth(user, pw))
    res.raise_for_status()

    # print results
    print('deleted existing "scenario_import.csv" from PBCS inbox')
    print(res.status_code)

    #return reponse object
    return res


def setStartPeriod(file_name, start_period):
    """
        set a new start period for the forecast scenario_import
        accepts 2 parameters:
            1) file_name = name of the file to be manipulated
            2) start_period = new start period
    """

        # replace start period value with nPer
    df = pd.read_csv('./data/content/IYehezkelov_ExportedMetadata_Scenario.csv',encoding='utf-8')
    df.iloc[2, 20] = start_period
    df[2:3].to_csv('./data/content/Scenario_import.csv',encoding='utf-8', index=False)

    print('Forecast start period set to: ' + start_period)
