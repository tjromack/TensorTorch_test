import tensorflow as tf

# Create a dataset
dataset = tf.data.Dataset.from_tensor_slices([1, 2, 3, 4, 5])

# Transform the dataset
dataset = dataset.map(lambda x: x * 2).shuffle(buffer_size=5).batch(2)

for item in dataset:
    print(item.numpy())
