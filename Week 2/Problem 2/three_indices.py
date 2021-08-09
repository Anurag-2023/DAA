import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")

def differ_pair(arr,size):
    c=0
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if arr[i]+arr[j]==arr[k] and i!=j and i<j:
                    print(f'{i+1},{j+1},{k+1}')
                    c+=1

    if c==0:
        print('No sequence found')

n=int(input())
for i in range(n):
    size = int(input())
    arr = input()
    arr = arr.split()
    arr = [int(element) for element in arr]

    differ_pair(arr,size)