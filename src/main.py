import Points as p
import IO
import ClosestPair as cp
import time


# Main begin
IO.art()
IO.welcome()

while(True):     
	run = IO.getChoices(['Start', 'Exit'], 'action')
	
	print("Input format:")
	print("N D							\{N is the number of points, and D is the dimension of the points\}")
	print("X1_1 X1_2 X1_3 ... X1_D")
	print("X2_1 X2_2 X2_3 ... X2_D")
	print("...")
	print("XN_1 XN_2 XN_3 ... XN_D		\{where Xi_j represents the value of i-th point in j-th dimension\}")

	if (run == 1):
		# # boolean flag to mark input failure
		# failFlag = False

		choice = IO.getChoices(['Console', 'Random', 'File'], 'input mode')

		if (choice == 1):
			n, dim = IO.initPointsInput()
			points = [None for _ in range(n)]
			i = 0
			while(i < n):
				while(True):
					tempIn = IO.realInput(n=dim)
					if(tempIn != None):
						break
				points[i] = tempIn
				i += 1

		elif (choice == 2):
			n, dim = IO.initPointsInput()
			points = p.generateRandomPoints(n, dim, -1e6, 1e6)

		else:	# choice == 3
			print("File format follows the input format")
			temp = IO.fileToPoints()
			if(temp == None):
				print("file read error, returning to menu.\n")
				continue
			n = temp[0]
			dim = temp[1]
			points = temp[2]

		# p.sort(points)

		runMode = IO.getChoices(["Divide and Conquer Algorithm", "Brute-force Algorithm", "Run both algorithm (benchmark)"], "run mode")

		if(runMode == 1 or runMode == 3):
			start = time.time()
			DNCresult = cp.findNearestPair(points)
			end = time.time()

			print('Divide and Conquer getDistance() calls count :', p.counter.count)
			print('Divide and Conquer execution time:', (end - start) * (10 ** 3), 'ms')
			print('\n')

			print(f"Closest points distance = {DNCresult[0]}")
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
			print('\n')

			print(f"Closest points distance = {BFresult[0]}")
			if(dim == 3):
				IO.plot3DPoints(points, BFresult[1][0], BFresult[1][1])
			elif(dim == 2):
				IO.plot2DPoints(points, BFresult[1][0], BFresult[1][1])

	else:
		break
# End while

# -- Main program ends --