# gaussian_eliminator
I'm going to try to make a matrix Gaussian eliminator. It's probably going to be pretty bad, but here goes. 

## Current issues
1. If matrix doesn't reduce, errors all over the place
2. Only looks for pivots in diagonals of matrix - if it finds a zero, errors all over the place
3. Apparently looping through a list by creating a variable for the index and then looping though that index variable is not pythonic. 
