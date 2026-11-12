
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            a_left = float('-inf') if i == 0 else nums1[i - 1]
            a_right = float('inf') if i == m else nums1[i]

            b_left = float('-inf') if j == 0 else nums2[j - 1]
            b_right = float('inf') if j == n else nums2[j]

            if a_left <= b_right and b_left <= a_right:
                if (m + n) % 2:
                    return float(max(a_left, b_left))

                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            elif a_left > b_right:
                right = i - 1

            else:
                left = i + 1
