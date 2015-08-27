"""If we list all the natural numbers below 10 that are multiples of 3 or 5,
 we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""


def multiples(n):
    return (i for i in range(1, n) if i % 3 == 0 or i % 5 == 0)

print(sum(multiples(1000)))


# print(sum((i for i in range(1000) if i % 3 == 0 or i % 5 == 0)))

# print(sum(set(range(3, 1000, 3)) | set(range(5, 1000, 5))))