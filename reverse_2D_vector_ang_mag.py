# type List 
#   magnitude and deg_angle in degrees: [60, 55]
# rtype List
#   the reverse of a should only be output in the format of angle and magnitude [240, ]
# 
# Because the format of magnitude is never in negatives the way that most distances are
#   return the vector with the proper angle to suffice for a reverse


def reverse_vector_components(vector):
    if vector[0] < 0:
        vector[0] += 360
    if vector[0] < 180:
        vector[0] -= 180
    elif vector[0] > 180:
        vector[0] += 180
    return vector