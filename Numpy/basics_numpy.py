import numpy as np


python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])

# print(python_list*2)
# print(numpy_array*2)
# print(type(python_list))
# print(type(numpy_array))


# 2D ARRAY


Python_list =[[1, 2, 3],[4, 5, 6],[7, 8, 9]]

numpy_2d_array = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

# print(numpy_2d_array[0:2 ,0:2])
# print(numpy_2d_array)

# print(numpy_2d_array.shape)

# new_array = np.ones((3,3))
# print(new_array)

goals = np.array([8, 6, 7, 5, 9, 4])

# print(np.sum(goals))
# print(np.mean(goals))
# print(np.max(goals))
print(np.min(goals))


print(np.zeros((3, 3)))
print(np.ones((3, 3)))

