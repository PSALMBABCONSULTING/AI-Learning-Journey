# Lesson 03: Operators and Expressions in Python

# Basic healthcare analytics variables
total_patients = 150
fall_incidents = 12
readmission_count = 8
discharged_patients = 135
compliance_rate = 88.5
bed_occupancy_rate = 94.2
training_completed = False

# Arithmetic operators
remaining_patients = total_patients - discharged_patients
fall_rate = (fall_incidents / total_patients) * 100
readmission_rate = (readmission_count / discharged_patients) * 100

print("Remaining Patients:", remaining_patients)
print("Fall Rate (%):", round(fall_rate, 2))
print("Readmission Rate (%):", round(readmission_rate, 2))

# Comparison operators
print("Fall rate above 5%:", fall_rate > 5)
print("Compliance meets 90% target:", compliance_rate >= 90)
print("Bed occupancy below or equal to 95%:", bed_occupancy_rate <= 95)

# Assignment operators
fall_incidents += 1
total_patients -= 2

print("Updated Fall Incidents:", fall_incidents)
print("Updated Total Patients:", total_patients)

# Logical operators
needs_quality_review = fall_rate > 5 and compliance_rate < 90
needs_capacity_review = bed_occupancy_rate > 95 or remaining_patients < 10
training_follow_up_required = not training_completed

print("Needs Quality Review:", needs_quality_review)
print("Needs Capacity Review:", needs_capacity_review)
print("Training Follow-up Required:", training_follow_up_required)