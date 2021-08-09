import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")

def differ_pair(arr,size,key):
    c=0
    for i in range(size):
        for j in range(size):
            if arr[i]-arr[j]==key:
                c+=1
    print(c)

n=int(input())
for i in range(n):
    size = int(input())
    arr = input()
    arr = arr.split()
    arr = [int(element) for element in arr]
    key = int(input())
    differ_pair(arr,size,key)
