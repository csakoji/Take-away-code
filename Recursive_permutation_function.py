def permutations(string, step = 0):
    print("Value of step is {}".format(step))
    # if we've gotten to the end, print the permutation
    if step == len(string):
        print("".join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):
        print('value of inside for loop of step = {} and i = {}'.format(step, i))

        # copy the string (store as array)
        string_copy = [character for character in string]
        print("String copy 1 {}".format(string_copy))

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        print("String copy 2 {}".format(string_copy))

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        print("permutations call from inside for loop\n")
        permutations(string_copy, step + 1)

permutations("abc")
