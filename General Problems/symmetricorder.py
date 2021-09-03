n = int(input())

set_num = 1

while not n == 0:
	new_list1 = []
	new_list2 = []
	for i in range(n):
		name = input()
		if i % 2 == 0:
			new_list1.append(name)
		else:
			new_list2.insert(0, name)

	new_list = new_list1 + new_list2
	print("SET", set_num)
	for name in new_list:
		print(name)

	set_num += 1
	n = int(input())