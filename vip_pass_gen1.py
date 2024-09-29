import random
import string
import datetime
import os

# Function to generate a random password
def generate_password(length, use_numbers, use_alphabets, use_symbols):
    characters = ''
    if use_numbers:
        characters += string.digits
    if use_alphabets:
        characters += string.ascii_uppercase  # Only uppercase for the key generator
    if use_symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate redeem code-like password
def generate_key_gen():
    segments = []
    for _ in range(4):  # Create 4 segments
        segment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))  # Each segment 4 chars
        segments.append(segment)
    return '-'.join(segments)  # Join segments with dashes

# Function to log the generated password
def log_password(password, password_type):
    log_file = 'password_log.txt'
    
    if not os.path.isfile(log_file):
        with open(log_file, 'w') as f:
            f.write("Password Log\n")
            f.write("Type, Password, Date & Time\n")
    
    with open(log_file, 'a') as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{password_type}, {password}, {timestamp}\n")

def main():
    print("PASSWORD GENERATOR")
    print("Current Date & Time:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    while True:
        print("\nSELECT OPTION")
        print("1. NUMBERS")
        print("2. ALPHABET")
        print("3. NUMBERS AND ALPHABET")
        print("4. MIX GEN (NUMBERS, ALPHABET, SYMBOLS)")
        print("5. KEY GEN (REDEEM CODE FORMAT)")
        print("6. EXIT")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            length = int(input("Enter length (4-50): "))
            password = generate_password(length, use_numbers=True, use_alphabets=False, use_symbols=False)
            log_password(password, "Numbers")
        
        elif choice == '2':
            length = int(input("Enter length (4-50): "))
            password = generate_password(length, use_numbers=False, use_alphabets=True, use_symbols=False)
            log_password(password, "Alphabet")
        
        elif choice == '3':
            length = int(input("Enter length (4-50): "))
            password = generate_password(length, use_numbers=True, use_alphabets=True, use_symbols=False)
            log_password(password, "Numbers and Alphabet")
        
        elif choice == '4':
            length = int(input("Enter length (4-50): "))
            password = generate_password(length, use_numbers=True, use_alphabets=True, use_symbols=True)
            log_password(password, "MIX GEN")
        
        elif choice == '5':
            password = generate_key_gen()  # Generate redeem code
            log_password(password, "KEY GEN (Redeem Code)")
        
        elif choice == '6':
            print("THANKS FOR USING ME GOOD BYE...")
            print("Created by @siestaa_1")
            break
        
        else:
            print("Invalid choice. Please try again.")
            continue

        # Display success message
        print("\033[92mPASSWORD GENERATED SUCCESSFULLY:\033[0m", password)

        # Prompt for continuing or exiting
        continue_choice = input("Do you want to use the tool again? (Y/N): ").strip().upper()
        if continue_choice != 'Y':
            print("THANKS FOR USING ME GOOD BYE...")
            print("Created by @siestaa_1")
            break

if __name__ == "__main__":
    main()
