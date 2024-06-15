def calculate_area(P, k, f, B):
    """Calculate the area of the transformer core based on power, current density, frequency, and magnetic flux density"""
    return P / (k * f * B)

def calculate_turns(V, f, A, B):
    """Calculate the number of turns of wire based on voltage, frequency, core cross-sectional area, and magnetic flux density"""
    return V / (4.44 * f * A * B)

def get_positive_float_input(prompt):
    """Get a positive float input from the user"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Input must be a positive number")
            return value
        except ValueError as e:
            print(e)

def main():
    print("Welcome to the Hogwarts Transformer Calculator!")
    
    while True:
        try:
            print("\nChoose the calculation type:")
            print("1. Calculate core cross-sectional area")
            print("2. Calculate primary and secondary turns")
            print("3. Calculate both core area and turns")
            print("4. Exit")
            choice = int(input("Enter your choice (1/2/3/4): "))
            
            if choice == 1:
                P = get_positive_float_input("Enter the power (in watts): ")
                k = get_positive_float_input("Enter the current density (in A/m^2): ")
                f = get_positive_float_input("Enter the frequency (in Hz): ")
                B = get_positive_float_input("Enter the magnetic flux density (in Tesla): ")
                area = calculate_area(P, k, f, B)
                print(f"The core cross-sectional area is: {area} square meters")
            
            elif choice == 2:
                V1 = get_positive_float_input("Enter the primary voltage (in volts): ")
                V2 = get_positive_float_input("Enter the secondary voltage (in volts): ")
                f = get_positive_float_input("Enter the frequency (in Hz): ")
                A = get_positive_float_input("Enter the core cross-sectional area (in square meters): ")
                B = get_positive_float_input("Enter the magnetic flux density (in Tesla): ")
                N1 = calculate_turns(V1, f, A, B)
                N2 = calculate_turns(V2, f, A, B)
                print(f"The primary turns are: {N1}")
                print(f"The secondary turns are: {N2}")
            
            elif choice == 3:
                
                P = get_positive_float_input("Enter the power (in watts): ")
                k = get_positive_float_input("Enter the current density (in A/m^2): ")
                f = get_positive_float_input("Enter the frequency (in Hz): ")
                B = get_positive_float_input("Enter the magnetic flux density (in Tesla): ")
                V1 = get_positive_float_input("Enter the primary voltage (in volts): ")
                V2 = get_positive_float_input("Enter the secondary voltage (in volts): ")
                
                f=open("dlc.txt", "a")
                area = calculate_area(P, k, f, B)
                print(f"The core cross-sectional area is: {str(area)} square meters")
                N1 = calculate_turns(V1, f, area, B)
                N2 = calculate_turns(V2, f, area, B)
                print(f"The primary turns are: {N1}")
                print(f"The secondary turns are: {N2}")
            
            elif choice == 4:
                print("Exiting the program. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError as e:
        
            print(e)

if __name__ == "__main__":
    main()
