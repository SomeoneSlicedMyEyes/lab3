class SimpleStringManipulator:
    def __init__(self):
        self.input_string = ""

    def get_string(self):
        self.input_string = input().upper()

    def print_string(self):
        print(self.input_string)

simple_manipulator = SimpleStringManipulator()
simple_manipulator.get_string()
simple_manipulator.print_string()
