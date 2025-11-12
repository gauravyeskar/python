# Calling the shares module.

import shares,time,importlib
def show(d):
    print("-"*50)
    print("\tShare Name\tValue")
    for sn,sv in d.items():
        print("\t{}\t:\t{}".format(sn,sv))
    else:
        print("-"*50)
d= shares.sharesinfo()
show(d)
time.sleep(20)
print("Updated Values ")
importlib.reload(shares)
d= shares.sharesinfo()
show(d)