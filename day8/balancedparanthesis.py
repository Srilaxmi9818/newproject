def is_balanced_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{', '>': '<'}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            # Ignore non-parentheses characters
            continue
    
    return len(stack) == 0

# Test the function
test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}", "<>", "<({[]})>", "((()))", "((())"]
for test_case in test_cases:
    print(f"{test_case}: {is_balanced_parentheses(test_case)}")
