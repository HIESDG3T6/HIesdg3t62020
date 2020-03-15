import PriaidDiagnosisClient
import random
import config
import sys
import json

class PriaidDiagnosisClientDemo:
    'Demo class to simulate how to use PriaidDiagnosisClient'

    def __init__(self):
        username = config.username
        password = config.password
        authUrl = config.priaid_authservice_url
        healthUrl = config.priaid_healthservice_url
        language = config.language
        self._printRawOutput = config.pritnRawOutput

        self._diagnosisClient = PriaidDiagnosisClient.DiagnosisClient(username, password, authUrl, language, healthUrl)
    def _writeRawOutput(self, methodName, data):
        print("")
        if self._printRawOutput: 
            print("+++++++++++++++++++++++++++++++++++++++++++++")
            print("Response from method {0}: ".format(methodName))
            print(json.dumps(data))
            print("+++++++++++++++++++++++++++++++++++++++++++++")

    
    def _loadBodyLocations(self):
        bodyLocations = self._diagnosisClient.loadBodyLocations()
        self._writeRawOutput("loadBodyLocations", bodyLocations)
        
        if not bodyLocations:
            raise Exception("Empty body locations results")
        
        # self._writeHeaderMessage("Body locations:")    
        for bodyLocation in bodyLocations:
            print("{0} ({1})".format(bodyLocation["Name"], bodyLocation["ID"]))

        randomLocation = random.choice(bodyLocations)
        # self._writeHeaderMessage("Sublocations for randomly selected location {0}".format(randomLocation["Name"]))
        return randomLocation["ID"]

diagnosisClientDemo = PriaidDiagnosisClientDemo()
diagnosisClientDemo._loadBodyLocations()