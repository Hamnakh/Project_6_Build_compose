# Class representing the Engine
class Engine:
    def start(self):
        print("Engine started.")


# Class representing the Car that uses Engine (composition)
class Car:
    def __init__(self, engine):
        self.engine = engine  # Engine object is stored as a part of Car

    def start_car(self):
        # Accessing the Engine's start method via composition
        print("Starting the car...")
        self.engine.start()


# Create an Engine object
my_engine = Engine()

# Pass the Engine object to the Car (composition in action)
my_car = Car(my_engine)

# Start the car, which internally starts the engine
my_car.start_car()
