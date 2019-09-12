# william Pulkownik
# assignment 1 part 3
# create a list of integers from user input

print('We are collecting a list of 10 integers.')
numbers = []
while (len(numbers) < 10):
    try:
        x = int(input ('enter an integer and press enter:'))
    except ValueError:
        print('Sorry, your entries is not an integer')
        continue
    numbers.append(x)
    continue

print(*numbers, sep=', ')