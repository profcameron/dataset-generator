class Client:
    """
    Represents a client with personal information.

    Attributes:
        first_name (str): The client's first name.
        last_name (str): The client's last name.
        address (str): The client's address.
        email (str): The client's email address.
        phone (str): The client's phone number.
        ethnicity (str): The client's ethnicity.
    """
    def __init__(self, first_name, last_name, address, email, phone, ethnicity):
        """
        Initializes a Client object.

        Args:
            first_name (str): The client's first name.
            last_name (str): The client's last name.
            address (str): The client's address.
            email (str): The client's email address.
            phone (str): The client's phone number.
            ethnicity (str): The client's ethnicity.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.email = email
        self.phone = phone
        self.ethnicity = ethnicity