# job    profit    deadline
# J1      25         4
# J2      20         2
# J3      30         4
# J4      15         3
# J5      5          2
# J6      35         3
# J7      12         1

# write a code to find jobs with maimum profit using kruskal algorithm in python


class Job:
    def __init__(self, name, profit, deadline):
        self.name = name
        self.profit = profit
        self.deadline = deadline

def find_max_profit_jobs(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)  # Sort jobs by profit in descending order
    max_profit_jobs = []
    max_deadline = max(jobs, key=lambda x: x.deadline).deadline  # Find the maximum deadline

    # Initialize an array to track deadlines. Initially, all slots are available.
    slots = [False] * (max_deadline + 1)

    # Iterate over each job and assign it to the latest available slot before its deadline.
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
