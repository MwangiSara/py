counter = 1
# while loop from counter = 1 to 10
while counter <= 10:
    print(counter)
    counter = counter + 1

outer_count = 1

while outer_count <= 3:
    print(f"Outer Loop - Iteration {outer_count}")

    inner_count = 1

    for letter in ['a', 'b', 'c']:
        print(f"  Inner Loop - Iteration {inner_count}, Letter: {letter}")
        inner_count += 1

    outer_count += 1