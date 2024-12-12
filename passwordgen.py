import random
import string

def generate_strong_password(length=12):
    # Define the character sets to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure each generated password meets certain criteria
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Check if the password meets the criteria (at least one of each: uppercase, lowercase, digit, punctuation)
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)):
            break
    
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_strong_password(password_length)
    print(f"Generated Strong Password: {generated_password}")
