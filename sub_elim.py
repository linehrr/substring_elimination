counter = int(raw_input())

global x,y
global char_list
char_list = {}

def getYtype(y):
	for i in range(len(y)):
		char = y[i]
		char_list[char] = 1

		if len(char_list.keys()) > 2 :
			return len(char_list.keys())
		elif (i + 1) < len(y) and y.find(char,i + 1) != (i + 1) and len(char_list.keys()) > 1:
			return 3
	return len(char_list.keys())



def find_min(offset,first,last):
	left = 0
	right = 0
	while(abs(offset-left) < len(x) and x[offset-left] == first):
		left += 1
	
	while(abs(offset + right + len(y) - 1) < len(x) and x[offset + right + len(y) - 1] == last):
		right += 1
	
	if left >= right:
		return right,1
	else:
		return left,0
	
def find_dup(offset, indice):
	counter = 0
	while ((offset + counter) < len(x) and x[offset + counter] == indice):
		counter += 1
	return counter

def recursion_find(sub_x):
	location = sub_x.find(y)
	if location < 0:
		return 0 

	try1 = 1 + recursion_find(sub_x[0:location] + sub_x[(location + 1):]) 
		
	if (location + len(y) >= len(sub_x)):
		return 1
	if not sub_x[location + len(y)] in char_list.keys():
		return 1
	try2 = 1 + recursion_find(sub_x[0:(location + len(y))] + (sub_x[(location + len(y) + 1):]))

	if (try1 >= try2):
		return try2
	else:
		return try1

def run():
	offset = 0
	last_offset = -1
	count = 0

	type = getYtype(y)

	while(True):

		if (x.find(y,offset) < 0):
			break
		else:
			offset = x.find(y,offset)

			if type > 2:
				count += 1
				if last_offset != -1 and offset - last_offset < len(y) and offset != 0:
					count -= 1
					last_offset = offset
					offset += len(y) - 1
				else:
					last_offset = offset
				offset += 1
			elif type == 2:
				count = recursion_find(x)
				break
			elif type == 1:
				dup_length = find_dup(offset, y[0])
				count += dup_length - len(y) + 1;
				offset += dup_length;


	print(count)

for i in range(counter):
	x,y = raw_input().split()
	run()

