def main():
	x = 0
	y = 0
	f = ""
	faces = ["NORTH", "north", "SOUTH", "south", "EAST", "east", "WEST", "west"]
	try:
		userInput = input().split()
		place = userInput [0]
		position = userInput[1]

		if place == "place" or place == "PLACE" or place == "Place":
			pass
		else:
			print("Invalid place command place")
			main()

		x = int(position[0])
		y = int(position[2])
		if position[0].isdigit() == True and position[2].isdigit() == True:
			pass
		else:
			print("Invalid place command x")
			main()

		if position[1] == ",":
			pass
		else:
			print("Invalid place command")
			main()

		f = userInput[2]
		if f in faces:
			pass
		else:
			print("Invalid place command f")
			main()

	except:
		print("Input must be initial position")
		print(userInput[2])
		main()
	
	while True:
		movement = input()

		if movement.lower() == "move":
			if f.lower() == "north":
				if y+1 >= y:
					y += 1
				else:
					pass
			
			elif f.lower() == "south":
				if y-1 <= y:
					y -= 1
				else:
					pass
			
			elif f.lower() == "east":
				if x+1 >= x:
					x += 1
				else:
					pass
			
			elif f.lower() == "west":
				if x-1 <= x:
					x -= 1
				else:
					pass
			continue
		
		if movement.lower() == "left":
			if f.lower() == "north":
				f = "WEST"
			elif f.lower() == "south":
				f = "EAST"
			elif f.lower() == "east":
				f = "NORTH"
			elif f.lower() == "west":
				f = "SOUTH"
			continue
		
		if movement.lower() == "right":
			if f.lower() == "north":
				f = "EAST"
			elif f.lower() == "south":
				f = "WEST"
			elif f.lower() == "east":
				f = "SOUTH"
			elif f.lower() == "west":
				f = "NORTH"
			continue
		
		if movement.lower() == "report":
			print('{},{},{}'.format(x, y, f))
			exit()
		else: 
			print("ABRACADABRA")
			continue

main()
