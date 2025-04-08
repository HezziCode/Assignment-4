# def mars_weight():
#     weight = float(input("Enter your weight on Earth : "))
#     mars_weight = weight * 0.378
#     rounded_weight : float = round(mars_weight, 2)
#     print(f"Your weight on Mars is {rounded_weight} kg")

# mars_weight()

GRAVITY_RATIO: dict = {
    "mercury": 37.6,
    "venus": 88.9,
    "mars": 37.8,
    "jupiter": 236.0,
    "saturn": 108.1,
    "uranus": 81.5,
    "neptune": 114.0
}

def calculate_weight_on_planet():
    try:
        weight_on_earth = float(input("Enter your weight on Earth (kg): ")) 
        destination_planet = input("Enter the planet you want to visit: ").strip().lower()
        
        if destination_planet in GRAVITY_RATIO:
            weight_on_planet = (weight_on_earth * GRAVITY_RATIO[destination_planet]) / 100
            rounded_weight: float = round(weight_on_planet, 2)
            print(f"\nYour weight on {destination_planet.capitalize()} would be: {rounded_weight} kg.\n")
        else:
            print("\nError: Please check your spelling or enter a valid planet name.\n")
    
    except ValueError: 
        print("\nError: Please enter a valid numeric weight.\n")

calculate_weight_on_planet()
