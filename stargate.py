# DNA Center script from Module 3

#--------------------------------
# importing everything
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pprint
import getpass
import requests
from requests.auth import HTTPBasicAuth
#--------------------------------

#--------------------------------
# defining global vars we don't want to change
# still rocking the Stargate theme

# username prompt (devnetuser)
CHEVERON_ONE = input("Please enter your username: ")
# password prompt (Cisco123!)
ENCODED = getpass.getpass()
LOCKED = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"
#-------------------------------

#-------------------------------
# token collection

kree = {'Content-Type': 'application/json'}

openTheIris = requests.post(LOCKED, auth=HTTPBasicAuth(CHEVERON_ONE, ENCODED), headers=kree, verify=False)

tokra = openTheIris.json()['Token']

print("Your generated token is:\n" + tokra)
print()
#-------------------------------

#-------------------------------
# getting a count of the devices
HARCESIS = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/count"

omaDesala = {'Accept': 'application/json', 'X-auth-token': tokra}

thisIsStargateCommand = requests.get(HARCESIS, headers=omaDesala, verify=False)

gateAddress = thisIsStargateCommand.json()['response']

print("Retreiving data from {} devices:".format(gateAddress))
print()
#------------------------------

#------------------------------
# getting the location, type, and role of the machines

REPOSITORY_OF_KNOWLEDGE = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

replicators = {'Accept': 'application/json', 'X-auth-token': tokra}

indeed = requests.get(REPOSITORY_OF_KNOWLEDGE, headers=replicators, verify=False)

offworldActivity = indeed.json()['response']

for situation in offworldActivity:
    p5x777 = situation['locationName']
    furlingHomeworld = situation['location']
    furlings = situation['type']
    allianceMember = situation['role']
    print("The device at {} {} is a {} that performs {}".format(p5x777, furlingHomeworld, furlings, allianceMember))
#------------------------------
# end of script!
