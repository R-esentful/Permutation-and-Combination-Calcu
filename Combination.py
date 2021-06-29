def Combination(number,r):

    nfactorial = []
    rfactorial = []

    temp = number - r
    tempnf = 1
    tempnr = 1

    total= 0

    if number >r : 
        for a in range(1,number + 1):
            nfactorial.append(a)
            for a in nfactorial[::-1]:
                if a == temp:
                    nfactorial.remove(a)
                    temp = temp -1
        for b in nfactorial:
            tempnf = tempnf * b

        for c in range(1,r+1):
            rfactorial.append(c)
        
        for d in rfactorial:
            tempnr = tempnr * d
        
        total = tempnf / tempnr

        print("Answer: {}".format(total))
    else:
        print("Input is incorrect!")

