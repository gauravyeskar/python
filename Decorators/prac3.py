def converter(a):
    def caseconvert():
        text = a()
        res = text.upper()
        return res
    return caseconvert

@converter
def getline():
    line = input("Enter the line of text:- ")
    return line

# Main program
res = getline()
print(f"Upper Case Data:- {res}")