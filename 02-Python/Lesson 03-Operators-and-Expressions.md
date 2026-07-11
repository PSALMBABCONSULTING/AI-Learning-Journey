# Lesson 03: Operators and Expressions in Python

## What Are Operators?

Operators are symbols or keywords that Python uses to perform calculations, compare values, assign values, or combine conditions.

Operators are important in healthcare analytics because they help calculate metrics, compare performance against targets, and create logic for reporting and analysis.

## Arithmetic Operators

Arithmetic operators are used for calculations.

| Operator | Meaning        | Example                                |
| -------- | -------------- | -------------------------------------- |
| `+`      | Addition       | `total_patients + new_admissions`      |
| `-`      | Subtraction    | `total_patients - discharged_patients` |
| `*`      | Multiplication | `fall_rate * 100`                      |
| `/`      | Division       | `fall_incidents / total_patients`      |
| `%`      | Remainder      | `10 % 3`                               |
| `**`     | Power          | `2 ** 3`                               |

Example:

```python
total_patients = 150
fall_incidents = 12

fall_rate = (fall_incidents / total_patients) * 100

print("Fall Rate:", fall_rate)
```

## Comparison Operators

Comparison operators compare values and return either `True` or `False`.

| Operator | Meaning                  | Example                    |
| -------- | ------------------------ | -------------------------- |
| `==`     | Equal to                 | `compliance_rate == 90`    |
| `!=`     | Not equal to             | `care_area != "Emergency"` |
| `>`      | Greater than             | `fall_rate > 5`            |
| `<`      | Less than                | `compliance_rate < 90`     |
| `>=`     | Greater than or equal to | `compliance_rate >= 90`    |
| `<=`     | Less than or equal to    | `bed_occupancy_rate <= 95` |

Example:

```python
compliance_rate = 88.5

print(compliance_rate >= 90)
```

## Assignment Operators

Assignment operators are used to assign or update values.

| Operator | Meaning             | Example               |
| -------- | ------------------- | --------------------- |
| `=`      | Assign value        | `fall_incidents = 12` |
| `+=`     | Add and update      | `fall_incidents += 1` |
| `-=`     | Subtract and update | `total_patients -= 5` |
| `*=`     | Multiply and update | `score *= 2`          |
| `/=`     | Divide and update   | `rate /= 100`         |

Example:

```python
fall_incidents = 12
fall_incidents += 1

print(fall_incidents)
```

## Logical Operators

Logical operators combine conditions.

| Operator | Meaning                             | Example                                  |
| -------- | ----------------------------------- | ---------------------------------------- |
| `and`    | Both conditions must be true        | `fall_rate > 5 and compliance_rate < 90` |
| `or`     | At least one condition must be true | `fall_rate > 5 or compliance_rate < 90`  |
| `not`    | Reverses the result                 | `not training_completed`                 |

Example:

```python
fall_rate = 8.0
compliance_rate = 88.5

needs_review = fall_rate > 5 and compliance_rate < 90

print(needs_review)
```

## Healthcare Analytics Example

Operators can be used to calculate healthcare metrics such as fall rate, readmission rate, compliance rate, occupancy rate, and performance status.

For example, Python can calculate a fall rate by dividing the number of fall incidents by the total number of patients and multiplying by 100.

## Full Practice Code

The full Python practice code for this lesson is available in the practice folder:

[View Lesson 03 Practice Code](practice/lesson_03_operators.py)

This file contains the complete Python script for arithmetic, comparison, assignment, and logical operators.

## My Career Application

Understanding operators is important because healthcare analytics often involves calculations, comparisons, and decision logic. These same concepts are used in SQL, Power BI, Python, machine learning, and AI workflows.
