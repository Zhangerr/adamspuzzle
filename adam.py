#!/usr/bin/python
"""
ADAM.PY 
python script to solve adam's puzzle - 4 numbers that you use arbitrary operators on to get 24
all numbers must be used once, while each operator can be used multiple times or not all

i'm not sure if iterating through the different combinations of numbers is necessary because of the communitive properties of addition and multiplication but perhaps its necessary for subtraction and division
"""
import itertools #imports a module, lets me use functions from this external package that contains tools for permutations/combinations
numbers=[] #empty list (list of items like 1,2,3,4,5)
for i in range(0,4): #do the following code 4 times; i equals 0 the first time, 1 the second time, 2 the third time, and 3 fourth time
    numbers.append(int(raw_input("enter a number: ")))	#get input from the user, convert it to a number, and add it to the empty list earlier
for i in list(itertools.product("+-/*",repeat=3)): #go through all the possible combinations of operators, like 3 additions in a row, 1 addition 2 subtraction, and etc
     for j in list(itertools.permutations(numbers)): #go through all the permutations of the numbers with each of the possible combinations of operators, so all the possible orders of the numbers (4 factorial)
             k = eval(str(float(j[0]))+i[0]+str(float(j[1]))) #use the first operator on the 1st and 2nd numbers of that combinations
             l = eval(str(k) + i[1] + str(float(j[2]))) #use the 2nd operator on the result of the last one and the 3rd number
             m = eval(str(l) + i[2] + str(float(j[3]))) #use the final operator on the result of the last operation and the last number
             if m == 24: #if the result is 24
                 print j,i,str(j[0])+i[0]+str(j[1])+i[1]+str(j[2])+i[2]+str(j[3]) #print it out in a readable form

