a = 0
b = 1
sum = 0
while b <= 4000000:
	temp = a + b
	a = b
	b = temp
	if temp % 2 == 0:
		sum += temp
		
print(str(sum))