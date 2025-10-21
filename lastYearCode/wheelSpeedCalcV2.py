#1.5, this bad boy has input boxes for easy use.
import math

class Differential:
    def __init__(self, wheel_base, track_width):
        self.wheel_base = wheel_base
        self.track_width = track_width

    def calculate_wheel_speeds(self, turn_radius, car_speed):
        if turn_radius == 0:
            # No turny, wheels move at the same speed
            return car_speed, car_speed

        # Calculate inner and outer wheel turn radii
        inner_radius = turn_radius - (self.track_width / 2)
        outer_radius = turn_radius + (self.track_width / 2)

        # Speed of inner and outer wheels
        inner_wheel_speed = (inner_radius / turn_radius) * car_speed
        outer_wheel_speed = (outer_radius / turn_radius) * car_speed

        return inner_wheel_speed, outer_wheel_speed

# usage
if __name__ == "__main__":
    # Collect user input
    try:
        wheel_base = float(input("Enter wheel base (m): "))
        track_width = float(input("Enter track width (m): "))
        turn_radius = float(input("Enter turn radius (m): "))
        car_speed = float(input("Enter car speed (m/s): "))

        # Set up the differential with the user input values
        car_differential = Differential(wheel_base=wheel_base, track_width=track_width)

        # Calculate wheel speeds
        inner_speed, outer_speed = car_differential.calculate_wheel_speeds(turn_radius=turn_radius, car_speed=car_speed)

        # Display results
        print(f"Inner wheel speed: {inner_speed:.2f} m/s")
        print(f"Outer wheel speed: {outer_speed:.2f} m/s")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

        #in explination

