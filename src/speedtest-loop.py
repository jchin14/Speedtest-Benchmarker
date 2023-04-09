import os
import time
import datetime

resultsCSV = r"outputs/speedtest-loop_results.csv"
startTime = time.time()

while True:
    try:
        print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Test running please wait...")

        initialTime = time.time()
        output = os.popen('speedtest').read()
        print(output)

        testDuration = str(time.time() - initialTime)
        testTime = str(datetime.datetime.now())
        print("Test Taken At: " + testTime)
        testDurationStr = "Test Duration: " + testDuration
        
        try:
            with open(resultsCSV, 'a') as csvfile:
                result = output.splitlines()
                list = [result[3],result[4],result[5],result[7],result[9],result[10],result[11],testTime,testDurationStr]
                for item in list:
                    csvfile.write(item)
                    csvfile.write(",")
                csvfile.write("\n")
        except:
            print("\nError: Failed to write to CSV file.")

    except:
        timeElapsed = time.time() - startTime
        print(f"\nTime Elapsed Since Start: {timeElapsed} seconds")
        
        userInput = input("\nPaused. Press enter to resume or type 'exit'. ")
        if userInput == "exit":
            exit()