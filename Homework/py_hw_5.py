def calculate(number1,number2,op):
    if(op=="+"):
        print(number1+number2)
    elif(op=="-"):
        print(number1-number2)
    elif(op=="*"):
        print(number1*number2)
    elif(op=="/"):
        print(number1/number2)
    else:
        print("invalid operation")
        
calculate(4,5,"/")      