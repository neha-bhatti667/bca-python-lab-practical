import numpy as np

# Lab Sheet 1: Python Libraries and Applications
# Array Creation, Indexing, Operations, File I/O and Random Module

# 1. Multiples of 7 between 7 and 100
print("\n1. Multiples of 7")
arr = np.arange(7, 101, 7)
print(arr)
print("Length:", len(arr))

# 2. A 4x4 array filled with 9
print("\n2. 4x4 array filled with 9")
arr = np.full((4, 4), 9)
print(arr)

# 3. Convert an integer array to float
print("\n3. Integer to float")
arr = np.arange(1, 11)
float_arr = arr.astype(float)
print("Original:", arr, arr.dtype)
print("Converted:", float_arr, float_arr.dtype)

# 4. Compare memory size of a list and a NumPy array
print("\n4. Memory size comparison")
import sys
values = [10, 20, 30, 40, 50]
np_arr = np.array(values)
print("List memory:", sys.getsizeof(values), "bytes")
print("NumPy array memory:", sys.getsizeof(np_arr), "bytes")

# 5. Extract four corner elements from a 6x6 array
print("\n5. Four corner elements")
arr = np.arange(1, 37).reshape(6, 6)
print(arr)
corners = arr[[0, 0, -1, -1], [0, -1, 0, -1]]
print("Corners:", corners)

# 6. Every third element starting from index 1
print("\n6. Every third element from index 1")
arr = np.arange(1, 13)
print(arr[1::3])

# 7. Reverse the rows of a 5x5 array
print("\n7. Reverse row order")
arr = np.arange(1, 26).reshape(5, 5)
print(arr[::-1])

# 8. Replace elements divisible by 3 with -1
print("\n8. Replace multiples of 3")
arr = np.arange(1, 16)
arr[arr % 3 == 0] = -1
print(arr)

# 9. Normalize values between 0 and 1
print("\n9. Normalize an array")
arr = np.array([10, 20, 30, 40, 50])
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print(normalized)

# 10. Transpose a matrix and check the double transpose
print("\n10. Transpose verification")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
transposed = arr.T
print("Transpose:\n", transposed)
print("Double transpose returns original:", np.array_equal(transposed.T, arr))

# 11. Maximum value and its index
print("\n11. Maximum and its index")
arr = np.random.randint(1, 100, 10)
index = np.argmax(arr)
print("Array:", arr)
print("Maximum:", arr[index])
print("Index:", index)

# 12. Element-wise remainder of two arrays
print("\n12. Element-wise remainder")
a = np.array([10, 17, 24, 31])
b = np.array([3, 5, 7, 6])
print(np.remainder(a, b))

# 13. Stack two 2x3 arrays into a 3-D array
print("\n13. Stack arrays")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
stacked = np.stack((a, b))
print(stacked)
print("Shape:", stacked.shape)

# 14. Reshape arrays before concatenating
print("\n14. Reshape and concatenate")
a = np.array([1, 2])
b = np.array([[3, 4]])
c = np.array([5, 6, 7])
combined = np.concatenate((a.reshape(-1), b.reshape(-1), c.reshape(-1)))
print(combined)

# 15. Reshape 16 elements and transpose
print("\n15. Reshape and transpose")
arr = np.arange(1, 17).reshape(4, 4)
print("Original:\n", arr)
print("Transposed:\n", np.transpose(arr))

# 16. Split a 3-D array into two equal parts along the first axis
print("\n16. Split 3-D array")
arr = np.arange(32).reshape(2, 4, 4)
part1, part2 = np.split(arr, 2, axis=0)
print("Part 1:\n", part1)
print("Part 2:\n", part2)

# 17. Split 17 elements into 4 parts
print("\n17. Split into four parts")
arr = np.arange(1, 18)
parts = np.array_split(arr, 4)
for i, part in enumerate(parts, start=1):
    print(f"Part {i}: {part}, size = {part.size}")

# 18. Identify and remove outliers beyond 2 standard deviations
print("\n18. Remove outliers")
arr = np.array([10, 12, 11, 13, 12, 14, 11, 100])
mean = np.mean(arr)
std = np.std(arr)
clean_arr = arr[np.abs(arr - mean) <= 2 * std]
print("Original:", arr)
print("Without outliers:", clean_arr)

# 19. Average marks for each student and each subject
print("\n19. Student and subject averages")
marks = np.array([
    [78, 85, 90, 80],
    [88, 76, 84, 91],
    [69, 72, 75, 70],
    [92, 89, 95, 94],
    [81, 83, 79, 86]
])
print("Student averages:", np.mean(marks, axis=1))
print("Subject averages:", np.mean(marks, axis=0))

# 20. Correlation coefficient between two arrays
print("\n20. Correlation coefficient")
a = np.array([10, 20, 30, 40, 50])
b = np.array([12, 18, 33, 38, 52])
print(np.corrcoef(a, b))

# 21. Save a random 5x5 array to CSV and reload it
print("\n21. Save and reload CSV")
arr = np.random.randint(1, 100, (5, 5))
np.savetxt("random_array.csv", arr, delimiter=",", fmt="%d")
loaded_arr = np.loadtxt("random_array.csv", delimiter=",", dtype=int)
print("Original array:\n", arr)
print("Loaded array:\n", loaded_arr)
print("Arrays match:", np.array_equal(arr, loaded_arr))

# 22. Save three arrays in one NPZ file and list their names
print("\n22. Save and load NPZ file")
a = np.array([1, 2, 3])
b = np.array([[4, 5], [6, 7]])
c = np.array([8, 9, 10, 11])
np.savez("arrays.npz", first=a, second=b, third=c)
with np.load("arrays.npz") as data:
    print("Stored array names:", data.files)

# 23. Random 3x3 matrix from 10 to 50 and sort each row
print("\n23. Sort each row")
arr = np.random.randint(10, 51, (3, 3))
print("Original:\n", arr)
print("Sorted rows:\n", np.sort(arr, axis=1))

# 24. Simulate 200 biased coin flips with 70% chance of heads
print("\n24. Biased coin simulation")
flips = np.random.binomial(1, 0.7, 200)
heads = np.sum(flips)
print("Heads:", heads)
print("Observed proportion of heads:", heads / 200)

# 25. Normal sample and count values outside [-4, 4]
print("\n25. Normal distribution")
values = np.random.normal(0, 2, 2000)
outside = np.sum((values < -4) | (values > 4))
print("Values outside [-4, 4]:", outside)

# 26. Website visits per minute using Poisson distribution
print("\n26. Website visits")
visits = np.random.poisson(lam=5, size=60)
minute = np.argmax(visits) + 1
print("Visits in each minute:", visits)
print("Minute with highest visits:", minute)
print("Highest number of visits:", visits.max())

# 27. Simulate product choices using a multinomial distribution
print("\n27. Product survey")
counts = np.random.multinomial(200, [0.5, 0.3, 0.2])
print("Product 1:", counts[0])
print("Product 2:", counts[1])
print("Product 3:", counts[2])

# 28. Shuffle a deck and deal five cards
print("\n28. Shuffle and deal cards")
deck = np.arange(1, 53)
shuffled_deck = np.random.permutation(deck)
hand = shuffled_deck[:5]
print("Five cards in hand:", hand)
