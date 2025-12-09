# namedtuple: A factory function for creating tuple subclasses with named fields. This allows for more readable and self-documenting 
# code when working with structured data.
from collections import namedtuple

# 1. 
'''x = namedtuple("Courses","Name ,Language ")
t = x("Data Science" , "Python")
print(t)
'''

# 2. Accessing List inside
'''x = namedtuple("Point",['x','y'])
p = x(1,2)
print(p)'''

# 3. Create a namedtuple to store basic student information and access its fields in different ways.
si = namedtuple("Student Info","name","Age","Grade")
details = si("Gaurav",22,"A-")
print(details)