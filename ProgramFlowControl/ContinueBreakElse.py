# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         continue
#     print("Buy " + item)

# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         break
#     print("Buy " + item)

meal = ["egg", "bacon", "tomato", "spam", "sausages"]
nasty_food_item = ""

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:  # Will only run if there is no spam in meal (no break during for)
    print("I'll have a plate of that, then, please")

if nasty_food_item:
    print("Can't I have anything without spam in it")
