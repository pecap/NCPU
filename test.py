user = "a490304.IYehezkelov"
pw = "A0547780121b"

pln_ver = requests.get(url = 'https://planning-test-a490304.pbcs.em2.oraclecloud.com/HyperionPlanning/rest/', auth=HTTPBasicAuth(user, pw)) # get planning api version
lcm_ver = requests.get(url = 'https://planning-test-a490304.pbcs.em2.oraclecloud.com:443/interop/rest/', auth=HTTPBasicAuth(user, pw)) # get lcm api version
