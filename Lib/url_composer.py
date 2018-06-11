import requests                                 # python HTTP module
from requests.auth import HTTPBasicAuth         # generate BasicAuth credentials
import json                                     # JSON parser

def url():
    """returns object 'url' which contains all Oracle PBCS URL's"""

    # url building blocks
    domain = '-'+'domain_name'
    env = '-'+'env_type'
    app_name = 'app_name'
    base = "https://planning"+env+domain+".pbcs.em2.oraclecloud.com"

    # credentials to get versions
    user = domain+"."+"user_name"
    pw = "pw"

    # get API versions
    res = requests.get(url = base+'/'+'HyperionPlanning/rest/', auth=HTTPBasicAuth(user, pw)) # get planning api version

    res_content = json.loads(getPlnVersion.text)
    items = res_content['items']

    for i in items:
        if i['isLatest'] == True:
            pln_ver = i['version']

    res = requests.get(url = base+':'+'443/interop/rest/', auth=HTTPBasicAuth(user, pw)) # get lcm api version

    res_content = json.loads(getLcmVersion.text)
    lcm_ver = res_content['items'][0]['version']

    # planning URL
    planning_url = base+'/'+'HyperionPlanning/rest/'+pln_ver
    # migration URL
    lcm_url = base+':'+'443/interop/rest/'+lcm_ver

    url =
    {
        'jobs':planning_url,
        'files':lcm_url
    }

    return url
