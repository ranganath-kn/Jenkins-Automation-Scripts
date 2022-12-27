import jenkins
import variables
import sys
import json

server = variables.server

def listJobs():
    print("Listing the Jobs from Jenkins Dashboard\n")
    jobData = server.get_jobs()
    jsonFormat = json.dumps(jobData)
    pretty_json = json.loads(jsonFormat)
    print (json.dumps(pretty_json, indent=2))

listJobs()