import array as arr
numbers_list = [4, 5, 24, 10]
numbers_array = arr.array('i',numbers_list)
print(numbers_array[2:4])
print(numbers_array[:3])
print(numbers_array[2:])
print(numbers_array[:])
