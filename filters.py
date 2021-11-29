"""Filters should receive key as first parameter and value as a second, other parameters can only be specified as
key-word arguments with default value. Filters should either return key,value tuple or None if this piece of data has
to be removed """


def filter_even_values(key, value) -> tuple:
    if type(value) == int and value % 2 == 0:
        return key, value
    return None


def filter_alpha_keys_transformed_to_lower(key, value) -> tuple:
    if type(key) == str and key.isalpha():
        return key.lower(), value
    return None


def filter_not_none_values(key, value) -> tuple:
    if value is not None:
        return key, value
    return None


# add your custom filters in this dictionary as follows name: function_object
func_dict = {
    'filter_even_values': filter_even_values,
    'filter_alpha_keys_transformed_to_lower': filter_alpha_keys_transformed_to_lower,
    'filter_not_none_values': filter_not_none_values
}
