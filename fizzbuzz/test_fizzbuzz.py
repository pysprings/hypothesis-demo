"""
FizzBuzz: Create a function that can take integers from 1 to 100 and will
return:
    Fizz if the number is divisible by 3
    Buzz if the number is divisible by 5
    FizzBuzz if the number is divisible by 3 and 5
    Otherwise return the number
"""


from hypothesis import assume, given, strategies as st
from fizzbuzz import fizzbuzz

@given(st.integers())
def test_fizzbuzz(i):
    if i % 3 == 0 and i % 5 ==0: #divisible by both 5 and 3
        assert fizzbuzz(i) == 'FizzBuzz'
    elif i % 3 == 0: # i divisible by 3
        assert fizzbuzz(i) == 'Fizz'
    elif i % 5 == 0: # i divisible by 5
        assert fizzbuzz(i) == 'Buzz'
