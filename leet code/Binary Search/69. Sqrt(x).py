#69. Sqrt(x)

#related topics math , binary search


#first solution
#math
def mySqrt(x):
    return int(x**0.5)

print(mySqrt(4))
print(mySqrt(8))


#binary search
def mySqrt2(x):
        lo, hi = 0, x
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if mid * mid > x:
                hi = mid - 1
            elif mid * mid < x:
                lo = mid + 1
            else:
                return mid
        return hi

print(mySqrt2(4))
print(mySqrt2(8))
