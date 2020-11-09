"""If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What
is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile).

Distance = velocity * time
velocity = Distance / time
time = Distance / velocity
"""

distance_km = 10
time = 43.30

average_speed_km = distance_km / time
average_time_km = time / distance_km

km_to_mi = 1.61
distance_mi = distance_km / km_to_mi

average_speed_mi = distance_mi / time
average_time_mi = time / distance_mi

print("Average speed in km per hour: %f km/h" % average_speed_km)
print("Average time in per km: %f m" % average_time_km)
print("Average speed in miles per hour: %f mi/h" % average_speed_mi)
print("Average time in per mi: %f m" % average_time_mi)
