def generate_password(length, complexity):
    # Define character sets based on complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Create a character set based on user-defined complexity
    if complexity == 1:
        characters = lowercase_letters
    elif complexity == 2:
        characters = lowercase_letters + uppercase_letters
    elif complexity == 3:
        characters = lowercase_letters + uppercase_letters + digits
    elif complexity == 4:
        characters = lowercase_letters + uppercase_letters + digits + special_characters
    else:
        return "Invalid complexity level."

    # Generate the password by randomly selecting characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length and complexity
try:
    length = int(input("Enter the desired length of the password: "))
    complexity = int(input("Enter the complexity level (1-4):\n"
                           "1. Lowercase letters\n"
                           "2. Lowercase and uppercase letters\n"
                           "3. Lowercase, uppercase letters, and digits\n"
                           "4. Lowercase, uppercase letters, digits, and special characters\n"))
    
    if 1 <= complexity <= 4:
        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
    else:
        print("Invalid complexity level. Please choose a level between 1 and 4.")
except ValueError:
    print("Invalid input. Please enter valid numbers for length and complexity.")