# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple():
    number = 1
    while True:
        for i in range(1, 21):
            if number % i == 0:
                if i == 20:
                    return number
                continue
            else:
                number += 1
                break


print(smallest_multiple())
