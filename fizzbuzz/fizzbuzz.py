def fizzbuzz(i):
    output = ''
    if i % 3 == 0:
        output += 'Fizz'
    if i % 5 == 0:
        output += 'Buzz'
    return output or i
