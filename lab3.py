class Property:
    """ Description of property """
    def __init__(self, square_feet='', beds='',
        baths='', **kwargs):
        """
        Initialization of instance
        :param square_feet: area
        :param beds: amount of bedrooms
        :param baths: amount of bathrooms
        :param kwargs: allows to take unlimited amount of arguments
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        () -> None

        Display the main information.
        """
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        () -> dict{str : str}

        Take information from user
        """
        return dict(square_feet=input("Enter the square feet: "),
        beds=input("Enter number of bedrooms: "),
        baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)

class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        Initialization of instance
        :param balcony: type of balcony
        :param laundry: type of laundry
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        () -> None

        Calls the method from parent class; then prints the information.
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        parent_init = Property.prompt_init()
        laundry = ''
        while laundry.lower() not in \
                Apartment.valid_laundries:
            laundry = input("What laundry facilities does "
                    "the property have? ({})".format(
                    ", ".join(Apartment.valid_laundries)))
        balcony = ''
        while balcony.lower() not in \
                Apartment.valid_balconies:
            balcony = input(
                    "Does the property have a balcony? "
                    "({})".format(
                    ", ".join(Apartment.valid_balconies)))
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    def prompt_init():
        """
        () -> dict{str : str}

        Calls the method from parent class; then take additional information.
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")
    def __init__(self, num_stories='',
            garage='', fenced='', **kwargs):
        """
        Initialize new instance
        :param num_stories: number of stories
        :param garage: type of garage
        :param fenced: type of fence
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        () -> None

        Calls the method from parent class; then prints the information.
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        () -> dict{str : str}

        Calls the method from parent class; then take additional information.
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                    House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    """
    Gets data from user.
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Purchase:
    """ The class which represents the purchase."""
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        """
        Initialize new instance
        :param num_stories: number of stories
        :param garage: type of garage
        :param fenced: type of fence
        """
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        () -> None

        Calls the method from parent class; then prints the information.
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        () -> dict{str : str}

        Calls the method from parent class; then take additional information.
        """
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    def __init__(self, furnished='', utilities='',
            rent='', **kwargs):
        """
        Initialize new instance
        :param furnished: state of furnishing
        :param utilities: utilities
        :param rent: amount of money to pay
        """
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        () -> None

        Calls the method from parent class; then prints the information.
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
        self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        () -> dict{str : str}

        Calls the method from parent class; then take additional information.
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                    ("yes", "no")))
    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """Represents house for rent"""
    def prompt_init():
        """Calls methods from parent classes"""
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """Represents apartment for rent"""
    def prompt_init():
        """Calls methods from parent classes"""
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """Represents apartment for purchasing"""
    def prompt_init():
        """Calls methods from parent classes"""
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """Represents apartment for purchasing"""
    def prompt_init():
        """Calls methods from parent classes"""
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    def __init__(self):
        """
        Initialize new instance
        """
        self.property_list = [(("house", "rental"), HouseRental),
                              (("house", "purchase"), HousePurchase),
                              (("apartment", "rental"), ApartmentRental),
                              (("apartment", "purchase"), ApartmentPurchase)]

    def display_properties(self):
        """
        Display property
        """
        for property in self.property_list:
            property.display()

    def adding_property(self):
        """
        Add property and option
        """
        property_type = get_valid_input("Type of property: ",
                                        ("house", "apartment")).lower()
        option_type = get_valid_input("Type of option: ",
                                        ("purchase", "rentak")).lower()
