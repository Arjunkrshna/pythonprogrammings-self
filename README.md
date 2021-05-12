# find-factorial
print("Factorial prgram")
a = int(input("enter a number for which factorial is to be calculated"))
fact = 1
for i in range(1,a+1):
     fact = fact * i
print("Factorial of {0} is {1}".format(a,fact))
