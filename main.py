import time
import pickle
import os.path
import os
import sys

if os.name == 'nt':
    import msvcrt


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ',.;".lower()
tester = "You have to not have the same bag of experiences as everyone else does, or else you're gonna make the same connections and you won't be innovative.".lower()

if __name__ == "__main__":
    
    fileName = input("Enter file name or predict: ").strip()
    print("Type this sentence:")
    print(tester)
    if fileName == "predict":
        d = dict.fromkeys(alphabet)
        for e in d:
            d[e] = dict()
    else:
        if os.path.exists(fileName + '.txt'):
            with open(fileName + '.txt', "rb") as myFile:
                d = pickle.load(myFile)
        else:
            d = dict.fromkeys(alphabet)
            for e in d:
                d[e] = dict()

    prevL = ''
    prevT = 0
    ite = 0 
    while ite < len(tester):
        test = tester[ite]
        inp = msvcrt.getch()
        timer = time.time_ns() / 1000000
        if inp == b'\r':
            print("Done!!")
            break
        if inp == b' ':
            inp = ' '
        else:
            inp = inp.strip().decode("utf-8").lower()

        if prevL != '' and inp == test and inp in alphabet:
            sys.stdout.write(inp)
            sys.stdout.flush()
            if (inp in d[prevL].keys()):
                d[prevL][inp] = (d[prevL][inp] + timer - prevT) / 2
            else:
                d[prevL].update({inp:timer - prevT})
            ite = ite + 1
            
            prevL = inp
            prevT = timer
        elif prevL == '' and inp == test:
            prevL = inp
            prevT = timer
            sys.stdout.write(inp)
            sys.stdout.flush()
            ite = ite + 1
    
    print(d)
    if fileName == "predict":
        curI = 1
        delTimeP = 0
        delTimeB = 0
        difP = 0
        difB = 0
        with open('pewt-1.txt', "rb") as myFile:
            delp1 = pickle.load(myFile)
        with open('pewt-2.txt', "rb") as myFile:
            delp2 = pickle.load(myFile)
        with open('pewt-3.txt', "rb") as myFile:
            delp3 = pickle.load(myFile)
        with open('bhoome-1.txt', "rb") as myFile:
            delb1 = pickle.load(myFile)
        with open('bhoome-2.txt', "rb") as myFile:
            delb2 = pickle.load(myFile)
        with open('bhoome-3.txt', "rb") as myFile:
            delb3 = pickle.load(myFile)
        while curI < len(tester):
            delTimeP = d[tester[curI - 1]][tester[curI]] - ((delp1[tester[curI - 1]][tester[curI]] + delp2[tester[curI - 1]][tester[curI]] + delp3[tester[curI - 1]][tester[curI]])/3)
            delTimeB = d[tester[curI - 1]][tester[curI]] - ((delb1[tester[curI - 1]][tester[curI]] + delb2[tester[curI - 1]][tester[curI]] + delb3[tester[curI - 1]][tester[curI]])/3)
            if -150 < delTimeP < 150:
                difP += 1
            if -150 < delTimeB < 150:
                difB += 1
            curI += 1
        print('\n')
        print('Too different from Pewt: '+ str(len(tester) - difP) + ' from ' + str(len(tester)))
        print('Too different from Bhoome: '+ str(len(tester) - difB) + ' from ' + str(len(tester)))
        print('\n')

        if difP < difB:
            print('You are bhoome!')
        elif difB < difP:
            print('You are Pewt!')
        else:
            print('Your maybe Bhoome or Pewt.')
    else:
        with open(fileName + '.txt', "wb") as myFile:
            pickle.dump(d, myFile)