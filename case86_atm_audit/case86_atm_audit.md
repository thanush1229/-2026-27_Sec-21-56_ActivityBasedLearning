# Case Study 86: Multi-Stage ATM Transaction Audit

## 1. Problem Statement
A simulated bank account processes a sequence of deposits, withdrawals and transfers. The program must keep the balance, reject operations that break the rules, detect suspicious repeated patterns and print an audit summary.

## 2. Objectives
- Process a list of transaction tuples with loops and unpacking.
- Apply several validation rules with chained conditional statements.
- Maintain running totals: balance, daily outflow, accepted and rejected counts.
- Detect repeated patterns by looking back at earlier tuples in the list.
- Print a transaction log and an audit summary.

## 3. Assumptions
- Opening balance is Rs 5000 and the balance must never fall below Rs 500.
- Types: D = deposit, W = withdrawal, T = transfer (needs a 10-digit account number).
- Deposit limit Rs 50,000; each withdrawal/transfer must be a multiple of 100 and at most Rs 3000.
- Total withdrawals plus transfers in the day must not exceed Rs 5000.
- A request is suspicious if it has the same type and amount as the two requests before it (accepted or not).
- All transactions belong to one day.

## 4. Algorithm
1. Set the opening balance and limits; load the transaction list.
2. For each transaction, unpack (type, amount, target).
3. Reject unknown types and non-positive amounts.
4. For deposits, reject amounts above the deposit limit; otherwise add to the balance.
5. For withdrawals/transfers check account number (transfers), multiple of 100, per-transaction limit, daily limit and minimum balance; if all pass, subtract and update the daily total.
6. Compare the current request with the previous two to flag suspicious repeats.
7. Print one log line per transaction and finally the summary.

## 5. Pseudocode
```text
START
balance <- 5000 ; daily_out <- 0 ; accepted <- 0 ; rejected <- 0
FOR i <- 0 TO n-1
    (type, amount, target) <- transaction[i]
    IF type not in {D,W,T} THEN reject
    ELSE IF amount <= 0 THEN reject
    ELSE IF type = D THEN
        IF amount > 50000 THEN reject ELSE balance += amount
    ELSE
        IF type = T AND target is not 10 digits THEN reject
        ELSE IF amount MOD 100 != 0 THEN reject
        ELSE IF amount > 3000 THEN reject
        ELSE IF daily_out + amount > 5000 THEN reject
        ELSE IF balance - amount < 500 THEN reject
        ELSE balance -= amount ; daily_out += amount
    END IF
    update accepted / rejected counters
    IF i >= 2 AND type and amount equal those of i-1 and i-2 THEN flag SUSPICIOUS
    PRINT log line
END FOR
PRINT summary
END
```

## 6. Flowchart
![Flowchart for Case Study 86](images/case86_flowchart.png)

## 7. Python Source Code
File: `programs/case86_atm_audit.py`

```python
# Case Study 86: Multi-Stage ATM Transaction Audit
# Uses: loops, conditionals, lists, tuples, unpacking, strings
# Rules: D=deposit (max 50000)  W=withdraw (multiple of 100, max 3000 each)
#        T=transfer (needs 10-digit account, max 3000 each)
#        daily W+T total <= 5000, balance must stay >= 500
#        suspicious = 3 consecutive requests with same type and amount

balance = 5000
MIN_BALANCE = 500
PER_TXN_LIMIT = 3000
DAILY_LIMIT = 5000
DEPOSIT_LIMIT = 50000

# (type, amount, target_account)
transactions = [
    ("D", 2000, ""),
    ("W", 1000, ""),
    ("W", 1000, ""),
    ("W", 1000, ""),
    ("W", 3500, ""),
    ("W", 1250, ""),
    ("T", 1500, "9876543210"),
    ("T", 800, "12345"),
    ("W", 1000, ""),
    ("D", -200, ""),
    ("X", 100, ""),
    ("W", 500, ""),
    ("D", 60000, ""),
]

daily_out = 0
accepted = 0
rejected = 0
total_dep = 0
total_out = 0
suspicious = []

print("No  Type Amount  Status    Balance  Remark")
for i in range(len(transactions)):
    t_type, amount, target = transactions[i]       # unpacking
    status = "ACCEPTED"
    remark = ""

    if t_type != "D" and t_type != "W" and t_type != "T":
        status = "REJECTED"
        remark = "unknown transaction type"
    elif amount <= 0:
        status = "REJECTED"
        remark = "amount must be positive"
    elif t_type == "D":
        if amount > DEPOSIT_LIMIT:
            status = "REJECTED"
            remark = "deposit limit exceeded"
        else:
            balance += amount
            total_dep += amount
    else:                                          # W or T
        if t_type == "T" and (len(target) != 10 or not target.isdigit()):
            status = "REJECTED"
            remark = "invalid account number"
        elif amount % 100 != 0:
            status = "REJECTED"
            remark = "amount must be a multiple of 100"
        elif amount > PER_TXN_LIMIT:
            status = "REJECTED"
            remark = "per-transaction limit exceeded"
        elif daily_out + amount > DAILY_LIMIT:
            status = "REJECTED"
            remark = "daily limit exceeded"
        elif balance - amount < MIN_BALANCE:
            status = "REJECTED"
            remark = "minimum balance violated"
        else:
            balance -= amount
            daily_out += amount
            total_out += amount

    if status == "ACCEPTED":
        accepted += 1
    else:
        rejected += 1

    # suspicious pattern: this and previous two requests identical
    if i >= 2:
        p1 = transactions[i - 1]
        p2 = transactions[i - 2]
        if t_type == p1[0] and t_type == p2[0] and amount == p1[1] and amount == p2[1]:
            suspicious.append(i + 1)
            remark = remark + " [SUSPICIOUS REPEAT]"

    print(str(i + 1).ljust(3), t_type.ljust(4), str(amount).rjust(6), " ",
          status.ljust(9), str(balance).rjust(7), " ", remark)

print("\n=== SUMMARY ===")
print("Accepted transactions :", accepted)
print("Rejected transactions :", rejected)
print("Total deposited       :", total_dep)
print("Total withdrawn/transferred:", total_out)
print("Final balance         :", balance)
print("Suspicious transaction numbers:", suspicious)
```

