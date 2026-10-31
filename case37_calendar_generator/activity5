# Case Study 37: Nested Loop Calendar Generator
# Uses: nested loops, conditionals, strings, input validation

print("Weekdays: 1=Mon 2=Tue 3=Wed 4=Thu 5=Fri 6=Sat 7=Sun")
start = int(input("Enter weekday on which the 1st falls (1-7): "))
days = int(input("Enter number of days in the month (28-31): "))

if start < 1 or start > 7:
    print("Error: weekday must be between 1 and 7")
elif days < 28 or days > 31:
    print("Error: a month has 28 to 31 days")
else:
    print()
    print("Mo  Tu  We  Th  Fr  Sa  Su")
    day = 1
    for week in range(6):                 # a month needs at most 6 week rows
        line = ""
        for col in range(1, 8):           # columns 1..7 = Mon..Sun
            if week == 0 and col < start:
                line = line + "    "      # blank cells before the 1st
            elif day <= days:
                line = line + str(day).rjust(2) + "  "
                day = day + 1
            # after the last day nothing is added
        if line.strip() != "":            # skip completely empty rows
            print(line.rstrip())
