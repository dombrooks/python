debug = True
#debug = False
def log(s):
    if debug:
        print(s)

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main(*argv):
    postFixStack = []
    result = 0
    log("Input length : " + str(len(argv)))
    log("Input: " + ' '.join(str(v) for v in argv))
    for v in argv:
        token = str(v)
        log(token)
        if is_number(v):
            postFixStack.append(int(token))
            log("Appended " + token)
        elif token in ['*', '/', '+', '-', '%']:
            #log(token +  " is not number")
            rhs = int(postFixStack.pop())
            lhs = int(postFixStack.pop())
            log(str(lhs) + " " + str(v) + " " + str(rhs))
            if token == "*":
                result = lhs * rhs
            elif token == "/":
                result = lhs / rhs
            elif token == "+":
                result = lhs + rhs
            elif token == "-":
                result = lhs - rhs
            elif token == "%":
                result = lhs % rhs
            postFixStack.append(result)
        else:
            raise ValueError("Invalid symbol: {0}".format(token))
    print("Result: " + str(postFixStack.pop()))


main(5, 6, 7, '*', '+', 1, '-')
