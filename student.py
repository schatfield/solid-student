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
    
     # def first_name is a function that can be accessed as a property because of the @decorater

    @property
    def first_name(self):
        try:
            return self.__first_name
        # .__first_name is private: it's only available for changing inside this class
        except AttributeError:
            return ""

    @first_name.setter
    def first_name(self, first_name):
        if type(first_name) is str:
            self.__first_name = first_name
        else:
            raise TypeError('Please provide first name as a string. NO NUMBERS ALLOWED I HATE MATH')

      
    @property
    def full_name(self):
        return f'{self.__first_name} {self.last_name}' 

    