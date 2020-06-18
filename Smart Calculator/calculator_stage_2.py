while True:
    numbers = input()
    if numbers == '/help':
        print('The program calculates the sum of numbers')
        continue

    if numbers == '/exit':
        print('Bye!')
        break

    if len(numbers) == 0:
        continue

    try:
        numbers = [int(i) for i in numbers.split()]
    except ValueError:
        print(numbers)
        continue

    print(sum(numbers))
