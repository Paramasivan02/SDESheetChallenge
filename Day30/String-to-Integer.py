class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        
        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
            
        # If the string is completely empty or just spaces
        if i == n:
            return 0
            
        # Step 2: Determine the sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # Step 3: Read digits and construct the integer
        result = 0
        while i < n and s[i].isdigit():
            # In Python, integers have arbitrary precision, so we can just 
            # keep adding. In languages like C++ or Java, we'd have to 
            # check for overflow before multiplying by 10.
            result = result * 10 + int(s[i])
            i += 1
            
        # Apply the sign
        result *= sign
        
        # Step 4: Rounding (Clamping to 32-bit signed integer range)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result