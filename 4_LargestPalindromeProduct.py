# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

a = 100  # Create a variable initialised to 100
b = 100  # Create b variable initialised to 100
palindromes = []  # Create empty array for palindromes to be collected
while a < 1000:  # Begin A while loop to iterate var a
    while b < 1000:  # Begin B while loop to iterate var b
        original = a * b  # Create original variable to hold original calculation of a * b
        number = original  # Create number variable to grab value of original to be reversed to maintain the
        numString = str(number)  # Create numString variable and give it the value of number, converted to a string
        reversedNum = numString[
                      ::-1]  # Create reversedNum variable and use reverse slice to grab each letter from the right to left creating a reversed number
        reversedAsInt = int(
            reversedNum)  # Create a reversedAsInt variable to return reversed number string to an integer
        if reversedAsInt == original:  # Check if reversedAsInt is equal to the original number
            palindromes.append(reversedAsInt)  # If it is, add it to the palindromes array
        b += 1  # Increment b by 1
        # Once B reaches 1000
    b = 100  # Reset b to 100
    a += 1  # Increment a by 1
palindromes.sort()  # Sort the palindromes list from smallest to largest
print(palindromes[-1])  # Print the last (highest) element of the palindromes array
