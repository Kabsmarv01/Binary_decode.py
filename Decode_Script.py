cipher_text = input("Enter the cipher 8-bit binary string: ")
binary_blocks = cipher_text.split()
if not all(c in '01 ' for c in cipher_text):
    print("Invalid binary input.")
elif  all(c in '01' for c in cipher_text):
    print("Please type 8 bit binary code only")
elif len(binary_blocks) == 0 or not all(len(block) == 8 for block in binary_blocks):
    print("Please type 8 bit binary code only separated by spaces.")
else:
    # Binary to ASCII
    ascii_text = ''.join([chr(int(b, 2)) for b in cipher_text.split()])
    print("Decoded ASCII text:", ascii_text)
