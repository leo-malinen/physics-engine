def calculate_force(mass, acceleration):
    """
    Calculate force using Newton's second law of motion.
    
    Parameters:
    mass (float): Mass in kilograms
    acceleration (float): Acceleration in meters per second squared
    
    Returns:
    float: Force in newtons
    """
    return mass * acceleration

def calculate_kinetic_energy(mass, velocity):
    """
    Calculate kinetic energy.
    
    Parameters:
    mass (float): Mass in kilograms
    velocity (float): Velocity in meters per second
    
    Returns:
    float: Kinetic energy in joules
    """
    return 0.5 * mass * velocity ** 2

def calculate_potential_energy(mass, height, gravity=9.81):
    """
    Calculate potential energy.
    
    Parameters:
    mass (float): Mass in kilograms
    height (float): Height in meters
    gravity (float, optional): Acceleration due to gravity in meters per second squared. Default is 9.81.
    
    Returns:
    float: Potential energy in joules
    """
    return mass * gravity * height

def calculate_series_resistance(resistances):
    """
    Calculate total resistance in a series circuit.
    
    Parameters:
    resistances (list of float): List of resistances in ohms
    
    Returns:
    float: Total resistance in ohms
    """
    return sum(resistances)

def main():
    # Example usage
    mass = 10  # in kilograms
    acceleration = 5  # in meters per second squared
    velocity = 3  # in meters per second
    height = 2  # in meters
    resistances = [10, 20, 30]  # in ohms

    force = calculate_force(mass, acceleration)
    kinetic_energy = calculate_kinetic_energy(mass, velocity)
    potential_energy = calculate_potential_energy(mass, height)
    total_resistance = calculate_series_resistance(resistances)

    print(f"Force: {force} N")
    print(f"Kinetic Energy: {kinetic_energy} J")
    print(f"Potential Energy: {potential_energy} J")
    print(f"Total Resistance in Series Circuit: {total_resistance} Ω")

if __name__ == "__main__":
    main()
