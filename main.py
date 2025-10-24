import time

# TASK 1.1
print("===========TASK 1.1===========\n")
SIM_SPEED = 0.2  # speed multiplier; lower -> faster simulation

def open_water_valve(seconds):
    """Open valve incrementally; each second adds 100ml.
    Returns total water flow after given seconds."""
    while True:
        flowed = 0
        elapsed = 0
        while elapsed < seconds:
            time.sleep(1 * SIM_SPEED)
            flowed += 100
            elapsed += 1
            print(f"Valve flow +100ml (total={flowed}ml)")
        return flowed

water = open_water_valve(3)
print(f"Water flow: {water} ml")

# TASK 1.2
print("\n===========TASK 1.2===========\n")
def is_temperature_ok(current_temp):
    while True :
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
    while True:
        # simulate checking each ingredient
        time.sleep(0.5 * SIM_SPEED)
        print("Checking ketchup...")
        time.sleep(0.5 * SIM_SPEED)
        print("Checking sausage...")
        time.sleep(0.5 * SIM_SPEED)
        print("Checking powder...")
        if ketchup_ml == check_ketchup and sausage_ml == check_sausage and powder_ml == check_powder:
            print("All seasoning correct")
            return "SEASONING ADDED"
        else:
            print("Seasoning mismatch")
            return "SEASONING AMOUNT INCORRECT"
    
print(add_seasoning(3,2,3))
print(add_seasoning(2,2,3))

# TASK 2.1
print("\n===========TASK 2.1===========\n")
def fill_bucket(target_amount):
    """Fill bucket 100ml per simulated second; return seconds taken."""
    while True:
        filled = 0
        seconds = 0
        while filled < target_amount:
            time.sleep(1 * SIM_SPEED)
            add = 100
            if filled + add > target_amount:
                add = target_amount - filled
            filled += add
            seconds += 1
            print(f"Bucket +{add}ml (current={filled}/{target_amount}ml)")
        return seconds
    
print(fill_bucket(300))
print(f"Need {fill_bucket(300)} seconds to fill 300ml")

# TASK 2.2
print("\n===========TASK 2.2===========\n")
def heat_water(current_temp, target_temp):
    while True:
        temp = current_temp
        steps = 0
        while temp < target_temp:
            time.sleep(1 * SIM_SPEED)
            temp += 5
            if temp > target_temp:
                temp = target_temp
            steps += 1
            print(f"Heating... temp={temp}C")
        return steps

print(heat_water(70,80))
print(f"Need {heat_water(70,80)} seconds to heat water from 70C to 80C")

# TASK 2.3
print("\n===========TASK 2.3===========\n")
def maintain_temperature(current_temp, target_temp ):
    while True :
        if current_temp < target_temp:
            return "HEATING"
        elif current_temp > target_temp:
            return "COOLING"
        else:
            return "STABLE"
    
print(maintain_temperature(78,80))
print(maintain_temperature(70,80))
print(maintain_temperature(82,80))

# TASK 2.4
print("\n===========TASK 2.4===========\n")
def cook_noodle(cooking_seconds):
    while True:
        elapsed = 0
        while elapsed < cooking_seconds:
            time.sleep(1 * SIM_SPEED)
            elapsed += 1
            if elapsed % 30 == 0 or elapsed == cooking_seconds:
                print(f"Cooking progress {elapsed}/{cooking_seconds}")
        return "NOODLE COOKED" if cooking_seconds >= 120 else "COOKING INCOMPLETE"
        
print(cook_noodle(130))
print(cook_noodle(90))

