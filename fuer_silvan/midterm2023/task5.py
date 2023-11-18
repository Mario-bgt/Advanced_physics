# Implement both functions. Change the method signatures to add parameters as specified!
# Remember to return enrollments at the end of each function!
def register(enrollments, student, course):
    if student in enrollments:
        enrollments[student].add(course)
    else:
        enrollments[student] = course
    return enrollments


def deregister(enrollments, student, course):
    if student not in enrollments:
        return enrollments
    if course not in enrollments[student]:
        return enrollments
    if len(enrollments[student]) == 1:
        del enrollments[student]
    else:
        enrollments[student].remove(course)
    return enrollments


print( register(  {},                        111, "INF-1") )
print( register(  {222: {"INF-1", "BIO-2"}}, 222, "PHY-2") )
print( register(  {222: {"INF-1", "BIO-2"}}, 333, "PHY-2") )
print( deregister({222: {"INF-1", "BIO-2"}}, 222, "INF-1") )
print( deregister({222: {"INF-1"}},          222, "INF-1") )
print( deregister({222: {"INF-1", "BIO-2"}}, 111, "INF-1") )
print( deregister({},                        111, "INF-1") )