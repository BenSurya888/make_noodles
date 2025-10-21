# TASK 1.1
print("===========TASK 1.1===========\n")
def open_water_valve(seconds):
    water_flow = seconds * 100
    return water_flow

water = open_water_valve(3)
print(f"Water flow: {water} ml")

# TASK 1.2
print("\n===========TASK 1.2===========\n")
def is_temperature_ok(current_temp):
    if current_temp >= 75 and current_temp <= 80:
        return True
    else:
        return False
print(is_temperature_ok(78))
print(is_temperature_ok(72))

# TASK 1.3
print("\n===========TASK 1.3===========\n")
def add_seasoning(ketchup_ml,sausage_ml,powder_ml):
    check_ketchup = 3
    check_sausage = 2
    check_powder = 3

    if ketchup_ml == check_ketchup and sausage_ml == check_sausage and powder_ml == check_powder:
        return "Seasoning is correct"
    else:
        return "Incorrect seasoning"
    
print(add_seasoning(3,2,3))
print(add_seasoning(2,2,3))

# TASK 2.1
print("\n===========TASK 2.1===========\n")
def fill_bucket(target_amount):
    seconds_needed = target_amount / 100
    return seconds_needed

print(fill_bucket(300))
print(f"Need {fill_bucket(300)} seconds to fill 300ml")

# TASK 2.2
print("\n===========TASK 2.2===========\n")
def heat_water(current_temp, target_temp):
    temp_difference = target_temp - current_temp
    secconds_needed = temp_difference / 5
    return secconds_needed

print(heat_water(70,80))
print(f"Need {heat_water(70,80)} seconds to heat water from 70C to 80C")

# TASK 2.3
print("\n===========TASK 2.3===========\n")
def maintain_temperature(current_temp, target_temp ):
    if current_temp >= 75 and current_temp <= 80:
        return "MAINTAIN"
    
    elif current_temp < target_temp:
        return "INCREASE"
    else:
        return "DECREASE"
    
print(maintain_temperature(78,80))
print(maintain_temperature(70,80))
print(maintain_temperature(82,80))

# TASK 2.4
print("\n===========TASK 2.4===========\n")
def cook_noodle(cooking_seconds):
    if cooking_seconds >= 120:
        return "READY"
    else:
        return "COOKING"
    
print(cook_noodle(130))
print(cook_noodle(90))

# TASK 2.5
print("\n===========TASK 2.5===========\n")
def dispense_all_seasoning():
    ketchup_amount = 3
    sausage_amount = 2
    powder_amount = 3

    all_seasoning = {
    "ketchup": ketchup_amount,
    "sausage": sausage_amount,
    "powder": powder_amount
    }
    return all_seasoning

seasonings = dispense_all_seasoning()
print(seasonings)

# TASK 3.1
print("\n===========TASK 3.1===========\n")
class WaterSystem:
    def __init__(self):
        self.tank_capacity = 5000
        self.current_water_in_tank = 5000 
        self.bucket_capacity = 500
        self.current_water_in_bucket = 0
        self.current_temperature = 25
        self.is_valve_open = False 

    def open_valve(self, seconds):
        self.is_valve_open = True
        water_flow = seconds * 100

        if self.current_water_in_bucket + water_flow > self.bucket_capacity:
            water_added = self.bucket_capacity - self.current_water_in_bucket
            print(f"bucket overflow! Only added {water_added} ml to fill the bucket.")

        if water_flow > self.current_water_in_tank:
            water_flow = self.current_water_in_tank
            print("not enough water in tank to fill the bucket completely.")

        self.current_water_in_bucket += water_flow
        self.current_water_in_tank -= water_flow
        self.is_valve_open = False

    def heat_up(self,seconds):
        temperature_increase = seconds * 5
        self.current_temperature += temperature_increase

        if self.current_temperature > 100:
            self.current_temperature = 100
            print("water temperature has reached the maximum limit of 100C.")
    
    def cool_down(self,seconds):
        temperature_decrease = seconds * 5
        self.current_temperature -= temperature_decrease

        if self.current_temperature < 0:
            self.current_temperature = 0
            print("water temperature has reached the minimum limit of 0C.")

    def empty_bucket(self):
        self.current_water_in_bucket = 0
        print("bucket has been emptied.")

    def get_status(self):
        status = {
            "current_water_in_tank": self.current_water_in_tank,
            "current_water_in_bucket": self.current_water_in_bucket,
            "current_temperature": self.current_temperature
        }
        return status
    
