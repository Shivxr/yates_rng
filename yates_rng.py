import time

class ranbit:
    def __init__(self):
        # Use current time in milliseconds as seed
        self.x = int(time.time() * 1000) & 0xFFFFFFFF

    def rfind(self):
        x = self.x
        x ^= (x << 13) & 0xFFFFFFFF
        x ^= (x >> 17) & 0xFFFFFFFF
        x ^= (x << 5) & 0xFFFFFFFF
        self.x = x & 0xFFFFFFFF
        return x

def domino_search(arr,target):
    n=len(arr)-1
    left=0
    v=ranbit()
    for i in range(len(arr)):

        z=v.rfind()

        r=z%(n+1)

        if r-1>=0:
            left=r-1
        
        if arr[r]==target or arr[left]==target:
            return i

        arr[r],arr[n]=arr[n],arr[r]

        if r!=left:
            arr[left],arr[n-1]=arr[n-1],arr[left]
            n-=1
        
        n-=1
        if n<0:
            return -1
    return -1


def domino_shuffle(arr):

    n=len(arr)-1

    v=ranbit()

    for i in range(len(arr)):
        narr=[]

        z=v.rfind()

        r=z%(n+1)

        narr.append(arr[r])

        n-=1
    
    return narr


def domino_pick(arr):

    v=ranbit()

    z=v.rfind()

    return arr[z%len(arr)]

def rin(arr,target):

    v=domino_search(arr,target)

    if v>=0:
        return True
    
    return False







        

        



    



    
