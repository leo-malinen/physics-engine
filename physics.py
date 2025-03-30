import numpy as np

# Calculates force using mass and acceleration
def calculate_force(mass, acceleration):
    if mass < 0 or acceleration < 0:
        raise ValueError("Mass and acceleration must be non-negative.")
    return mass * acceleration

# Converts energy from joules to volts
def joules_to_volts(joules):
    return joules * 6.242e+18

# Calculates kinetic energy using mass and velocity
def calculate_kinetic_energy(mass, velocity):
    if mass < 0 or velocity < 0:
        raise ValueError("Mass and velocity must be non-negative.")
    return 0.5 * mass * velocity ** 2

# Calculates potential energy using mass, height, and gravity
def calculate_potential_energy(mass, height, gravity=9.81):
    if mass < 0 or height < 0:
        raise ValueError("Mass and height must be non-negative.")
    return mass * gravity * height

# Calculates total resistance for resistors in series
def calculate_series_resistance(resistances):
    if any(r < 0 for r in resistances):
        raise ValueError("Resistances must be non-negative.")
    return np.sum(resistances)

# Calculates torque using force and distance
def calculate_torque(force, distance):
    if force < 0 or distance < 0:
        raise ValueError("Force and distance must be non-negative.")
    return force * distance

def main():
    import logging
    logging.basicConfig(level=logging.INFO)
    
    try:
        mass = 10
        acceleration = 5
        velocity = 3
        height = 2
        resistances = [10, 20, 30]
        distance = 4

        force = calculate_force(mass, acceleration)
        kinetic_energy = calculate_kinetic_energy(mass, velocity)
        potential_energy = calculate_potential_energy(mass, height)
        total_resistance = calculate_series_resistance(resistances)
        torque = calculate_torque(force, distance)

        logging.info(f"Force: {force} N")
        logging.info(f"Kinetic Energy: {kinetic_energy} J")
        logging.info(f"Potential Energy: {potential_energy} J")
        logging.info(f"Total Resistance: {total_resistance} Ω")
        logging.info(f"Torque: {torque} Nm")
    
    except ValueError as e:
        logging.error(e)

if __name__ == "__main__":
    main()
