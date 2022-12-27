import jenkins
import os

host = "" #Enter the Jenkins Host here
username = "" #Enter the username
password = "" #Enter your password/token here
server = jenkins.Jenkins(host,username=username, password=password)