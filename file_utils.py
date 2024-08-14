import os

def check_output_file(file_name: str) -> bool:
    """
    Check if the output file already exists and handle accordingly.

    Args:
        file_name (str): The name of the output file.

    Returns:
        bool: True if the file can be written, False if the user chooses to quit.
    """

    file_present = os.path.exists(file_name)

    if(file_present):
        result = True
        remove_file = input("Output file is already here. Delete (D), Rename (R), or Quit (Q): ")
        if remove_file.upper() == "D":
            print("Deleting existing",file_name)
            os.remove(file_name)
        elif remove_file.upper() == "R":
            rename_file_present = os.path.exists("SQLFile.old")
            if rename_file_present:
                rename_file_name = input("Enter file name: ")
                os.rename(file_name,rename_file_name)
                print("Renaming existing file to",rename_file_name)
            else:
                print("Renaming existing file to SQLFile.old")
                os.rename(file_name,"SQLfile.old")
        else:
            # User did not pick a valid option
            result = False
    else:
        result = True
        
    return result
    
def load_names(file_name: str) -> tuple:
    """
    Process names from a file.

    Args:
        file_name (str): The name of the file to process.

    Returns:
        tuple: A tuple containing lists of names for each ethnicity.
    """
    with open(file_name, "r") as name_file:

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
        print(f"Loading and parsing {file_name.split('.')[0]} names data set...")

        # bring in data from name dataset
        # Need to rstrip() to remove carriage return
        for current_line in name_file:
            current_line = current_line.rstrip()
            # If there is a * in the line, it's a header for a type of name
            if '*' in current_line:
                # lowercase the type, and then split on the asterisk
                # [0] is the asterisk, [1] is the value
                # data file format for a header row is asterisk followed by name, such as
                # *american
                name_type = current_line.lower().split("*")[1]
            else:
                # Craft a Python command to append the name to the appropriate list
                # Probably a cleaner way to do this
                # command = chinese.append("Liang")
                command = f"{name_type}.append('{current_line}')"
                exec(command)

    return(chinese, japanese, korean, indian, arabic, spanish, american)

def load_data_files(file_name: str, data_list: list):
    """
    Load data from a file into a list.

    Args:
        file_name (str): The name of the file to load.
        data_list (list): The list to store the loaded data.

    Returns:
        None
    """
    with open(file_name, "r") as file:
        for line in file:
            data_list.append(line.rstrip())

def load_zip_file(file_name: str, city: list, state: list, zip: list):
    """
    Load ZIP code data from a file into separate lists for city, state, and ZIP.

    Args:
        file_name (str): The name of the file to load.
        city (list): The list to store the city data.
        state (list): The list to store the state data.
        zip (list): The list to store the ZIP code data.

    Returns:
        tuple: The city, state, and ZIP code lists.
    """
    in_zip = open(file_name,"r")

    print("Loading and parsing ZIP code data set...")
    # bring in data from USPS ZIP database
    # In the format 07013,Clifton,NJ
    # ZIP,City,State
    # Need to rstrip() state to remove carriage return
    for line_zip in in_zip:
        split_line = line_zip.split(",")
        zip.append(split_line[0])
        city.append(split_line[1])
        state.append(split_line[2].rstrip())

    in_zip.close()

    return city, state, zip
