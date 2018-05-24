def change(cents):
    coins = {
        "dollars": 0,
        "half-dollars": 0,
        "quarters": 0,
        "dimes": 0,
        "nickels": 0,
        "pennies": 0,
    }
    total = 0
    while total + 1 <= cents:
        coins["dollars"] += 1
        total += 1
    
    while total + 0.50 <= cents:
        coins["half-dollars"] += 1
        total += 0.50

    while total + 0.25 <= cents:
        coins["quarters"] += 1
        total += 0.25

    while total + 0.1 <= cents:
        coins["dimes"] += 1
        total += 0.1

    while total + 0.05 <= cents:
        coins["nickels"] += 1
        total += 0.05

    while total + 0.01 <= cents:
        coins["pennies"] += 1
        total += 0.01
    
    return coins

print(change(168.94))