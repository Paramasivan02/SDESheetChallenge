class Solution:
    def findContentChildren(self, student: list[int], cookie: list[int]) -> int:
        student.sort()
        cookie.sort()
        
        i = 0  
        j = 0  
        
        while i < len(student) and j < len(cookie):
            if cookie[j] >= student[i]:
                i += 1  
            j += 1      

        return i