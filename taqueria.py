#MMM MKHABELE
#06/07/2023
def main():
    try:
        total=0
        while True:
            menu={"Baja Taco": 4.00,"Burrito": 7.50,"Bowl": 8.50,"Nachos": 11.00,"Quesadilla": 8.50,"Super Burrito": 8.50,"Super Quesadilla": 9.50,"Taco": 3.00,"Tortilla Salad": 8.00}
            meal=input("Item: ")
            if meal.title() in menu:
                 price=menu[meal.title()]
                 total+=price
                 print('Total: ${:.2f}'.format(total))
            else:
                 print("F")
                 continue

    except:
            pass
main()