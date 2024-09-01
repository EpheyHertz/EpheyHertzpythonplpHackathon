def reverse_string(s: str) -> str:
    stack = []
    for character in s:
        stack.append(character)

    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

input_str = "hello"
output_str = reverse_string(input_str)
print(output_str)
