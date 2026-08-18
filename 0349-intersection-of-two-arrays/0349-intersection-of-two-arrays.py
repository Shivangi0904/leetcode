class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set()
        for num in nums1:
            seen.add(num)
        answer = set()
        for num in nums2:
            if num in seen:
                answer.add(num)
        return list(answer)

        