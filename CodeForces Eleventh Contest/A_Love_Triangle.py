n = int(input())
planes = list(map(int, input().split()))
isfound = False

for i, plane in enumerate(planes):
    first = i + 1
    second = plane
    third = planes[second - 1]

    if second < n + 1 and planes[third - 1] == first:
        isfound = True
        break

if isfound:
    print("YES")

else:
    print("NO")

