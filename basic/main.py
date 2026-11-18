mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

first_destination = mission_route[0]
final_destination=mission_route[5]
total=len(mission_route)
print("Initial Destination:",first_destination)
print("Final Destination:",final_destination)
print("Total Routes:", total)
print("DESTINATION ORDER")
for destination in mission_route:
    print(destination)
print("ROUTE CHECK")
if "Europa" in mission_route:
    print("Europa in in the mission route")
else:
    print("Europa is not in the mission route")