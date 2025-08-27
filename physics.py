#!/usr/bin/env python3
import math

# Vector formulas
def vector_dot(v1, v2):
    return sum(x * y for x, y in zip(v1, v2))

def vector_cross(v1, v2):
    return [v1[1]*v2[2] - v1[2]*v2[1],
            v1[2]*v2[0] - v1[0]*v2[2],
            v1[0]*v2[1] - v1[1]*v2[0]]

def vector_magnitude(v):
    return math.sqrt(sum(x**2 for x in v))

def vector_operations():
    while True:
        print("\n--- Vector Operations ---")
        print("1. Dot Product (v · w)")
        print("2. Cross Product (v × w) [3D only]")
        print("3. Magnitude (|v|)")
        print("4. Back")
        choice = input("Select an option: ")
        if choice.lower() == '4':
            break
        elif choice == '1':
            v1 = list(map(float, input("Enter vector 1 components separated by space: ").split()))
            v2 = list(map(float, input("Enter vector 2 components separated by space: ").split()))
            print("Dot product =", vector_dot(v1, v2))
        elif choice == '2':
            v1 = list(map(float, input("Enter 3 components for vector 1: ").split()))
            v2 = list(map(float, input("Enter 3 components for vector 2: ").split()))
            if len(v1) == 3 and len(v2) == 3:
                print("Cross product =", vector_cross(v1, v2))
            else:
                print("Both vectors must have exactly 3 components.")
        elif choice == '3':
            v = list(map(float, input("Enter vector components separated by space: ").split()))
            print("Magnitude =", vector_magnitude(v))
        else:
            print("Invalid option.")

# Kinematics equations
def kinematics():
    while True:
        print("\n--- Kinematics ---")
        print("1. Displacement: s = ut + 0.5*a*t^2")
        print("2. Final Velocity: v = u + a*t")
        print("3. Displacement (using average velocity): s = ((u+v)/2)*t")
        print("4. Back")
        choice = input("Select an option: ")
        if choice.lower() == '4':
            break
        elif choice == '1':
            u = float(input("Enter initial velocity, u: "))
            a = float(input("Enter acceleration, a: "))
            t = float(input("Enter time, t: "))
            s = u * t + 0.5 * a * t * t
            print("Displacement s =", s)
        elif choice == '2':
            u = float(input("Enter initial velocity, u: "))
            a = float(input("Enter acceleration, a: "))
            t = float(input("Enter time, t: "))
            v = u + a * t
            print("Final velocity v =", v)
        elif choice == '3':
            u = float(input("Enter initial velocity, u: "))
            v = float(input("Enter final velocity, v: "))
            t = float(input("Enter time, t: "))
            s = ((u + v) / 2) * t
            print("Displacement s =", s)
        else:
            print("Invalid option.")

# Particle Dynamics
def particle_dynamics():
    while True:
        print("\n--- Particle Dynamics ---")
        print("1. Force: F = m * a")
        print("2. Acceleration: a = F / m")
        print("3. Mass: m = F / a")
        print("4. Back")
        choice = input("Select an option: ")
        if choice.lower() == '4':
            break
        elif choice == '1':
            m = float(input("Enter mass, m: "))
            a = float(input("Enter acceleration, a: "))
            print("Force F =", m * a)
        elif choice == '2':
            F = float(input("Enter force, F: "))
            m = float(input("Enter mass, m: "))
            if m != 0:
                print("Acceleration a =", F / m)
            else:
                print("Error: Mass cannot be zero.")
        elif choice == '3':
            F = float(input("Enter force, F: "))
            a = float(input("Enter acceleration, a: "))
            if a != 0:
                print("Mass m =", F / a)
            else:
                print("Error: Acceleration cannot be zero.")
        else:
            print("Invalid option.")

# Friction equation
def friction():
    while True:
        print("\n--- Friction ---")
        print("1. Friction Force: f = μ * N")
        print("2. Back")
        choice = input("Select an option: ")
        if choice.lower() == '2':
            break
        elif choice == '1':
            mu = float(input("Enter coefficient of friction, μ: "))
            N = float(input("Enter normal force, N: "))
            print("Friction force f =", mu * N)
        else:
            print("Invalid option.")

# Work, Energy, and Power equations
def work_energy_power():
    while True:
        print("\n--- Work, Energy, and Power ---")
        print("1. Work: W = F * d * cos(theta)")
        print("2. Kinetic Energy: KE = 0.5 * m * v^2")
        print("3. Potential Energy: PE = m * g * h")
        print("4. Power: P = W / t")
        print("5. Back")
        choice = input("Select an option: ")
        if choice.lower() == '5':
            break
        elif choice == '1':
            F = float(input("Enter force, F: "))
            d = float(input("Enter displacement, d: "))
            theta = float(input("Enter angle theta (in degrees): "))
            print("Work W =", F * d * math.cos(math.radians(theta)))
        elif choice == '2':
            m = float(input("Enter mass, m: "))
            v = float(input("Enter velocity, v: "))
            print("Kinetic Energy KE =", 0.5 * m * v**2)
        elif choice == '3':
            m = float(input("Enter mass, m: "))
            g = float(input("Enter gravitational acceleration, g: "))
            h = float(input("Enter height, h: "))
            print("Potential Energy PE =", m * g * h)
        elif choice == '4':
            W = float(input("Enter work, W: "))
            t = float(input("Enter time, t: "))
            if t != 0:
                print("Power P =", W / t)
            else:
                print("Error: Time cannot be zero.")
        else:
            print("Invalid option.")

