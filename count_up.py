"""Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

def count_up(start, stop):
    end = stop + 1
    r = range(start, end)
    for num in r:
        print(num)
 


count_up(5, 7)        
