class Job:
    def __init__(self, name, profit, deadline):  
        self.name = name
        self.profit = profit
        self.deadline = deadline

def find_max_profit_jobs(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)  
    max_profit_jobs = []
    max_deadline = max(jobs, key=lambda x: x.deadline).deadline  

    slots = [False] * (max_deadline + 1)

    
    for job in jobs:
        for i in range(job.deadline, 0, -1):
            if not slots[i]:
                max_profit_jobs.append(job)
                slots[i] = True
                break

    return max_profit_jobs

jobs = [
    Job("J1", 25, 4),
    Job("J2", 20, 2),
    Job("J3", 30, 4),
    Job("J4", 15, 3),
    Job("J5", 5, 2),
    Job("J6", 35, 3),
    Job("J7", 12, 1)
]

max_profit_jobs = find_max_profit_jobs(jobs)
print("Jobs with maximum profit:")
for job in max_profit_jobs:
    print(f"Job: {job.name}, Profit: {job.profit}, Deadline: {job.deadline}")
