#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # For each integer in the data array
    for num in data:
        # Get the binary representation of the byte
        bin_rep = format(num, '#010b')[-8:]

        # If this is the case then we have an incomplete UTF-8 character
        if n_bytes == 0:
            # in this UTF-8 character
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            # 1 byte characters
            if n_bytes == 0:
                continue
            # Invalid UTF-8 character
            elif n_bytes > 4 or n_bytes == 1:
                return False

        else:
            # Check if the current byte is a valid continuation byte
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        # Decrement the number of bytes to process
        n_bytes -= 1

    return n_bytes == 0
