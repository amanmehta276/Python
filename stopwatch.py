import time

def stopwatch():
    input("Press enter to start the stopwatch")
    start_time=time.time()

    input("Stopwatch has started.\nPress enter to stop the stopwatch")
    end_time=time.time()

    

    elapsed_time=end_time - start_time
    print(f"Elapsed time={elapsed_time:.3f}")

stopwatch()

# input("Press enter to start the stopwatch")
# start_time=time.time()

# input("Stopwatch has started.\nPress enter to stop the stopwatch")
# end_time=time.time()

# elapsed_time=end_time - start_time
# print(f"Elapsed time={elapsed_time:.3f}")
