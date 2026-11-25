def calculate_energy_charge(units):
    if units <= 100:
        charge = units * 5
    elif units <= 200:
        charge = (100 * 5) + ((units - 100) * 7)
    else:
        charge = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    return charge


def calculate_tax(energy_charge):
    return energy_charge * 0.05


def calculate_total_bill(energy_charge, tax):
    return energy_charge + tax


# Input
units = float(input("Enter units consumed: "))

# Calculations
energy_charge = calculate_energy_charge(units)
tax = calculate_tax(energy_charge)
total_bill = calculate_total_bill(energy_charge, tax)

# Display bill
print("\nElectricity Bill")
print("----------------")
print("Units Consumed :", units)
print("Energy Charge  : ₹", energy_charge)
print("Tax (5%)       : ₹", tax)
print("Total Bill     : ₹", total_bill)