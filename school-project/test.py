
#bit_len is the binary representation
def twos_compliment(n,bit_len):
      if n >0 :
           # When n is positive, it converts to binary using the format() 
            #then padded with leading zeroes to reach the specified bit_length
            return format(n, "b").zfill(bit_len)
      else:
            # If the input number is negative, it first calculates the 2's complement by adding 2^n, 
            # where n is the number of bits and then convert it to binary.
            return format(2**bit_len + n,'b').zfill(bit_len)

try:
    ent1 = float(input("Enter 1st value:"))
    ent2 = float(input("Enter 2nd value:"))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    # Round the float values to a specified number of decimal places
    ent1 = int(round(ent1))
    ent2 = int(round(ent2))

    total = ent1 + ent2
    print(twos_compliment(total, 4))