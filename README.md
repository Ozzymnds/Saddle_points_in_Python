# Saddle_points_in_Python
Code that shows if a matrix has or not saddle points
First of all, a saddle point in a matrix is an element inside the matrix that could be the lowest value of its row and the highest value of its column, or vice versa, the lowest value in its column and the highest value in its row.
On this basis, we have 2 scripts with the same function, but they do their work in a different way: on one hand, we have a script that uses cache to optimize the code; and on the other hand we have a script that doesn't use the cache. The difference between these two codes is that the non-caching one will have a longer execution time than the caching one, this difference only can be seen if we make a matrix with very huge values for the columns and the rows.
