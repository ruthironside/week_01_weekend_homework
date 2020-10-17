# 1. 
def get_pet_shop_name(petshop):
    return petshop ["name"]

# 2.
def get_total_cash(money):
    return money ["admin"]["total_cash"]

# 3.
# def test_add_or_remove_cash__add(money):
#   add_or_remove_cash = []
#   for money in monies:
#     add_or_remove_cash += money["admin"]["total_cash"]
#   return add_or_remove_cash
    

# 4.

# 5. 
def get_pets_sold(sold):
    return sold ["admin"]["pets_sold"]

# 6.
# def get_pets_sold(sold):
#   sold["pets_sold"] += 2

# def get_pets_sold(sold):
#   return ["admin]["pets_sold"].append()

# 7.
def get_stock_count(dict):
    return len(dict["pets"])


# 8.
def get_pets_by_breed(pet_shop_info, breed_type):
    breed_list = []
    for pet in pet_shop_info["pets"]:
        if pet["breed"] == breed_type:
            breed_list.append(pet["breed"])
    return breed_list




# 9.
# 10.
# def find_pet_by_name( list, pet_name ):
#   found_pet = None
#   for pet in list:
#     if pet["pets]["name"] == pet_name:
#       found_pet = pet

#   return found_pet
# 11.
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

