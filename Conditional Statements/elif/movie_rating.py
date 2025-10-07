# movie_rating
rate = int(input("Enter the rating of movie from 0-5: "))
if(0 <= rate <= 1):
    print("Terrible")
elif(1 <= rate <= 2):
    print("Bad")
elif(3 <= rate <=4):
    print("Okay")
elif(4<= rate <= 5):
    print("Excellent")
else:
    print("Invalid Input")