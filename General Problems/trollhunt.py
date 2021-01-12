	import math

	num_bridges, num_knights, knights_per_group = map(int, input().split())
	num_groups = math.floor(num_knights / knights_per_group)
	print(math.ceil((num_bridges - 1) / num_groups))