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

    # static method: needs neither self nor cls
    @staticmethod
    def is_valid_age(age_weeks):
        return age_weeks > 0


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

# display all records
farm1.display_records()

# class method and static method
Poultry.get_total_birds()
print(Poultry.is_valid_age(5))
print(Poultry.is_valid_age(0))