class Solution:
    def searchInsert(name,target):
        for i in range(len(name)):
            if name[i] >= target:
                return i
        return len(name)

list = Solution()
name = []
n = int(input("How many numbers: "))
for i in range(n):
    name.append(int(input("Enter the number: ")))
target =int(input("Target: "))
print("Input : ","name =",name,",","target =",target)
print("Output : ",list.searchInsert(name,target))
