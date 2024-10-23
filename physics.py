import numpy as np

def calculate_force(mass, acceleration):
    #Calculate force using Newton's second law of motion.
    # Parameters: mass (float); Mass in kilograms and acceleration (float); Acceleration in meters per second squared Returns a float: Force in newtons
    if mass < 0 or acceleration < 0:
        raise ValueError("Mass and acceleration must be non-negative.")
    return mass * acceleration

def JoulesVolts(J):
    #Simple conversion to convert joules to electronic volts
    return J*6.242e+18

def calculate_kinetic_energy(mass, velocity):
    # Calculates kinetic energy. 
    #Parameters: mass (float); Mass in kilograms and velocity (float); Velocity in meters per second
    Returns:
    float: Kinetic energy in joules
    if mass < 0 or velocity < 0:
        raise ValueError("Mass and velocity must be non-negative.")
    return 0.5 * mass * velocity ** 2

def calculate_potential_energy(mass, height, gravity=9.81):
    #Calculate potential energy.
    #Parameters: mass (float); Mass in kilograms, height (float); Height in meters and gravity (float, optional); Acceleration due to gravity in meters per second squared. Default is 9.81.
    Returns:
    float: Potential energy in joules
    if mass < 0 or height < 0:
        raise ValueError("Mass and height must be non-negative.")
    return mass * gravity * height

def calculate_series_resistance(resistances):
    # Calculate total resistance in a series circuit. Parameters: resistances (list of float): List of resistances in ohms
    # Returns a float: Total resistance in ohms
    if any(r < 0 for r in resistances):
        raise ValueError("Resistances must be non-negative.")
    return np.sum(resistances)

def calculate_torque(force, distance):
    # Calculate torque based on force and distance from pivot.
    #Parameters: force (float); Force in newtons, distance (float); Distance from pivot in meters
    if force < 0 or distance < 0:
        raise ValueError("Force and distance must be non-negative.")
    return force * distance

def main():
    # Example usage with exception handling and logging
    import logging
    logging.basicConfig(level=logging.INFO)
    
    try:
        mass = 10  # in kilograms
        acceleration = 5  # in meters per second squared
        velocity = 3  # in meters per second
        height = 2  # in meters
        resistances = [10, 20, 30]  # in ohms

        force = calculate_force(mass, acceleration)
        kinetic_energy = calculate_kinetic_energy(mass, velocity)
        potential_energy = calculate_potential_energy(mass, height)
        total_resistance = calculate_series_resistance(resistances)
        torque = calculate_torque(force, distance)

        logging.info(f"Force: {force} N")
        logging.info(f"Kinetic Energy: {kinetic_energy} J")
        logging.info(f"Potential Energy: {potential_energy} J")
        logging.info(f"Total Resistance in Series Circuit: {total_resistance} Ω")
        logging.info(f"Torque: {torque} Nm")
    
    except ValueError as e:
        logging.error(e)

if __name__ == "__main__":
    main()
