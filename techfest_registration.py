print("Welcome to SMIT TechFest!")
print("Event Organised by Rafael Alcantara of APPDAET BTCS1")

num_parti = int(input("\nEnter the number of Participants: "))
if num_parti < 1:
    print("Invalid Input; Exiting Program...")
    exit()

participants = []
for i in range(num_parti):
    print("\nParticipant", i+1, ":")
    name = input("Enter Participant Name: ")
    track = input("Enter Chosen Track: ")
    participant = {"name": name, "track": track}
    participants.append(participant)

print("\nRegistered Participants:")
for i in range(len(participants)):
    print(str(i+1) + ".", participants[i]["name"], "-", participants[i]["track"])