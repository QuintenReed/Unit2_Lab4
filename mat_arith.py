# There is no need to import SAMPLE_MATRICES
# YOUR CODE AND HEADING HERE

# Quinten Reed
# U2L4
# Matrix Arithmetic

def mat_sum(m1, m2):
  if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
    return "No solution"

  height = len(m1)
  width = len(m1[0])
  new = [[0]*width for i in range(height)]

  for i in range(width):
    for j in range(height):
      new[j][i] = m1[j][i] + m2[j][i]

  return new

def mat_mul(m1, m2):
  if len(m1[0]) != len(m2):
    return "No solution"

  width = len(m2[0])
  height = len(m1)
  new = [[0]*width for i in range(height)]

  for i in range(height):
    for j in range(width):
      final = 0
      for k in range(len(m2)):
        final += m1[i][k] * m2[k][j]

      new[i][j] = final

  return new