# TASK 2.5
print("\n===========TASK 2.5===========\n")
def dispense_all_seasoning():
    ketchup_amount = 3
    sausage_amount = 2
    powder_amount = 3
    while True:
        dispensed = {}
        for name, amt in [("ketchup_ml", ketchup_amount), ("sausage_ml", sausage_amount), ("powder_ml", powder_amount)]:
            time.sleep(0.3 * SIM_SPEED)
            print(f"Dispensing {name} ({amt}ml)")
            dispensed[name] = amt
        return dispensed

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
        while True:
            added = 0
            for _ in range(seconds):
                time.sleep(1 * SIM_SPEED)
                flow = 100
                if flow > self.current_water_in_tank:
                    flow = self.current_water_in_tank
                if self.current_water_in_bucket + flow > self.bucket_capacity:
                    flow = self.bucket_capacity - self.current_water_in_bucket
                if flow <= 0:
                    break
                self.current_water_in_bucket += flow
                self.current_water_in_tank -= flow
                added += flow
                print(f"Valve added {flow}ml (bucket={self.current_water_in_bucket}/{self.bucket_capacity})")
                if self.current_water_in_bucket >= self.bucket_capacity or self.current_water_in_tank <= 0:
                    break
            return added

    def heat_up(self,seconds):
        while True:
            increased = 0
            for _ in range(seconds):
                time.sleep(1 * SIM_SPEED)
                if self.current_temperature >= 100:
                    break
                self.current_temperature += 5
                increased += 5
                if self.current_temperature > 100:
                    self.current_temperature = 100
                print(f"Heating... {self.current_temperature}C")
            return increased
    
    def cool_down(self,seconds):
        while True:
            decreased = 0
            for _ in range(seconds):
                time.sleep(1 * SIM_SPEED)
                if self.current_temperature <= 25:
                    break
                self.current_temperature -= 5
                decreased -= 5
                if self.current_temperature < 25:
                    self.current_temperature = 25
                print(f"Cooling... {self.current_temperature}C")
            return decreased

    def empty_bucket(self):
        while True :
            self.current_water_in_bucket = 0
            break

    def get_status(self):
        while True :
            status = {
                "tank_capacity": self.tank_capacity,
                "current_water_in_tank": self.current_water_in_tank,
                "bucket_capacity": self.bucket_capacity,
                "current_water_in_bucket": self.current_water_in_bucket,
                "current_temperature": self.current_temperature,
                "is_valve_open": self.is_valve_open
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
        while True:
            dispensed = 0
            for i in range(times):
                if self.current_amount <= 0:
                    print(f"{self.name} empty.")
                    break
                time.sleep(0.3 * SIM_SPEED)
                if self.ml_per_trigger > self.current_amount:
                    amount = self.current_amount
                else:
                    amount = self.ml_per_trigger
                self.current_amount -= amount
                dispensed += amount
                print(f"Trigger {i+1}/{times}: {amount}ml {self.name} (left={self.current_amount}ml)")
            return dispensed

    def refill(self):
        while True :
            self.current_amount = self.capacity
            break
        print(f"{self.name} dispenser has been refilled to {self.capacity} ml.")
    
    def get_status(self):
        while True :
            status = f"[{self.current_amount} ml / {self.capacity} ml]"
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
        while True:
            print("-- Filling water bucket --")
            self.water_system.open_valve(3)
            print(f"Bucket now {self.water_system.current_water_in_bucket}ml")

            print("-- Heating water to 80C --")
            while self.water_system.current_temperature < 80:
                self.water_system.heat_up(1)
            print(f"Water ready at {self.water_system.current_temperature}C")

            print("-- Dispensing noodles --")
            noodles_dispensed = self.noodles_dispenser.trigger(1)

            print("-- Cooking noodles --")
            cook_result = cook_noodle(130)  # use cooking_seconds > 120 for cooked
            print(f"Cooking result: {cook_result}")

            print("-- Adding seasonings --")
            ketchup_dispensed = self.ketchup_dispenser.trigger(3)
            sausage_dispensed = self.sausage_dispenser.trigger(2)
            powder_dispensed = self.powder_dispenser.trigger(3)

            print("-- Emptying bucket --")
            self.water_system.empty_bucket()

            self.noodles_made += 1
            print(f"Noodle batch #{self.noodles_made} complete")
            return {
                "noodles": noodles_dispensed,
                "ketchup": ketchup_dispensed,
                "sausage": sausage_dispensed,
                "powder": powder_dispensed,
                "temperature": self.water_system.current_temperature
            }
    
    def get_machine_status(self):
        while True :
            status = {
                "noodles_made": self.noodles_made,
                "water_system": self.water_system.get_status(),
                "noodles_dispenser": self.noodles_dispenser.get_status(),
                "ketchup_dispenser": self.ketchup_dispenser.get_status(),
                "sausage_dispenser": self.sausage_dispenser.get_status(),
                "powder_dispenser": self.powder_dispenser.get_status()
            }
            for key, value in status.items():
                print(f"{key}: {value}")
            break

while True :
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
    break

