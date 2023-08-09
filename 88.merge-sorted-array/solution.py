class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in range(m + n - 1, -1, -1):
            e1 = nums1[m - 1] if m > 0 else None
            e2 = nums2[n - 1] if n > 0 else None
            if e1 is None or (e2 is not None and e2 > e1):
                nums1[x] = e2
                n -= 1
            else:
                nums1[x] = e1
                m -= 1
