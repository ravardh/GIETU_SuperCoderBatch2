def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def count_required_labs(start, end):
    events = [(time_to_minutes(start[i]), time_to_minutes(end[i])) for i in range(len(start))]
    events.sort()

    ongoing_classes = []
    required_labs = 0

    for start_time, end_time in events:
        while ongoing_classes and ongoing_classes[0] <= start_time:
            ongoing_classes.pop(0)
        ongoing_classes.append(end_time)
        required_labs = max(required_labs, len(ongoing_classes))

    return required_labs

# Test Cases
S1 = ["10:00", "10:30", "11:00", "11:30"]
E1 = ["10:30", "11:00", "11:30", "12:00"]
print("Test Case 1:", count_required_labs(S1, E1))  # Output: 1

S2 = ["9:00", "9:30", "11:00", "12:00"]
E2 = ["10:15", "11:00", "12:15", "13:00"]
print("Test Case 2:", count_required_labs(S2, E2))  # Output: 2

S3 = ["9:00", "9:15", "9:30", "9:00", "10:15"]
E3 = ["10:00", "10:30", "10:45", "9:30", "11:30"]
print("Test Case 3:", count_required_labs(S3, E3))  # Output: 3
    