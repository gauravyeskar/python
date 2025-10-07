'''
# Anonymous Function.
1. doesnot have any function name.
2. purpose is to perform instance operations.
3. This functions are used at that point of time only and not be used in other part of the function again. 
4. Contains single executable statements not multiple executable statements.
5. No need of writing the return function automatically returns the output.

Syn:-  varnm = lambda params_list:expression

'''
r = lambda x:x+10
print(r(100))

hd = lambda a,b:a+b
print(hd(10,20))

findmax = lambda a,b :a if a > b else b
print(findmax(20,10))

getword = lambda line : line.split()
line = input("Enter the string: ")
words = getword(line)
for word in words:
    print("\t {}".format(word))


