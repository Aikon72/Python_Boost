arr = [1,0,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0]
new_arr = []
count_one = 0
for i in range (0, len(arr)):
	if arr[i] > 0:
		count_one += 1
	else:
		new_arr.append(count_one)
		count_one = 0
new_arr.append(count_one)
print(new_arr)

index_zero = -1
count_one = 0

for i in range (0, len(new_arr) - 1):
	count_tmp = new_arr[i] + 1 + new_arr[i + 1]
	if count_tmp > count_one:
		count_one = count_tmp
		index_zero = i
print(index_zero)

sum = 0
for i in range (0, index_zero + 1):
	sum += new_arr[i]

index_zero += sum
print(index_zero)