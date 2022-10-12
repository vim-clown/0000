from random import randint
import os, time
flg = True
while flg: 
    egg1, egg2 = 696969, 420420
    bucket = []
    f_list = []
    cond = egg1 and egg2 not in f_list
    layer = randint(0, 200)
    while layer < 100 and cond:
        O = randint(0, 2000)
        t = 0
        while O < 1000 and cond:
            a = randint(1, 1000)
            b = randint(1001, 2000)
            c = randint(2001, 3000)
            d = randint(3001, 4000)

            x = lambda a, b, c, d: a * b + c/d
            y = lambda ff: ff + "f"
            f = randint(0, 500)
            while x(a, b, c, d) + f <= 100 and cond:
                print(str(x(a, b, c, d)+f) + "\t" + y(str(f)) + "\n")
                f = f + 1
            print(f"pass #{t}")
            f_list.append(t)
            t = t + 1
        layer = layer * 2
        
    print(f"sum: {sum(f_list)}")
    if 696969 and 420420 in f_list:
        print(f"eggs found in index {f_list.index(696969)} and {f_list.index(420420)}")
        egg_id = randint(100000000000, 9999999999)
        bucket.append(egg_id)
        egg2_id =  randint(100000000000, 9999999999) 
        bucket.append(egg_id)
        print(f"Bucket balance: {len(bucket)} eggs")
        print("resuming in 10 seconds...")
        time.sleep(10)

    else:
        print("F")
        print("resuming in 10 seconds...") 
        time.sleep(10)
        