# Momentum calculation
def momentum():
    while True:
        print("\n--- Momentum ---")
        print("1. Momentum: p = m * v")
        print("2. Back")
        choice = input("Select an option: ")
        if choice.lower() == '2':
            break
        elif choice == '1':
            m = float(input("Enter mass, m: "))
            v = float(input("Enter velocity, v: "))
            print("Momentum p =", m * v)
        else:
            print("Invalid option.")

# Rigid bodies (Dynamics and Statics)
def rigid_bodies():
    while True:
        print("\n--- Dynamics & Statics of Rigid Bodies ---")
        print("1. Torque (perpendicular force): τ = F * r")
        print("2. Rotational dynamics: τ = I * α")
        print("3. Back")
        choice = input("Select an option: ")
        if choice.lower() == '3':
            break
        elif choice == '1':
            F = float(input("Enter force, F: "))
            r = float(input("Enter lever arm length, r: "))
            print("Torque τ =", F * r)
        elif choice == '2':
            I = float(input("Enter moment of inertia, I: "))
            alpha = float(input("Enter angular acceleration, α: "))
            print("Torque τ =", I * alpha)
        else:
            print("Invalid option.")

# Oscillations formulas
def oscillations():
    while True:
        print("\n--- Oscillations ---")
        print("1. Simple Pendulum Period: T = 2π * sqrt(l / g)")
        print("2. Mass-Spring System Period: T = 2π * sqrt(m / k)")
        print("3. Back")
        choice = input("Select an option: ")
        if choice.lower() == '3':
            break
        elif choice == '1':
            l = float(input("Enter pendulum length, l: "))
            g = float(input("Enter gravitational acceleration, g: "))
            print("Period T =", 2 * math.pi * math.sqrt(l / g))
        elif choice == '2':
            m = float(input("Enter mass, m: "))
            k = float(input("Enter spring constant, k: "))
            print("Period T =", 2 * math.pi * math.sqrt(m / k))
        else:
            print("Invalid option.")

# Gravitation formula
def gravitation():
    while True:
        print("\n--- Gravitation ---")
        print("1. Newton's Law of Gravitation: F = G * m1 * m2 / r^2")
        print("2. Back")
        choice = input("Select an option: ")
        if choice.lower() == '2':
            break
        elif choice == '1':
            m1 = float(input("Enter mass m1: "))
            m2 = float(input("Enter mass m2: "))
            r = float(input("Enter distance r: "))
            if r != 0:
                G = 6.67430e-11  # gravitational constant
                print("Gravitational Force F =", G * m1 * m2 / (r**2))
            else:
                print("Error: Distance cannot be zero.")
        else:
            print("Invalid option.")

# Fluids equation
def fluids():
    while True:
        print("\n--- Fluids ---")
        print("1. Hydrostatic Pressure: P = ρ * g * h")
        print("2. Back")
        choice = input("Select an option: ")
        if choice.lower() == '2':
            break
        elif choice == '1':
            rho = float(input("Enter fluid density ρ: "))
            g = float(input("Enter gravitational acceleration, g: "))
            h = float(input("Enter depth/height, h: "))
            print("Hydrostatic Pressure P =", rho * g * h)
        else:
            print("Invalid option.")

# Calculus tools if needed: here a numerical derivative example
def calculus_tools():
    def numerical_derivative(f, x, h=1e-5):
        return (f(x + h) - f(x - h)) / (2 * h)
    while True:
        print("\n--- Calculus Tools ---")
        print("1. Numerical Derivative of a function at a point")
        print("2. Back")
        choice = input("Select an option: ")
        if choice.lower() == '2':
            break
        elif choice == '1':
            expr = input("Enter a function f(x) using math module (e.g., math.sin(x)): ")
            x_val = float(input("Enter the value of x: "))
            h_val = input("Enter a small value h (or press enter for default 1e-5): ")
            h_val = float(h_val) if h_val.strip() else 1e-5
            try:
                f = lambda x: eval(expr)
                deriv = numerical_derivative(f, x_val, h_val)
                print("Numerical derivative f'({}) = {}".format(x_val, deriv))
            except Exception as e:
                print("Error evaluating function:", e)
        else:
            print("Invalid option.")

def print_ascii_banner():
    print(r"""
______ _               _            _____       _            _       _             
| ___ \ |             (_)          /  __ \     | |          | |     | |            
| |_/ / |__  _   _ ___ _  ___ ___  | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
|  __/| '_ \| | | / __| |/ __/ __| | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |   | | | | |_| \__ \ | (__\__ \ | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
\_|   |_| |_|\__, |___/_|\___|___/  \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
              __/ |                                                                 

    """)

# Main menu loop
def main():
    print_ascii_banner()
    while True:
        print("\n=== Physics Calculator ===")
        print("1. Vectors")
        print("2. Kinematics")
        print("3. Particle Dynamics")
        print("4. Friction")
        print("5. Work, Energy and Power")
        print("6. Momentum")
        print("7. Dynamics & Statics of Rigid Bodies")
        print("8. Oscillations")
        print("9. Gravitation")
        print("10. Fluids")
        print("11. Calculus Tools")
        print("Type 'exit' to quit")
        topic = input("Select a topic: ")
        if topic.lower() == 'exit':
            break
        elif topic == '1':
            vector_operations()
        elif topic == '2':
            kinematics()
        elif topic == '3':
            particle_dynamics()
        elif topic == '4':
            friction()
        elif topic == '5':
            work_energy_power()
        elif topic == '6':
            momentum()
        elif topic == '7':
            rigid_bodies()
        elif topic == '8':
            oscillations()
        elif topic == '9':
            gravitation()
        elif topic == '10':
            fluids()
        elif topic == '11':
            calculus_tools()
        else:
            print("Invalid topic selection.")
    print("\nExiting Physics Calculator. Goodbye!")

if __name__ == "__main__":
    main()
