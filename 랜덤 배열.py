def Create_random_array(n):
    import numpy as np

    size = n*n
    variable = 0
    numpy_array = []

    random_array = np.random.choice(range(1, size + 1), size, replace=False)

    for _ in range(n):
        variable += n
        numpy_array.append(random_array[variable - n : variable])

    numpy_array = np.array(numpy_array)

    return numpy_array

Create_random_array() #여기에 어떤 숫자를 넣는지에 따라 크기가 정해짐 ㅇㅋ?
#print(Create_random_array(7))
# print(type(Create_random_array(7)))