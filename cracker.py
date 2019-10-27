import sys
import os
import crypt
    
#dictionary attack function
def crackAttempt(saltFull, trueHash):
    with open("realhuman_phill.txt", "r") as crackerListFile:
        for attemptWord in enumerate(crackerListFile):
            #crypt takes password, then the salt with encoding type, then encrypts it
            if (trueHash == crypt.crypt(attemptWord,saltFull)):
                print("Hash: %s has password %s" % (trueHash, attemptWord))
                break
    
def main():
    #print crypt.crypt("puddle","$6$6b3y0laq")
    # open file of pure hashes to compare with later
    trueHashFile = open("compare.txt", "r")
    
    #counter for pure hash line
    count = 1
    #encodingType = "$6$"
    #open file of salts, pass single salt and hash into dictionary attack fuction
    #With statement same as try: f=open('file') finally: f.close()
    with open("salts.txt", "r") as saltListFile:
        for saltStart in enumerate(saltListFile):
            trueHash = trueHashFile.readline(count)
            #saltFull = encodingType + saltStart
            saltFull = saltStart
            crackAttempt(saltFull, trueHash)
            count += 1
    trueHashFile.close()

if __name__ == "__main__":
    main()
