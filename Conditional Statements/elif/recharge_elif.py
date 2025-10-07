# recharge plan
recharge =int(input("Enter the amount of plan: "))
if(recharge == 100):
    print("Successfully recharged.. 90 days pack, data 5Gb.")
elif(recharge == 3599):
    print("Successfully recharged.. 365 days pack, data 912.5 Gb, 2.5 Gb/day + Netflix")
elif(recharge == 48):
    print("Successfully recharged.. 3 days data pack")
elif(recharge== 999):
    print("Successfully recharged.. 98 days pack, data 196 Gb, 2Gb/day")
elif(recharge == 899):
    print("Successfully recharged.. 90 days pack, data 200 Gb, 2Gb/day")
elif(recharge == 349):
    print("Successfully recharged.. 28 days pack, data 56 Gb, 2 Gb/day")
elif(recharge == 1299):
    print("Successfully recharged.. 84 days pack, 168 Gb, 2 Gb/day + Netflix")
elif(recharge == 1049):
    print("Successfully recharged.. 84 days pack, 168 Gb, 2 Gb/day + sony LIV + ZEE5")
elif(recharge == 1029):
    print("Successfully recharged.. 84 days pack, 168 Gb, 2 Gb/day + Amazon Prime Lite")
elif(recharge == 1028):
    print("Successfully recharged.. 84 days pack, 168 Gb, 2Gb/day + Swiggy + Jio Cloud")
elif(recharge == 445):
    print("Successfully recharged.. 28 days pack, 56 Gb, 2Gb/day + Discovery+")
elif(recharge == 949):
    print("Successfully recharged.. 84 days pack, 168 Gb, 2Gb/day + JioHotstar")
elif(recharge == 198):
    print("Successfuly recharged.. 14 days pack, 28 Gb, 2Gb/day + JioTV")
else:
    print("Wrong Plan Please Choose Again...")
