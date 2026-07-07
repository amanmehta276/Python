# nums=[1,2,3]
# k=3
# ans=[1,2]

def subarray(arr,k):
    prefix_sum=0
    count=0
    prefix_map={0:1}

    for a in arr:
        prefix_sum+=a
        if prefix_sum-k in prefix_map:
            count+=prefix_map[prefix_sum-k]

        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1
    
    return count

arr=[1,2]
k=2
print(subarray(arr,k))