# Case Study 29: Password Policy Validation Engine
# Uses: strings, loops, conditionals, lists

SPECIALS = "!@#$%^&*"
PROHIBITED = ["password", "admin", "1234", "qwerty"]
MIN_LENGTH = 8

print("Password Policy Validator (type 'quit' to stop)")
pwd = input("Enter password: ")

while pwd != "quit":
    failed = []
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False
    repeat = False

    for i in range(len(pwd)):
        ch = pwd[i]
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SPECIALS:
            has_special = True
        if ch == " ":
            has_space = True
        # three identical characters in a row
        if i >= 2 and pwd[i] == pwd[i - 1] and pwd[i] == pwd[i - 2]:
            repeat = True

    if len(pwd) < MIN_LENGTH:
        failed.append("Too short: needs at least 8 characters (has " + str(len(pwd)) + ")")
    if not has_upper:
        failed.append("Missing an uppercase letter")
    if not has_lower:
        failed.append("Missing a lowercase letter")
    if not has_digit:
        failed.append("Missing a digit")
    if not has_special:
        failed.append("Missing a special character (!@#$%^&*)")
    if has_space:
        failed.append("Spaces are not allowed")
    if repeat:
        failed.append("Same character repeated 3 or more times in a row")
    for word in PROHIBITED:
        if word in pwd.lower():
            failed.append("Contains prohibited text '" + word + "'")

    if len(failed) == 0:
        print("  RESULT: STRONG - all rules satisfied")
    else:
        print("  RESULT: WEAK -", len(failed), "rule(s) failed")
        for f in failed:
            print("   x", f)
    pwd = input("Enter password: ")

print("Goodbye!")
