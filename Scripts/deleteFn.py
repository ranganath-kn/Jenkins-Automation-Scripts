import jenkins
import variables
import sys

server = variables.server

def deleteJob(deleteJobName):
    server.delete_job(deleteJobName)

deleteJob(*sys.argv[1:])