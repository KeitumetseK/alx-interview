#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes to process in the current UTF-8 character
    num_bytes = 0
    
    for num in data:
        # Ensure that the byte is within the valid range (0-255)
        if num > 255:
            return False
        
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (num >> 5) == 0b110:       # 2-byte character
                num_bytes = 1
            elif (num >> 4) == 0b1110:    # 3-byte character
                num_bytes = 2
            elif (num >> 3) == 0b11110:   # 4-byte character
                num_bytes = 3
            elif (num >> 7) != 0:         # 1-byte character must start with 0
                return False
        else:
            # Check that the next byte starts with '10'
            if (num >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If there are no remaining expected continuation bytes, return True
    return num_bytes == 0

