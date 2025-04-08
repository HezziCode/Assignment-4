c = 299792458  
while True:
    try:
        m = float(input("Enter kilos of mass: "))
        break
    except ValueError:
        print("Please enter a valid number")

E = m * c**2
print("\ne = m * c^2...")
print(f"m = {m} kg")
print(f"c = {c} m/s")
print(f"Energy = {E} Joules")
