from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
]


def reverse_index(dataset):
    for i in range(len(dataset)):
        dataset[i] = dataset[i].lower()
        dataset[i] = dataset[i].split()
    index_dictionary = {}
    for index, i in enumerate(dataset):
        for j in i:
            if j not in index_dictionary:
                index_dictionary[j] = [index]
            else:
                index_dictionary[j].append(index)
    return index_dictionary

# You can see the output of your function here
print(reverse_index(dataset))
