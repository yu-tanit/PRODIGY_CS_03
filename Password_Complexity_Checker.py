import re

def check_password_strength(password):
    # Criteria for assessing password strength
    length = len(password) >= 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.match(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assess password strength based on criteria
    strength = 0
    if length:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    
    if strength == 5:
        print("Password is very strong.")
    elif strength >= 3:
        print("Password is strong.")
    elif strength >= 2:
        print("Password is moderate.")
    else:
        print("Password is weak. Please consider a stronger password.")

if __name__ == "__main__":
    main()
