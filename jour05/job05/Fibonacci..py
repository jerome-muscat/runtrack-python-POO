def suiteFibonacci(num1, num2, repetition):
    total = num1 + num2
    if repetition == 0:
        # total = total
        print(total)
    else:
        if num1 > num2:
            suiteFibonacci(num1=total, num2=num1, repetition = repetition - 1)
        elif num1 < num2:
            suiteFibonacci(num1=num2, num2=total, repetition = repetition - 1)
   

suiteFibonacci(0, 1, 5)