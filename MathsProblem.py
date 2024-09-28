total = 0

# Iterate over possible differences 'i'
for i in range(1, 100):  # 'i' defines the difference in the arithmetic sequence
    for j in range(0, 100):  # 'j' defines the starting point of the sequence
        new = []
        for k in range(5):
            # Generate the sequence, keeping numbers as strings
            new.append(f"{(k * i) + j:02}")  # Format to ensure two digits with leading zeros if needed

        # Check if any number in the sequence exceeds 99 (since we're formatting to 2 digits)
        if any(int(num) > 99 for num in new):
            continue

        # Convert numbers to strings and concatenate them
        test = ''.join(new)

        # Check if the concatenated string is exactly 10 digits long
        # and contains all digits '0' to '9' exactly once
        if len(test) == 10 and set(test) == set('0123456789'):
            print("Valid sequence:", new)  # Output the valid sequence
            total += sum(int(num) for num in new)  # Sum the sequence

# Output the final total
print("Final total:", total)
