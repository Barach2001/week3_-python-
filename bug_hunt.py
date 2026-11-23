count = 1
total = 0

# BUG: The while statement was missing a colon, so Python could not parse it.
# BUG: The condition stopped at 4; using count < 6 includes 5 in the sum.
while count < 6:
    total = total + count
    count = count + 1

# BUG: total is an integer, so concatenate it with text using an f-string.
print(f"Sum of 1 to 5 is: {total}")
