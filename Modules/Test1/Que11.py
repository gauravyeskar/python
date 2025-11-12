# Koi bhi program ko chalne mein kitna time lagta hai calculate kare.
import time
a = 10
b = 20
start = time.time()
c = a + b 
end = time.time()
diff = abs(start - end)
print("Total timing is:- ",diff)