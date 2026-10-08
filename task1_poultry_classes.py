# poultry class
class Poultry:
    def __init__(self, bird_id, breed, age_weeks, health_status, vaccinated):
        self.bird_id = bird_id
        self.breed = breed
        self.age_weeks = age_weeks
        self.health_status = health_status
        self.vaccinated = vaccinated

    def display_info(self):
        print("\n----------poultry information----------")
        print(f"ID : {self.bird_id}")
        print(f"Breed : {self.breed}")
        print(f"Age (weeks) : {self.age_weeks}")
        print(f"Health status : {self.health_status}")
        print(f"Vaccinated : {self.vaccinated}")

    def update_health(self, new_status):
        self.health_status = new_status
        print(f"Bird {self.bird_id} health updated to {new_status}.")

    def vaccinate(self):
        self.vaccinated = True
        print(f"Bird {self.bird_id} has been vaccinated.")


# farm class
class Farm:
    def __init__(self, farm_name, location):
        self.farm_name = farm_name
        self.location = location

    def display_info(self):
        print("\n----------farm information----------")
        print(f"Farm name : {self.farm_name}")
        print(f"Location : {self.location}")

    def inspect(self, bird):
        print(f"\n{self.farm_name} is inspecting bird {bird.bird_id}...")
        if bird.health_status == "Sick":
            bird.update_health("Under treatment")
        if not bird.vaccinated:
            bird.vaccinate()


# poultry objects
bird1 = Poultry("P001", "Broiler", 6, "Healthy", False)
bird2 = Poultry("P002", "Layer", 20, "Healthy", True)
bird3 = Poultry("P003", "Kuroiler", 12, "Sick", False)

# farm object
farm1 = Farm("Kafallah women poultry farm", "Makeni, Sierra Leone")

farm1.display_info()
bird1.display_info()
bird2.display_info()
bird3.display_info()