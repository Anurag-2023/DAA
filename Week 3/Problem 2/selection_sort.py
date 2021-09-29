import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")


def selection_sort(arr,size):
    comparisons=0
    swap=0
    for i in range(size-1):
        small=arr[i]
        temp=i
        for j in range(i+1,size):
            comparisons +=1
            if small>arr[j]:

                small=arr[j]
                temp=j
        arr[temp]=arr[i]
        arr[i]=small
        swap+=1

    arr = ' '.join(str(element) for element in arr)
    print(arr)
    print(f'comparisons = {comparisons}')
    print(f'swaps = {swap}')


n=int(input())
for i in range(n):
    size = int(input())
    arr = input()
    arr = arr.split()
    arr = [int(element) for element in arr]

    selection_sort(arr,size)