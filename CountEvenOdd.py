def count(list):
    even = 0
    odd = 0

    for i in list:
        if i%2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd


list = [20, 15, 21, 45, 80, 90, 23]
even, odd = count(list)

print("Count of Even = {} and count of Odd = {}".format(even,odd))    #this is used to format into a string