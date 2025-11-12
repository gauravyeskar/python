def getline():
    line = input("Enter a line of text:- ")
    return line

def converttoupper(a):
    def caseconvert():
        text = a()
        res = text.upper()
        return res
    return caseconvert


#Main Program
resstr = converttoupper(getline)
res = resstr()
print("Upper Case Data = ",res)