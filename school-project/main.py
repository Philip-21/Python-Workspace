def ones_complement(num):
    return format(num, 'b').zfill(4)
ent = int(input("enter value:"))
print(ones_complement(ent)) # '00000101'



