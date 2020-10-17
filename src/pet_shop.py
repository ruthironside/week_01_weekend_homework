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


# 10.
def find_pet_by_name(pet_shop_info, pet_name):
    for name in pet_shop_info["pets"]:
        if name["name"] == pet_name:

            return name

# 11.
def find_pet_by_name(pet_shop_info, pet_name):
    for name in pet_shop_info["pets"]:
        if name["name"] == pet_name:

            return name


# 12.
def remove_pet_by_name(pet_shop_info, pet_name):
    pet_shop_info["pets"].remove(find_pet_by_name(pet_shop_info, pet_name))

#13.

def add_pet_to_stock(pet_shop_info, new_pet):
    pet_shop_info["pets"].append(new_pet)
