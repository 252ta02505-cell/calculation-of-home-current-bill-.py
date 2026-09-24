def calculate_bill(units):
    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = (100 * 1.50) + ((units - 100) * 2.50)
    elif units <= 500:
        bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
    else:
        bill = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.00)

    return bill

# Main program
units = float(input("Enter electricity units consumed: "))
bill = calculate_bill(units)

print(f"Electricity Units: {units}")
print(f"Total Bill: ₹{bill:.2f}")
