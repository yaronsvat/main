import re

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        for i in range (0,len(prices)):
            for j in range (i+1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit

    # Fibonacci
    def climbStairs(self, n):
        if n < 1:
            return -1
        if n == 1:
            return 1
        if n == 2:
            return 2
        second_out = 2
        first_out = 1
        for i in range(3, n + 1):
            current = second_out + first_out
            first_out = second_out
            second_out = current
        return second_out

    def isPalindrome(self, s):
        s = s.replace(" ", "").lower()
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        temp = clean_text[::-1]
        return clean_text == temp

    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

    def firstUniqChar(self, s):
        for i in range (0, len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1

    def reverseString(self, s):
        temp = []
        for i in range(len(s) - 1, -1, -1):
            temp.append(s[i])
        return temp

    def maxSubArray(self, nums):
        max_sum = nums[0]
        for i in range (0,len(nums)):
            for j in range (i+1,len(nums)+1):
                if (sum(nums[i:j])) > max_sum:
                    max_sum = sum(nums[i:j])
        return max_sum

    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev2 = 0
        prev1 = 0
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        return prev1

    def romanToInt(self, s):
        dict_roman = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900, "I":1, "V":5, "X":10, "L":50,
                      "C":100, "D":500, "M":1000}
        i = 0
        int_number = 0
        while i < len(s):
            if s[i:(i+2)] in dict_roman.keys():
                int_number = int_number + dict_roman[s[i:(i+2)]]
                i+=2
            elif s[i] in dict_roman.keys():
                int_number = int_number + dict_roman[s[i]]
                i+=1
        return int_number

    def countPrimes(self, n):
        prime_numbers = 0
        for i in range (1, n):
            count=0
            for j in range (1, i+1):
                if i%j == 0:
                    count+=1
                if count > 2:
                    break
            if count == 2:
                prime_numbers+=1
        return prime_numbers

    def isPowerOfThree(self, n):
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

    def hammingWeight(self, n):
        count_ones = 0
        while n > 0:
            if n % 2 == 1:
                count_ones+=1
            n//=2
        return count_ones

    def hammingDistance(self, x, y):
        return bin(x ^ y).count('1')

    def pascalTriangle(self, numRows):
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        final = [[1], [1,1]]
        previous_line = [1,1]
        repeat_next = 2
        while numRows > 2:
            line_to_add = [1]
            for i in range (0, repeat_next-1):
                line_to_add.append(previous_line[i] + previous_line[i+1])
            line_to_add.append(1)
            final.append(line_to_add)
            numRows-=1
            previous_line = line_to_add
            repeat_next = len(line_to_add)
        return final

    def isValid(self, s):
        bracket_map = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in bracket_map:
                stack.append(char)
            elif stack and char == bracket_map[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack

    def missingNumber(self, nums):
        for i in range (0, len(nums)+1):
            if i not in nums:
                return i

    def fizzBuzz(self, n):
        answer=[]
        for i in range (1, n+1):
            if (i % 3)==0 and (i % 5)==0:
                answer.append("FizzBuzz")
            elif (i % 3)==0:
                answer.append("Fizz")
            elif (i % 5)==0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

    def sevenboom(self, n):
        answer=[]
        for i in range (1, n+1):
            if "7" in str(i):
                answer.append("Boom")
            elif i % 7 == 0:
                answer.append("Boom")
            else:
                answer.append(str(i))
        return answer

    def find_substring_index(self, main_string, substring):
        main_length = len(main_string)
        sub_length = len(substring)

        for i in range(main_length - sub_length + 1):  # Limit to avoid overflow
            match = True
            for j in range(sub_length):
                if main_string[i + j] != substring[j]:
                    match = False
                    break
            if match:
                return i  # Return the start index of the substring
        return -1  # Return -1 if the substring is not found

    def plusOne(self, digits):
        def int_to_list_of_digits(n):
            return [int(digit) for digit in str(n)]
        base10 = 1
        number = 0
        for i in range (len(digits)-1,-1,-1):
            number = number+digits[i]*base10
            base10 = base10*10
        number+=1
        result = int_to_list_of_digits(number)
        return result

    def moveZeroes(self, nums):
        last_non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1
        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0

    def isValidSudoku(self, board):
        # Create sets to track seen numbers in rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3 boxes
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':  # Ignore empty cells
                    # Calculate box index
                    box_index = (i // 3) * 3 + (j // 3)

                    # Check for duplicates in the respective row, column, and box
                    if (num in rows[i]) or (num in cols[j]) or (num in boxes[box_index]):
                        return False

                    # Add the number to the respective sets
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)
        return True

    def removeDuplicates(self, nums):
        j=0
        for i in range (0,len(nums)):
            if nums[j] != nums[i]:
                j+=1
                nums[j] = nums[i]
        for i in range (j+1, len(nums)):
            nums[i] = -1
        return j+1

    def intersect(self, nums1, nums2):
        final = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2 and i not in final:
                    final.append(i)
        else:
            for i in nums2:
                if i in nums1 and i not in final:
                    final.append(i)
        return final

    def twoSum(self, nums, target):
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i

    def containsDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False

    def maxProfit2(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

    def rotate(self, nums, k):
        temp=[0]*len(nums)
        for index,value in enumerate (nums):
            if index+k <= (len(nums)-1):
                temp[index+k] = nums[index]
            else:
                indexnew = (index+k) % (len(nums))
                temp[indexnew] = nums[index]
        return temp

    def singleNumber(self, nums):
        single_appear = []
        for num in nums:
            if num not in single_appear:
                single_appear.append(num)
            else:
                single_appear.remove(num)
        if single_appear:
            return single_appear[0]
        return None

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix




solution = Solution()

# # Example usage for maxProfit:
# prices = [2, 21, 41, 9, 6, 47]
# print(solution.maxProfit(prices))
#
# # Example for climb stairs:
# n = 5
# print(solution.climbStairs(n))

# # Example for isPalindrome:
# polString = "BAbbab"
# print("Is {0} a polidrome? {1}".format(polString, solution.isPalindrome(polString)))
#
# # Example for firstUniqChar:
# s = "TgTgTgRg"
# print("firstUniqChar= {0}".format(solution.firstUniqChar(s)))
#
# # Example for reverseString
# s = ["a", "b", "c", "X"]
# print("The reverse string of {0} is {1}".format(s, solution.reverseString(s)))

# # Example for maxSubArray
#nums = [-2, 5,4,-1,7,8]
#print("The subarray {0} has the largest sum {1}".format(nums, solution.maxSubArray(nums)))

# # Example for rob
# houses = [1, 2, 3, 6, 9]
# print(solution.rob(houses))

# # Example for roman to integer
# roman = "MCMXCIV"
# print("Int of the roman: {0} is {1}".format(roman, solution.romanToInt(roman)))

# # Example for count Primes
# n = 5
# print("There are {0} prime numbers less than {1}".format(solution.countPrimes(n), n))

# # Example for is Power Of Three
# n = 8
# print(solution.isPowerOfThree(n))

# # Example for hammingWeight
# n = 11
# print(solution.hammingWeight(n))

# # Example for hamming Distance
# print(solution.hammingDistance(1, 4))

# # Example for pascal Triangle
# print(solution.pascalTriangle(5))

# # Example for Valid Parentheses
# s = "[()([]{}[])]"
# print(solution.isValid(s))

# # Example for Missing Number
# nums = [8,6,4,2,3,5,7,0,1]
# print(solution.missingNumber(nums))

# # Example for Fizz Buzz
# print(solution.fizzBuzz(12))

# # Example for seven boom
# print(solution.sevenboom(2000))

# # Example for find substring index
# result = solution.find_substring_index("hello world", "world")
# print(result)

# # Example for plus one
# print(solution.plusOne([9,9,9,9,9,9,9,9]))

# # Example for move zeros
# print(solution.moveZeroes([0,0,0,1,0,0,3,12,0,15]))

# # Example for is Valid Sudoku
# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9",".",".",".",".",".","6","."]
# ,[".",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","."]]
# print(solution.isValidSudoku(board))

# # Example for remove Duplicates
# nums = [0,0,1,1,1,2,2,3,3,4,4,4,4,6,6,6,7]
# print(solution.removeDuplicates(nums))

# # Example for intersect
# nums1 = [1,2]
# nums2 = [1,1]
# print(solution.intersect(nums1, nums2))

# Example for two Sum
# nums = [2,3,3,8]
# target = 5
# print(solution.twoSum(nums, target))

# # Example for contains Duplicate
# nums = [1,1,1,3,3,4,3,2,4,2]
# print(solution.containsDuplicate(nums))

# # Example for max profit 2 (best time to buy and sell stock II
# prices = [7,1,5,3,6,4]
# print(solution.maxProfit2(prices))

# # Example for rotate
# print(solution.rotate(nums = [1,2,3,4,5,6,7], k = 3))

# # Example for singleNumber
# nums = [4,1,2,1,2,4,8,8,19]
# print(solution.singleNumber(nums))

# # Example for longest Common Prefix
# print(solution.longestCommonPrefix(["flower","flow","xlight"]))