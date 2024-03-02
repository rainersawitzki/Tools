from dateutil import parser

def check_company_branch_name(branch_name):
    # Extract the potential date substring from the end of the input string
    splitted = branch_name.split("_")
    splitted_length = len(splitted)
    if splitted_length > 0:
        potential_date_str =splitted [splitted_length - 1]    
        # Try parsing the potential date
        try:
            parsed_date = parser.parse(potential_date_str)
            return (True, potential_date_str)
        except ValueError:
            # Parsing failed
            return (False, branch_name)
    else:
        return False
# Example usage:
input_string = "This is a sample_string ending with_1.2024"
result = check_company_branch_name(input_string)

print(f"{result[0]} {result[1]}")