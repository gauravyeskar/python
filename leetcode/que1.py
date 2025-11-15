# print pattern of 
''' LeetCode: Question 
*
**
***
****
*****   '''
# for i in range(6):
#     for j in range(1,i+1):
#         print("*",end = "")
#     print()

# print following patterns of
'''
    *
   **
  ***
 ****
*****
'''
# for i in range(5):
#     for j in range(i+1):
#         print(" ",end="")
#     print("*")

'''
A
AB
ABC
ABCD
ABCDE  '''
# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(j),end=" ")
#     print()

'''
1
12
123
1234
12345  '''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

'''
1
122
333
4444
55555  '''
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

'''
A
BB
CCC
DDDD
EEEEE  '''
# for i in range(65,70):
#     for j in range(65,i+1):
#         print(chr(i),end=" ")
#     print()

'''
    *
   **
  ***
 ****
*****  '''
# for i in range(1,6):
#     for k in range(1,6-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

''' 7.
        1
       1 2 
      1 2 3
     1 2 3 4
    1 2 3 4 5  '''
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     print()

''' 8. 
    5
   4 5
  3 4 5
 2 3 4 5
1 2 3 4 5   '''
# r = 5
# for i in range(r,0,-1):
#     for j in range(1,i):
#         print(end=" ")
#     for k in range(i,r+1):
#         print(k,end=" ")
#     print()

''' 9.
     A
    A B
   A B C
  A B C D
 A B C D E
'''

'''11
    *
   * *
  * * *
 * * * * 
* * * * *   '''
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end=" ")
#     print()

'''12
    1
   2 2
  3 3 3
 4 4 4 4 
5 5 5 5 5   '''
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(i,end=" ")
#     print()

''' 13
    A
   B B
  C C C
 D D D D
E E E E E    '''
# n = 5
# k = 2 * n - 2
# x = 65
# for i in range(0,n):
#     ch= chr(x)
#     x+=1
#     for j in range(0,k):
#         print(end=" ")
#     k = k-1
#     for l in range(0,i+1):
#         print(ch,end=" ")
#     print("\r")