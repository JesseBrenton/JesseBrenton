
# CSC500 Mod3 Part 1:  Bill + Tip + Tax
# need float input for the bill
bill = float(input("How much is the bill? "))
tax = round(bill*.07,2)
print("7% Sales Tax = ",tax)
tip = bill*.18
# combined round with print just to try something different
print("18% tip (on total pre-tax) = ",round(tip,2))
total = bill + tax + tip
total = round(total,2)
print("Total = ",total)