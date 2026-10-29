def longest(arr):
    if not arr:
        return ""
    
    ref=arr[0]

    for i in range(len(ref)):
        char=ref[i]

        for string in arr[1:]:
            if i>=len(string) or string[i] !=char:
                return ref[:i]
    return ref




print(longest(["geeksforgeeks", "geeks", "geek", "geezer"]))