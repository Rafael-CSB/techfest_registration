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
    participants.append({"name": name, "track": track})

print("\nRegistered Participants:")
for i in range(len(participants)):
    print(str(i+1) + ".", participants[i]["name"], "-", participants[i]["track"])

tracks = []
for p in participants:
    if p["track"] not in tracks:
        tracks.append(p["track"])

print("\nTracks Offered in this Event:")
print(", ".join(tracks))

if len(tracks) < 2:
    print("Not Enough Variety in Tracks")

duplicate = False
for i in range(len(participants)):
    for j in range(i+1, len(participants)):
        if participants[i]["name"] == participants[j]["name"]:
            print("\nDuplicate Participant Found:", participants[i]["name"])
            duplicate = True
if not duplicate:
    print("\nNo Duplicate Names Found")

print("\nParticipants Per Tracks:")
track_count = {}

for p in participants:
    if p["track"] in track_count:
        track_count[p["track"]] += 1
    else:
        track_count[p["track"]] = 1

for t in track_count:
    print(t + ": " + str(track_count[t]))
