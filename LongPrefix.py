

def longestCommonPrefix( arr, n):
    if n == 0:
        return "-1"

    prefix = arr[0]

    for i in range(1, n):
        while not arr[i].startswith(prefix):
                # Reduce the prefix by one character
            prefix = prefix[:-1]

                # If the prefix becomes empty, there's no common prefix
            if not prefix:
                return "-1"
        return prefix

arr = ["apple", "appetite", "apparatus"]
res=longestCommonPrefix(arr,3)
print(res)