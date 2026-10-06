name = input("Enter passenger name: ")
destination = input("Enter destination: ")
ticket_count = int(input("Enter number of tickets: "))
passenger_type = input("Enter passenger type (child/student/adult/senior): ").lower()

fare_table = {
    "Dhaka": 500,
    "Chittagong": 800,
    "Sylhet": 600,
    "Rajshahi": 700
}

fare = fare_table[destination]

if passenger_type == "child":
    discount = 0.50
elif passenger_type == "student":
    discount = 0.20
elif passenger_type == "senior":
    discount = 0.30
else:
    discount = 0

discounted_fare = fare * (1 - discount)
total_fare = discounted_fare * ticket_count

print("\n========== TRAIN TICKET ==========")
print("Passenger:", name)
print("Destination:", destination)
print("Passenger Type:", passenger_type)
print("Number of Tickets:", ticket_count)
print("Fare per ticket:", fare)
print("Discount:", discount * 100, "%")
print("Total Fare:", total_fare)
print("==================================")