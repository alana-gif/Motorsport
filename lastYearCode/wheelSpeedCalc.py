#01 of Code Explained Fs Document
#works
import math

class Differential:

  def __init__(self, wheel_base, track_width):

    #wheel_base: distance between front and rear axles (meters)
    #track_width: distance between the left and right wheels (meters)

    self.wheel_base = wheel_base
    self.track_width = track_width

  def calculate_wheel_speeds(self, turn_radius, car_speed):

    #turn_radius: radius of the turn (meters)
    #car_speed: speed of the car (meters/second)

    #Returns:
    #Speeds of inner and outer wheels (m/s)

    if turn_radius == 0:
      # No turn, wheels move at the same speed
      return car_speed, car_speed

    # Calculate inner and outer wheel turn radii
    inner_radius = turn_radius - (self.track_width / 2)
    outer_radius = turn_radius + (self.track_width / 2)

    # Speed of inner and outer wheels
    inner_wheel_speed = (inner_radius / turn_radius) * car_speed
    outer_wheel_speed = (outer_radius / turn_radius) * car_speed
    return inner_wheel_speed, outer_wheel_speed

# Example usage
if __name__ == "__main__":
  # Set up the differential with wheelbase 2.5m, track width 1.5m
  car_differential = Differential(wheel_base=2.5, track_width=1.5)

  # Calculate wheel speeds for a turn with 10m radius, car speed 10m/s
  inner_speed, outer_speed = car_differential.calculate_wheel_speeds(
      turn_radius=10, car_speed=10)

  print(f"Inner wheel speed: {inner_speed:.2f} m/s")
  print(f"Outer wheel speed: {outer_speed:.2f} m/s")

#numberds can be changed
# wanker fucking peice of shit this shit is so bad. kill me now.
#all numbers are interchangable and if i had to i could make it so you,
#could input the numbers instead of them being set into the code but *i wont be happy about it