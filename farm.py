def get_number_of_plants(field_size, unit, crop):
    # convert field size to square meters
    if unit == "acres":
        field_area_sqm = field_size * 4046.86
    elif unit == "hectares":
        field_area_sqm = field_size * 10000
    else:
        raise ValueError("unit must be 'acres' or 'hectares'")

    # space needed per plant for each crop (in square meters)
    crop_space = {
        "corn": 1.0,
        "wheat": 0.1,
        "soybeans": 0.5,
        "tomatoes": 0.25,
        "lettuce": 0.2,
    }

    if crop not in crop_space:
        raise ValueError("unknown crop")

    space_per_plant = crop_space[crop]

    # number of plants that fit (use int to get whole plants)
    num_plants = int(field_area_sqm / space_per_plant)
    return num_plants

# manual tests
print(get_number_of_plants(1, "acres", "corn"))
print(get_number_of_plants(2, "hectares", "wheat"))