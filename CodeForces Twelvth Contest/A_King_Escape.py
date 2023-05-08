n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

def check_quad(x, y, quad):
    return quad[0] <= x <= quad[1] and quad[2] <= y <= quad[3]

quad1 = [1, ax, 1, ay]
quad2 = [ax, n, 1, ay]
quad3 = [1, ax, ay, n]
quad4 = [ax, n, ay, n]

quads = [quad1, quad2, quad3, quad4]

def find_quad(x, y):
    for i, quad in enumerate(quads):
        if check_quad(x, y, quad):
            return i + 1
        
if find_quad(bx, by) == find_quad(cx, cy):
    print("YES")

else:
    print("NO")