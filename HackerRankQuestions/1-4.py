'''You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck 
    should be capitalised correctly as Alison Heck.

Given a full name, your task is to capitalize the name appropriately.
Input Format:- 
A single line of input containing the full name,s.

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format
Print the capitalized string,S.

Sample Input :- chris alan
Sample Output:- Chris Alan   '''

'''import math
import os
import random
import re
import sys
# Complete the solve function below.

def solve(s):
    # The correct function logic
    return ' '.join([word.capitalize() for word in s.split(' ')])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()'''
#########################################################################
'''
Question: The Minion game [Python Strings]
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S .
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring

A player gets +1 point for each occurrence of the substring in the string S

For example:

String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
'''
'''def minion_game(string):
    kevin = stuart = 0
    length: int = len(string)
    for i, char in enumerate(string):
        points: int = length - i
        if char in {"A", "E", "I", "O", "U"}:
            kevin += points
        else:
            stuart += points
    if kevin == stuart:
        print("Draw")
    else:
        print(*("Stuart", stuart) if stuart > kevin else ("Kevin", kevin))

minion_game('BANANA')'''
##################################################################################################
"""
s = “AAABCADDE”
k = 3
There are three substrings of length 3 to consider: ‘AAA’, ‘BCA’ and ‘DDE’. The first substring is all ‘A’ characters, 
so u1 = ‘A’. The second substring has all distinct characters, so u2 = ‘BCA’. The third substring has 2 different characters,
 so u3 = ‘DE’. Note that a subsequence maintains the original order of characters encountered. The order of characters in each 
 subsequence shown is important.
 
Split s into n/k = 9/3 = 3 equal parts of length k = 3. Convert each ti to ui by removing any subsequent occurrences of non-distinct 
characters in ti:

t0 = 'AAB' : u0 = 'AB'
t1 = 'CAA' : u1 = 'CA'
t2 = 'ADA' : u2 = 'AD' """
'''def merge_the_tools(string, k):
    l = len(string)//k
    for i in range(l):
        print(''.join(dict.fromkeys(string[i*k:(i*k)+k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)'''
#########################################################################################################
'''Palandromic Triangle
1
12
121
12321
1234321
123454321  '''
'''for i in range(1,int(input("Enter num: "))+1):
    print(((10**i-1)//9)**2)
'''
##########################################################################################################
'''
1
22
333
4444  '''
'''for i in range(1,int(input())):
    print((10**i)//9*i)'''
##########################################################################################################
'''The input consists of three lines. The first line contains the integer N, denoting the length of the list. The next line consists of N
space-separated lowercase English letters, denoting the elements of the list.
The third and the last line of input contains the integer K, denoting the number of indices to be selected.'''
'''from itertools import * 
n = int(input())
ls = input().split()
k = int(input())
com = list(combinations(ls, k))
tol = [i for i in com  if "a" in i ]
print(f'{(len(tol)/len(com)):.12f}') '''
#############################################################################################################
# are_Anagrams
'''def are_anagrams(w1,w2):
    word1 = sorted(w1.replace(' ','').lower())
    word2 = sorted(w2.replace(' ','').lower())
    return word1 == word2
wordA = "Listen"
wordB = "Silent"
print(f"'{wordA}' and '{wordB}' \nare_anagrams: {are_anagrams(wordA,wordB)}")
'''
##############################################################################################################################
'''sq = []
for x in range(5):
    sq.append(lambda:x**2)
print(sq[0]())
print(sq[4]())'''
##############################################################################################################################
