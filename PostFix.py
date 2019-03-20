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

def doCalc(lhs, operand, rhs):
    result = 0
    if operand == "*":
        result = lhs * rhs
    elif operand == "/":
        result = lhs / rhs
    elif operand == "+":
        result = lhs + rhs
    elif operand == "-":
        result = lhs - rhs
    elif operand == "%":
        result = lhs % rhs
    return result

def main(*argv):
    postFixStack = []
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
            result = doCalc(lhs, token, rhs)
            postFixStack.append(result)
        else:
            raise ValueError("Invalid symbol: {0}".format(token))
    print("Result: " + str(postFixStack.pop()))
    if len(postFixStack) != 0:
        raise Exception("Unexpected")


main(5, 6, 7, '*', '+', 1, '-')
