def url():
    """returns object 'url' which contains all Oracle PBCS URL's"""

    # url building blocks
    domain = '-'+'a490304'
    env = '-'+'test'
<<<<<<< HEAD
    app_name = 'DELPHI'

=======
>>>>>>> aa8ab5b429e73b40f6f062b575235cc09bb37738
    base = "https://planning"+env+domain+".pbcs.em2.oraclecloud.com"
    pln_ver = requests.get(url = 'https://planning-test-a490304.pbcs.em2.oraclecloud.com/HyperionPlanning/rest/', auth=HTTPBasicAuth(user, pw)) # get planning api version
    lcm_ver = requests.get(url = 'https://planning-test-a490304.pbcs.em2.oraclecloud.com:443/interop/rest/', auth=HTTPBasicAuth(user, pw)) # get lcm api version

    planning = base+'/'+'HyperionPlanning/rest/'+pln_ver
    lcm = base+':'+'443/interop/rest/'+lcm_ver

    url = {
            "jobs":"https://planning-test-a490304.pbcs.em2.oraclecloud.com/HyperionPlanning/rest/v3/applications/DELPHI/jobs",
            "files":"https://planning-test-a490304.pbcs.em2.oraclecloud.com:443/interop/rest/11.1.2.3.600/applicationsnapshots"
    }

    return url