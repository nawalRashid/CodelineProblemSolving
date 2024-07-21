

def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    
    remainders = []
    while decimal_num > 0:
        remainders.append(str(decimal_num % 2))
        decimal_num = decimal_num // 2
    
    remainders.reverse()  # Reverse the list 
    return ''.join(remainders)

# Get input from the user
user_input = int(input("Enter a positive decimal number: "))
binary_output = decimal_to_binary(user_input)

print(f"Input: {user_input}, Output: {binary_output}")
