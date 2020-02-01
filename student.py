# Define a Python class named Student. This class will have 5 properties.

# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.

class Student:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort_number = 0
        self. full_name = ""
        
    
    @property
        def full_name