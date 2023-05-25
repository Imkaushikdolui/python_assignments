# 3) Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] 

class SubsetGenerator:
    def get_subsets(self, nums):
        subsets = [[]]
        for num in nums:
            subsets += [curr_subset + [num] for curr_subset in subsets]
        return subsets


generator = SubsetGenerator()
print(generator.get_subsets([3,4,5]))