def job_sequencing(deadlines, profits):
    jobs = list(zip(range(1, len(deadlines) + 1), deadlines, profits))
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(deadlines)
    schedule = [0] * (max_deadline + 1)
    total_profit = 0
    for job in jobs:
        job_id, deadline, profit = job
        while deadline > 0 and schedule[deadline] != 0:
            deadline -= 1
        if deadline > 0:
            schedule[deadline] = job_id
            total_profit += profit
    return schedule, total_profit
def main():
    num_jobs = int(input("Enter the number of jobs: "))
    deadlines = []
    profits = []
    for i in range(num_jobs):
        deadline, profit = map(int, input(f"Enter deadline and profit for job {i+1} (separated by space): ").split())
        deadlines.append(deadline)
        profits.append(profit)
    schedule, total_profit = job_sequencing(deadlines, profits)
    print("\nJob Schedule:")
    for day, job_id in enumerate(schedule[1:], start=1):
        if job_id != 0:
            print(f"Day {day}: Job {job_id}")
    print("\nTotal Profit:", total_profit)
if __name__ == "__main__":
    main()