# Version 1.1.5

import os
import csv
import time
import datetime

wait = 1
resultsCSV = r"./results_all_servers.csv"
startTime = time.time()
csvRows = []
preselectedServers = [12491,2169,12492,6355,12493,2165,12495,234,12494,6153,28463,34083,21569,28910,40508,50344,19081,47668,30907,30593,26996,35058,24281,34948,40509,37211,14928,31122,14236,16974,14228,17384,14238,17386,14237,37499,16976,28032,21568,34143,34555,1536,29545,4036,2690,2599,11871,49594,49421,8864]


def average_latency():
    totalLatency = 0
    colLatency = [x[3]for x in csvRows]
    for value in colLatency:
        totalLatency += float(value)
    aveLatency = round(totalLatency / len(colLatency),2)
    return aveLatency

def average_jitter():
    totalJitter = 0
    colJitter = [x[4]for x in csvRows]
    for value in colJitter:
        totalJitter += float(value)
    aveJitter = round(totalJitter / len(colJitter),2)
    return aveJitter

def average_dl_speed():
    totalDL = 0
    colDL = [x[5]for x in csvRows]
    for value in colDL:
        totalDL += float(value)
    aveDL = round(totalDL / len(colDL),2)
    return aveDL

def average_ul_speed():
    totalUL = 0
    colUL = [x[7]for x in csvRows]
    for value in colUL:
        totalUL += float(value)
    aveUL = round(totalUL / len(colUL),2)
    return aveUL

def average_pl():
    totalPL = 0
    colPL = [x[9]for x in csvRows]
    for value in colPL:
        totalPL += float(value)
    avePL = round(totalPL / len(colPL),2)
    return avePL

def total_tests():
    totalTests = 0
    colServers = [x[0]for x in csvRows]
    totalTests = len(colServers)
    return totalTests

def total_data():
    totalData = 0
    colDownData = [x[6]for x in csvRows]
    colUpData = [x[8]for x in csvRows]
    for value in colDownData:
        totalData += float(value)
    for value in colUpData:
        totalData += float(value)
    totalData = round(totalData,2)
    return totalData

def average_duration():
    totalDuration = 0
    colDuration = [x[12]for x in csvRows]
    for value in colDuration:
        totalDuration += float(value)
    aveDuration = round(totalDuration / len(colDuration),2)
    return aveDuration


try:
    print("BJROXN")
    while True:
        downloadSpeed = input("\nEnter the download speed of your internet plan tier without over-provisioning. E.g. '250' for a NBN Superfast 250/25 plan: ")
        try:
            downloadSpeed = int(downloadSpeed)
            if downloadSpeed > 0:
                break
            else:
                print("Positive integers greater than 0 only")
        except:
            print("Please enter only whole numbers in Mbps.")

    while True:
        uploadSpeed = input("\nEnter the upload speed of your internet plan tier without over-provisioning. E.g. '25' for a NBN Superfast 250/25 plan: ")
        try:
            uploadSpeed = int(uploadSpeed)
            if uploadSpeed > 0:
                break
            else:
                print("Positive integers greater than 0 only")
        except:
            print("Please enter only whole numbers in Mbps.")

    while True:
        downloadTES = input("\nEnter the download Typical Evening Speed as specified by your provider for your speed tier. E.g. '240' for a NBN Superfast 250/25 plan: ")
        try:
            downloadTES = int(downloadTES)
            if downloadTES > 0:
                break
            else:
                print("Positive integers greater than 0 only")
        except:
            print("Please enter only whole numbers in Mbps.")

    while True:
        uploadTES = input("\nEnter the upload Typical Evening Speed as specified by your provider for your speed tier. If unspecified, press enter. E.g. '22' for a NBN Superfast 250/25 plan: ")
        try:
            if uploadTES == "":
                uploadTES = uploadSpeed * 0.9
                break
            else:
                uploadTES = int(uploadTES)
                if uploadTES > 0:
                    break
                else:
                    print("Positive integers greater than 0 only")
        except:
            print("Please enter only whole numbers in Mbps.")

    while True:
        serverIDCount = len(preselectedServers)
        numServers = input("\nHow many servers to test? Or press enter for all: ")
        try:
            if numServers == "":
                allServers = True
                break
            numServers = int(numServers)
            if numServers == 69 or numServers == 420:
                os.popen('explorer "https://www.youtube.com/watch?v=dQw4w9WgXcQ"')
            if numServers > 0 and numServers <= serverIDCount:
                numServers = round(numServers/2)*2
                if numServers == 0:
                    numServers = 2
                serverIDList = preselectedServers[0:numServers]
                allServers = False
                break
            print(f"Positive integers between 0 and {serverIDCount} only.")
        except:
            print(f"Please enter only whole numbers.")
    #print("\nBJROXN")
