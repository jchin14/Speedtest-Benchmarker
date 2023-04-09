import os

serversList = ["speedtest.ams01.softlayer.com","speedtest.fra02.softlayer.com","ookla1.lon2.uk.m247.com","lg.lon-c.fdcservers.net","lg.par-c.fdcservers.net","silverblades.fr","lg.ny-z.fdcservers.net","speedtest.nyc.rr.com","dallas.tx.speedtest.frontier.com","dallas02.speedtest.windstream.net"]

for i in range(len(serversList)):
    output = os.popen('ping ' + serversList[i] + ' -n 5').read()
    print(serversList[i] + ": " + output[-6:-1])

input("\nDONE!")