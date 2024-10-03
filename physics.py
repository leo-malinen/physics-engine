def calculate_force(mass, acceleration):
    force = mass * acceleration
    return force

def calculate_kinetic_energy(mass, velocity):
    kinetic_energy = 0.5 * mass * velocity ** 2
    return kinetic_energy

def calculate_potential_energy(mass, height, gravity=9.81):
    potential_energy = mass * gravity * height
    return potential_energy

mass = 0
acceleration = 0 
velocity = 0
height = 0

force = calculate_force(mass, acceleration)
kinetic_energy = calculate_kinetic_energy(mass, velocity)
potential_energy = calculate_potential_energy(mass, height)

print(f"Force: {force} N")
print(f"Kinetic Energy: {kinetic_energy} J")
print(f"Potential Energy: {potential_energy} J")
