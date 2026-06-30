class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeats = (len(b) + len(a) - 1) // len(a)
        
        repeated_a = a * min_repeats
        
        if b in repeated_a:
            return min_repeats
            
        repeated_a += a
        if b in repeated_a:
            return min_repeats + 1
            
        return -1