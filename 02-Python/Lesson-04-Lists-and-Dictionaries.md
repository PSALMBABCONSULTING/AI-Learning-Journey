# Lesson 04: Lists and Dictionaries in Python

## What Are Lists and Dictionaries?

Lists and dictionaries are Python data structures used to store multiple values.

They are important in healthcare analytics because real-world healthcare data often includes multiple patients, units, quality indicators, metrics, and reporting periods.

## Lists

A list stores multiple values in one variable.

Example:

```python
quality_indicators = ["Falls", "Readmissions", "Infections", "Medication Errors"]
```

A list is useful when you have a group of related items.

For example, a healthcare analytics list may include several quality indicators:

```python
quality_indicators = ["Falls", "Readmissions", "Infections", "Medication Errors"]
```

You can print the full list:

```python
print(quality_indicators)
```

You can access one item from the list using its position:

```python
print(quality_indicators[0])
```

Python starts counting from `0`, so the first item is at position `0`.

## Common List Actions

You can add an item to a list using `append()`:

```python
quality_indicators.append("Pressure Injuries")
```

You can count the number of items in a list using `len()`:

```python
print(len(quality_indicators))
```

## Dictionaries

A dictionary stores data as key-value pairs.

Example:

```python
patient_summary = {
    "patient_group": "Older Adults",
    "total_patients": 150,
    "fall_incidents": 12,
    "compliance_rate": 94.5
}
```

In a dictionary, each key has a related value.

For example:

| Key               | Value            |
| ----------------- | ---------------- |
| `patient_group`   | `"Older Adults"` |
| `total_patients`  | `150`            |
| `fall_incidents`  | `12`             |
| `compliance_rate` | `94.5`           |

## Accessing Dictionary Values

You can access a dictionary value by using its key:

```python
print(patient_summary["total_patients"])
```

## Updating Dictionary Values

You can update a dictionary value:

```python
patient_summary["compliance_rate"] = 96.2
```

You can also add a new key-value pair:

```python
patient_summary["readmission_count"] = 8
```

## List of Dictionaries

A list can contain multiple dictionaries.

This is useful when working with records that look like rows in a table.

Example:

```python
unit_metrics = [
    {"unit": "Unit A", "fall_incidents": 5, "compliance_rate": 91.2},
    {"unit": "Unit B", "fall_incidents": 3, "compliance_rate": 95.4},
    {"unit": "Unit C", "fall_incidents": 7, "compliance_rate": 88.9}
]
```

This structure is similar to a small healthcare dataset.

| Unit   | Fall Incidents | Compliance Rate |
| ------ | -------------: | --------------: |
| Unit A |              5 |            91.2 |
| Unit B |              3 |            95.4 |
| Unit C |              7 |            88.9 |

## Healthcare Analytics Example

Lists can store groups of healthcare indicators, while dictionaries can store detailed information about a patient group, unit, dashboard, or metric.

For example, a list can store quality indicators, and a dictionary can store summary values such as total patients, fall incidents, compliance rate, and readmission count.

## Full Practice Code

The full Python practice code for this lesson is available in the practice folder:

[View Lesson 04 Practice Code](practice/lesson_04_lists_dictionaries.py)

This file contains the complete Python script for lists, dictionaries, list actions, dictionary updates, and list of dictionaries.

## My Career Application

Understanding lists and dictionaries is important because they are foundational for working with real healthcare datasets. They help organize multiple values, structure records, and prepare data for analysis, automation, dashboards, machine learning, and AI workflows.

