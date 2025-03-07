#!/usr/bin/python3
"""
    Returns a list of available attributes and methods of an object.
    """


    def lookup(obj):
        """
        Returns a list of available attributes and methods of an object.
        """
        attrs = dir(obj)
        filtered_attrs = []
        for attr in attrs:
            if attr.startswith(''):
                filtered_attrs.append(attr)

        return filtered_attrs
