def print_schedule(n, s):
    """ Prints a student's schedule 
    n -- the student's name, a string
    s -- the student's schedule, a list of strings.
    """

    header = "Schedule for {}".format(n)

    print('='*len(header))
    print(header)
    print('='*len(header))

    for period, cls in enumerate(s):
        print("{}. {}\n".format(period+1, cls))
