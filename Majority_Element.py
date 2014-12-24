__author__ = 'youfu'
"""
Runtime: O(n2) — Brute force solution: 
		Check each element if it is the majority element.
				
Runtime: O(n), Space: O(n) — Hash table: 
		Maintain a hash table of the counts of each element, then find the most common one.
				
Runtime: O(n log n) — Sorting: 
		Find the longest contiguous identical element in the array after sorting.
		
Average runtime: O(n), Worst case runtime: Infinity — Randomization: 
				Randomly pick an element and check if it is the majority element. 
				If it is not, do the random pick again until you find the majority element. 
				As the probability to pick the majority element is greater than 1/2, 
				the expected number of attempts is < 2.

Runtime: O(n log n) — Divide and conquer: 
		 Divide the array into two halves, 
		 then find the majority element A in the first half and the majority element B in the second half. 
		 The global majority element must either be A or B. If A == B, 
		 then it automatically becomes the global majority element.
		 If not, then both A and B are the candidates for the majority element, 
		 and it is suffice to check the count of occurrences for at most two candidates. 
		 The runtime complexity, T(n) = T(n/2) + 2n = O(n log n).
		 
Runtime: O(n) — Moore voting algorithm: 
		We maintain a current candidate and a counter initialized to 0. 
		As we iterate the array, we look at the current element x:
		If the counter is 0, we set the current candidate to x and the counter to 1.
		If the counter is not 0, we increment or decrement the counter based on whether x is the current candidate.
		After one pass, the current candidate is the majority element. Runtime complexity = O(n).
Runtime: O(n) — Bit manipulation: 
		We would need 32 iterations, each calculating the number of 1's for the ith bit of all n numbers.
		Since a majority must exist, therefore, either count of 1's > count of 0's or vice versa (but can never be equal).
		The majority number’s ith bit must be the one bit that has the greater count.

"""
# Time Limit Exceeded
#Runtime: O(n log n) — Sorting
class Solution1:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        self.quick_sort(num, 0, len(num))
        return num[len(num)//2]

    def quick_sort(self, L, low, high):
        if low == high:
            return
        store_index = low+1
        for i in range(low+1, high):
            if L[i] < L[low]:
                L[i], L[store_index] = L[store_index], L[i]
                store_index += 1
        L[low], L[store_index-1] = L[store_index-1], L[low]
        self.quick_sort(L, low, store_index-1)
        self.quick_sort(L, store_index, high)

#Runtime: O(n), Space: O(n) — Hash table
class Solution2:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        dict1 = {}
        for x in num:
            if x in dict1:
                dict1[x] += 1
            else:
                dict1[x] = 1
        values = dict1.values()
        max_value = max(values)
        for x in dict1:
            if dict1[x] == max_value:
                return x

#Runtime: O(n) — Moore voting algorithm
class Solution3:
    def majorityElement(self, num):
        elem = self.find_element(num)
        count = 0
        for x in num:
            if x == elem:
                count += 1
        if count > len(num)//2:
            return elem
        else:
            return None

    def find_element(self, L):
        mark = 0
        for i in range(len(L)):
            if mark == 0:
                mark = 1
                elem = L[i]
            elif elem == L[i]:
                mark += 1
            else:
                mark -= 1
        return elem

#Runtime: O(n) — Bit manipulation
class Solution5:

    def majorityElement(self, num):
        major = 0
        mid = len(num) // 2
        for i in range(32):
            count_1bit = 0
            for x in num:
                if x < 0:
                    x = abs(x)
                count_1bit += (x >> i) & 0x1
            if count_1bit > mid:
                major += 2 ** i
        negative_count = 0
        for x in num:
            if x < 0:
                negative_count += 1
        if negative_count > mid:
            major -= major * 2
        return major


s5 = Solution5()
L = [-1,1,1,1,2,1]

majority = s5.majorityElement(L)
print(majority)
s3 = Solution3()
majority = s3.majorityElement(L)
print(majority)