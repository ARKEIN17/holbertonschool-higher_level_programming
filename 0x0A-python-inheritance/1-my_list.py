<<<<<<< HEAD
#!/usr/bin/python3
"""
Module with class MyList
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))
=======
#!/usr/bin/python3
"""Module that creates a list subclass"""


class MyList(list):
    """Creates a subclass"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        my_new_list = self.copy()
        my_new_list.sort()
        print(my_new_list)
>>>>>>> 38492aa2f652bda047895a4871f5a072d0aa3090
