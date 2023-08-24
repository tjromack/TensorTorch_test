import tensorflow as tf

# Creating a tensor
tensor_tf = tf.constant([[1, 2], [3, 4]])
print(tensor_tf)

# Basic operations
addition_tf = tensor_tf + tensor_tf
print(addition_tf)

# Multiplication
multiplication_tf = tensor_tf * 5
print(multiplication_tf)

# Using functions
square_tf = tf.square(tensor_tf)
print(square_tf)
