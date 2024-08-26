def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
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

# Test cases
print(validUTF8([65]))  # True
print(validUTF8([80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]))  # True
print(validUTF8([229, 65, 127, 256]))  # False

