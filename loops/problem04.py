# Exponentioal backoff: 
# implement an exponential backoff strategythat double wait time between retries, starting from 1second,but stop after 7 retries
import time

# Reset values
attemps = 0
wait_time = 1
max_retries = 7

while attemps < max_retries:
    print("Attempt", attemps+1, "with wait time:", wait_time, "seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attemps += 1
print("Maximum retries reached")