## 8. Test Cases
| ID | Input / Scenario | Expected Output |
|----|------------------|-----------------|
| T1 | Deposit 2000 | Accepted, balance 7000 |
| T2 | Three withdrawals of 1000 in a row | All accepted (balance 4000); 3rd flagged SUSPICIOUS (#4) |
| T3 | Withdraw 3500 | REJECTED: per-transaction limit exceeded |
| T4 | Withdraw 1250 | REJECTED: amount must be a multiple of 100 |
| T5 | Transfer 1500 to 9876543210 | Accepted, balance 2500 |
| T6 | Transfer 800 to account 12345 | REJECTED: invalid account number |
| T7 | Withdraw 1000 after Rs 4500 already used | REJECTED: daily limit exceeded |
| T8 | Deposit -200 | REJECTED: amount must be positive |
| T9 | Type X, amount 100 | REJECTED: unknown transaction type |
| T10 | Withdraw 500 (daily total becomes exactly 5000) | Accepted, balance 2000 |
| T11 | Deposit 60000 | REJECTED: deposit limit exceeded |
| T12 | Summary | 6 accepted, 7 rejected, final balance 2000, suspicious list [4] |

*Run the program and type the input shown. For the data-driven programs, the test data is already stored in the program as lists/tuples; edit those lists to try your own cases.*

## 9. Sample Output
Full output saved in `outputs/case86_atm_audit_output.txt`.

```text
No  Type Amount  Status    Balance  Remark
1   D      2000   ACCEPTED     7000   
2   W      1000   ACCEPTED     6000   
3   W      1000   ACCEPTED     5000   
4   W      1000   ACCEPTED     4000    [SUSPICIOUS REPEAT]
5   W      3500   REJECTED     4000   per-transaction limit exceeded
6   W      1250   REJECTED     4000   amount must be a multiple of 100
7   T      1500   ACCEPTED     2500   
8   T       800   REJECTED     2500   invalid account number
9   W      1000   REJECTED     2500   daily limit exceeded
10  D      -200   REJECTED     2500   amount must be positive
11  X       100   REJECTED     2500   unknown transaction type
12  W       500   ACCEPTED     2000   
13  D     60000   REJECTED     2000   deposit limit exceeded

=== SUMMARY ===
Accepted transactions : 6
Rejected transactions : 7
Total deposited       : 2000
Total withdrawn/transferred: 5000
Final balance         : 2000
Suspicious transaction numbers: [4]
```

## 10. Output Screenshot
> Add your own terminal screenshot as `docs/screenshots/case86_atm_audit_output.png` and the image below will appear:
>
> `![Output screenshot](screenshots/case86_atm_audit_output.png)`

## 11. Conclusion
The audit shows how several independent rules can be combined with if-elif chains while keeping running totals correct. The log makes every decision traceable, and the daily-limit and minimum-balance cases confirm that boundaries are handled correctly.
