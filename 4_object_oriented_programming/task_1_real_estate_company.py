class Customer:
    def __init__(self, email: str, first_name: str, tax_percent: int):
        self.email = email
        self.first_name = first_name
        self.tax_percent = tax_percent

    def total_amount(self, price: float) -> float:
        """Method accept a price of a flat and return total amount including tax for service for simple customer"""
        self.price = price
        total_price_after_tax = price + round(price * (self.tax_percent / 100))
        return total_price_after_tax

    def __str__(self):
        return f"Customer: {self.first_name}, {self.email}"


class LoyalCustomer(Customer):

    def __init__(self, email: str, name: str, tax_percent: int):
        super().__init__(email, name, tax_percent)


class Flat:
    def __init__(self, price: int, address: str):
        self.price = price
        self.address = address

    def show_information(self):
        print(self.address)
        print(self.price)

    def __str__(self):
        return f"Flat: {self.price}, {self.address}"


class RealEstateCompany():
    def __init__(self, flats: list[Flat], customers: list[Customer]):
        self.flats = flats
        self.customers = customers

    def __str__(self):
        return f"Flats and customers: {self.flats}, {self.customers}"

    def cheapest(self):
        """Method find and return a flat with the smallest price"""
        if not self.flats:
            print("Sorry, no flats for this time")
            return None
        cheapest_flat = self.flats[0]
        for flat in self.flats:
            if flat.price < cheapest_flat.price:
                cheapest_flat = flat
        return cheapest_flat

    def sell(self, flat: Flat, customers: Customer):
        """Method find and return a flat which was sold with customer information"""
        if flat not in self.flats:
            print("Sorry, flat is not found")
        elif customers not in self.customers:
            print("Sorry, you are not our client, please fill the form to become a partner")
        else:
            message = f'Flat {flat.address} is sold for {flat.price}, name: {customers.first_name}, email: {customers.email}'
            print(message)
            self.flats.remove(flat)


c1 = Customer("jane@gmail.com", "Jane", 2)
c2 = Customer("tom@gmail.com", "Tom", 2)
c3 = Customer("bob@gmail.com", "Bob", 2)
lc1 = LoyalCustomer("sam@gmail.com", "Sam", 1)
lc2 = LoyalCustomer("sofia@gmail.com", "Sofia", 1)
c1_price = c1.total_amount(200000)
c2_price = c2.total_amount(400000)
c3_price = c3.total_amount(350000)
lc1_price = lc1.total_amount(340000)
lc2.total_amount(500000)
flat1 = Flat(200000, "Daukanto 30")
flat2 = Flat(300000, "Lazdyneliu 48")
flat3 = Flat(400000, "Zveryno 24")
flat4 = Flat(400000, "Upes 60")

flats = [flat1, flat2, flat3, flat4]
customers = [c1, c2, c3]

print(c1_price)
print(lc1_price)

real_estate_company = RealEstateCompany(flats, customers)
print(str(real_estate_company))
cheapest_flat = real_estate_company.cheapest()
print(cheapest_flat.price)

real_estate_company.sell(cheapest_flat, c1)
real_estate_company.sell(cheapest_flat, c2)
# real_estate_company.sell(cheapest_flat, lc1)
