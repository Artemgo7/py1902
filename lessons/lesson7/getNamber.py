number = int (input("Enter the number: "))
sum = (number // 10000) + (number // 10 // 10 // 10 % 10) + (number // 10 // 10 % 10) + (number // 10 % 10) + (number % 10)
mul = (number // 10000) * (number // 10 // 10 // 10 % 10) * (number // 10 // 10 % 10) * (number // 10 % 10) * (number % 10)
print (sum)
print (mul)

print (number // 10000)
print (number // 10 // 10 // 10 % 10)
print (number // 10 // 10 % 10)
print (number // 10 % 10)
print (number % 10)