class Robot:

    def __init__(self):
        self.x_coordinate = 10
        self.y_coordinate = 10
        self.fuel_amount = 100

    def left(self):
        if self.fuel_amount >= 5:
            self.x_coordinate -= 1
            self.fuel_amount -= 5
        else:
            print('Insufficient fuel to perform action')
    
    def right(self):
        if self.fuel_amount >= 5:
            self.x_coordinate += 1
            self.fuel_amount -= 5
        else:
            print('Insufficient fuel to perform action')

    def up(self):
        if self.fuel_amount >= 5:
            self.y_coordinate -= 1
            self.fuel_amount -= 5
        else:
            print('Insufficient fuel to perform action')
    
    def down(self):
        if self.fuel_amount >= 5:
            self.y_coordinate += 1
            self.fuel_amount -= 5
        else:
            print('Insufficient fuel to perform action')

    def fire(self):
        if self.fuel_amount >= 15:
            print('Pew! Pew!')
            self.fuel_amount -= 15
        else:
            print('Insufficient fuel to perform action')

    def status(self):
        print(f'({self.x_coordinate}, {self.y_coordinate}) - Fuel: {self.fuel_amount}')

def main():
    play = True
    robot = Robot()

    while play:
        user_command = input('Enter command: ').lower()
        if user_command == 'left':
            robot.left()
        elif user_command == 'right':
            robot.right()
        elif user_command == 'up':
            robot.up()
        elif user_command == 'down':
            robot.down()
        elif user_command == 'fire':
            robot.fire()
        elif user_command == 'status':
            robot.status()
        elif user_command == 'quit':
            break

    print('Goodbye.')

if __name__ == "__main__":
    main()