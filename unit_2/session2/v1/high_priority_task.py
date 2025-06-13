def get_highest_priority_task(tasks):
	max = 0
	max_task = None
	for task in tasks:
		if tasks[task] > max:
			max = tasks[task]
			max_task = task
	tasks.pop(max_task)
	return max_task

tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)