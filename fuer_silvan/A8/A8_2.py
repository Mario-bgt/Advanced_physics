def req_steps(num_disks):
    if num_disks == 1:
        return 1
    else:
        step = 2 * req_steps(num_disks - 1) + 1
    return step



    # The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("For moving {} disks, {} steps are required.".format(3, req_steps(3)))