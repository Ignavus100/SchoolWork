row = []
found = False
Magic = True

# Taking input
while not found:
    line = input().strip()
    if "#" in line:
        found = True
    else:
        row.append(list(map(int, line.split())))

size = len(row)

# The sum of the first row is the number to be matched
number = sum(row[0])

# Check rows and columns
for i in range(size):
    # Check row sum
    if sum(row[i]) != number:
        Magic = False
        break

    # Check column sum
    column_sum = 0
    for j in range(size):
        column_sum += row[j][i]

    if column_sum != number:
        Magic = False
        break

# Check main diagonal sum
if Magic:
    main_diagonal_sum = sum(row[i][i] for i in range(size))
    if main_diagonal_sum != number:
        Magic = False

# Check anti-diagonal sum
if Magic:
    anti_diagonal_sum = sum(row[i][size-1-i] for i in range(size))
    if anti_diagonal_sum != number:
        Magic = False

if Magic:
    print("is magic")
else:
    print("is not magic")
