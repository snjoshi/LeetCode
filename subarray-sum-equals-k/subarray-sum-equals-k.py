class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_freq = {0: 1}  
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - k in sum_freq:
                count += sum_freq[current_sum - k]

            sum_freq[current_sum] = sum_freq.get(current_sum, 0) + 1

        return count
                