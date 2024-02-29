import re


def check_password_strength(password, min_length=10):
    # Criteria for password strength
    criteria = {
        "length": len(password) >= min_length,
        "digit": re.search(r"\d", password) is not None,
        "uppercase": re.search(r"[A-Z]", password) is not None,
        "lowercase": re.search(r"[a-z]", password) is not None,
        "special_char": re.search(r"[!@#$%^&*()\-_=+[\]{}`~;:'\"\\|,.<>/?]", password) is not None,
        "no_common_patterns": re.search(r"(1234|password|abcd)", password) is None
    }

    strength = all(criteria.values())
    feedback = [k for k, v in criteria.items() if not v]

    return "Strong" if strength else f"Weak, improve on: {', '.join(feedback)}"


# User input
user_password = input("Enter your password to check its strength: ")
strength = check_password_strength(user_password)
print(f"Your password is: {strength}")
