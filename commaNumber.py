import random

Significance = ['Centitillion','Novenonagintatillion','Octononagintatillion','Septenonagintatillion','Senonagintatillion','Quinquanonagintatillion','Quattuornonagintatillion','Trenonagintatillion','Duononagintatillion','Unonagintatillion','Nonagintatillion','Noveoctogintatillion','Octoctogintatillion','Septeoctogintatillion','Seoctogintatillion','Quinquaoctogintatillion','Quattuoroctogintatillion','Treoctogintatillion','Duoctogintatillion','Unoctogintatillion','Octogintatillion','Noveseptuagintatillion','Octoseptuagintatillion','Septeseptuagintatillion','Seseptuagintatillion','Quinquaseptuagintatillion','Quattuorseptuagintatillion','Treseptuagintatillion','Duoseptuagintatillion','Unseptuagintatillion','Septuagintatillion','Novesexagintatillion','Octosexagintatillion','Septesexagintatillion','Sesexagintatillion','Quinquasexagintatillion','Quattuorsexagintatillion','Tresexagintatillion','Duosexagintatillion','Unsexagintatillion','Sexagintatillion','Sexagintatillion','Novequinquagintatillion','Octoquinquagintatillion','Septequinquagintatillion','Sequinquagintatillion','Quinquaquinquagintatillion','Quattuorquinquagintatillion','Trequinquagintatillion','Duoquinquagintatillion','Unquinquagintatillion','Quinquagintatillion','Novequadragintatillion','Octoquadragintatillion','Septequadragintatillion','Sequadragintatillion','Quinquaquadragintatillion','Quattuorquadragintatillion','Trequadragintatillion','Duoquadragintatillion','Unquadragintatillion','Quadragintatillion','Novetrigintatillion','Octotrigintatillion','Septetrigintatillion','Setrigintatillion','Quinquatrigintatillion','Quattuortrigintatillion','Tretrigintatillion','Duotrigintatillion','Untrigintatillion','Trigintatillion','Novevigintilion','Octovigintilion','Septevigintilion','Sevigintilion','Quinquavigintilion','Quattuorvigintilion','Trevigintilion','Duovigintilion','Unvigintilion','Vigintillion','Novemdecillion','Octodecillion','Septendecillion','Sexdecillion','Quindecillion','Quattuordecillion','Tredecillion','Duodecillion','Undecillion','Decillion','Nonillion','Octillion','Septillion','Sextillion','Quintillion','Quadrillion','Trillion','Billion','Million','Thousand','']

def commaNumber(num):
    'This function takes a numeric type (int/float) and returns a striing representation with commas seperating groups of three digits starting with the ones, tens, and hundreds place in the first (right-most) group'
    fullNumberStr = str(num)
    strList = []
    numList = fullNumberStr.split('.')
    intStr = numList[0]
    while len(intStr) > 0:
        strList.append(intStr[-3:]) # Builds a list with groups of three digits on the lhs of the .
        intStr = intStr[:-3]
    fStr = ''
    for i in range(len(strList)):
        fStr += strList.pop()
        if len(strList) > 0:
            fStr += ','
    for elem in numList[1:]:
        fStr += '.' + elem # Adds the rhs of the . to the string
    return fStr

def sayRhs(rhs):
    toReturn = ''
    ones = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    digitList = [char for char in rhs]
    digitList.reverse()
    for digit in digitList:
        toReturn = ones[eval(digit)] + ' ' + toReturn
    return toReturn[:-1]

def sayGroup(group):
    toReturn = ''
    ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
    tens = ['','Ten','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']
    teens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
    digits = str(group)
    while len(digits) < 3:
        digits = '0' + digits
    if digits[0] != '0':
        if digits[1] == '0' and digits[2] == '0':
            toReturn += ones[int(digits[0])] + ' Hundred'
        else:
            toReturn += ones[int(digits[0])] + ' Hundred '
    if digits[1] != '1':
        if digits[1] != '0':
            toReturn += tens[int(digits[1])] 
            if digits[2] != '0':
                toReturn += ' ' + ones[int(digits[2])]
        else:
            if digits[2] != '0':
                toReturn += ones[int(digits[2])]
    else:
        toReturn += teens[int(digits[2])]
    return toReturn

def sayFullName(num):
    'Does say name with words for groups of three digits'
    if not num:
        return 'Zero'
    name = ''
    cStr = commaNumber(num)
    cLst = cStr.split(',')
    significance = [x for x in Significance]
    while len(cLst) and len(significance):
        if '.' not in cLst[-1]:
            group = int(cLst.pop())
            if group:
                name = ' ' + significance.pop() + ' ' + name
                name = sayGroup(group) + name
            else:
                significance.pop()
        else:
            group = cLst.pop()
            lhs = eval(group.split('.')[0])
            rhs = group.split('.')[1]
            name = ' ' + significance.pop() + ' ' + name
            name = sayGroup(lhs) + ' Point ' + sayRhs(rhs) + name
    if cLst:
        name = cLst.pop() + ' ' + name
    while cLst:
        name = cLst.pop() + ',' + name
    while name[-1] == ' ':
        name = name[:-1]
    return name

def sayName(num):
    if not num:
        return '0'
    name = ''
    cStr = commaNumber(num)
    cLst = cStr.split(',')
    significance = [x for x in Significance]
    while len(cLst) and len(significance):
        if '.' not in cLst[-1]:
            group = int(cLst.pop())
            if group:
                name = ' ' + significance.pop() + ' ' + name
                name = str(group) + name
            else:
                significance.pop()
        else:
            name = ' ' + significance.pop() + ' ' + name
            name = cLst.pop() + name
    while cLst:
        name = cLst.pop() + ',' + name
    while name[-1] == ' ':
        name = name[:-1]
    return name

def randPrint(maxVal):
    ui = ''
    while ui.lower() != 'exit':
        x = random.randint(0, maxVal + 1)
        print(32*'*')
        print(x)
        print(32*'*')
        print(commaNumber(x))
        print(32*'*')
        print(sayName(x))
        print(32*'*')
        print(sayFullName(x))
        print(32*'*')
        ui = input(">>> ")

# randPrint(1000**5)

#  x = 3939382010282
#  x = 123342
#  print(sayName(x))
#  print(sayFullName(x))
# print(x)
# print(commaNumber(x))
# print(sayName(x))
# print(sayFullName(x))
#print(commaNumber(1393812345638000883876727657))
# print(sayName(30491357.23455))
#print(sayName(4838372921393812345949482810389484717124393813848471201638000883876727657))

# print(commaNumber(12345.678)) # Example usage