water_system = WaterSystem()
water_system.open_valve(3)
print(water_system.current_water_in_bucket)
print(water_system.current_water_in_tank)

water_system.heat_up(11)
print(water_system.current_temperature)

# TASK 3.2
print("\n===========TASK 3.2===========\n")
class Dispenser:
    def __init__(self,name,capacity,ml_per_trigger):
        self.name = name
        self.capacity = capacity
        self.current_amount = capacity
        self.ml_per_trigger = ml_per_trigger

    def trigger(self,times = 1):
        total_dispensed = times * self.ml_per_trigger
        if total_dispensed > self.current_amount:
            total_dispensed = self.current_amount
            print(f"{self.name} dispenser is out of seasoning!")
        self.current_amount -= total_dispensed
        print(f"Dispensed {total_dispensed} ml from {self.name} dispenser.")
        return total_dispensed

    def refill(self):
        self.current_amount = self.capacity
        print(f"{self.name} dispenser has been refilled to {self.capacity} ml.")
    
    def get_status(self):
        status = {
            "name": self.name,
            "capacity": self.capacity,
            "current_amount": self.current_amount,
            "ml_per_trigger": self.ml_per_trigger
        }
        return status
    
ketchup_dispenser = Dispenser("Ketchup",capacity=1000,ml_per_trigger=1 ) 
dispensed = ketchup_dispenser.trigger(3)
print(f"{dispensed} ml")
print(f"{ketchup_dispenser.current_amount} ml")

class NoodleMachine:
    def __init__(self):
        self.water_system = WaterSystem()
        self.noodles_dispenser = Dispenser("Noodles",capacity=50,ml_per_trigger=1 )
        self.ketchup_dispenser = Dispenser("Ketchup",capacity=1000,ml_per_trigger=1 )
        self.sausage_dispenser = Dispenser("Sausage",capacity=1000,ml_per_trigger=1 )
        self.powder_dispenser = Dispenser("Powder",capacity=1000,ml_per_trigger=1 )
        self.noodles_made = 0

    def make_noodles(self):
        print("\n" + "="*30)
        print("STARTING NOODLE MAKING PROCESS")
        print("="*30)
        
        print("\n1. FILLING WATER")
        seconds_to_fill = 300 / 100 
        self.water_system.open_valve(seconds_to_fill)
        
        print("\n2. HEATING WATER")
        seconds_to_heat = (77 - 25) / 5
        self.water_system.heat_up(seconds_to_heat)
        
        print("\n3. DISPENSING NOODLE")
        self.noodles_dispenser.trigger(1)
        
        print("\n4. COOKING NOODLE")
        print("Cooking for 120 seconds")
        
        print("\n5. ADDING SEASONINGS")
        self.ketchup_dispenser.trigger(3)
        self.sausage_dispenser.trigger(2) 
        self.powder_dispenser.trigger(3)
        
        print("\n6. SERVING")
        self.noodles_made += 1
        print("Noodle is ready")
        
        print("\n7. CLEANING")
        self.water_system.empty_bucket()
        
        print("="*30)
        print("PROCESS COMPLETED")
        print("="*30)
    
    def get_machine_status(self):
        print("\n" + "="*50)
        print("MACHINE STATUS")
        print("="*50)
        
        print(self.water_system.get_status())
        
        print(f"Noodles {self.noodles_dispenser.get_status()}")
        print(f"Ketchup{self.ketchup_dispenser.get_status()}")
        print(f"Sausage {self.sausage_dispenser.get_status()}")
        print(f"Powder {self.powder_dispenser.get_status()}")
        
        print(f"Noodles Made: {self.noodles_made}")
        
        print("="*50)
        
        #print("\n=== EXAMPLE TEST ===")
        #machine = NoodleMachine()

        #machine.get_machine_status()

        #machine.make_noodle()

        #machine.get_machine_status()

# Create the machine
print("🍜 INSTANT NOODLE MAKER MACHINE")
print("="*50)

machine = NoodleMachine()

# Show initial status
print("\n📊 INITIAL STATUS:")
machine.get_machine_status()

# Make first noodle
print("\n" + "="*50)
print("🍜 MAKING NOODLE #1...")
print("="*50)
machine.make_noodles()

# Make second noodle
print("\n" + "="*50)
print("🍜 MAKING NOODLE #2...")
print("="*50)
machine.make_noodles()

# Show final status
print("\n📊 FINAL STATUS:")
machine.get_machine_status()

