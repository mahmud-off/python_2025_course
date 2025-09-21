#input
a = [1, 8, 6, 2, 5, 4, 8, 3, 8]

p1 = 0
p2 = len(a)-1

maxSquare = 0

while p1 != p2:
    newSquare = 0
    if(a[p1] < a[p2]):
        #computing square
        newSquare = (p2 - p1) * a[p1]
        if(newSquare > maxSquare):
            maxSquare = newSquare
            print(f"p1 - {p1}; p2 - {p2}; newMaxSquare - {maxSquare}")
        p1 += 1    
    else:
        #computing square
        newSquare = (p2 - p1) * a[p2]
        if(newSquare > maxSquare):
            maxSquare = newSquare
            print(f"p1 - {p1}; p2 - {p2}; newMaxSquare - {maxSquare}")
        p2 -= 1

print(maxSquare)

#Time complexity - O(n)