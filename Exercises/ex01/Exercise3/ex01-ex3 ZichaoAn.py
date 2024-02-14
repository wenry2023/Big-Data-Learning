from functools import reduce

text = {1: "welcome to the World", 2: "of Big Big Data", 3: "welcome world Bye"}

# Concatenate all the text values into a single string
concatenated_text = ' '.join(text.values())

# Split the concatenated text into a list of words
tempList = concatenated_text.split()

# Map function to calculate length of each word
def map_func(word):
    return (len(word), 1)

# Apply map function to each word
shuffle = list(map(map_func, tempList))
print(shuffle)
# Reduce function to sum up lengths and count of words
def reduce_func(x, y):
    total_length = x[0] + y[0]
    total_words = x[1] + y[1]
    return (total_length, total_words)

# Apply reduce function to calculate total length and total words
output = reduce(reduce_func, shuffle)

# Calculate average length
average_length = output[0] / output[1]

print("Total length of words:", output[0])
print("Total number of words:", output[1])
print("Average length of words:", average_length)
