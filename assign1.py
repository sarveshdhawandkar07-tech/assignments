# Algorithm to convert infix to postfix

infix = input("Enter Infix expression :")
stack = []
postfix = ""

# Precedence function
def precedence(op):
    if op == "^":
        return 3
    elif op == "*" or op == "/":
        return 2
    elif op == "+" or op == "-":
        return 1 
    return 0

for symb in infix:
    if symb == "(":
        stack.append(symb)
    elif symb == ")":
        while stack[-1] != "(" :
            postfix += stack.pop()
        stack.pop()
    
    elif symb.isalnum():
        postfix += symb

    elif symb in ["^","*","/","+","-"]:
        while stack and stack[-1] != "(" and (precedence(stack[-1]) > precedence(symb) or (precedence(stack[-1]) == precedence(symb) and symb != "^")) :
            postfix += stack.pop()
        stack.append(symb)
    
    
while stack:
    postfix += stack.pop()


print(postfix)
