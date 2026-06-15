class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def JobScheduling(self, jobs_list, n):
        jobs = []
        max_deadline = 0
        for i in range(n):
            j_id, deadline, profit = jobs_list[i]
            jobs.append(Job(j_id, deadline, profit))
            if deadline > max_deadline:
                max_deadline = deadline
                
        jobs.sort(key=lambda x: x.profit, reverse=True)
        
        schedule = [-1] * (max_deadline + 1)
        
        count_jobs = 0
        max_profit = 0
        
        for i in range(n):
            for j in range(jobs[i].deadline, 0, -1):
                if schedule[j] == -1:
                    schedule[j] = jobs[i].id 
                    count_jobs += 1
                    max_profit += jobs[i].profit
                    break 
                
        return [count_jobs, max_profit]