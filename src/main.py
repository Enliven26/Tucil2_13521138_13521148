import Points as p
import IO
import ClosestPair as cp
import time


# Main begin
IO.art()
IO.welcome()

while(True):     
	run = IO.getChoices(['Start', 'Exit'], 'action')

	if (run == 1):
		# # boolean flag to mark input failure
		# failFlag = False

		choice = IO.getChoices(['Console', 'Random', 'File'], 'input mode', cancelOpt=True)

		if(choice == 4): # user chose return
			continue
	
		IO.inputFormatInfo(choice)

		if (choice == 1):
			n, dim = IO.initPointsInput()
			points = [None for _ in range(n)]
			i = 0

			print("Input Points")
			while(i < n):
				
				while(True):
					print("Point", i+1, ": ", end="")
					tempIn = IO.realInput(n=dim)
					if(tempIn != None):
						break
				points[i] = tempIn
				i += 1

		elif (choice == 2):
			n, dim = IO.initPointsInput()
			points = p.generateRandomPoints(n, dim, -1e6, 1e6)

		elif (choice == 3):
			print("File format follows the input format")
			temp = IO.fileToPoints()
			if(temp == None):
				print("file read error, returning to menu.\n")
				continue
			n = temp[0]
			dim = temp[1]
			points = temp[2]

		# else:
		# 	continue

		# p.sort(points)

		runMode = IO.getChoices(["Divide and Conquer Algorithm", "Brute-force Algorithm", "Run both algorithm (benchmark)"], "run mode")

		if(runMode == 1 or runMode == 3):
			start = time.time()
			DNCresult = cp.findNearestPair(points)
			end = time.time()

			print('Divide and Conquer getDistance() calls count :', p.counter.count)
			print('Divide and Conquer execution time:', (end - start) * (10 ** 3), 'ms')
			print(f"Closest points distance = {DNCresult[0]}\n")

			if(dim == 3):
				IO.plot3DPoints(points, DNCresult[1][0], DNCresult[1][1])
			elif(dim == 2):
				IO.plot2DPoints(points, DNCresult[1][0], DNCresult[1][1])
	
		if(runMode == 2 or runMode == 3):
			start = time.time()
			BFresult = cp.findNearestPair(points, 1)
			end = time.time()
			print('Brute Force getDistance() calls count :', p.counter.count)
			print('Brute Force execution time:', (end - start) * (10 ** 3), 'ms')
			print(f"Closest points distance = {BFresult[0]}")
			
			if(dim == 3):
				IO.plot3DPoints(points, BFresult[1][0], BFresult[1][1])
			elif(dim == 2):
				IO.plot2DPoints(points, BFresult[1][0], BFresult[1][1])

	else:
		break
# End while

# -- Main program ends --