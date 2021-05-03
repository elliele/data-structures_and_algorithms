from array_stacks import ArrayStack


def reverse_file(filename):
    """Overwrite given file with its content line-by-line reversed."""
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))                   # we will re-insert newlines when writing
    original.close()

    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')                    # repopening file overwrites original
    while not S.is_empty():
        output.write(S.pop() + '\n')                # re-insert newline characters
    output.close()