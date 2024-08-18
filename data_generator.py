import datetime
import random

def generate_client_table(size: int) -> str:
    """
    Generate the start of a data file, including the date/time, 
    and the CREATE TABLE statement.

    Args:
        size (int): The size of the ClientNum field.

    Returns:
        str: The start of the data file.
    """
    # Add date/time information
    output = "-- Fake data set generated on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n"

    # Dropping and creating table
    output += "DROP TABLE IF EXISTS Client;\n"
    output += "CREATE TABLE Client (\n"
    output += "    ClientNum CHAR("
    # Use the number of digits in the user's input to determine length of ClientNum (using sequential values, but character)
    # They will start with the letter "C", so we need to use size + 1
    # Could do this using various data types like SERIAL but they are not always compatible between DBMSs
    output += str(size + 1)
    output += ") PRIMARY KEY,\n"
    # TODO: Calculate max length of names, address, city to be more memory efficient
    output += "    LastName CHAR(15),\n"
    output += "    FirstName CHAR(15),\n"
    output += "    Street CHAR(40),\n"
    output += "    City CHAR(30),\n"
    output += "    State CHAR(2),\n"
    output += "    ZIPCode CHAR(5),\n"
    output += "    Email CHAR(75),\n"
    output += "    Phone CHAR(12)\n"
    output += ");\n"

    return output

def generate_email(first_name: str, last_name: str) -> str:
    """
    Generate a random email address.
    faker library could be used here, but I wanted to do my own implementation

    Args:
        first_ame (str): The first name.
        last_name (str): The last name.

    Returns:
        str: A random email address.
    """
    mail_servers = ["yahoo.com","gmail.com","hotmail.com","gmail.com","live.com","mail.com","aol.com","ymail.com","zohomail.com","optonline.net","verizon.net"]

    # Take a random segment of the first name to generate a fake email address
    first_len = random.randint(1,len(first_name))
    email_first_part = first_name[:first_len]

    # Take a random segment of the last name to generate a fake email address
    last_len = random.randint(1,len(last_name))
    email_second_part = first_name[:last_len]

    # Generate a random number to pad at the end of the username
    random_email_padding = random.randint(10000, 99999)

    # Choose a domain name from the mail servers list
    domain = random.choice(mail_servers)

    # Generate an email consisting of a random amount of characters in the first and last name, followed by a number, followed by a domain
    email = f"{email_first_part}{email_second_part}{random_email_padding}@{domain}"
    
    return email

def generate_id(id_size: int, value: int) -> str:
    """
    Generate a client ID with a fixed size, prefixed with 'C'.

    Args:
        id_size (int): The size of the ID.
        value (int): The value to be converted to a string and padded.

    Returns:
        str: A client ID with a fixed size, prefixed with 'C'.
    """

    # Take the id and pad the extra characters with 0
    # Calculates this using the id_size (length of the id field)
    id = str(value).zfill(id_size)

    # Prepend the letter C before the ID
    # In case there are multiple tables, this will make it more obvious this
    # value is associated with a customer
    id = 'C' + id

    return id

def generate_phone() -> str:
    """
    Generate a random phone number in the format XXX-XXX-XXXX.
    faker library could also be used here for more realistic results

    Returns:
        str: A random phone number.
    """

    area_code = random.randint(200,999)
    exchange_code = random.randint(200, 999)
    line_number = random.randint(1000, 9999)
    
    return f"{area_code}-{exchange_code}-{line_number}"

def generate_record(key: str, last: str, first: str, street_num: str, street_name: str, street_type: str, city: str, state: str, zip: str) -> str:
    """
    Generate an INSERT statement for a client record.

    Args:
        key (str): The client ID.
        last (str): The last name.
        first (str): The first name.
        street_num (str): The street number.
        street_name (str): The street name.
        street_type (str): The street type.
        city (str): The city.
        state (str): The state.
        zip (str): The zip code.

    Returns:
        str: An INSERT statement for a client record.
    """
    record = f"""INSERT INTO Client VALUES (
    '{key}', '{last}', '{first}',
    '{street_num} {street_name} {street_type}',
    '{city}', '{state}', '{zip}',
    '{generate_email(first, last)}',
    '{generate_phone()}');\n"""

    return record