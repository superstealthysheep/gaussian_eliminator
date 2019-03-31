7
matrix_height = 3
matrix_width = 3

def takeInput(): 
  
  
  matrix = []

  print("INPUT MATRIX")
  #Constructs matrix by combining row vectors
  for row_number in range(0, matrix_height): 
    new_row_vector = []

    #Constructs row vectors by combining individual entries
    for column_number in range(0, matrix_width): 
      new_entry = input("({},{})=".format(row_number, column_number))
      new_row_vector.append(float(new_entry))

    matrix.append(new_row_vector)
    
  print(matrix)
  return(matrix)


#multiplies a row by a scalar
def multiplyRow(row_vector, scalar):
  output_row_vector = []

  #does it element-wise
  for element in row_vector:
    output_row_vector.append(element*scalar)
  return(output_row_vector)

#adds two rows
def addRows(row_vector_1, row_vector_2):
  output_row_vector = []

  #does it element_wise
  for column_number in range(0, len(row_vector_1)):
    output_row_vector.append(row_vector_1[column_number] + row_vector_2[column_number])

  return(output_row_vector)


def doGaussianElimination(matrix):

  for working_column_number in range(0, matrix_width):
    #for now, the pivot row will just be chosen to be the row with number equal to the working_column_number
    pivot_row_number = working_column_number

    #sets up pivot_row
    pivot_row = matrix[pivot_row_number]
    #multiplies pivot_row by scalar such that it actually has a pivot.
    pivot_row = multiplyRow(pivot_row, 1/(pivot_row[working_column_number]))
    #Possible error: divide by zero if the matrix has any zeros along its diagonal

    """for non_pivot_row in (matrix.pop(working_column_number)):
      addRows(non_pivot_row, multiplyRow(pivot_row, -non_pivot_row[working_column_number]))"""

    #adds ("adjusts") rows so that all rows except for the pivot row have an entry of 0 in the working column
    for row_number in range(0, matrix_height):
      if row_number == pivot_row_number:
        matrix.pop(row_number)
        matrix.insert(row_number, pivot_row)
      else:
        current_row = matrix[row_number]
        #subtracts correct multiple of pivot_row from current_row
        adjusted_row = addRows(current_row, multiplyRow(pivot_row, -1 * current_row[working_column_number]))

        #replace current_row in matrix with adjusted_row
        matrix.pop(row_number)
        matrix.insert(row_number, adjusted_row)

  return matrix

#takeInput()

"""
#input_matrix = [[2, 1, 1],
                [1, 2, 1], 
                [0, 0, -1]]
"""

#print(doGaussianElimination(input_matrixtdoGaussianElimination ))
#P#P phonesphones areare diumb
#Pri

#printprint()
#)

print(doGaussianElimination(takeInput()))
