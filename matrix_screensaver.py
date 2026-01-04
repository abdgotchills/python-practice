import random, sys, time

width = 70
column = [0]*width
try:
    while True:
        for i in range(width):
            if random.random()<0.05:
                column[i]=random.randint(4,14)

            if column[i]==0:
                print(" ",end="")
            else:
                print(random.choice([0,1]), end="")
                column[i] -= 1
        print()
        time.sleep(0.3)
except KeyboardInterrupt:
    sys.exit()
