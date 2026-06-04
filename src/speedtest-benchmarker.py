#!/usr/bin/env python3
version = "1.4"

import csv
import datetime
import os
import re
import time

resultsCSV = r"outputs/benchmark_results.csv"
startTime = time.time()
csvRows = []

OCList = [12491]
NAList = [12491]
SAList = [12491]
EUList = [12491]
ASList = [6969]
AFList = [12491]
preselectedServers = [
    12491, 2169, 12492, 6355, 12493, 2165, 12495, 234, 12494, 6153,
    28463, 34083, 21569, 28910, 40508, 50344, 19081, 47668, 30907, 30593,
    26996, 35058, 24281, 34948, 40509, 37211, 14928, 31122, 14236, 16974,
    14228, 17384, 14238, 17386, 14237, 37499, 16976, 28032, 21568, 34143,
    34555, 1536, 29545, 4036, 2690, 2599, 11871, 49594, 49421, 8864,
]


def find_average(column):
    values = [float(row[column]) for row in csvRows]
    return round(sum(values) / len(values), 2)


def total_tests():
    return len(csvRows)


def total_data():
    down = sum(float(row[7]) for row in csvRows)
    up = sum(float(row[9]) for row in csvRows)
    return round(down + up, 2)


def prompt_positive_int(prompt, allow_empty=False):
    while True:
        value = input(prompt)
        if allow_empty and value == "":
            return None
        try:
            n = int(value)
            if n > 0:
                return n
            print("Positive integers greater than 0 only.")
        except ValueError:
            print("Please enter only whole numbers in Mbps.")


def _to_mb(value_str, unit):
    val = float(value_str)
    if unit == "k":
        val /= 1024
    elif unit == "G":
        val *= 1024
    return str(val)


def parse_speed_line(line):
    speed_match = re.search(r"([\d.]+)\s+Mbps", line)
    data_match = re.search(r"\(([\d.]+)\s*(k|M|G)B\)", line)
    speed = speed_match.group(1) if speed_match else "0"
    data = _to_mb(data_match.group(1), data_match.group(2)) if data_match else "0"
    return speed, data


def parse_output(lines):
    server_match = re.search(r"Server:\s+(.+?)\s+=\s+", lines[3])
    server_str = server_match.group(1).replace(",", ";") if server_match else ""
    parts = server_str.rsplit(" - ", 1)
    server_name = parts[0].strip() if len(parts) == 2 else server_str
    city = parts[1].strip() if len(parts) == 2 else ""

    isp_match = re.search(r"ISP:\s+(.+)", lines[4])
    isp = isp_match.group(1).strip().replace(",", ";") if isp_match else ""

    latency_match = re.search(r"Latency:\s+([\d.]+)\s+ms\s+\(([\d.]+)\s+ms jitter\)", lines[5])
    latency = latency_match.group(1) if latency_match else "0"
    jitter = latency_match.group(2) if latency_match else "0"

    dl_speed, dl_data = parse_speed_line(lines[7])
    ul_speed, ul_data = parse_speed_line(lines[9])

    ploss_match = re.search(r"([\d.]+)%", lines[10])
    packet_loss = ploss_match.group(1) if ploss_match else "0.0"

    url_match = re.search(r"Result URL:\s+(.+)", lines[11])
    result_url = url_match.group(1).strip().replace(",", ";") if url_match else ""

    return city, server_name, isp, latency, jitter, dl_speed, dl_data, ul_speed, ul_data, packet_loss, result_url


