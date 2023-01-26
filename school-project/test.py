
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
ent1 = int(input("Enter 1st value:"))
ent2 = int(input("enter value:"))
total = ent1 +ent2
print(twos_compliment(total, 4))