def check_parentheses(strings):
    results = []
    for s in strings:
        markers = [' '] * len(s)  # Initialize markers with spaces
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    markers[i] = '?'

        while stack:
            markers[stack.pop()] = 'x'

        results.append(s)
        results.append(''.join(markers))

    return results


# Collect user input
input_strings = []
print("Enter your test cases, one per line. Double Enter to finish :")

while True:
    user_input = input()
    if user_input == '':
        break
    input_strings.append(user_input)

# Check parentheses
output = check_parentheses(input_strings)

# Print output
for line in output:
    print(line)
