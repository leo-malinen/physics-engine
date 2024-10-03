def calculate_force(mass, acceleration):
    """
    Calculate force using Newton's second law of motion.
    F = m * a
    """
    force = mass * acceleration
    return force

def calculate_kinetic_energy(mass, velocity):
    """
    Calculate kinetic energy.
    KE = 0.5 * m * v^2
    """
    kinetic_energy = 0.5 * mass * velocity ** 2
    return kinetic_energy

def calculate_potential_energy(mass, height, gravity=9.81):
    """
    Calculate potential energy.
    PE = m * g * h
    """
    potential_energy = mass * gravity * height
    return potential_energy

def calculate_series_resistance(resistances):
    """
    Calculate total resistance in a series circuit.
    R_total = R1 + R2 + ... + Rn
    """
    total_resistance = sum(resistances)
    return total_resistance

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
