'''
Cosine Similarity can be defined as the similarity 
of two non-zero vectors. This can be derived from 
the Euclidean dot product forumula.

a dot b = |a|*|b| * cos(Ø) 

More specifically, the magnitude of vector a multiplied by
the magnitute of vector b multipled by the cosine of 
the angle between the two.

We can re-arrange to set the similarity (cosine Ø) to equal
(A dot B) / {|A|*|B|}

Formally, 

similarity = cosø =  ∑(A_i * B_i) / √(∑(A_i ^ 2)) * √(∑(B_i ^ 2)) 

similarity will range between [-1,1], with -1 being completely dissimilar
and 1 being completely similar. 

'''

import math

def cosine_similarity(vector_1, vector_2):
    #initialize vector sums
    sumv1, sumv2, sumv1v2 = 0, 0, 0
    for i in range(len(vector_1)):
        x = vector_1[i]
        y = vector_2[i]
        sumv1 += x * x
        sumv2 += y * y
        sumv1v2 += x * y
    return sumv1v2 / (math.sqrt(sumv1) * math.sqrt(sumv2))


#EXAMPLES
v1 = [10,-12,4,21,3,5] ; v2 = [-21,2311,1,2,6,12]
print(v1, v2, cosine_similarity(v1,v2))
#Outputs a similarity of 0.785324416084657