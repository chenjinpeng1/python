from django.test import TestCase

# Create your tests here.
def find_three(lst,goal):
    closed = (float("inf"),)
    closed_value = float("inf")
    for i in range(len(lst)-2):
        j=i+1
        k=len(lst)-1
        while j<k:
            tmp=tuple(lst[x]for x in (i,j,k))
            value_tmp = abs(sum(tmp)-goal)
            if value_tmp ==0:
                return tmp
            else:
                if value_tmp<closed_value:
                    closed_value = value_tmp
                    closed = tmp
                    if sum(tmp) - goal > 0:
                        k-=1
                    else:
                        j+=1
                else:
                    break
    return closed

a = [1,2,2,3,4,5,6,7]
value = find_three(a,7)
print(value)
