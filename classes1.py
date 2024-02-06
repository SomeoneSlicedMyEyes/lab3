class SimpleStringManipulator:
    def __init__(self, input_string=""):
        self.input_string = input_string.upper()

    def print_string(self):
        print(self.input_string)

simple_manipulator = SimpleStringManipulator(input(": "))
simple_manipulator.print_string()
