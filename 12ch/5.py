class Data:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_data(self, index, n):
        self.nums[index] = n

num = Data()
print(num.nums)
num.change_data(3, 5)
print(num.nums)
