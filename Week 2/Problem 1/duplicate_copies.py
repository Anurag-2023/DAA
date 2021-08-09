import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")

def duplicate_copies(arr,size,key):
    c=0
    for i in range(size):
        if arr[i]==key:
            c+=1
    if c!=0:
        print(f'{key}-{c}')
    else:
        print('Key not present')


n=int(input())
for i in range(n):
    size = int(input())
    arr = input()
    arr = arr.split()
    arr = [int(element) for element in arr]
    key = int(input())
    duplicate_copies(arr,size,key)