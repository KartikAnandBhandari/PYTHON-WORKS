def bit_stuffing(data):
    count = 0
    stuffed = []
    
    for bit in data:
        if bit == '1':
            count += 1
        else:
            count = 0 
        
        stuffed.append(bit)
        
        if count == 5:  
            stuffed.append('0')
            count = 0 
        
    return ''.join(stuffed)

def bit_destuffing(data):
    count = 0
    destuffed = []
    
    i = 0
    while i < len(data):
        destuffed.append(data[i])
        
        if data[i] == '1':
            count += 1
        else:
            count = 0  
        if count == 5 and i + 1 < len(data) and data[i + 1] == '0':  
          
            i += 1
            count = 0  
        
        i += 1
    
    return ''.join(destuffed)

original_data = "110111111011111010"
stuffed_data = bit_stuffing(original_data)
destuffed_data = bit_destuffing(stuffed_data)

print("Original Data:  ", original_data)
print("Bit Stuffed:    ", stuffed_data)
print("Bit Destuffed:  ", destuffed_data)
