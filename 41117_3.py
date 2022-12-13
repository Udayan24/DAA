# 41117 - Udayan Chavan - P1
# Write a program to solve a 0-1 Knapsack problem using dynamic programming
# --------------------------------
def knapSack(Capacity, Weights, Values, n):
	# Create a table K
	K = [[0 for x in range(Capacity + 1)] for x in range(n + 1)]

	# Build the table in bottom up manner
	for i in range(n + 1):
		for w in range(Capacity + 1):
			if i == 0 or w == 0:
				K[i][w] = 0

			elif Weights[i-1] <= w:
				K[i][w] = max(Values[i-1] + K[i-1][w-Weights[i-1]], K[i-1][w])

			else:
				K[i][w] = K[i-1][w] 
	
	# Print the table
	for i in K:
		print(i)

	return K[n][Capacity]

# --------- TEST CASE 1 ---------
Values = [60, 100, 120]
Weights = [1, 2, 3]
Capacity = 5

n = len(Values)
# --------- OUTPUT ---------
maxValue = knapSack(Capacity, Weights, Values, n)
print("\nValues: ", Values)
print("Weights: ", Weights)
print("\nMaximum Total Value:", maxValue)