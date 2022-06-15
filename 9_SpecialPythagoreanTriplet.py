# A Pythagorean triplet is a set of three natural numbers,
# a < b < c, for which,
# a2 + b2 = c2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# Answer:

def is_triple():
    for a in range(200, 1000):
        if a % 100 == 0:
            print(a)
        for b in range(a, 1000):
            for c in range(b, 1000):
                if int(a**2) + int(b**2) == int(c**2):
                    print(f"Pythagorean Triple {a},{b},{c}")
                    if a + b + c == 1000:
                        return f"Final result: {a},{b},{c}"
print(is_triple())
