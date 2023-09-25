class Property:
    def __init__(self, address, price, bedrooms, bathrooms):
        self.address = address
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

class Realtor:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)
        print(f"Property at {property.address} added to {self.name}'s listings.")

    def list_properties(self):
        print(f"{self.name}'s Property Listings:")
        for i, property in enumerate(self.properties, start=1):
            print(f"{i}. Address: {property.address}, Price: ${property.price}, Bedrooms: {property.bedrooms}, Bathrooms: {property.bathrooms}")

    def search_properties(self, max_price, min_bedrooms):
        print(f"Searching properties under ${max_price} with at least {min_bedrooms} bedrooms:")
        matching_properties = [property for property in self.properties if property.price <= max_price and property.bedrooms >= min_bedrooms]
        if matching_properties:
            for i, property in enumerate(matching_properties, start=1):
                print(f"{i}. Address: {property.address}, Price: ${property.price}, Bedrooms: {property.bedrooms}, Bathrooms: {property.bathrooms}")
        else:
            print("No matching properties found.")

def main():
    realtor_name = input("Enter the realtor's name: ")
    realtor = Realtor(realtor_name)

    while True:
        print("\nOptions:")
        print("1. Add a property")
        print("2. List all properties")
        print("3. Search properties")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            address = input("Enter the property address: ")
            price = float(input("Enter the property price: $"))
            bedrooms = int(input("Enter the number of bedrooms: "))
            bathrooms = int(input("Enter the number of bathrooms: "))
            property = Property(address, price, bedrooms, bathrooms)
            realtor.add_property(property)
        elif choice == '2':
            realtor.list_properties()
        elif choice == '3':
            max_price = float(input("Enter the maximum price: $"))
            min_bedrooms = int(input("Enter the minimum number of bedrooms: "))
            realtor.search_properties(max_price, min_bedrooms)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
