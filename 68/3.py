# Write your code here
water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
coffee = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
demand = int(input("Write how many cups of coffee you will need:\n"))
capacity = min(water // 200, milk // 50, coffee // 15)
if capacity < demand:
    print(f"No, I can make only {capacity} cups of coffee")
elif capacity == demand:
    print("Yes, I can make that amount of coffee")
elif capacity > demand:
    print(f"Yes, I can make that amount of coffee (and even {capacity - demand} more than that)")