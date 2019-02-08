number=int(input())
if number < 0:
	print("")
else:	
	total = 0
   	while(number > 0):
   		total +=number
   		number -= 1
   	print(total)
