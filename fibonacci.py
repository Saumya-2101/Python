def fibonacci(num):
    if(num<=0):
        return 0
    elif(num==1):
        return 1
    else:
        return (fibonacci(num-1) + fibonacci(num-2))

nterms = int(input("Enter the number of terms:"))
for i in range(nterms):
    print(fibonacci(i))   
  