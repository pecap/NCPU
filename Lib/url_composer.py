def url():
    """returns object 'url' which contains all Oracle PBCS URL's"""

    domain = '-'+'a490304'
    env = '-'+'test'

    base = "https://planning"+env+".pbcs.em2.oraclecloud.com"

    pln_ver = requests.get(url = 'https://planning-test-a490304.pbcs.em2.oraclecloud.com/HyperionPlanning/rest/', auth=HTTPBasicAuth(user, pw)) # get planning api version
    lcm_ver = requests.get(url = 'https://planning-test-a490304.pbcs.em2.oraclecloud.com:443/interop/rest/', auth=HTTPBasicAuth(user, pw)) # get lcm api version

    planning = base+'/'+'HyperionPlanning/rest/'+pln_ver
    lcm = base+':'+'443/interop/rest/'+lcm_ver

    url = {
            "jobs":"https://planning-test-a490304.pbcs.em2.oraclecloud.com/HyperionPlanning/rest/v3/applications/DELPHI/jobs",
            "files":"https://planning-test-a490304.pbcs.em2.oraclecloud.com:443/interop/rest/11.1.2.3.600/applicationsnapshots"
    }

    return url
