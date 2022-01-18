new_string = [1, 2, 3, ('a', 33, 52, 'c'), 'abc', 33, '99', '101', 24, [9, '2'], 20]

numbers = []
for i in new_string:
    if isinstance(i, int):
        numbers.append(i)
print(numbers)
    