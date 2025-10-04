task = input("Enter your task: ")
Priority = input("Priority(high/medium/low:")
time_bound=input("Is it time-bound? (yes/no): ")
message= " Consider completing it when you have free time" if time_bound.lower() == "no" else "that requires immediate attention today"
match Priority:
    case "high":
        print(f"Reminder: {task} is a high priority task {message}")
    case "medium":
        print(f"Reminder: {task} is a medium priority task {message}")
    case "low":
        print(f"Reminder: {task} is a low priority task {message}")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")