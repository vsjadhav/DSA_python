import math #for bucket sort

def bubble_sort(l):
    for a in range(len(l)-1):
        i,j = 0,1
        for b in range(len(l)-a-1):
            if l[i]>l[j]:
                temp = l[j]
                l[j] = l[i]
                l[i] = temp
            i+=1
            j+=1

def selection_sort(l):
    for i in range(len(l)-1):
        min_value_index= i
        for j in range(i+1,len(l)):
            if l[j] < l[min_value_index]:
                min_value_index = j
        temp = l[i]
        l[i] = l[min_value_index]
        l[min_value_index] = temp

def insertion_sort(l):
    for i in range(len(l)-1):
        t=i
        j= t+1
        while t>=0:
            if l[j]<l[t]:
                temp = l[j]
                l[j] = l[t]
                l[t] = temp
                j-=1
                t-=1
            else: break
      
def bucket_sort(l): # effective only for uniformly distributed data
    max_value = l[0]
    for i in range(len(l)):
        if l[i]> max_value:
            max_value = l[i]
    numberOfBuckets = round(math.sqrt(len(l)))
    buckets = []
    for _ in range(numberOfBuckets):
        buckets.append([])
    for i in l:
        bucketNumber = math.ceil(i*numberOfBuckets/max_value)
        buckets[bucketNumber-1].append(i)
        # print(buckets)
    l.clear()
    for bucket in buckets:
        bucket.sort() #use any sorting algo to sort individual buckets
        # print(bucket)
        for value in bucket:
            l.append(value)
    

l = [9,6,8,4,2,3,1,4687,65,648,464,5,7,9,34,64,684,654,12]
print(l)

# bubble_sort(l)
# print(l)

# selection_sort(l)
# print(l)

# insertion_sort(l)
# print(l)

bucket_sort(l)
print(l)