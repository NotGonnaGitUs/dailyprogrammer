def fruits(x,y):
	sum = 0;
	week = 1;
	while sum < x:
		y += sum
		sum += y
		week += 1
		
	print week;
	
f = open('input.txt')
for line in f:
	fruits( int(line.split(" ")[0]), int(line.split(" ")[1]) )

f.close()