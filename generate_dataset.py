import io
import os
import random
import sys

import data_generator
import file_utils

def main():
    # Will hold the name of the street (i.e. Main, College)
    street = []
    # Will hold the type of street (i.e. Street, Road, Court)
    street_type = []

    # Three lists to hold the city, state, and ZIP
    city = []
    state = []
    zip = []

    # Current ethnicities
    ethnicity_types = ["chinese","japanese","korean","indian","arabic","spanish","american"]

    # Lists to hold last and first names of each ethnicity
    chinese_last = []
    japanese_last = []
    korean_last = []
    indian_last = []
    arabic_last = []
    spanish_last = []
    american_last = []
    
    chinese_first = []
    japanese_first = []
    korean_first = []
    indian_first = []
    arabic_first = []
    spanish_first = []
    american_first = []

    first_file_name = "first.txt"
    last_file_name = "last.txt"
    street_file_name = "streets.txt"
    street_type_file_name = "street_types.txt"
    zip_file_name = "ZIP.csv"

    input_file_names = {
        "first": first_file_name,
        "last": last_file_name,
        "street": street_file_name,
        "street_type": street_type_file_name,
        "zip": zip_file_name
    }
    
    for check_file in input_file_names.values():
        if not os.path.exists(check_file):
            print(f"File not found: {check_file}.")
            sys.exit()

    print("All required data files present.")

    output_file_name = "output_dataset.sql"

    if file_utils.check_output_file(output_file_name):
        # Open SQLfile.sql to store script
        output_file = open(output_file_name, "w")
    else:
        print(f"Exiting program, please remove or rename {output_file_name}.")
        sys.exit()

    file_utils.load_zip_file(input_file_names["zip"], city, state, zip)

    file_utils.load_data_files(input_file_names["street"], street)
    file_utils.load_data_files(input_file_names["street_type"], street_type)

    # process_names will open files and load values
    chinese_last, japanese_last, korean_last, indian_last, arabic_last, spanish_last, american_last = file_utils.load_names(last_file_name)
    chinese_first, japanese_first, korean_first, indian_first, arabic_first, spanish_first, american_first = file_utils.load_names(first_file_name)

    num_clients = int(input("Enter number of values to generate: "))

    len_clients = len(str(num_clients))

    output_start = data_generator.generate_client_table(len_clients)
    output_file.write(output_start)

    # TODO: pad the clientNumber with leading 0?
    for loop_counter in range(num_clients):
        ethnicity = ethnicity_types[random.randint(0,6)]

        first_name_value = random.randint(0,19)
        last_name_value = random.randint(0,19)
        
        # Tricky way to get Python to combine the variable value and array:
        # Will be evaluated in this form: chineseFirst[3]
        command = ethnicity + "_first[" + str(first_name_value) + "]"
        random_first_name = eval(command)

        command = ethnicity + "_last[" + str(last_name_value) + "]"
        random_last_name = eval(command)

        # Create a random name, address, email, phone, and add to the output file  
        random_street_name = street[random.randint(0,len(street)-1)]
        random_street_type = street_type[random.randint(0,len(street_type)-1)]
        # Create a random number to start an address
        random_address_number = str(random.randint(100,9999))

        location = random.randint(0,len(zip)-1)
        random_city = city[location]
        random_state = state[location]
        random_zip = zip[location]

        next_id = data_generator.generate_id(len_clients, loop_counter + 1)

        # Doing separate inserts rather than one big insert in case of large data set
        current_line = data_generator.generate_record(next_id, random_last_name, random_first_name, random_address_number, random_street_name, random_street_type, random_city, random_state, random_zip)
        output_file.write(current_line)
    # Close the output
    output_file.close()

    # TODO: Add connector to DBMS

    print("Complete!")

# This is here in case I decide to use this as a library for another program    
if __name__ == "__main__":
    main()