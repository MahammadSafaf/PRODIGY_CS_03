import re

def check_password_strength(password):
    
    feedback = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should have at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should have at least one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Password should have at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Password should have at least one special character (e.g., !, @, #, etc.).")

    if score == 5:
        return "Password is strong.", feedback
    elif score >= 3:
        return "Password is moderate.", feedback
    else:
        return "Password is weak.", feedback


if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"Password strength: {strength}")
    
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")
