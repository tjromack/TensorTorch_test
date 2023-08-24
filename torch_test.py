import torch

# Creating a tensor
tensor_pt = torch.tensor([[1, 2], [3, 4]])
print(tensor_pt)

# Basic operations
addition_pt = tensor_pt + tensor_pt
print(addition_pt)

# Multiplication
multiplication_pt = tensor_pt * 5
print(multiplication_pt)

# Using functions
square_pt = torch.square(tensor_pt)
print(square_pt)
