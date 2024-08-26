#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Ensure that the byte is within the valid range (0-255)
        if num > 255:
            return False
        
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & num:
                num_bytes += 1
                mask = mask >> 1
            
            # 1-byte character
            if num_bytes == 0:
                continue
            
            # UTF-8 can be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the next byte starts with '10'
            if not (num & mask1 and not (num & mask2)):
                return False
        
        # Decrease the number of bytes to process
        num_bytes -= 1
    
    # All characters must be processed
    return num_bytes == 0

