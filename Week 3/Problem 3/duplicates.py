import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")


def duplicates(arr,size):
    temp=0
    for i in range(size-1):

        for j in range(i+1,size):
            if arr[i]==arr[j]:
                temp+=1
                break
    if temp>0:

        print("YES")
    else:
        print("NO")




n=int(input())
for i in range(n):
    size = int(input())
    arr = input()
    arr = arr.split()
    arr = [int(element) for element in arr]

    duplicates(arr,size)