class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display_info(self):
        print(f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Disease: {self.disease}")

    def calculate_total_bill(self, medicine_charges=0):
        return self.consultation_fee + medicine_charges

p = Patient(501, "Bob", 45, "Flu", 50)
p.display_info()
print(f"Total Bill (with meds): ${p.calculate_total_bill(30)}")
