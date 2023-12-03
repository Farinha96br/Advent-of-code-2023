import numpy as np
import matplotlib.pyplot as plt

puzzle_data = np.loadtxt("data_d01.dat",dtype="str")

def l():
    print("-------")

def get_ver(word):
    i = 0
    L = len(word)
    code = ["0","0"]
    while word[i].isnumeric() != True:
        i += 1
    #print(i,word[i])
    code[0] = word[i]
    i = -1
    while word[i].isnumeric() != True:
        i -= 1
    #print(i,word[i])
    code[1] = word[i]
    return int(code[0] + code[1])

vfinal = 0
for i in range(0,len(puzzle_data)):
    word = puzzle_data[i]
    val = get_ver(word)
    #print(word, val)
    vfinal += val

print("first vfinal:" , vfinal)


l()
print("Agora versão corrigida:")

def get_ver2(word):
    spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    txt = word
    print("word: ",txt)
    
    # working on the left first
    print("going -->")
 
    replaced = []
    lindexs = []
    lnumbers = []
    for i in range(0,9):
        temp = txt.replace(str(spelled[i]),str(i+1))
        replaced.append(temp)
    
    for i in range(0,9):
        temp = replaced[i]
        j = 0
        while temp[j].isnumeric() != True:
            j += 1
        lindexs.append(j)
        lnumbers.append(temp[j])
    print(replaced)
    print(lindexs)
    print(lnumbers)
    #print("----")
    lnumber = lnumbers[np.argmin(lindexs)]
    #print(lnumber)
    #print("--------")

    print("going <--")

    rindexs = []
    rnumbers = []
    for i in range(0,9):
        temp = replaced[i]
        j = -1
        while temp[j].isnumeric() != True:
            j -= 1
        rindexs.append(j)
        rnumbers.append(temp[j])
    print(replaced)
    print(rindexs)
    print(rnumbers)
    rnumber = rnumbers[np.argmax(rindexs)]



    code = int(str(lnumber) + str(rnumber))
    print(code)
    return code

     


val = get_ver2(puzzle_data[402])

#vfinal = 0
#for i in range(0,len(puzzle_data)):
#    word = puzzle_data[i]
#    val = get_ver2(word)
#    #print(word, val)
#    vfinal += val
#
#print("second vfinal:" , vfinal)

