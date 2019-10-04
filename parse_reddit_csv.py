from __future__ import division
import matplotlib.pyplot as plt
from datetime import datetime
import time
import math
import numpy as np


##################################################
# NEW USERS AND POSTS

def get_day(nodeTime):
    ''' Get day since Jan 1 2015. '''
    return int((nodeTime - datetime(2015,1,1)).total_seconds() / 86400)


activeCommunity = ['t5_38wba', 't5_2qnp7', 't5_1rqwi', 't5_2qh1a', 't5_2qh16', 't5_2rlgy', 't5_2sgp1', 't5_2s3qj', 't5_2r8c5', 't5_2qlqh']
activeCommunityCount = [57497, 3464, 2910, 1854, 800, 706, 647, 643, 592, 567]

nodeUser = {}
node = {}


openfile = open("/home/frank/Dropbox/coding/darpa/reddit/Reddit.csv", "r")
lines = openfile.readlines()[1:]

for line in lines:
    nodeID, nodeUserID, parentID, rootID, actionType, platform, communityID, has_URL, domain_linked, links_to_external, nodeTime1, informationID = line.strip().split("\t")
    nodeTime = datetime.strptime(nodeTime1, '%Y-%m-%dT%H:%M:%SZ')

    if nodeUserID == "vHwXTX4FohkDUqQMdjb3zg":
        ''' User with 50k+ activities. '''
        continue
    
    if not nodeUserID in nodeUser: # This is a new user
        nodeUser[nodeUserID] = nodeTime
    else:
        nodeUser[nodeUserID] = min(nodeUser[nodeUserID], nodeTime)

    if not nodeID in node:         # This is a new post
        node[nodeID] = nodeTime
    else:
        node[nodeID] = min(node[nodeID], nodeTime)


newUserRate = [0] * 1200        # number of new users per day
for nodeUserID in nodeUser.keys():
    newUserRate[get_day(nodeUser[nodeUserID])] += 1
    
activityRate = [0] * 1200       # number of activities per day
for nodeID in node.keys():
    activityRate[get_day(node[nodeID])] += 1


fig = plt.figure()
plt.plot(range(1200), newUserRate, "-r", label="new user rate")
plt.plot(range(1200), activityRate, "-g", label="activity rate")
plt.legend()

fig = plt.figure()
plt.plot(newUserRate, activityRate, "x")
plt.xlabel("new user rate")
plt.ylabel("activity rate")

plt.show()
