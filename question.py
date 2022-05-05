#Every opening bracket '(' should close with ')'
def bracketMatcher(strParam):
    counter =0
    string = str(strParam)
    lenght = string.__len__()
    for i in range(lenght):
        if counter < 0:
            return 0
        if string[i] == '(':
            counter+=1
        if string[i] == ')':
            counter-=1
    if counter == 0:
        return 1
    else:
        return 0
      

print(bracketMatcher("This program will match every (brack))(et"))

