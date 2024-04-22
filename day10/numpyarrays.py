import numpy as np

#EXERCISE SET FOR CREATING ARRAYS


# Create a NumPy array of size 8 filled with zeros
zeros_array = np.zeros(8)

print(zeros_array)

# Generate a NumPy array containing numbers from 10 to 50
numbers_array = np.arange(10, 51)

print(numbers_array)

# Generate a 1D NumPy array containing numbers from 0 to 8
num_array = np.arange(9)

# Reshape the 1D array into a 3x3 matrix
matrix_3x3 = num_array.reshape(3, 3)

print(matrix_3x3)



#Exercise Set for Array Indexing and Slicing

# Extract the third element from the array
print("Third element:",numbers_array[2] )

# Retrieve the second row from the matrix
print("Second row:", matrix_3x3[1])

# Create a 4x4 matrix
matrix_4x4 = np.arange(16).reshape(4, 4)

# Obtain the first two rows
first_two_rows = matrix_4x4[:2, :]

# Obtain the last two columns
last_two_columns = matrix_4x4[:, 2:]

print("First two rows:")
print(first_two_rows)

print("\nLast two columns:")
print(last_two_columns)


#EXERCISE FOR DATATYPES

# Create an array with the elements [1.1, 2.2, 3.3]
original_array = np.array([1.1, 2.2, 3.3])

# Convert the elements to integers
integer_array = original_array.astype(int)

print("Original array:", original_array)
print("Array with elements converted to integers:", integer_array)


# Define an array with the elements ["1", "2", "3"]
orig_array = np.array(["1", "2", "3"])

# Convert the elements to floats
float_array = orig_array.astype(float)

print("Original array:", orig_array)
print("Array with elements converted to floats:", float_array)


# Create an array of five random numbers
random_array = np.random.rand(5)

# Make a copy of the original array
copied_array = random_array.copy()

# Change the first element of the original array
random_array[0] = 10

# Print both arrays
print("Original array:", random_array)
print("Copied array:", copied_array)


# Create an array of five random numbers
random_array2 = np.random.rand(5)

# Create a view of the original array
view_array = random_array2.view()

# Change the first element of the view array
view_array[0] = 10

# Print both arrays
print("Original array:", random_array2)
print("View array:", view_array)


#Exercise Set for Array Shape and Reshape

# Create a 2x6 matrix
matrix_2x6 = np.arange(12).reshape(2, 6)
print("Original 2x6 matrix:")
print(matrix_2x6)

# Reshape it into a 3x4 matrix

print("\nReshaped 3x4 matrix:\n",matrix_2x6.reshape(3, 4))

# Create an array of 12 random numbers
random12_array = np.random.rand(12)
print("Original array of 12 random numbers:")
print(random12_array)

# Reshape it into a 3D array of dimensions 2x2x3
reshaped_array = random12_array.reshape(2, 2, 3)
print("\nReshaped 3D array of dimensions 2x2x3:")
print(reshaped_array)

#ARRAY ITERATING

# Create a 3x3 matrix
matrix2_3x3 = np.arange(9).reshape(3, 3)

# Print each element using a nested loop
print("Elements of the 3x3 matrix:")
for row in matrix2_3x3:
    for element in row:
        print(element)


# Create a 3D array of dimensions 2x2x3
array_3D = np.random.rand(2, 2, 3)
print(array_3D)
# Iterate over the 3D array using np.nditer and print each element
print("Elements of the 3D array:")
for element in np.nditer(array_3D):
    print(element)


#ARRAY JOIN

# Create two 1D arrays of different sizes
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6, 7])

# Concatenate the two arrays
concatenated_array = np.concatenate((array1, array2))

print("Concatenated array:", concatenated_array)

# Create two 2D arrays
firstarray = np.array([[1, 2], [3, 4]])
secondarray = np.array([[5, 6], [7, 8]])

# Vertically stack the two arrays
stacked_array = np.vstack((firstarray, secondarray))

print("Vertically stacked array:")
print(stacked_array)


import numpy as np

# Create an array of 10 elements
array = np.arange(10)

# Split it into 3 arrays
split_arrays = np.array_split(array, 3)

print("Original array:", array)
print("Split arrays:", split_arrays)

# Create a 4x4 matrix
matrix2_4x4 = np.arange(16).reshape(4, 4)

# Horizontally split it into 2 equal parts
split_matrix = np.hsplit(matrix2_4x4, 2)

print("Original matrix:")
print(matrix2_4x4)
print("\nSplit matrix:")
print(split_matrix)

#ARRAY SEARCH

# Create an array of 10 elements
arrayx = np.array([2, 7, 3, 8, 6, 1, 9, 4, 5, 10])

# Use np.where to find indices of all elements greater than 5
indices = np.where(arrayx > 5)

print("Original array:", arrayx)
print("Indices of elements greater than 5:", indices)

# Create an array
arraya = np.array([0, 5, 0, 7, 0, 9, 0])

# Use np.nonzero to find all non-zero elements
nonzero_indices = np.nonzero(arraya)

# Print the non-zero elements
nonzero_elements = arraya[nonzero_indices]
print("Non-zero elements:", nonzero_elements)

#ARRAY SORT

# Create a random array of 10 elements
random_array3 = np.random.randint(1, 100, size=10)

# Sort the array in ascending order
sorted_array = np.sort(random_array3)

print("Original array:", random_array3)
print("Sorted array in ascending order:", sorted_array)



# Create a 3x3 matrix
matrixb = np.array([[5, 8, 3],
                   [1, 7, 9],
                   [4, 2, 6]])

# Sort each row in descending order
sorted_matrix = np.sort(matrixb, axis=1)[:, ::-1]

print("Original matrix:")
print(matrixb)
print("\nSorted matrix with rows in descending order:")
print(sorted_matrix)


#ARRAY FILTER

# Create an array of 15 elements from 1 to 15
array15 = np.arange(1, 16)

# Use boolean indexing to filter out all odd numbers
filtered_array = array15[array15 % 2 == 0]

print("Original array:", array15)
print("Filtered array (even numbers only):", filtered_array)

# Given array
array_given = np.array([1, 2, 3, 4, 5, 6])

# Create a filter array that will return only elements greater than 3
filter_array = array_given[array_given > 3]

print("Original array:", array_given)
print("Filtered array (elements greater than 3):", filter_array)


#RANDOM


# Generate an array of 15 random integers from 1 to 100
random_integers = np.random.randint(1, 101, size=15)

print("Array of 15 random integers from 1 to 100:", random_integers)

# Generate a 3x3 matrix with random floats between 0 to 1
random_floats = np.random.rand(3, 3)

print("3x3 matrix with random floats between 0 to 1:")
print(random_floats)

# Create two arrays of the same shape
arrayc = np.array([1, 2, 3, 4])
arrayd = np.array([5, 6, 7, 8])

# Perform element-wise addition
result = arrayc + arrayd

print("Array 1:", arrayc)
print("Array 2:", arrayd)
print("Element-wise addition result:", result)