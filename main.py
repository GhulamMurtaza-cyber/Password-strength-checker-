import re


def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # 2. Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # 3. Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # 4. Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>_\-+=/\\[\]]', password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    # 5. Determine password strength
    if score == 4:
        strength = "Strong"
    elif score >= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback


# Main program
print("=" * 40)
print("     PASSWORD STRENGTH CHECKER")
print("=" * 40)

password = input("Enter your password: ")

strength, feedback = check_password_strength(password)

print("\nPassword Strength:", strength)

if strength == "Strong":
    print("Great! Your password is strong.")
else:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)