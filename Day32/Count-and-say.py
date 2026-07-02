class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
            
        current_string = "1"
        
        for _ in range(n - 1):
            next_string_parts = []
            
            i = 0
            while i < len(current_string):
                count = 1
                while i + 1 < len(current_string) and current_string[i] == current_string[i+1]:
                    count += 1
                    i += 1
                    
                next_string_parts.append(str(count))
                next_string_parts.append(current_string[i])
                
                i += 1
                
            current_string = "".join(next_string_parts)
            
        return current_string