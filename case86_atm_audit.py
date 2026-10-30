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
