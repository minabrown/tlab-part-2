
def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    Loop over the data
    "if" are checking for valid data, if not valid, make a new list
    """
    clean_data = []        #list to store heart rate values that are valid
    missing_values = []    #list to store values that are invalid (e.g., non-numeric, negative, or above 220)

    for item in data:
        if item.isdigit():  #check if it's a positive number
            clean_data.append(int(item)) #convert string to integer and add to clean_data list
        else:
            missing_values.append(item) #convert string to integer and saves it
    return clean_data, missing_values #return lists