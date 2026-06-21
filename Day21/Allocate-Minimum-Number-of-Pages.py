class Solution:
    def findPages(self, arr: list[int], n: int, m: int) -> int:
        if m > n:
            return -1
            
        def count_students(max_pages: int) -> int:
            students = 1
            current_pages = 0
            
            for pages in arr:
                if current_pages + pages > max_pages:
                    students += 1
                    current_pages = pages
                else:
                    current_pages += pages
                    
            return students

        low = max(arr)  
        high = sum(arr) 
        
        while low <= high:
            mid = (low + high) // 2
            
            if count_students(mid) <= m:
                high = mid - 1
            else:
                low = mid + 1
                
        return low