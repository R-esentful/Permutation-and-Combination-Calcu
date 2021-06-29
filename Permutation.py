
from ast import Num


def Permutation(number,r):

    nfactorial = []
    temp = number - r
    total = 1 

    if number >r : 
        for x in range(1,number + 1):
            nfactorial.append(x)
            for y in nfactorial[::-1]:
                if y == temp:
                    nfactorial.remove(y)
                    temp = temp -1

        for z in nfactorial:
            total = total * z  
        print("Answer = {}".format(total))      
    else:
        print("Input is incorrect!")

    
  
