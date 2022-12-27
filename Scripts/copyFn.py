import jenkins
import variables
import sys

server = variables.server

def copyJob(sourceJob,destinationJob):
    print("Job Copy In-Progress")
    server.copy_job(sourceJob,destinationJob)

copyJob(*sys.argv[1:])