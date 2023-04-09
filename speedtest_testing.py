#!/usr/bin/env python3
version = "1.3.1"

import os
import csv
import time
import datetime
import subprocess


wait = 1
resultsCSV = r"./benchmark_results.csv"
startTime = time.time()
csvRows = []
OCList = [12491]
NAList = [12491]
SAList = [12491]
EUList = [12491]
ASList = [6969]
AFList = [12491]
preselectedServers = [12491,2169,12492,6355,12493,2165,12495,234,12494,6153,28463,34083,21569,28910,40508,50344,19081,47668,30907,30593,26996,35058,24281,34948,40509,37211,14928,31122,14236,16974,14228,17384,14238,17386,14237,37499,16976,28032,21568,34143,34555,1536,29545,4036,2690,2599,11871,49594,49421,8864]


def find_average(column):
    totalValue = 0
    colList = [x[column]for x in csvRows]
    for value in colList:
        totalValue += float(value)
    averageValue = round(totalValue / len(colList),2)
    return averageValue

def total_tests():
    totalTests = 0
    colServers = [x[0]for x in csvRows]
    totalTests = len(colServers)
    return totalTests

def total_data():
    totalData = 0
    colDownData = [x[7]for x in csvRows]
    colUpData = [x[9]for x in csvRows]
    for value in colDownData:
        totalData += float(value)
    for value in colUpData:
        totalData += float(value)
    totalData = round(totalData,2)
    return totalData

if 1 == 0:
    try:
        os.popen('explorer "https://www.aussiebroadband.com.au/lp/rise-of-gru/?kid=2CCG2Z"')
        os.popen('explorer "https://members.superloop.com/signup/referral?referral_code=BJROXN&plan=1531"')
    except:
        pass

try:
    print(f"Version: {version}")
    print("BJROXN :)")
    while True:
        downloadSpeed = input("\nEnter the download speed of your internet plan tier. E.g. '250' for a NBN Superfast 250/25 plan: ")
        try:
            downloadSpeed = int(downloadSpeed)
            if downloadSpeed > 0:
                break
            else:
                print("Positive integers greater than 0 only")
        except:
            print("Please enter only whole numbers in Mbps.")

    while True:
        uploadSpeed = input("\nEnter the upload speed of your internet plan tier. E.g. '25' for a NBN Superfast 250/25 plan: ")
        try:
            uploadSpeed = int(uploadSpeed)
            if uploadSpeed > 0:
                break
            else:
                print("Positive integers greater than 0 only")
        except:
            print("Please enter only whole numbers in Mbps.")

    while True:
        downloadTES = input("\nEnter the download Typical Evening Speed as specified by your provider. E.g. '240' for a NBN 250/25 plan: ")
        try:
            downloadTES = int(downloadTES)
            if downloadTES > 0:
                break
            else:
                print("Positive integers greater than 0 only")
        except:
            print("Please enter only whole numbers in Mbps.")

    while True:
        uploadTES = input("\nEnter the upload Typical Evening Speed. If unspecified, press enter. E.g. '22' for a NBN 250/25 plan: ")
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
        serverIDList = []
        regionsOrNum = input("\n\nSelect servers by region? Or press enter to select by number/all servers: ")
        
        if regionsOrNum == "":
            pass

        elif regionsOrNum[0] == "y" or regionsOrNum[0] == "Y":            
            inputOC = input("Oceania: ")
            if inputOC[0] == "y" or inputOC[0] == "Y":
                serverIDList.extend(OCList)         
            inputNA = input("North America: ")
            if inputNA[0] == "y" or inputNA[0] == "Y":
                serverIDList.extend(NAList)     
            inputSA = input("South America: ")
            if inputSA[0] == "y" or inputSA[0] == "Y":
                serverIDList.extend(SAList)           
            inputEU = input("Europe: ")
            if inputEU[0] == "y" or inputEU[0] == "Y":
                serverIDList.extend(EUList)          
            inputAS = input("Asia: ")
            if inputAS[0] == "y" or inputAS[0] == "Y":
                serverIDList.extend(ASList)          
            inputAF = input("Africa: ")
            if inputAF[0] == "y" or inputAF[0] == "Y":
                serverIDList.extend(AFList)
            inputAN = input("Antarctica: ")
            if inputAN[0] == "y" or inputAN[0] == "Y":
                try:
                    os.popen('explorer "https://www.youtube.com/watch?v=dQw4w9WgXcQ"')
                    time.sleep(6.9)
                    os.popen('explorer "https://www.youtube.com/watch?v=dQw4w9WgXcQ"')
                except:
                    pass
            allServers = False
            break
                
        serverIDCount = len(preselectedServers)
        numServers = input("\nHow many servers to test? Or press enter for all: ")
        try:
            if numServers == "":
                allServers = True
                break
            numServers = int(numServers)
            if numServers == 69 or numServers == 420:
                try:
                    os.popen('explorer "https://www.youtube.com/watch?v=dQw4w9WgXcQ"')
                except:
                    pass
            if numServers > 0 and numServers <= serverIDCount:
                numServers = round(numServers/2)*2
                if numServers == 0:
                    numServers = 2
                serverIDList = preselectedServers[0:numServers]
                allServers = False
                break
            print(f"Positive integers between 1 and {serverIDCount} only.")
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
        colID = [x[2]for x in csvRows]
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
        colID = [x[2]for x in csvRows]
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
    if True:
        if allServers:
            pass
        else:
            try:
                serverID = serverIDList[serverIndex]
            except:
                raise KeyboardInterrupt
        
        print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Server ID: {serverID}")

        if not allServers:
            print(f"Testing server {serverIndex+1} of {numServers}\n")
        print("Test running please wait...")
        
        initialTime = time.time()
        output = subprocess.run('speedtest -u Mbps -s ' + str(serverID),capture_output=True)
        print("finish")
        print(output)
        try:
            tcpvcon = os.popen('tcpvcon64 -n -nobanner speedtest.exe').read()
        except:
            pass

        testDuration = str(round(time.time() - initialTime,2))
        testTime = str(datetime.datetime.now())
        print("Test Taken at: " + testTime)
        testDurationStr = "Test Duration: " + testDuration

        if True:
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

            cityList = list(result[3])
            dashIndex = 999
            for i in range(len(cityList)):
                if cityList[i] == "-":
                    dashIndex = i
            result[3] = "".join(cityList[:dashIndex-1])
            city = "".join(cityList[dashIndex+2:])

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
                if i < 48:
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
                resultList = [city,result[3],str(serverID),result[4],result[5],jitter,result[7],downData,result[9],upData,result[10],testTime,testDuration,result[11]]
                for item in resultList:
                    csvfile.write(item)
                    if item != result[11]:
                        csvfile.write(",")
                csvfile.write("\n")

        else:
            time.sleep(wait)
        
        if allServers:
            serverID += 1
        else:
            serverIndex += 1

    elif KeyboardInterrupt:
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

            aveDL = find_average(6)
            aveUL = find_average(8)

            print(f"\nAverage Latency: {find_average(4)} ms")
            print(f"Average Jitter: {find_average(5)} ms")
            print(f"Average Download Speed: {aveDL} Mbps")
            print(f"Average Upload Speed: {aveUL} Mbps")
            print(f"Average Packet Loss: {find_average(10)}%")

            print(f"\nNumber of Tests: {total_tests()}")
            print(f"Total Data Used: {total_data()} MB")
            print(f"Average Test Duration: {find_average(13)} seconds")

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

    else:
        print(f"\nERROR with server {serverID}")
        time.sleep(wait)
        if allServers:
            serverID += 1
        else:
            serverIndex += 1