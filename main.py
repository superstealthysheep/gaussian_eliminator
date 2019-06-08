matrix_height = 3
matrix_width = 4

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
    
  print(matrix, "\n")
  return(matrix)


def printMatrix(matrix):
  print("[")
  for row in matrix:
    print(row)
  print("]")


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

def swapRows(matrix, rowNumber1, rowNumber2):
  row1 = matrix[rowNumber1]
  row2 = matrix[rowNumber2]
  
  matrix.pop(rowNumber1)
  matrix.insert(rowNumber1, row2)

  matrix.pop(rowNumber2)
  matrix.insert(rowNumber2, row1)

  return matrix


#Takes matrix, then tries to find pivot row 
#swaps the pivot row into the working_column number-th row, then returns if it was successful.
def findPivotRow(matrix, working_column_number):
  
  for possiblePivotRowNumber in range(working_column_number, matrix_height):
    print("Testing row {}, column {}".format(possiblePivotRowNumber, working_column_number))
    possiblePivotRow = matrix[possiblePivotRowNumber]

    if possiblePivotRow[working_column_number] == 0:
      continue
    else:
      swapRows(matrix, working_column_number, possiblePivotRowNumber)
      pivot_found = True
      return (matrix, pivot_found)

  #this executes only if no pivots are found 
  pivot_found = False
  print("No pivot found in column {}".format(working_column_number))
  return (matrix, pivot_found)


def doGaussianElimination(matrix):

  #The min is because you can only have as many potential pivots as there are diagonal entries (which is equal to the min of matrix width and length)
  for working_column_number in range(0, min(matrix_width, matrix_height)):
    
    #adjusts matrix until a possible pivot for this column is in the row with number equal to the working_column_number
    find_pivot_row_results = findPivotRow(matrix, working_column_number)
    matrix = find_pivot_row_results[0]
    pivot_found = find_pivot_row_results[1]
    #If a pivot is not found, skip this column.
    if not pivot_found:
      print("Continuing, because pivot was not found")
      continue

    #this is true because the findPivotRow step moves the pivot row into the correct row.
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

"""
input_matrix = [[0, 0, 1],
                [1, 0, 0],
                [0, 1, 0]]
"""

printMatrix(doGaussianElimination(takeInput()))
