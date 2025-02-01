def calculate_hamming_code(data_bits, parity_type="odd"):
    
    m = len(data_bits)
    r = 0 
    while (2**r) < (m + r + 1):
        r += 1

   
    hamming_code = ['P'] * (m + r)  
    j = 0  
    
    for i in range(1, len(hamming_code) + 1):
        if (i & (i - 1)) == 0:  
            continue
        hamming_code[i - 1] = data_bits[j]
        j += 1

    
    for i in range(r):
        parity_pos = 2**i
        parity_bits = [hamming_code[j] for j in range(parity_pos - 1, len(hamming_code), 2 * parity_pos)]
        ones_count = sum(1 for bit in parity_bits if bit == '1')

        if parity_type == "odd":
            parity_value = '1' if ones_count % 2 == 0 else '0'  
        else:
            parity_value = '0' if ones_count % 2 == 0 else '1'  
        hamming_code[parity_pos - 1] = parity_value

    return "".join(hamming_code)

data_bits_3 = "11001"
hamming_code_3 = calculate_hamming_code(data_bits_3, "odd")

print("Hamming Code for 11001 with odd parity:", hamming_code_3)