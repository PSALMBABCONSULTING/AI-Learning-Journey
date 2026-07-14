# Lesson 04: Lists and Dictionaries in Python

# List example
quality_indicators = ["Falls", "Readmissions", "Infections", "Medication Errors"]

print("Quality Indicators:", quality_indicators)

# Accessing items in a list
print("First Quality Indicator:", quality_indicators[0])
print("Second Quality Indicator:", quality_indicators[1])

# Adding a new item to a list
quality_indicators.append("Pressure Injuries")

print("Updated Quality Indicators:", quality_indicators)

# Counting items in a list
print("Number of Quality Indicators:", len(quality_indicators))


# Dictionary example
patient_summary = {
    "patient_group": "Older Adults",
    "total_patients": 150,
    "fall_incidents": 12,
    "readmission_count": 8,
    "compliance_rate": 94.5
}

print("Patient Summary:", patient_summary)

# Accessing dictionary values
print("Patient Group:", patient_summary["patient_group"])
print("Total Patients:", patient_summary["total_patients"])
print("Fall Incidents:", patient_summary["fall_incidents"])
print("Compliance Rate:", patient_summary["compliance_rate"])

# Updating a dictionary value
patient_summary["compliance_rate"] = 96.2

print("Updated Compliance Rate:", patient_summary["compliance_rate"])

# Adding a new key-value pair
patient_summary["bed_occupancy_rate"] = 91.3

print("Bed Occupancy Rate:", patient_summary["bed_occupancy_rate"])


# List of dictionaries example
unit_metrics = [
    {"unit": "Unit A", "fall_incidents": 5, "compliance_rate": 91.2},
    {"unit": "Unit B", "fall_incidents": 3, "compliance_rate": 95.4},
    {"unit": "Unit C", "fall_incidents": 7, "compliance_rate": 88.9}
]

print("Unit Metrics:", unit_metrics)

# Accessing values from a list of dictionaries
print("First Unit:", unit_metrics[0]["unit"])
print("First Unit Fall Incidents:", unit_metrics[0]["fall_incidents"])
print("Second Unit Compliance Rate:", unit_metrics[1]["compliance_rate"])