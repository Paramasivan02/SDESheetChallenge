class Solution:
    def solve(self, A: list[int], B: int) -> int:
        freq_map = {0: 1}
        
        count = 0
        prefix_xor = 0
        
        for num in A:
            prefix_xor ^= num
            
            target = prefix_xor ^ B
            
            if target in freq_map:
                count += freq_map[target]
                
            if prefix_xor in freq_map:
                freq_map[prefix_xor] += 1
            else:
                freq_map[prefix_xor] = 1
                
        return count