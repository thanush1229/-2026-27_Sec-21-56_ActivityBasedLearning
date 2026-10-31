# Case Study 29: Password Policy Validation Engine

## 1. Problem Statement
Websites require passwords to follow a policy. The program reads password strings from the user and checks them against rules for length, character categories, repetition and prohibited substrings, explaining every rule that a password fails.

## 2. Objectives
- Traverse strings character by character using loops and indexing.
- Use string methods (isupper, islower, isdigit) and the in operator.
- Detect three identical characters in a row.
- Compare against a list of prohibited substrings regardless of letter case.
- Give a separate, readable message for each failed rule.

## 3. Assumptions
- Minimum length is 8 characters.
- Required: an uppercase letter, a lowercase letter, a digit and one special character from !@#$%^&*.
- Spaces are not allowed.
- Three or more identical characters in a row are not allowed.
- Prohibited text (case-insensitive): password, admin, 1234, qwerty.
- The user types quit to stop the program.

## 4. Algorithm
1. Read a password.
2. If it is 'quit', stop.
3. Scan every character and set flags for uppercase, lowercase, digit, special character and space; also check whether the current character equals the two before it.
4. Check length, each flag and the repeat flag; add one message per failure.
5. For each prohibited word, check whether it appears in the lower-case password.
6. If the failure list is empty print STRONG, otherwise print WEAK and every message.
7. Read the next password and repeat.

## 5. Pseudocode
```text
START
READ pwd
WHILE pwd != "quit"
    failed <- empty list ; set all flags to FALSE
    FOR i <- 0 TO length(pwd)-1
        classify pwd[i] and set the matching flag
        IF i >= 2 AND pwd[i] = pwd[i-1] = pwd[i-2] THEN repeat <- TRUE
    END FOR
    IF length < 8 THEN add message
    IF NOT has_upper / has_lower / has_digit / has_special THEN add message
    IF has_space THEN add message
    IF repeat THEN add message
    FOR each word in PROHIBITED
        IF word in lowercase(pwd) THEN add message
    END FOR
    IF failed is empty THEN PRINT "STRONG" ELSE PRINT "WEAK" and all messages
    READ pwd
END WHILE
END
```

## 6. Flowchart
![Flowchart for Case Study 29](images/case29_flowchart.png)

## 7. Python Source Code
File: `programs/case29_password_validation.py`

```python
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
```

## 8. Test Cases
| ID | Input / Scenario | Expected Output |
|----|------------------|-----------------|
| T1 | Abcdef1! | STRONG - all rules satisfied |
| T2 | abc | WEAK, 4 failures: too short (3), no uppercase, no digit, no special |
| T3 | Password123 | WEAK, 2 failures: no special character, prohibited text 'password' |
| T4 | aaaBBB12 | WEAK, 2 failures: no special character, repeated characters |
| T5 | Hello@2024 | STRONG |
| T6 | (empty string) | WEAK, 5 failures (length 0, upper, lower, digit, special) |
| T7 | Ab1! | WEAK, 1 failure: too short (has 4) |
| T8 | Admin@9999x | WEAK, 2 failures: repeated characters, prohibited text 'admin' |
| T9 | Qwerty!23A | WEAK, 1 failure: prohibited text 'qwerty' |
| T10 | Hi there 1A! | WEAK, 1 failure: spaces are not allowed |

*Run the program and type the input shown in the table.*

## 9. Sample Output
Full output saved in `outputs/case29_password_validation_output.txt`.

```text
--- Input: Abcdef1! | abc | Password123 | aaaBBB12 | Hello@2024 |  | Ab1! | Admin@9999x | Qwerty!23A | Hi there 1A! | quit ---
Password Policy Validator (type 'quit' to stop)
Enter password:   RESULT: STRONG - all rules satisfied
Enter password:   RESULT: WEAK - 4 rule(s) failed
   x Too short: needs at least 8 characters (has 3)
   x Missing an uppercase letter
   x Missing a digit
   x Missing a special character (!@#$%^&*)
Enter password:   RESULT: WEAK - 2 rule(s) failed
   x Missing a special character (!@#$%^&*)
   x Contains prohibited text 'password'
Enter password:   RESULT: WEAK - 2 rule(s) failed
   x Missing a special character (!@#$%^&*)
   x Same character repeated 3 or more times in a row
Enter password:   RESULT: STRONG - all rules satisfied
Enter password:   RESULT: WEAK - 5 rule(s) failed
   x Too short: needs at least 8 characters (has 0)
   x Missing an uppercase letter
   x Missing a lowercase letter
   x Missing a digit
   x Missing a special character (!@#$%^&*)
Enter password:   RESULT: WEAK - 1 rule(s) failed
   x Too short: needs at least 8 characters (has 4)
Enter password:   RESULT: WEAK - 2 rule(s) failed
   x Same character repeated 3 or more times in a row
   x Contains prohibited text 'admin'
Enter password:   RESULT: WEAK - 1 rule(s) failed
   x Contains prohibited text 'qwerty'
Enter password:   RESULT: WEAK - 1 rule(s) failed
   x Spaces are not allowed
Enter password: Goodbye!
```

## 10. Output Screenshot
> Add your own terminal screenshot as `docs/screenshots/case29_password_validation_output.png` and the image below will appear:
>
> `![Output screenshot](screenshots/case29_password_validation_output.png)`

## 11. Conclusion
The engine checks each rule independently and so can list every problem at once, instead of stopping at the first. This is more helpful for a user and shows how strings, flags and loops work together in a real validation task.
