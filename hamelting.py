def calculate_hamming_code(data_bits, parity_type="even"):
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
        ones_count = sum(bit == '1' for bits in parity_bits for bit in bits)

        if parity_type == "even":
            parity_value = '0' if ones_count % 2 == 0 else '1'
        else: 
            parity_value = '1' if ones_count % 2 == 0 else '0'

        hamming_code[parity_pos - 1] = parity_value

    return "".join(hamming_code)


data_bits_1 = "1011"
hamming_code_1 = calculate_hamming_code(data_bits_1, "even")
print("Hamming Code for 1011 with even parity:", hamming_code_1)