#!/usr/bin/python3
""" Task zero"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""

    """Number of bytes in the current UTF-8 character"""
    num_bytes = 0

    """Masks for checking the most significant bits"""
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        bin_rep = byte & 0xFF

        if num_bytes == 0:
            """Determine the number of bytes in the current UTF-8 character"""
            if (bin_rep & mask1) == 0:
                """# 1-byte character (0xxxxxxx)"""
                continue
            elif (bin_rep & (mask1 | mask2)) == mask1:
                return False
            elif (bin_rep & (mask1 | mask2)) == (mask1 | mask2):
                """# 2-byte character (110xxxxx)"""
                num_bytes = 1
            elif (bin_rep & (mask1 | mask2 | (1 << 5))) == (
                    mask1 | mask2 | (1 << 5)):
                """# 3-byte character (1110xxxx)"""
                num_bytes = 2
            elif (bin_rep & (mask1 | mask2 | (1 << 5) | (1 << 4))) == (
                    mask1 | mask2 | (1 << 5) | (1 << 4)):
                """# 4-byte character (11110xxx)"""
                num_bytes = 3
            else:
                return
        else:
            """# Continuation bytes must start with 10xxxxxx"""
            if (bin_rep & (mask1 | mask2)) != mask1:
                return False
            num_bytes -= 1

    """# All characters must be completely processed"""
    return num_bytes == 0
