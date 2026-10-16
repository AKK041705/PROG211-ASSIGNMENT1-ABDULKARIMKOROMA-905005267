# Poultry Farm Health & Tracking System



## Project Description

A Python console program that keeps health records for the birds on a small poultry farm. It is based on Kafallah women poultry farm in Makeni, Sierra Leone, and falls under the Agriculture domain (Livestock Health & Tracking System).

## Problem Being Solved

On a small farm it is hard to remember which birds are sick, which are under treatment and which have been vaccinated. This program records each bird, lets the farm update its health, and shows all the records in one place.

## Objectives

- Build the program with Object-Oriented Programming (classes and objects)
- Store many bird records in one Python data structure
- Use instance, class and static methods
- Follow Digital Public Goods (DPG) principles
- Keep the code simple and easy to read

## Features

- Two classes: `Poultry` (one bird) and `Farm` (the farm that looks after the birds)
- The farm inspects a bird and updates its health and vaccination status
- Add and display bird records
- Add a new bird through the console, with checks on every answer
- Counts how many bird objects have been created

## OOP Concepts Demonstrated

- Classes and objects
- Constructor (`__init__`) and instance attributes
- A class attribute (`total_birds`)
- Instance methods, a class method (`@classmethod`) and static methods (`@staticmethod`)
- Interaction between objects

## Task 1: Classes, Attributes and Objects

**Poultry** represents one bird.

| Attributes | Description |
|---|---|
| `bird_id` | Unique ID, for example P001 |
| `breed` | Broiler, Layer, Kuroiler or Local |
| `age_weeks` | Age in weeks |
| `health_status` | Healthy, Sick or Under treatment |
| `vaccinated` | True or False |

**Farm** represents the farm.

| Attributes | Description |
|---|---|
| `farm_name` | Name of the farm |
| `location` | Where the farm is |
| `capacity` | Maximum number of birds |
| `birds` | List of Poultry objects (see Task 2) |

**Objects created:** `bird1` to `bird4` (Poultry) and `farm1` (Farm).

**Object interaction:** `farm1.inspect(bird)` takes a Poultry object. If the bird is sick, the farm calls the bird's `update_health()`. If the bird is not vaccinated, the farm calls the bird's `vaccinate()`. One object works on another object.

## Task 2: Data Structure

**Main data structure: list** - `Farm.birds`.

- `add_record(bird)` adds a Poultry object to the list. It refuses a record if the age is invalid, the ID is already used or the farm is full.
- `display_records()` loops through the list and shows every bird.

Tuples are also used for fixed options that never change: `HEALTH_STATUSES` and `BREEDS`.

## Task 3: Methods

| Method | Type | What it does |
|---|---|---|
| `display_info()` | Instance method | Shows one bird's details |
| `update_health(new_status)` | Instance method | Changes one bird's health status |
| `vaccinate()` | Instance method | Marks one bird as vaccinated |
| `Farm.inspect(bird)` | Instance method | Farm checks a bird and fixes its status |
| `Farm.add_record(bird)` | Instance method | Adds a bird to the list |
| `Farm.display_records()` | Instance method | Shows all birds in the list |
| `get_total_birds()` | Class method | Uses `cls` to show how many Poultry objects were created |
| `is_valid_age(age_weeks)` | Static method | Checks the age is between 1 and 104 weeks |
| `is_valid_status(status)` | Static method | Checks the status is in the `HEALTH_STATUSES` tuple |

**Instance vs class vs static:** an instance method works on one object (`self`). A class method works on the class itself (`cls`), for example the shared `total_birds` counter. A static method needs neither, it is just a helper that belongs with the class.

Other functions: `choose_from()` (numbered menu), `ask_bird_id()`, `ask_age()` and `add_bird_from_input()`.

## How to Run

Install Python 3, then run this in the project folder:

```
python poultry_farm_system.py
```

## Example Usage (shortened)
```
----------farm information----------
Farm name : Kafallah women poultry farm
Location : Makeni, Sierra Leone
Capacity : 500 birds

Kafallah women poultry farm is inspecting bird P003...
Bird P003 health updated to Under treatment.
Bird P003 has been vaccinated.

----------add a new bird----------
Bird ID (starts with P, example P005): X1
Please enter a valid ID starting with P followed by numbers, for example P005.
Bird ID (starts with P, example P005): P005

Select the breed:
1. Broiler
2. Layer
3. Kuroiler
4. Local
Please enter the number of your choice (1 to 4): 9
Please enter a valid number from 1 to 4.
Please enter the number of your choice (1 to 4): 2
Age in weeks (1 to 104): ten
Please enter a valid age as a whole number, for example 10.
Age in weeks (1 to 104): 10

Select the health status:
1. Healthy
2. Sick
3. Under treatment
Please enter the number of your choice (1 to 3): 1

Is the bird vaccinated?
1. Yes
2. No
Please enter the number of your choice (1 to 2): 2
Bird P005 added to records.

----------poultry information----------
ID : P005
Breed : Layer
Age (weeks) : 10
Health status : Healthy
Vaccinated : False

Total poultry objects created: 5

Is an age of 5 weeks valid? True
Is an age of 0 weeks valid? False
Is an age of 500 weeks valid? False
Is the status Sick valid? True
Is the status Flying valid? False
```

## Digital Public Goods (DPG) Alignment

**1. Open-source**
The code is in a public GitHub repository and uses the MIT License (see `LICENSE`), so anyone can read, use and improve it. The code has short comments to make it easy to follow.

**2. Inclusive and accessible design**
The program runs in a plain text console on any computer with Python, with no internet or special hardware. Breed, health status and vaccination are chosen from numbered menus, so users do not need to type or spell anything. Every error message starts with "Please..." and says what to enter, and the program keeps asking until the answer is valid instead of crashing.

**3. Privacy-respecting**
The program stores only bird and farm information (ID, breed, age, health, vaccination). It does not ask for or store any personal data about owners, workers or customers. Records stay in memory while the program runs and are not saved to a file or sent anywhere.

**4. Modular and reusable**
`Poultry` and `Farm` are separate classes with one clear job each. Small functions do one task each, and `choose_from()` is reused for three different menus. The settings (`BREEDS`, `HEALTH_STATUSES`, `MAX_AGE_WEEKS`) sit at the top of the file, so another farm can change them without touching the rest of the code.

## Privacy Considerations

- No personal or sensitive data is collected
- Bird IDs are simple codes (P001, P002), not linked to any person
- Nothing is stored after the program closes

## GitHub / Open-Source Information

- Repository: https://github.com/AKK041705/PROG211-ASSIGNMENT1-ABDULKARIMKOROMA-905005267
- License: MIT
- Source file: `poultry_farm_system.py`

## Author

Abdul Karim Koroma
Student ID: 905005267
PROG211 - Object-Oriented Programming 1 (Individual Assignment)
BSEM1201F, Software Engineering and Multimedia
Lecturer: Mr. Amadu Kamara 
Lecturer GitHub: AmaduKamara
Limkokwing University of Creative Technology, Sierra Leone
GitHub: AKK041705
