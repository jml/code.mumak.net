


.. code-block:: python

    def sorted_items(d):
        result = []
        sorted_keys = sorted(d.keys())
        for key in sorted_keys:
            result.append((key, d[key]))
        return result

    for name, age in sorted_items(ages):
        print("{}\t{}".format(name, ages[name]))



The `sorted_items` above isn't very idiomatic Python, but is perhaps more
familiar to Go programmers. A more common way to approach this in Python would
be to use a list comprehension:

.. code-block:: python

    def sorted_items(d):
        return [(key, d[key]) for key in sorted(d.keys())]

