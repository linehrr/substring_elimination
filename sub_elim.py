#!/usr/bin/python

counter = int(raw_input())

global x,y

def getYtype(y):
	char_list = {}
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



def run():
	offset = 0
	last_offset = -1
	count = 0

	type = getYtype(y)
	print type

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
				min1,direction = find_min(offset,y[0],y[-1])
				count += min1
				if (direction):
					offset += min1
				else:
				 	offset += 1
			elif type == 1:
				dup_length = find_dup(offset, y[0])
				count += dup_length - len(y) + 1;
				offset += dup_length;


	print(count)

for i in range(counter):
	x,y = raw_input().split()
	run()


