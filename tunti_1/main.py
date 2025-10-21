import numpy as np

rads = [2.493, 0.911]
print("RADS TO DEGREES")
for rad in rads:
    print(np.degrees(rad))

print("\n")

degrees = [133.7, 62.3]
print("DEGREES TO RAD")
for degree in degrees:
    print(np.radians(degree))


print("\n")

degrees_list = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
rad_degree_dict = {}

for degree in degrees_list:
    rad_degree_dict[degree] = np.deg2rad(degree)

print("DEGREE TO RAD TABLE")
for key, value in rad_degree_dict.items():
    print(f"DEG: {key} = {value} RAD")

