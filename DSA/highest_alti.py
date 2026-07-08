# There is a biker going on a road trip.
# You are given an integer array gain where:
# gain[i] is the altitude gain between point i and i+1.
# The biker starts at altitude 0.
# Return the highest altitude reached.
gain = [-5,1,5,0,-7]
highest_altitude = 0
current_altitude = 0

for i in range(len(gain)):
    current_altitude = current_altitude + gain[i]
    if(current_altitude>highest_altitude):
        highest_altitude = current_altitude
        
print(highest_altitude)