
import numpy as np

#1-D array
a = np.array([1,2,3])
print(a)


#2-D Array
b = np.array([[1,2,3],
              [4,5,6]])
print(b)

#find the shape 
shape1= a.shape
print(shape1)
shape2 = b.shape
print(shape2)


#getting a specific element 
get = np.array([[1,2,3] 
                ,[4,5,6]])
var1 = get[1 ,2]
print(var1)
var2 = get[0, 1]
print(var2)
change = get[0,1]= -3
print(change)

#arranging and reshaping elements
c = np.arange(28).reshape(2,14)
print(c)
d= np.array(range(0))
print(d)

#initialize all zero's and ones's
zeros =np.zeros((2,3))
print(zeros)
ones =np.ones((4,2))
print(ones)

#Broadcasting
a= [1,2,3]
z= [4,5,6]
broadcast = a+z
print(broadcast)




# 4x-3x+x=10
# 2x-x2+3x=0
#-x+2x-5x=17
A= np.array([[4,-3,1],[2,1,3],[-1,2,-5]])
print(A)
#shape fetches and finds the dimension of an array
shape1 = A.shape
print(shape1)
B = np.array([-10,0,17])
shape2=  B.shape
print(B)
print(shape2)

radiant=np.random.randint(6, size=(4,2))
#stacks arrays and sequence horizontaly (column wise)
A_system = np.hstack ((A, B.reshape((3,1))))
print(A_system)

#interchange, reshaping and rearranging



#This function takes a matrix M, a row number row_num, and a multiplier row_num_multiple. 
# It creates a new matrix M_new that is a copy of M, and then multiplies
# the specified row row_num by the multiplier row_num_multiple in M_new. Finally, it returns the updated matrix M_new.
def MultiplyRows(M, row_num, row_num_multiple):
  M_new= M.copy() #copys an array to another arry
  M_new[row_num]= M_new[row_num]*row_num_multiple
  return M_new


#This function takes a matrix M, two row numbers row_num_1 and row_num_2, and a multiplier row_num_1_multiple. 
# It creates a new matrix M_new as a copy of M. Then, it adds the product of row_num_1 multiplied by row_num_1_multiple to the row row_num_2 in M_new. Essentially, it performs a linear combination of the two specified rows and updates M_new accordingly.
# Finally, it returns the updated matrix M_new.
def AddRows(M, row_num_1, row_num_2, row_num_1_multiple):
  M_new = M.copy()
  M_new[row_num_2]= row_num_1_multiple * M_new[row_num_1]+M_new[row_num_2]
  return M_new


#This function takes a matrix M and two row numbers row_num_1 and row_num_2. 
# It creates a new matrix M_new as a copy of M. Then, it swaps the positions of the specified rows row_num_1 and row_num_2 in M_new.
# This function is useful for rearranging the rows of a matrix. Finally, it returns the updated matrix M_new.
def SwapRows(M, row_num_1, row_num_2):
  M_new= M.copy()
  M_new[[row_num_1, row_num_2]]= M_new[[row_num_2, row_num_1]]
  return M_new



#swapping rows
A_ref = SwapRows(A_system,0,2)
print(A_ref)
A_ref = AddRows(A_ref, 0,2,4)
A_ref = AddRows(A_ref, 0,1,2)
A_ref = AddRows(A_ref, 1,2,-1)
print(A_ref)

A_ref = MultiplyRows(A_ref,2,-1/12)
print(A_ref)
