def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(jobs, key=lambda x: x[1])[1]
    schedule = [-1] * max_deadline
    total_profit = 0

    for job in jobs:
        deadline = job[1] - 1
        while deadline >= 0:
            if schedule[deadline] == -1:
                schedule[deadline] = job[0]
                total_profit += job[2]
                break
            deadline -= 1

    return total_profit, [job_id for job_id in schedule if job_id != -1]


# Example usage
jobs = [("J1", 2, 15), ("J2", 3, 1), ("J3", 1, 10), ("J4", 2, 20), ("J5", 3, 5)]
profit, schedule = job_sequencing(jobs)
print("Maximum profit:", profit)
print("Scheduled jobs:", schedule)