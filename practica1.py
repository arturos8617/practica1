import os

def main():
    d = open("result.txt","w") 
    f = open("prueba2.txt", "r") 
    wholeText = ""
    for x in f.readlines():
        splitedSentence = x.split(',')
        #print(splitedSentence[2])
        #print(firstHexaNum(splitedSentence[0]))
        #print(lastDecimalNum(splitedSentence[5]))
        wholeText  += ":".join([splitedSentence[2],firstHexaNum(splitedSentence[0]),lastDecimalNum(splitedSentence[5])]) + "\n"
    d.write("hi")
   
def firstHexaNum(hexaNum):
    splitedHexaNum = list(hexaNum.replace('/', ':').split(':'))
    splitedHexaNum.pop(len(splitedHexaNum)-1)
    for x in range(len(splitedHexaNum)):
        splitedHexaNum[x] = str(int(splitedHexaNum[x],16))

    return ":".join(splitedHexaNum)


def lastDecimalNum(decimalNum):
    splitedDecimalNum = list(decimalNum.strip().split('.'))
    for x in range(len(splitedDecimalNum)):
        splitedDecimalNum[x] = str(hex(int(splitedDecimalNum[x]))).replace('0x','').upper()
    return ".".join(splitedDecimalNum)




main()
