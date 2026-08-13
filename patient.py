patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Amit", 30, "B+"),
    (103, "Raghav", 22, "O+"),
    (104, "Ram", 28, "A+")
)

# Display all records
print("Patient Records:")
for patient in patients:
    print(patient)

# Search patient by ID
id = int(input("\nEnter Patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == id:
        print("Patient Found:", patient)
        found = True

if found == False:
    print("Patient not found")

# Count total patients
print("\nTotal Patients:", len(patients))

# Display patients with specific blood group
group = input("\nEnter Blood Group: ")

print("Patients with", group, "blood group:")

for patient in patients:
    if patient[3] == group:
        print(patient)