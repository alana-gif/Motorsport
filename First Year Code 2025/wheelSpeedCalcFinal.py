#03
#a more compex version and with added math shite (math might be wrong)
#this came from camerons help when i gave him what i had, teamwork lol
#no longer buggy to my knowledge

import math

class Differential:
    def __init__(self, wheel_base, track_width, max_torque_split=0.8):
        """
        Initialize the Differential object.

        Args:
        wheel_base (float): Distance between front and rear axles (meters).
        track_width (float): Distance between the left and right wheels (meters).
        max_torque_split (float): Maximum torque split (e.g., 0.8 means 80% torque can go to one wheel).
        """

        self.wheel_base = wheel_base
        self.track_width = track_width
        self.max_torque_split = max_torque_split

    def calculate_wheel_speeds(self, turn_radius, car_speed):

        #Calculate the speeds of the inner and outer wheels during a turn.

        try:
            epsilon = 1e-6  # Threshold for considering a zero turn radius
            if abs(turn_radius) < epsilon:
                # No turn; wheels move at the same speed
                return car_speed, car_speed

            # Calculate inner and outer wheel turn radii
            inner_radius = turn_radius - (self.track_width / 2)
            outer_radius = turn_radius + (self.track_width / 2)

            # Speed of inner and outer wheels
            inner_wheel_speed = (inner_radius / turn_radius) * car_speed
            outer_wheel_speed = (outer_radius / turn_radius) * car_speed

            return inner_wheel_speed, outer_wheel_speed

        except Exception as e:
            print(f"Error in calculate_wheel_speeds: {e}")
            return None, None

    def calculate_torque_split(self, turn_radius, base_torque):

        #Calculate the torque split between the inner and outer wheels during a turn.

        try:
            epsilon = 1e-6  # Threshold for considering a zero turn radius
            if abs(turn_radius) < epsilon:
                # No turn; equal torque distribution
                return base_torque / 2, base_torque / 2

            # Calculate inner and outer radii
            inner_radius = turn_radius - (self.track_width / 2)
            outer_radius = turn_radius + (self.track_width / 2)
            total_radius = inner_radius + outer_radius

            # Torque distribution is proportional to the turn radii
            inner_torque = (inner_radius / total_radius) * base_torque
            outer_torque = (outer_radius / total_radius) * base_torque

            # Ensure torque split does not exceed max limits
            max_inner_torque = base_torque * self.max_torque_split
            max_outer_torque = base_torque * (1 - self.max_torque_split)

            # Apply the max limits
            inner_torque = min(inner_torque, max_inner_torque)
            outer_torque = min(outer_torque, max_outer_torque)

            # Ensure the total torque does not exceed base_torque
            total_torque = inner_torque + outer_torque
            if total_torque > base_torque:
                inner_torque = (inner_torque / total_torque) * base_torque
                outer_torque = (outer_torque / total_torque) * base_torque

            return inner_torque, outer_torque

        except Exception as e:
            print(f"Error in calculate_torque_split: {e}")
            return None, None

    def calculate_slip_ratio(self, car_speed, wheel_speed):

        #Calculate the slip ratio for traction control.

        try:
            if car_speed == 0:
                return 0  # Avoid division by zero; no slip when stationary.
            slip_ratio = (wheel_speed - car_speed) / car_speed
            return slip_ratio
        except Exception as e:
            print(f"Error in calculate_slip_ratio: {e}")
            return None


# Example usage
if __name__ == "__main__":
    try:
        # Set up the differential with wheelbase 2.5m, track width 1.5m, and max torque split 80%

        car_differential = Differential(wheel_base=2.5, track_width=1.5, max_torque_split=0.8)

        # Calculate wheel speeds for a turn with 10m radius and car speed 10m/s
        turn_radius = 10  # meters
        car_speed = 10    # meters/second

        inner_speed, outer_speed = car_differential.calculate_wheel_speeds(
            turn_radius=turn_radius, car_speed=car_speed
        )
        if inner_speed is not None and outer_speed is not None:
            print(f"Inner wheel speed: {inner_speed:.2f} m/s")
            print(f"Outer wheel speed: {outer_speed:.2f} m/s")

        # Calculate torque split for a base torque of 500Nm
        base_torque = 500  # Nm
        inner_torque, outer_torque = car_differential.calculate_torque_split(
            turn_radius=turn_radius, base_torque=base_torque
        )
        if inner_torque is not None and outer_torque is not None:
            print(f"Inner wheel torque: {inner_torque:.2f} Nm")
            print(f"Outer wheel torque: {outer_torque:.2f} Nm")

        # Calculate slip ratio for the inner wheel
        inner_slip_ratio = car_differential.calculate_slip_ratio(
            car_speed=car_speed, wheel_speed=inner_speed
        )
        if inner_slip_ratio is not None:
            print(f"Inner wheel slip ratio: {inner_slip_ratio:.2f}")

    except Exception as e:
        print(f"Error in main execution: {e}")
