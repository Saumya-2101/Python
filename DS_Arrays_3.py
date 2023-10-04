max = int(input("Enter the maximum number to print:"))

# ONLY TO PRINT THE ODD NUMBERS
# for i in range(1,max,2):
#     print(i)


# TO CREATE A LIST 

Odd_numbers = []

for i in range(1,max):

    if i%2==1:

        Odd_numbers.append(i)

print("Odd_numbers:"  , Odd_numbers)

   
