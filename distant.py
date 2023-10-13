#1

def evenOdd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(evenOdd(5))

#2

def multiply(a, b):
    i = a * b
    return i
print(multiply(4,5))

#3

def positive_sum(arr):
    positiveSum = 0
    for i in arr:
        if i >= 0:
            positiveSum += i
    return positiveSum
print(positive_sum([1, 2, -3, 7]))

#4

def make_negative( number ):
    return -abs(number)

#5

def evenOdd(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'
print(evenOdd(5))
