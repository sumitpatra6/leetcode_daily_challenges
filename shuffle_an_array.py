from random import randint
array = [1,2,3,4,5]



def shuffle(array):
    length = len(array)
    for i in range(length -1, -1, -1):
        j = randint(0, i)
        array[i], array[j] = array[j], array[i]
    print(array)

for i in range(1, 5):
    shuffle(array)