except KeyboardInterrupt:
    exit()

if allServers:
    try:
        with open(resultsCSV) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                csvRows.append(row)
        colID = [x[1]for x in csvRows]
        serverID = int(colID[-1]) + 1
        csvfile.close()
    except:
        serverID = 233
else:
    try:
        with open(resultsCSV) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                csvRows.append(row)
        colID = [x[1]for x in csvRows]
        lastServer = int(colID[-1])
        csvfile.close()

        indexFound = False
        for i in range(len(serverIDList)):
            if lastServer == serverIDList[i]:
                serverIndex = i + 1
                indexFound = True
        
        if not indexFound:
            serverIndex = 0
    except:
        serverIndex = 0

while True:
    try:
        if allServers:
            pass
        else:
            try:
                serverID = serverIDList[serverIndex]
            except:
                raise KeyboardInterrupt
        
        print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Server ID: {serverID}")
        print("Test running please wait...")
        
        initialTime = time.time()
        output = os.popen('speedtest -s ' + str(serverID)).read()
        print(output)

        testDuration = str(round(time.time() - initialTime,2))
        testTime = str(datetime.datetime.now())
        print("Test Taken at: " + testTime)
        testDurationStr = "Test Duration: " + testDuration

        try:
            result = output.splitlines()

            serverList = list(result[3])
            serverName = True
            for i in range(len(serverList)):
                if serverName:
                    if serverList[i] == ",":
                        serverList[i] = ";"
                    if i < 13:
                        serverList[i] = ""
                    if serverList[i] == "=":
                        serverName = False
                        serverList[i-1] = ""
                        serverList[i-2] = ""
                        serverList[i-3] = ""
                        serverList[i-4] = ""
                        serverList[i-5] = ""
                        serverList[i] = ""
                else:
                    serverList[i] = ""
            result[3] = "".join(serverList)

            ISPList = list(result[4])
            for i in range(len(ISPList)):
                if ISPList[i] == ",":
                    ISPList[i] = ";"
                if i < 13:
                    ISPList[i] = ""
            result[4] = "".join(ISPList)

            urlList = list(result[11])
            for i in range(len(urlList)):
                if urlList[i] == ",":
                    urlList[i] = ";"
                if i < 13:
                    urlList[i] = ""
            result[11] = "".join(urlList)

            latencyList = list(result[5])
            jitterBool = False
            jitterList = []
            for i in range(len(latencyList)):
                if jitterBool:
                    if latencyList[i] == "." or latencyList[i].isnumeric():
                        jitterList.append(latencyList[i])
                    latencyList[i] = ""
                elif latencyList[i] == "." or latencyList[i].isnumeric():
                    pass
                elif latencyList[i] == "(":
                    jitterBool = True
                    latencyList[i] = ""
                else:
                    latencyList[i] = ""
            result[5] = "".join(latencyList)
            jitter = "".join(jitterList)

            downloadList = list(result[7])
            downDataBool = False
            downDataList = []
            downDP = 999
            downDataDP = 999
            downUnit = "M"
            downDataUnit = "M"
            for i in range(len(downloadList)):
                if i == (downDP + 4):
                    if downloadList[i] == "k":
                        downUnit = "k"
                    elif downloadList[i] == "G":
                        downUnit = "G"
                if i == (downDataDP + 3):
                    if downloadList[i] == "k":
                        downDataUnit = "k"
                    elif downloadList[i] == "G":
                        downDataUnit = "G"

                if downDataBool:
                    if downloadList[i] == "." or downloadList[i].isnumeric():
                        downDataList.append(downloadList[i])
                        if downloadList[i] == ".":
                            downDataDP = i
                    downloadList[i] = ""
                elif downloadList[i] == "." or downloadList[i].isnumeric():
                    if downloadList[i] == ".":
                        downDP = i
                elif downloadList[i] == "(":
                    downDataBool = True
                    downloadList[i] = ""
                else:
                    downloadList[i] = ""
            result[7] = "".join(downloadList)
            downData = "".join(downDataList)
            if downUnit == "k":
                result[7] = str(float(result[7])/1000)
            elif downUnit == "G":
                result[7] = str(float(result[7])*1000)
            if downDataUnit == "k":
                downData = str(float(downData)/1024)
            elif downDataUnit == "G":
                downData = str(float(downData)*1024)

            uploadList = list(result[9])
            upDataBool = False
            upDataList = []
            upDP = 999
            upDataDP = 999
            upUnit = "M"
            upDataUnit = "M"
            for i in range(len(uploadList)):
                if i == (upDP + 4):
                    if uploadList[i] == "k":
                        upUnit = "k"
                    elif uploadList[i] == "G":
                        upUnit = "G"
                if i == (upDataDP + 3):
                    if uploadList[i] == "k":
                        upDataUnit = "k"
                    elif uploadList[i] == "G":
                        upDataUnit = "G"

                if upDataBool:
                    if uploadList[i] == "." or uploadList[i].isnumeric():
                        upDataList.append(uploadList[i])
                        if uploadList[i] == ".":
                            upDataDP = i
                    uploadList[i] = ""
                elif uploadList[i] == "." or uploadList[i].isnumeric():
                    if uploadList[i] == ".":
                        upDP = i
                elif uploadList[i] == "(":
                    upDataBool = True
                    uploadList[i] = ""
                else:
                    uploadList[i] = ""
            result[9] = "".join(uploadList)
            upData = "".join(upDataList)
            if upUnit == "k":
                result[9] = str(float(result[9])/1000)
            elif upUnit == "G":
                result[9] = str(float(result[9])*1000)
            if upDataUnit == "k":
                upData = str(float(upData)/1024)
            elif upDataUnit == "G":
                upData = str(float(upData)*1024)

            pLossList = list(result[10])
            for i in range(len(pLossList)):
                if pLossList[i] == "." or pLossList[i].isnumeric():
                    pass
                else:
                    pLossList[i] = ""
            result[10] = "".join(pLossList)

            if result[10] == ".":
                result[10] = "0.0"

            timeList = list(testTime)
            for i in range(len(timeList)):
                if timeList[i] == " ":
                    timeList[i] = ","
                if i > 21:
                    timeList[i] = ""
            testTime = "".join(timeList)

            with open(resultsCSV, 'a') as csvfile:
                resultList = [result[3],str(serverID),result[4],result[5],jitter,result[7],downData,result[9],upData,result[10],testTime,testDuration,result[11]]
                for item in resultList:
                    csvfile.write(item)
                    if item != result[11]:
                        csvfile.write(",")
                csvfile.write("\n")

        except:
            pass
        
        #time.sleep(wait/2)
        if allServers:
            serverID += 1
        else:
            serverIndex += 1

    except KeyboardInterrupt:
        timeElapsed = round(time.time() - startTime,2)
        print(f"\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\nTime Elapsed Since Start: {timeElapsed} seconds")
        print(str(datetime.timedelta(seconds=timeElapsed)))

        try:
            csvRows = []
            with open(resultsCSV) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    csvRows.append(row)

            aveDL = average_dl_speed()
            aveUL = average_ul_speed()

            print(f"\nAverage Latency: {average_latency()} ms")
            print(f"Average Jitter: {average_jitter()} ms")
            print(f"Average Download Speed: {aveDL} Mbps")
            print(f"Average Upload Speed: {aveUL} Mbps")
            print(f"Average Packet Loss: {average_pl()}%")

            print(f"\nNumber of Tests: {total_tests()}")
            print(f"Total Data Used: {total_data()} MB")
            print(f"Average Test Duration: {average_duration()} seconds")

            print(f"\nPercentage of Plan Download Speed: {round((aveDL/downloadSpeed)*100,2)}%")
            print(f"Percentage of Plan Upload Speed: {round((aveUL/uploadSpeed)*100,2)}%")

            print(f"\nPercentage of TES Download Speed: {round((aveDL/downloadTES)*100,2)}%")
            print(f"Percentage of TES Upload Speed: {round((aveUL/uploadTES)*100,2)}%")
        except:
            pass

        try:
            csvfile.close()
        except:
            pass

        try:
            userInput = input("\n\nPaused. Press enter to resume or type exit. ")
            if userInput != "":
                print("")
                exit()
        except:
            exit()

    except:
        print(f"\nERROR with server {serverID}")
        time.sleep(wait)
        if allServers:
            serverID += 1
        else:
            serverIndex += 1