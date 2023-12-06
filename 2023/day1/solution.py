fstream = open("input.txt")
puzzle_input = fstream.read().split("\n")
fstream.close()

numbers = '0123456789'

# part 1 solution
total = 0
for line in puzzle_input:
    if len(line) == 0:
        continue
    this_number = ""
    for c in line:
        if c in numbers:
            this_number = c
            break
    for c in line[::-1]:
        if c in numbers:
            this_number = this_number + c
            break
    total += int(this_number)
print("First answer:", total)

# part 2 solution
real_numbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
total = 0
for line in puzzle_input:
    if len(line) == 0:
        continue
    this_number = ""

    lowest_index = len(line)
    for n in numbers:
        if n not in line:
            continue
        current_index = line.index(n)
        if current_index < lowest_index:
            lowest_index = current_index
            this_number = n
    for n in real_numbers:
        if n not in line:
            continue
        current_index = line.index(n)
        if current_index < lowest_index:
            lowest_index = current_index
            this_number = real_numbers[n]

    second_digit = ""
    lowest_index = len(line)
    for n in numbers:
        if n not in line:
            continue
        current_index = line[::-1].index(n)
        if current_index < lowest_index:
            lowest_index = current_index
            second_digit = n
    for n in real_numbers:
        if n not in line:
            continue
        current_index = line[::-1].index(n[::-1])
        if current_index < lowest_index:
            lowest_index = current_index
            second_digit = real_numbers[n]

    total += int(this_number+second_digit)
print("Second answer:", total)
