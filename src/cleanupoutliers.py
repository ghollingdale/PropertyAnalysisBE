def clean_outliers(properties):
    removal_count = 0 
    # Check df of properties with a price greater than 2,000,000€
    print("There are", properties[properties['price'] > 2000000].shape[0], "properties with a value of more than 2,000,000€")
    removal_count = removal_count + properties[properties['price'] > 2000000].shape[0]
    # Remove all properties with a price greater than 2,000,000€
    properties = properties[properties['price'] <= 2000000]


    # Check df of properties with more than 10 bedrooms
    print("There are", properties[properties['number of bedrooms'] > 10].shape[0], "properties with more than 10 bedrooms.")
    removal_count = removal_count + properties[properties['number of bedrooms'] > 10].shape[0]
    # Remove all properties with more than 10 bedrooms
    properties = properties[properties['number of bedrooms'] <= 10]

    # Check df of properties with more than 100sqm living area
    print("There are", properties[properties['living area'] > 100].shape[0], "properties with a living area greater than 100sqm.")
    removal_count = removal_count + properties[properties['living area'] > 100].shape[0]
    # Remove all properties with a living area of more than 100sqm
    properties = properties[properties['living area'] <= 100]

    # Check df of properties with more than 750sqm total property area
    print("There are", properties[properties['total property area'] > 750].shape[0], "properties with a total property area greater than 750sqm.")
    removal_count = removal_count + properties[properties['total property area'] > 750].shape[0]
    # Remove all properties with a total property area of more than 750sqm
    properties = properties[properties['total property area'] <= 750]

    # Check df of properties with more than 20000sqm total land area
    print("There are", properties[properties['total land area'] > 20000].shape[0], "properties with a total property land greater than 20000sqm.")
    removal_count = removal_count + properties[properties['total land area'] > 20000].shape[0]
    # Remove all properties with a total land area of more than 20000sqm
    properties = properties[properties['total land area'] <= 20000]

    # Check df of proeprties with more than 250sqm terrace area
    print("There are", properties[properties['terrace area'] > 250].shape[0], "properties with a terrace area greater than 250sqm.")
    removal_count = removal_count + properties[properties['terrace area'] > 250].shape[0]
    # Remove all properties with a terrace area of more than 250sqm
    properties = properties[properties['terrace area'] <= 250]
    properties

    # Check df of properties with more than 4 facades
    print("There are", properties[properties['number of facades'] > 4].shape[0], "properties with more than 4 facades.\n")
    removal_count = removal_count + properties[properties['number of facades'] > 4].shape[0]
    # Remove all the properties with more than 4 facades
    properties = properties[properties['number of facades'] <= 4]
    
    print(removal_count,  "outliers have been removed from the dataframe in total.")
    return properties