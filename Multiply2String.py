#Given two numbers as strings s1 and s2. Calculate their Product.

class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        # return the product string
        n1=int(s1)
        n2=int(s2)
        return n1*n2

solution_instance = Solution()
s1 = "12"
s2 = "34"
result = solution_instance.multiplyStrings(s1, s2)

# Print the result
print("Product of", s1, "and", s2, "is:", result)
