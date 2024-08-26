#!/usr/bin/python3
"""
UTF-8 Validation Module
"""

def validUTF8(data):
    """
    Method to determine if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes.
    :return: True if the data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    # Masks to check the leading bits of each byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Check if the current integer fits in a byte
        if num > 255:
            return False
        
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & num:
                num_bytes += 1
                mask = mask >> 1
            
            # 1-byte character or invalid byte length
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check if it is a continuation byte ('10xxxxxx')
            if not (num & mask1 and not (num & mask2)):
                return False
        
        # Decrement the number of bytes left to check
        num_bytes -= 1

    # Return true if all bytes were correctly processed
    return num_bytes == 0

