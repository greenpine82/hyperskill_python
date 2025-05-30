class CoffeeMachine:

    def __init__(self):
        self.storage = [400, 540, 120, 9, 550]
        self.drinks = [[-250, 0, -16, -1, 4], [-350, -75, -20, -1, 7], [-200, -100, -12, -1, 6]]


    def remaining(self):
    
        def status(storage):
            print("The coffee machine has:\n",
                f"{storage[0]} ml of water\n",
                f"{storage[1]} ml of milk\n",
                f"{storage[2]} g of coffee beans\n",
                f"{storage[3]} disposable cups\n",
                f"${storage[4]} of money", sep='')


        print("")
        status(self.storage)
        print("")


    def buy(self):

        def sum_array(a, b):
            return [x + y for x, y in zip(a, b)]


        user_input = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if user_input == "back":
            return
        option = int(user_input)
        result = sum_array(self.storage, self.drinks[option - 1])
        res_name = ["water", "milk", "coffee", "cup"]
        for x, y in zip(result[:-1], res_name):
            if x < 0:
                print(f"Sorry, not enough {y}!")
                print("")
                return
        print("I have enough resources, making you a coffee!")
        print("")
        self.storage = result


    def fill(self):
        self.storage[0] += int(input("Write how many ml of water you want to add:\n"))
        self.storage[1] += int(input("Write how many ml of milk you want to add:\n"))
        self.storage[2] += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.storage[3] += int(input("Write how many disposable cups you want to add:\n"))
        print("")


    def take(self):
        print(f"I gave you ${self.storage[4]}")
        self.storage[4] = 0
        print("")


    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == "exit":
                break
            if action == "remaining":
                self.remaining()
                continue
            if action == "buy":
                self.buy()
                continue
            if action == "fill":
                self.fill()
                continue
            if action == "take":
                self.take()
                continue


if __name__ == "__main__":
    CoffeeMachine().start()