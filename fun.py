add = lambda x, y: x + y
print(add(2, 3))  

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter(is_even, numbers)

print(list(filtered_numbers))  


def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)

print(list(doubled_numbers))  



def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)

print(sum_of_numbers)  

