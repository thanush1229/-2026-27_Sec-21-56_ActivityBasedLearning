# Case Study 37: Nested Loop Calendar Generator

## 1. Problem Statement
Given the weekday on which a month starts and the number of days in the month, print a neatly aligned calendar with weeks as rows and Monday to Sunday as columns.

## 2. Objectives
- Use nested loops (weeks and weekdays) to generate a table.
- Align numbers with string methods (rjust) so columns line up.
- Place blank cells before the first day of the month.
- Validate the weekday (1-7) and number of days (28-31).
- Avoid printing empty rows at the end.

## 3. Assumptions
- Weekdays are numbered 1 = Monday ... 7 = Sunday; the week starts on Monday.
- A month has 28 to 31 days.
- At most 6 week rows are needed for any month.
- Month name and year are not required for the output.

## 4. Algorithm
1. Read the start weekday and the number of days.
2. If the weekday is outside 1-7 or the days outside 28-31, print an error and stop.
3. Print the header Mo Tu We Th Fr Sa Su.
4. Set day = 1. For week 0 to 5: set line to empty.
5. For col 1 to 7: if week is 0 and col < start, add four blank spaces; else if day <= days, add the day number (right-aligned) and increase day.
6. After the inner loop, print the line if it is not empty.

## 5. Pseudocode
```text
START
READ start, days
IF start < 1 OR start > 7 OR days < 28 OR days > 31 THEN PRINT error ; STOP
PRINT header "Mo Tu We Th Fr Sa Su"
day <- 1
FOR week <- 0 TO 5
    line <- ""
    FOR col <- 1 TO 7
        IF week = 0 AND col < start THEN
            line <- line + blank cell
        ELSE IF day <= days THEN
            line <- line + day (width 2) ; day <- day + 1
        END IF
    END FOR
    IF line is not empty THEN PRINT line
END FOR
END
```

## 6. Flowchart
![Flowchart for Case Study 37](images/case37_flowchart.png)

## 7. Python Source Code
File: `programs/case37_calendar_generator.py`

```python
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
```

## 8. Test Cases
| ID | Input / Scenario | Expected Output |
|----|------------------|-----------------|
| T1 | start = 3 (Wed), days = 31 | 1 appears under We; 5 rows; last row 27-31 |
| T2 | start = 7 (Sun), days = 30 | 1 appears under Su; 6 rows; last row contains only 30 |
| T3 | start = 1 (Mon), days = 28 | Exactly 4 full rows (1-7, 8-14, 15-21, 22-28), no blank cells |
| T4 | start = 5 (Fri), days = 31 | 1 under Fr; 5 rows; last row 25-31 |
| T5 | start = 8, days = 30 | Error: weekday must be between 1 and 7 |
| T6 | start = 3, days = 32 | Error: a month has 28 to 31 days |

*Run the program and type the input shown in the table.*

## 9. Sample Output
Full output saved in `outputs/case37_calendar_generator_output.txt`.

```text
--- Input: 3 | 31 ---
Weekdays: 1=Mon 2=Tue 3=Wed 4=Thu 5=Fri 6=Sat 7=Sun
Enter weekday on which the 1st falls (1-7): Enter number of days in the month (28-31): 
Mo  Tu  We  Th  Fr  Sa  Su
         1   2   3   4   5
 6   7   8   9  10  11  12
13  14  15  16  17  18  19
20  21  22  23  24  25  26
27  28  29  30  31

--- Input: 7 | 30 ---
Weekdays: 1=Mon 2=Tue 3=Wed 4=Thu 5=Fri 6=Sat 7=Sun
Enter weekday on which the 1st falls (1-7): Enter number of days in the month (28-31): 
Mo  Tu  We  Th  Fr  Sa  Su
                         1
 2   3   4   5   6   7   8
 9  10  11  12  13  14  15
16  17  18  19  20  21  22
23  24  25  26  27  28  29
30

--- Input: 1 | 28 ---
Weekdays: 1=Mon 2=Tue 3=Wed 4=Thu 5=Fri 6=Sat 7=Sun
Enter weekday on which the 1st falls (1-7): Enter number of days in the month (28-31): 
Mo  Tu  We  Th  Fr  Sa  Su
 1   2   3   4   5   6   7
 8   9  10  11  12  13  14
15  16  17  18  19  20  21
22  23  24  25  26  27  28

--- Input: 5 | 31 ---
Weekdays: 1=Mon 2=Tue 3=Wed 4=Thu 5=Fri 6=Sat 7=Sun
Enter weekday on which the 1st falls (1-7): Enter number of days in the month (28-31): 
Mo  Tu  We  Th  Fr  Sa  Su
                 1   2   3
 4   5   6   7   8   9  10
11  12  13  14  15  16  17
18  19  20  21  22  23  24
25  26  27  28  29  30  31

--- Input: 8 | 30 ---
Weekdays: 1=Mon 2=Tue 3=Wed 4=Thu 5=Fri 6=Sat 7=Sun
Enter weekday on which the 1st falls (1-7): Enter number of days in the month (28-31): Error: weekday must be between 1 and 7

--- Input: 3 | 32 ---
Weekdays: 1=Mon 2=Tue 3=Wed 4=Thu 5=Fri 6=Sat 7=Sun
Enter weekday on which the 1st falls (1-7): Enter number of days in the month (28-31): Error: a month has 28 to 31 days
```

## 10. Output Screenshot
> Add your own terminal screenshot as `docs/screenshots/case37_calendar_generator_output.png` and the image below will appear:
>
> `![Output screenshot](screenshots/case37_calendar_generator_output.png)`

## 11. Conclusion
The calendar is produced entirely with nested loops and simple counters. The test cases cover the shortest month, the longest layout (six rows) and invalid inputs, showing that alignment and validation both work.
