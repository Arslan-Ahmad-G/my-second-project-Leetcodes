#744. Find Smallest Letter Greater Than Target
# official version # binary search
import bisect

from typing import List
class Solution: # type: ignore
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = (l + r) // 2
            if letters[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return letters[l % len(letters)] 
    
# my version
from typing import List
class Solution:         # type: ignore
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        if  target >= letters[-1]:
            return letters[0]
        
        while left <= right:
            mid = (left+right)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid -1

        return letters[left]
            


class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        [DOC]
        Uses bisect_right to find the insertion point.
        Wraps around using modulo.
        """
        index = bisect.bisect_right(letters, target)
        return letters[index % len(letters)]
    
solution = Solution()

print(Solution().nextGreatestLetter(["c","f","j"], "a"))  # Output: "c"
print(Solution().nextGreatestLetter(["c","f","j"], "c"))
print(Solution().nextGreatestLetter(["c","f","j"], "d"))