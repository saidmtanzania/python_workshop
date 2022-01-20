"""
Recursion Function: 
routine that calls itself directly or indirectly.
"""
def count_down(x):
    if x == 1:
        print(x)
        return 1
    print(x)
    return count_down(x-1)
# intial count_down function value
count_down(9)

