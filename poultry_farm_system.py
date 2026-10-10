# tuples of fixed options (these never change)
HEALTH_STATUSES = ("Healthy", "Sick", "Under treatment")
BREEDS = ("Broiler", "Layer", "Kuroiler", "Local")

# oldest age (in weeks) a bird on this farm can be
MAX_AGE_WEEKS = 104


# poultry class
class Poultry:
    # class attribute shared by all poultry objects
    total_birds = 0

    def __init__(self, bird_id, breed, age_weeks, health_status, vaccinated):
        self.bird_id = bird_id
        self.breed = breed
        self.age_weeks = age_weeks
        self.health_status = health_status
        self.vaccinated = vaccinated
        Poultry.total_birds += 1

    # instance method: shows one bird's details
    def display_info(self):
        print("\n----------poultry information----------")
        print(f"ID : {self.bird_id}")
        print(f"Breed : {self.breed}")
        print(f"Age (weeks) : {self.age_weeks}")
        print(f"Health status : {self.health_status}")
        print(f"Vaccinated : {self.vaccinated}")

    # instance method: changes one bird's health status
    def update_health(self, new_status):
        if not Poultry.is_valid_status(new_status):
            print(f"{new_status} is not a valid health status.")
            return
        self.health_status = new_status
        print(f"Bird {self.bird_id} health updated to {new_status}.")

    # instance method: marks one bird as vaccinated
    def vaccinate(self):
        self.vaccinated = True
        print(f"Bird {self.bird_id} has been vaccinated.")

    # class method: works on the class, not on one bird
    @classmethod
    def get_total_birds(cls):
        print(f"\nTotal poultry objects created: {cls.total_birds}")

    # static method: checks the age without needing self or cls
    @staticmethod
    def is_valid_age(age_weeks):
        return 1 <= age_weeks <= MAX_AGE_WEEKS

    # static method: checks the status against the tuple
    @staticmethod
    def is_valid_status(status):
        return status in HEALTH_STATUSES


# farm class
class Farm:
    def __init__(self, farm_name, location, capacity):
        self.farm_name = farm_name
        self.location = location
        self.capacity = capacity
        # list to store poultry objects
        self.birds = []

    def display_info(self):
        print("\n----------farm information----------")
        print(f"Farm name : {self.farm_name}")
        print(f"Location : {self.location}")
        print(f"Capacity : {self.capacity} birds")

    # interaction: the farm checks a bird and fixes its status
    def inspect(self, bird):
        print(f"\n{self.farm_name} is inspecting bird {bird.bird_id}...")
        if bird.health_status == "Sick":
            bird.update_health("Under treatment")
        if not bird.vaccinated:
            bird.vaccinate()

    # add a bird to the records list
    def add_record(self, bird):
        if not Poultry.is_valid_age(bird.age_weeks):
            print(f"Bird {bird.bird_id} has an invalid age. Record not added.")
            return
        for record in self.birds:
            if record.bird_id == bird.bird_id:
                print(f"Bird {bird.bird_id} is already recorded.")
                return
        if len(self.birds) >= self.capacity:
            print("Farm is full. Record not added.")
            return
        self.birds.append(bird)
        print(f"Bird {bird.bird_id} added to records.")

    # show every bird in the records list
    def display_records(self):
        print(f"\n********** {self.farm_name} records **********")
        if len(self.birds) == 0:
            print("No poultry records found.")
        else:
            for bird in self.birds:
                bird.display_info()


# show a numbered menu and repeat until the user picks a valid number
def choose_from(title, options):
    print(f"\n{title}")
    number = 1
    for option in options:
        print(f"{number}. {option}")
        number += 1
    while True:
        choice = input(f"Please enter the number of your choice (1 to {len(options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print(f"Please enter a valid number from 1 to {len(options)}.")


# repeat until the ID starts with P, is followed by numbers and is not used
def ask_bird_id(farm):
    while True:
        bird_id = input("Bird ID (starts with P, example P005): ").strip().upper()
        if not (bird_id.startswith("P") and bird_id[1:].isdigit()):
            print("Please enter a valid ID starting with P followed by numbers, for example P005.")
            continue
        used = False
        for bird in farm.birds:
            if bird.bird_id == bird_id:
                used = True
        if used:
            print(f"Please enter a different ID, {bird_id} is already recorded.")
            continue
        return bird_id


# repeat until the age is a whole number within the allowed range
def ask_age():
    while True:
        try:
            age_weeks = int(input(f"Age in weeks (1 to {MAX_AGE_WEEKS}): "))
        except ValueError:
            print("Please enter a valid age as a whole number, for example 10.")
            continue
        if Poultry.is_valid_age(age_weeks):
            return age_weeks
        print(f"Please enter a valid age between 1 and {MAX_AGE_WEEKS} weeks.")


# collect a new bird from the user and add it to the farm
def add_bird_from_input(farm):
    print("\n----------add a new bird----------")
    bird_id = ask_bird_id(farm)
    breed = choose_from("Select the breed:", BREEDS)
    age_weeks = ask_age()
    status = choose_from("Select the health status:", HEALTH_STATUSES)
    vaccinated = choose_from("Is the bird vaccinated?", ("Yes", "No")) == "Yes"
    farm.add_record(Poultry(bird_id, breed, age_weeks, status, vaccinated))


# poultry objects
bird1 = Poultry("P001", "Broiler", 6, "Healthy", False)
bird2 = Poultry("P002", "Layer", 20, "Healthy", True)
bird3 = Poultry("P003", "Kuroiler", 12, "Sick", False)
bird4 = Poultry("P004", "Layer", 8, "Healthy", True)

# farm object
farm1 = Farm("Kafallah women poultry farm", "Makeni, Sierra Leone", 500)
farm1.display_info()

# farm inspects the birds
farm1.inspect(bird1)
farm1.inspect(bird2)
farm1.inspect(bird3)

# add the birds to the farm records
farm1.add_record(bird1)
farm1.add_record(bird2)
farm1.add_record(bird3)
farm1.add_record(bird4)

# add one more bird from user input
add_bird_from_input(farm1)

# display all records
farm1.display_records()

# class method and static methods
Poultry.get_total_birds()
print(f"\nIs an age of 5 weeks valid? {Poultry.is_valid_age(5)}")
print(f"Is an age of 0 weeks valid? {Poultry.is_valid_age(0)}")
print(f"Is an age of 500 weeks valid? {Poultry.is_valid_age(500)}")
print(f"Is the status Sick valid? {Poultry.is_valid_status('Sick')}")
print(f"Is the status Flying valid? {Poultry.is_valid_status('Flying')}")