reports = []
with open("day02_input.txt", 'r') as f:
  for report in f:
  	reports.append([int(x.strip()) for x in report.split(" ")])

def analyze_report(report):
	is_increasing = report[0]-report[1] > 0
	for i in range(len(report)-1):
		diff = report[i] - report[i+1]
		if abs(diff) > 3 or diff == 0:
			return False
		if is_increasing and diff < 0:
			return False
		if not is_increasing and diff > 0:
			return False
	return True

total_safe = 0
for report in reports:
	if analyze_report(report):
		total_safe += 1

print("part 1:",total_safe)

total_dampened = 0
for report in reports:
	if analyze_report(report):
		total_dampened += 1
	else:
		for i in range(len(report)):
			dampened_report = report[:i]+report[i+1:]
			if analyze_report(dampened_report):
				total_dampened += 1
				break

print("part 2:", total_dampened)