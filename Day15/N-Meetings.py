class Meeting:
    def __init__(self, start, end, index):
        self.start = start
        self.end = end
        self.index = index

class Solution:
    def maxMeetings(self, n: int, start: list[int], end: list[int]) -> list[int]:
        meetings = []
        for i in range(n):
            meetings.append(Meeting(start[i], end[i], i + 1))
            
        meetings.sort(key=lambda x: (x.end, x.index))
        
        result = []
        
        result.append(meetings[0].index)
        limit_time = meetings[0].end
        
        for i in range(1, n):
            if meetings[i].start > limit_time:
                result.append(meetings[i].index)
                limit_time = meetings[i].end 
                
        return result