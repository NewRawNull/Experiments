import time

def for_loop_function():
    result = 0
    for i in range(1, n+1):
        result += i
    print("[F] The sum from 1-{} is {}".format(n, result))
    
def while_loop_function():
    result = 0
    i = 1
    while i <= n:
        result += i
        i += 1
    print("[W] The sum from 1-{} is {}".format(n, result))
    
try:
    n = int(input("Enter number for cumulative sum: "))
except:
    print("It should be a number only!!!")
    input("Press Enter to continue...")
    exit(0)
    
time_start = time.time()
for_loop_function()
time_end = time.time()
time_total = time_end - time_start
print('Time for "for" function: {}'.format(time_total))

print()

time_start = time.time()
while_loop_function()
time_end = time.time()
time_total = time_end - time_start
print('Time for "while" function: {}'.format(time_total))
