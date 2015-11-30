f = open('input.txt', 'r')
for line in f:
	x=int(line)
	y = 1
	sum=0
	dx=2*x

	while y<=x:
		if x%y==0:
			sum+=y
		y+=1

	if sum==dx:
		print x,"perfect"
	elif sum<dx:
		print x,"deficient by",(dx-sum)
	else:
		print x,"abundant by",(sum-dx)
	
f.close()