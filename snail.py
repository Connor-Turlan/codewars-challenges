def sign(n):
	return 1 if n >= 0 else -1

""" def snail(snail_map):
	output = [snail_map[0][0]]

	x, y = 0, 0
	top, right, bottom, left = 0, 0, 0, 0
	direction = 0
	end_pos = len(snail_map) // 2

	print(output, x, y, end_pos)

	while top < end_pos:
		# move the cursor.
		if direction % 2 == 0:
			x += -sign(direction - 2)
			# change the direction of the cursor.
			if x <= 0 or x >= len(snail_map[0]) - 1:
				if direction == 0:
					top += 1
				direction = (direction + 1) % 4
		else:
			dy = -sign(direction - 2)
			y += dy
			# change the direction of the cursor.
			if (y <= top and dy < 0) or y >= len(snail_map) - 1: 
				if direction == 0:
					right += 1
				direction = (direction + 1) % 4
		
		# get the item at the cursor.
		print(direction, x, y)
		output.append(snail_map[y][x])
	return output """

def cc_rotation(array):
	return [[row[i] for row in array] for i in range(len(array[0])-1, -1, -1)] if array else []

def snail(snail_map):
	output = []
	while snail_map:
		output.extend(snail_map.pop(0))
		snail_map = cc_rotation(snail_map)
	return output;


smol = [[1, 2, 3], 
		[4, 5, 6],
	 	[7, 8, 9]]

print(smol)
print(cc_rotation(smol))

smol = [
		[4, 5, 6],
	 	[7, 8, 9]]

print(smol)
print(cc_rotation(smol))

out = snail(
	[
		[1, 2, 3], 
		[4, 5, 6],
	 	[7, 8, 9]
	]
)

print(out)

print('big')

out = snail(
	[
		[1, 2, 3, 4], 
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 14, 15, 16],
	]
)

print(out)