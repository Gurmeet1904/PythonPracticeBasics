from array import *
vals = array('i', [5, 9, 8, 10, 12])  #here 'i' is the typecode, it means it will only accept integer values in the array

#print(vals.buffer_info())   #gives address from where array is starting and also gives size of the array


#this prints the array values
for i in range(len(vals)):
    print(vals[i])



#Creating a new Array which is having square of vals
newArr = array(vals.typecode, (a*a for a in vals))

for e in newArr:
    print(e)

