from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()
coffee = CoffeeMaker()

is_on = True
# is that is boolean?

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like to oder ? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)

    # 这里的意思是把用户点的咖啡种类传入到咖啡名称对应的字典里去匹配咖啡需要的资源和花费，然后把对应的资源传入到
    # 检查资源是否足够完成用户订单的function里，如果if是true，那么就可以接着投钱，如果是false，程序就结束里
    # 这里的意思是调用money.machine里的payment，然后把饮料的名字传入去对应，然后调用cost