try:
    print("BJROXN :)")
    print(f"Version: {version}")

    downloadSpeed = prompt_positive_int(
        "\nEnter the download speed of your internet plan tier. E.g. '250' for a NBN Superfast 250/25 plan: "
    )
    uploadSpeed = prompt_positive_int(
        "\nEnter the upload speed of your internet plan tier. E.g. '25' for a NBN Superfast 250/25 plan: "
    )
    downloadTES = prompt_positive_int(
        "\nEnter the download Typical Evening Speed as specified by your provider. E.g. '240' for a NBN 250/25 plan: "
    )
    uploadTES_input = prompt_positive_int(
        "\nEnter the upload Typical Evening Speed. If unspecified, press enter. E.g. '22' for a NBN 250/25 plan: ",
        allow_empty=True,
    )
    uploadTES = uploadTES_input if uploadTES_input is not None else uploadSpeed * 0.9

    while True:
        serverIDList = []
        regionsOrNum = input("\n\nSelect servers by region? Or press enter to select by number/all servers: ")

        if regionsOrNum and regionsOrNum[0] in ("y", "Y"):
            for region_name, region_list in [
                ("Oceania", OCList),
                ("North America", NAList),
                ("South America", SAList),
                ("Europe", EUList),
                ("Asia", ASList),
                ("Africa", AFList),
            ]:
                ans = input(f"{region_name}: ")
                if ans and ans[0] in ("y", "Y"):
                    serverIDList.extend(region_list)
            ans = input("Antarctica: ")
            if ans and ans[0] in ("y", "Y"):
                try:
                    os.popen('explorer "https://www.youtube.com/watch?v=dQw4w9WgXcQ"')
                    time.sleep(6.9)
                    os.popen('explorer "https://www.youtube.com/watch?v=dQw4w9WgXcQ"')
                except Exception:
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
            if numServers in (69, 420):
                try:
                    os.popen('explorer "https://www.youtube.com/watch?v=dQw4w9WgXcQ"')
                except Exception:
                    pass
            if 0 < numServers <= serverIDCount:
                numServers = max(round(numServers / 2) * 2, 2)
                serverIDList = preselectedServers[:numServers]
                allServers = False
                break
            print(f"Positive integers between 1 and {serverIDCount} only.")
        except ValueError:
            print("Please enter only whole numbers.")

except KeyboardInterrupt:
    exit()

if allServers:
    try:
        with open(resultsCSV) as f:
            csvRows = list(csv.reader(f))
        serverID = int(csvRows[-1][2]) + 1 if csvRows else 233
    except (OSError, ValueError, IndexError):
        serverID = 233
else:
    serverIndex = 0
    try:
        with open(resultsCSV) as f:
            csvRows = list(csv.reader(f))
        lastServer = int(csvRows[-1][2])
        for i, sid in enumerate(serverIDList):
            if lastServer == sid:
                serverIndex = i + 1
                break
    except (OSError, ValueError, IndexError):
        pass

while True:
    try:
        if not allServers:
            if serverIndex >= len(serverIDList):
                raise KeyboardInterrupt
            serverID = serverIDList[serverIndex]

        print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Server ID: {serverID}")
        if not allServers:
            print(f"Testing server {serverIndex + 1} of {numServers}\n")
        print("Test running please wait...")

        initialTime = time.time()
        output = os.popen(f"speedtest -u Mbps -s {serverID}").read()
        print(output)

        testDuration = str(round(time.time() - initialTime, 2))
        testTime = str(datetime.datetime.now())
        print("Test Taken at: " + testTime)

        try:
            lines = output.splitlines()
            city, server_name, isp, latency, jitter, dl_speed, dl_data, ul_speed, ul_data, packet_loss, result_url = parse_output(lines)

            now = datetime.datetime.now()
            with open(resultsCSV, "a", newline="") as f:
                csv.writer(f).writerow([
                    city, server_name, str(serverID), isp,
                    latency, jitter,
                    dl_speed, dl_data,
                    ul_speed, ul_data,
                    packet_loss,
                    now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"),
                    testDuration, result_url,
                ])
        except Exception:
            time.sleep(1)

        if allServers:
            serverID += 1
        else:
            serverIndex += 1

    except KeyboardInterrupt:
        timeElapsed = round(time.time() - startTime, 2)
        print(f"\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"\nTime Elapsed Since Start: {timeElapsed} seconds")
        print(str(datetime.timedelta(seconds=timeElapsed)))

        try:
            csvRows = []
            with open(resultsCSV) as f:
                csvRows = list(csv.reader(f))

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
            print(f"\nPercentage of Plan Download Speed: {round((aveDL / downloadSpeed) * 100, 2)}%")
            print(f"Percentage of Plan Upload Speed: {round((aveUL / uploadSpeed) * 100, 2)}%")
            print(f"\nPercentage of TES Download Speed: {round((aveDL / downloadTES) * 100, 2)}%")
            print(f"Percentage of TES Upload Speed: {round((aveUL / uploadTES) * 100, 2)}%")
        except Exception:
            pass

        try:
            userInput = input("\n\nPaused. Press enter to resume or type 'exit'. ")
            if userInput != "":
                print("")
                exit()
        except (EOFError, KeyboardInterrupt):
            exit()

    except Exception:
        print(f"\nERROR with server {serverID}")
        time.sleep(1)
        if allServers:
            serverID += 1
        else:
            serverIndex += 1
