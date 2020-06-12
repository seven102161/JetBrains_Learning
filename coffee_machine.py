class CoffeeMachine:
    money = 550
    water = 400
    milk = 540
    beans = 120
    dis_cups = 9

    def __init__(self):
        self.money = CoffeeMachine.money
        self.water = CoffeeMachine.water
        self.milk = CoffeeMachine.milk
        self.beans = CoffeeMachine.beans
        self.dis_cups = CoffeeMachine.dis_cups
        self.type = None

    def action_remaing(self):
        print('\nThe coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n{} of money\n'.format(
            self.water, self.milk, self.beans, self.dis_cups, self.money))
        pass

    def action_buy(self):
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        self.type = input()
        if self.type == '1':
            self.buy_espresso()
        elif self.type == '2':
            self.buy_latte()
        elif self.type == '3':
            self.buy_cappuccino()
        elif self.type == 'back':
            print()
            return None
        else:
            print('Wrong type\n')
            return None

    def buy_espresso(self):
        if self.water < 250:
            print('Sorry, not enough water!\n')

            if self.beans < 16:
                print('Sorry, not enough coffee beans!\n')

                if self.dis_cups < 1:
                    print('Sorry, not enough disposable cups!\n')

        else:
            print('I have enough resources, making you a coffee!\n')

            CoffeeMachine.water -= 250
            CoffeeMachine.beans -= 16
            CoffeeMachine.money += 4
            CoffeeMachine.dis_cups -= 1

    def buy_latte(self):
        if self.water < 350:
            print('Sorry, not enough water!\n')

            if self.milk < 75:
                print('Sorry, not enough milk!\n')

                if self.beans < 20:
                    print('Sorry, not enough coffee beans!\n')

                    if self.dis_cups < 1:
                        print('Sorry, not enough disposable cups!\n')

        else:
            print('I have enough resources, making you a coffee!')
            print()
            CoffeeMachine.water -= 350
            CoffeeMachine.milk -= 75
            CoffeeMachine.beans -= 20
            CoffeeMachine.money += 7
            CoffeeMachine.dis_cups -= 1

    def buy_cappuccino(self):
        if self.water < 200:
            print('Sorry, not enough water!\n')

            if self.milk < 100:
                print('Sorry, not enough milk!\n')

                if self.beans < 12:
                    print('Sorry, not enough coffee beans!\n')

                    if self.dis_cups < 1:
                        print('Sorry, not enough disposable cups!\n')

        else:
            print('I have enough resources, making you a coffee!\n')

            CoffeeMachine.water -= 200
            CoffeeMachine.milk -= 100
            CoffeeMachine.beans -= 12
            CoffeeMachine.money += 6
            CoffeeMachine.dis_cups -= 1

    def action_fill(self):
        print()
        print('Write how many ml of water do you want to add:')
        CoffeeMachine.water += int(input())
        print('Write how many ml of milk do you want to add:')
        CoffeeMachine.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        CoffeeMachine.beans += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        CoffeeMachine.dis_cups += int(input())
        print()


    def action_take(self):
        print('\nI gave you ${}\n'.format(self.money))
        CoffeeMachine.money = 0


while True:
    print('Write action (buy, fill, take, remaining, exit):')
    customer = CoffeeMachine()
    action = input().lower()
    if action == 'exit':
        break

    elif action == 'buy':
        customer.action_buy()

    elif action == 'remaining':
        customer.action_remaing()

    elif action == 'fill':
        customer.action_fill()

    elif action == 'take':
        customer.action_take()

    else:
        print('Wrong action\n')
        continue
