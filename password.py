import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[\W_]', password))

    strength = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    
    if strength == 5:
        return "Very Strong"
    elif strength == 4:
        return "Strong"
    elif strength == 3:
        return "Moderate"
    elif strength == 2:
        return "Weak"
    else:
        return "Very Weak"

def main():
    while True:
        password = input("Enter a password to check its strength: ")
        strength = check_password_strength(password)
        print(f"Password Strength: {strength}")

        check_again = input("Do you want to check another password? (yes/no): ").strip().lower()
        if check_again != 'yes':
            print("Thank you for using the password strength checker!")
            break

if __name__ == "__main__":
    main()
