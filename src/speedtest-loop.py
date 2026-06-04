import csv
import datetime
import os
import time

resultsCSV = r"outputs/speedtest-loop_results.csv"
startTime = time.time()

while True:
    try:
        print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Test running please wait...")

        initialTime = time.time()
        output = os.popen("speedtest").read()
        print(output)

        testDuration = str(round(time.time() - initialTime, 2))
        testTime = str(datetime.datetime.now())
        print("Test Taken At: " + testTime)

        try:
            lines = output.splitlines()
            with open(resultsCSV, "a", newline="") as f:
                csv.writer(f).writerow([
                    lines[3], lines[4], lines[5],
                    lines[7], lines[9], lines[10], lines[11],
                    testTime, testDuration,
                ])
        except Exception:
            print("\nError: Failed to write to CSV file.")

    except KeyboardInterrupt:
        timeElapsed = round(time.time() - startTime, 2)
        print(f"\nTime Elapsed Since Start: {timeElapsed} seconds")

        userInput = input("\nPaused. Press enter to resume or type 'exit'. ")
        if userInput == "exit":
            exit()
