def selectionsort(arr):
    n=len(arr)


    for i in range(n):
        minindex=i

        for j in range(i+1 ,n):
            if arr[minindex]> arr[j]:
                minindex=j

        arr[i],arr[minindex]=arr[minindex],arr[i] 
    return arr     

num=[23,78,2,5,1]      
print(selectionsort(num))