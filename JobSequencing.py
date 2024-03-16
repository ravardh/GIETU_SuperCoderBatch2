def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slots = [False] * max_deadline
    total_profit = 0
    schedule = []
    for job in jobs:
        deadline = job[1] - 1
        while deadline >= 0:
            if not slots[deadline]:
                slots[deadline] = True
                total_profit += job[2]
                schedule.append(job[0])
                break
            deadline -= 1
    return total_profit, schedule
jobs = [("J1", 2, 15), ("J2", 3, 1), ("J3", 1, 10), ("J4", 2, 20), ("J5", 3, 5)]
profit, schedule = job_sequencing(jobs)
print("Maximum profit:", profit)
print("Scheduled jobs:", schedule)
