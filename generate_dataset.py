# import mysql.connector
import datetime
import os
import random
import sys

def process_names(file_name: str) -> tuple:
    """
    Process names from a file.

    Args:
        first_name (str): The name of the file to process.

    Returns:
        tuple: A tuple containing lists of names for each ethnicity.
    """
    name_file = open(file_name,"r")
    # Type of name (first or last)
    name_type = ""
    chinese = []
    japanese = []
    korean = []
    indian = []
    arabic = []
    spanish = []
    american = []

    # split out the file name from the extension, use it to print what we are parsing
    print("Loading and parsing " + file_name.split(".")[0]+" names data set...")

    # bring in data from name dataset
    # Need to rstrip() to remove carraige return
    for name_current_line in name_file:
        name_current_line = name_current_line.rstrip()
        # If there is a * in the line, it's a header for a type of name
        if '*' in name_current_line:
            # lowercase the type, and then split on the asterisk
            # [0] is the asterisk, [1] is the value
            # data file format for a header row is asterisk followed by name, such as
            # *american
            name_type = name_current_line.lower().split("*")[1]
        else:
            # Craft a Python command to append the name to the appropriate list
            # Probably a cleaner way to do this
            # command = chinese.append("Liang")
            command = name_type+".append(\""+name_current_line + "\")"
            exec(command)

    name_file.close()

    return(chinese, japanese, korean, indian, arabic, spanish, american)


def generate_email(first_name: str, last_name: str) -> str:
    """
    Generate a random email address.

    Args:
        first_ame (str): The first name.
        last_name (str): The last name.

    Returns:
        str: A random email address.
    """
    mail_servers = ["yahoo.com","gmail.com","hotmail.com","gmail.com","live.com","mail.com","aol.com","ymail.com","zohomail.com","optonline.net","verizon.net"]

    firstLen = random.randint(1,len(first_name))
    lastLen = random.randint(1,len(last_name))

    # Generate an email consisting of a random amount of characters in the first and last name, followed by a number, followed by a domain    
    email = first_name[0:firstLen]+last_name[0:lastLen]+str(random.randint(10000,99999))+"@"+mail_servers[random.randint(0,len(mail_servers)-1)]
    return(email)

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

    output_file_name = "SQLFile.sql"

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
        print(check_file)
        if not os.path.exists(check_file):
            print("File not found: " + check_file)
            sys.exit()

    print("All required data files present")

    output_file_present = os.path.exists(output_file_name)

    if(output_file_present):
        remove_file = input("Output file is already here. Delete (D), Rename (R), or Quit (Q): ")
        if remove_file.upper() == "D":
            print("Deleting existing",output_file_name)
            os.remove(output_file_name)
        elif remove_file.upper() == "R":
            rename_file_present = os.path.exists("SQLFile.old")
            if rename_file_present:
                rename_file_name = input("Enter file name: ")
                os.rename(output_file_name,rename_file_name)
                print("Renaming existing file to",rename_file_name)
            else:
                print("Renaming existing file to SQLFile.old")
                os.rename(output_file_name,"SQLfile.old")
        else:
            print("Exiting program, please rename",output_file_name,".")
            sys.exit()

    # Open SQLfile.sql to store script
    out_file = open(output_file_name, "w")

    in_zip = open(zip_file_name,"r")

    print("Loading and parsing ZIP code data set...")
    # bring in data from USPS ZIP database
    # In the format 07013,Clifton,NJ
    # (ZIP,City,State)
    # Need to rstrip() state to remove carraige return
    for line_zip in in_zip:
        split_line = line_zip.split(",")
        zip.append(split_line[0])
        city.append(split_line[1])
        state.append(split_line[2].rstrip())

    in_zip.close()

    in_street = open(street_file_name,"r")

    print("Loading and parsing street names data set...")
    # bring in data from street name dataset
    # Need to rstrip() to remove carraige return
    for line_street in in_street:
        street.append(line_street.rstrip())

    in_street.close()
    
    in_street_type = open(street_type_file_name,"r")

    print("Loading and parsing street types data set...")
    # bring in data from street type dataset
    # Need to rstrip() to remove carraige return
    for line_street_type in in_street_type:
        street_type.append(line_street_type.rstrip())

    in_street_type.close()

    # process_names will open files and load values
    chinese_last, japanese_last, korean_last, indian_last, arabic_last, spanish_last, american_last = process_names(last_file_name)
    chinese_first, japanese_first, korean_first, indian_first, arabic_first, spanish_first, american_first = process_names(first_file_name)

    num_clients = int(input("Enter number of values to generate: "))

    len_clients = len(str(num_clients))

    # Add date/time information
    out_file.write("-- Fake data set generated on " + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")

    # Creating schema (this is geared towards MySQL) and creating table
    out_file.write("CREATE SCHEMA studentTest;\n")
    out_file.write("CREATE TABLE Client (\n")
    out_file.write("    ClientNum CHAR(")
    # Use the number of digits in the user's input to determine length of ClientNum (using sequential values, but character)
    # Could do this using various data types but they are not always compatible between DBMSs
    out_file.write(str(len_clients))
    out_file.write(") PRIMARY KEY,\n")
    # TODO: Store max length of names
    out_file.write("    LastName CHAR(15),\n")
    out_file.write("    FirstName CHAR(15),\n")
    out_file.write("    Street CHAR(20),\n")
    out_file.write("    City CHAR(15),\n")
    out_file.write("    State CHAR(2),\n")
    out_file.write("    ZIPCode CHAR(5),\n")
    out_file.write("    Email CHAR(75),\n")
    out_file.write("    Phone CHAR(10)\n")
    out_file.write(");\n")


    # TODO: pad the clientNumber with leading 0?
    for loop_counter in range(num_clients):
        ethnicity = ethnicity_types[random.randint(0,6)]
        # TODO: Has to be a cleaner way to do this to ensure random values 
        first_name_value = random.randint(0,19)
        last_name_value = random.randint(0,19)
        
        # Tricky way to get Python to combine the variable value and array:
        # Will be evaluated in this form: chineseFirst[3]
        command = ethnicity + "_first[" + str(first_name_value) + "]"
        random_first_name = eval(command)

        command = ethnicity + "_last[" + str(last_name_value) + "]"
        random_last_name = eval(command)

        # Create a random name, address, email, phone, and add to the output file  
        location = random.randint(0,len(zip)-1)
        random_street_name = random.randint(0,len(street)-1)
        random_street_type = random.randint(0,len(street_type)-1)

        # Generate an INSERT for the current record
        # Doing separate inserts rather than one big insert in case of large data set
        out_file.write("INSERT INTO Client VALUES (\"" +
                      str(loop_counter + 1) +
                      "\", \"" +
                      random_last_name +
                      "\", \"" +
                      random_first_name +
                      "\", \"" +
                      str(random.randint(100,9999)) +
                      " " +
                      street[random_street_name] +
                      " " +
                      street_type[random_street_type] +
                      "\", \"" +
                      city[location] +
                      "\", \"" +
                      state[location] +
                      "\", \"" +
                      zip[location] +
                      "\", \"" +
                      generate_email(random_first_name,random_last_name) +
                      # Need to generate phone and email
                      "\", \"" +
                      str(random.randint(200,999))+"-"+str(random.randint(200,999))+"-"+str(random.randint(1000,9999)) +
                      "\")\n")
    # Close the output
    out_file.close()

    # TODO: Add connector to DBMS

    print("Complete!")

# This is here in case I decide to use this as a library for another program    
if __name__ == "__main__":
    main()