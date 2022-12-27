import jenkins
import os
import subprocess
import sys
import variables

server = variables.server
user = server.get_whoami()
version = server.get_version()

print('Running Execution as User: %s on Jenkins Version: %s' % (user['fullName'],version))

scriptAction = sys.argv[1]
print('Selected Action: ', scriptAction)

if(scriptAction == "Copy"):
    print('Input Parameters: ', *sys.argv[2:])
    subprocess.call(["python", "copyFn.py", *sys.argv[2:]])
elif(scriptAction == "Delete"):
    print('Input Parameters: ', *sys.argv[2:])
    subprocess.call(["python", "deleteFn.py", *sys.argv[2:]])
