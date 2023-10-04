#!/usr/bin/python3
""" Locked Class  """


class LockedClass:
    """ Locked Class  """
    def __setattr__(self, name, value):
        """ set attribute method  """
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"Cannot set '{name}' LockedClass")
