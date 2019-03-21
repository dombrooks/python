import sys

#debug = True
debug = False
def log(s, really = False):
    if debug | really:
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

def main(tokens):
    symbols = ['*', '/', '+', '-', '%'];
    postFixStack = []
    log("Input length : " + str(len(tokens)))
    log("Input: " + ' '.join(str(v) for v in tokens))
    for token in tokens:
        log(token)
        if is_number(token):
            postFixStack.append(int(token))
            log("Appended " + token)
        elif token in symbols:
            log(token +  " is not number")
            rhs = int(postFixStack.pop())
            lhs = int(postFixStack.pop())
            log(str(lhs) + " " + token + " " + str(rhs))
            result = doCalc(lhs, token, rhs)
            postFixStack.append(result)
        else:
            raise ValueError("Invalid symbol: {0}".format(token))
    log("Result: " + str(postFixStack.pop()), True)
    if len(postFixStack) != 0:
        raise Exception("Unexpected")


if __name__ == "__main__":
    # Test
    # main(5, 6, 7, '*', '+', 1, '-')
    # main(5, 6, 7, '*', '+', 1, '-','x')
    main(sys.argv[1:])
