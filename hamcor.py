def detect_and_correct_hamming(received_code):
    
    n = len(received_code)
    error_position = 0  
    
    for i in range(3): 
        parity_pos = 2**i  
        check_bits = [received_code[j] for j in range(parity_pos - 1, n, 2 * parity_pos)]
        
       
        ones_count = sum(1 for bit in check_bits if bit == '1')
        
      
        if ones_count % 2 != 0:
            error_position += parity_pos  
    if error_position > 0:
        corrected_code = list(received_code)
        corrected_code[error_position - 1] = '1' if received_code[error_position - 1] == '0' else '0'
        corrected_code = "".join(corrected_code)
    else:
        corrected_code = received_code 

    return error_position, corrected_code


received_code = "1011101"
error_position, corrected_code = detect_and_correct_hamming(received_code)


if error_position:
    print(f"Error detected at position: {error_position}")
    print(f"Corrected Hamming code: {corrected_code}")
else:
    print("No error detected, the code is correct.")