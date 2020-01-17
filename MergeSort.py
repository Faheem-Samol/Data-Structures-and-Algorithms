import random
def mergesrt(arr):
    if len(arr)>1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        
        mergesrt(L)
        mergesrt(R)
        
        i=j=k=0
        
        while i < len(L) and j < len (R):
            if L[i]<R[j]:
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1
            k+=1
            
        while i < len(L):
            arr[k] = L[i]
            k+=1
            i+=1
        while j < len(R):
            arr[k] = R[j]
            k+=1
            j+=1

def createArr(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(0,100))
    return arr
    
if __name__ == '__main__':
    print('The array is')
    arr = createArr(100)
    print(arr,'\n')
    print('The sorted array is')
    mergesrt(arr)
    print(arr,'\n')
