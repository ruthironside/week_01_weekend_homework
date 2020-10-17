# 1. 
def get_pet_shop_name(petshop):
    return petshop ["name"]

# 2.
def get_total_cash(money):
    return money ["admin"]["total_cash"]

# 3.
def add_or_remove_cash(money, amount_added_or_removed):
    money ["admin"]["total_cash"] += amount_added_or_removed
    

# 4.

# 5. 
def get_pets_sold(sold):
    return sold ["admin"]["pets_sold"]

# 6.
def increase_pets_sold(sold, amount_sold):
    sold ["admin"]["pets_sold"] += amount_sold

# 7.
def get_stock_count(stock):
    return len(stock["pets"])


# 8.
def get_pets_by_breed(pet_shop_info, breed_type):
    breed_list = []
    for pet in pet_shop_info["pets"]:
        if pet["breed"] == breed_type:
            breed_list.append(pet["breed"])
    return breed_list


# 9.

def get_pets_by_breed(pet_shop_info, breed_type):
    breed_list = []
    for pet in pet_shop_info["pets"]:
        if pet["breed"] == breed_type:
            breed_list.append(pet["breed"])
    return breed_list

# print(["breed"]"Dalmation")

# 10.
def find_pet_by_name(shop, pet_name):
    for name in shop["pets"]:
        if name["name"] == pet_name:

            return name

# print(find_pet_by_name(["pets"]["name"], 2))
# 11.
def find_pet_by_name(shop, pet_name):
    for name in shop["pets"]:
        if name["name"] == pet_name:

            return name


            
# 12.
# 13.
# 14.
# def get_customer_cash(customer):
#   total_money = 0
#   for customer in customers:
#     total_money += customer["cash"]
  
#   return total_money
# 15.
# 16.
# 17.

