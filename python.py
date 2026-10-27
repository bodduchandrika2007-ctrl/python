Examination Result and Grace-Mark Validation
Problem statement
Process marks in several subjects, apply subject-wise pass criteria and a grace-mark policy, and produce the final result without exceeding maximum marks.
Algorithm (step by step)
1.	Start and read the marks for each subject.
2.	Check that each mark is between 0 and 100.
3.	If a mark is below 35 but is at least 30, add 5 grace marks, without exceeding 100.
4.	Check every subject again against the pass mark of 35.
5.	Calculate total and percentage; print subject-wise final marks and result.
6.	Stop.
Python code
marks = [int(x) for x in input("Enter marks for 3 subjects: ").split()]
if len(marks) != 3 or any(m < 0 or m > 100 for m in marks):
    print("Invalid input: enter 3 marks from 0 to 100.")
else:
    final_marks = []
    for mark in marks:
        if 30 <= mark < 35:
            mark = min(mark + 5, 100)
        final_marks.append(mark)

    total = sum(final_marks)
    percentage = total / len(final_marks)
    result = "PASS" if all(m >= 35 for m in final_marks) else "FAIL"

    print("Final marks:", final_marks)
    print("Total:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Result:", result)
Sample output
Enter marks for 3 subjects: 32 76 81
Final marks: [37, 76, 81]
Total: 194 / 300
Percentage: 64.67 %
Result: PASS
Flowchart
Read the flowchart from top to bottom. START/END are terminators, ▱ is input/output, ▭ is a process, and ◇ is a decision.
(START)  Start
▱  Input 3 subject marks
◇  Are there exactly 3 valid marks from 0–100?
→  No: print invalid input → END
▭  For each mark: if 30 ≤ mark < 35, add 5 (maximum 100)
◇  Are all final marks ≥ 35?
▭  Calculate total and percentage; display marks and PASS/FAIL
(END)  Stop

 
Question 12: Attendance Recovery Computation
Problem statement
Calculate current attendance and determine how many consecutive classes a student must attend to reach a target attendance percentage.
Algorithm (step by step)
7.	Read classes attended, total classes, and target percentage.
8.	Validate that total classes is positive and attended classes is between zero and total.
9.	Calculate current attendance percentage.
10.	Assume the student attends every future class; increase both attended and total by one until the target is reached.
11.	Display current percentage and minimum additional classes needed.
12.	Stop.
Python code
attended = int(input("Classes attended: "))
total = int(input("Total classes held: "))
target = float(input("Target attendance (%): "))

if total <= 0 or attended < 0 or attended > total or not 0 < target <= 100:
    print("Invalid attendance details.")
else:
    current = attended / total * 100
    extra = 0
    a, t = attended, total

    while a / t * 100 < target:
        a += 1
        t += 1
        extra += 1

    print("Current attendance:", round(current, 2), "%")
    print("Additional classes to attend:", extra)
    print("Attendance after those classes:", round(a / t * 100, 2), "%")
Sample output
Classes attended: 36
Total classes held: 50
Target attendance (%): 75
Current attendance: 72.0 %
Additional classes to attend: 6
Attendance after those classes: 75.0 %
Flowchart
Read the flowchart from top to bottom. START/END are terminators, ▱ is input/output, ▭ is a process, and ◇ is a decision.
(START)  Start
▱  Input attended, total, target %
◇  Are inputs valid?
→  No: display invalid details → END
▭  Calculate current percentage; set extra = 0
◇  Is (attended + extra)/(total + extra) × 100 below target?
▭  Yes: increase attended, total and extra by 1; repeat check
▭  Display current percentage and extra classes
(END)  Stop

 
Question 13: ATM Transaction Sequence Simulation
Problem statement
Process deposits and withdrawals, maintain a balance, reject invalid transactions and withdrawals that exceed the available balance, and summarize transactions.
Algorithm (step by step)
13.	Set the opening balance and an empty transaction list.
14.	Read the number of transactions.
15.	For each transaction, read type and amount.
16.	If amount is not positive, reject it. For a deposit, add the amount. For a withdrawal, check the balance first.
17.	Record accepted transactions and print the final balance and transaction summary.
18.	Stop.
Python code
balance = 1000.0
transactions = [
    ("deposit", 500),
    ("withdraw", 300),
    ("withdraw", 1500),
    ("deposit", -50)
]

for kind, amount in transactions:
    if amount <= 0:
        print("Rejected:", kind, amount, "- amount must be positive")
    elif kind == "deposit":
        balance += amount
        print("Accepted deposit:", amount)
    elif kind == "withdraw":
        if amount <= balance:
            balance -= amount
            print("Accepted withdrawal:", amount)
        else:
            print("Rejected withdrawal:", amount, "- insufficient balance")
    else:
        print("Rejected: unknown transaction type")

print("Final balance:", f"{balance:.2f}")
print("Transactions processed:", len(transactions))
Sample output
Accepted deposit: 500
Accepted withdrawal: 300
Rejected withdrawal: 1500 - insufficient balance
Rejected: deposit -50 - amount must be positive
Final balance: 1200.00
Transactions processed: 4
Flowchart
Read the flowchart from top to bottom. START/END are terminators, ▱ is input/output, ▭ is a process, and ◇ is a decision.
(START)  Start with opening balance
▱  Read/process next transaction
◇  Is amount positive?
→  No: reject transaction
◇  Deposit or withdrawal?
▭  Deposit: add amount to balance
◇  Withdrawal: is amount ≤ balance?
▭  Yes: subtract; No: reject
▭  Repeat for all transactions; show final balance
(END)  Stop

 
Question 14: Warehouse Inventory Reconciliation
Problem statement
Compare opening stock, incoming quantity, dispatched quantity and recorded closing stock for products; detect discrepancies and calculate replenishment needs.
Algorithm (step by step)
19.	Store each product with opening, incoming, dispatched, recorded closing stock and target stock.
20.	Calculate expected closing stock = opening + incoming − dispatched.
21.	Compare expected closing stock with recorded closing stock.
22.	Calculate replenishment as the positive difference between target stock and expected stock.
23.	Display each product's reconciliation result.
24.	Stop.
Python code
# Product: name, opening, incoming, dispatched, recorded closing, target
products = [
    ("Pens", 100, 40, 70, 68, 90),
    ("Books", 50, 20, 25, 45, 60),
    ("Files", 80, 10, 30, 60, 50)
]

for name, opening, incoming, dispatched, recorded, target in products:
    expected = opening + incoming - dispatched
    difference = recorded - expected
    replenishment = max(0, target - expected)

    print("\nProduct:", name)
    print("Expected closing stock:", expected)
    print("Recorded closing stock:", recorded)
    if difference == 0:
        print("Status: Matched")
    else:
        print("Status: Discrepancy of", difference)
    print("Replenishment needed:", replenishment)
Sample output
Product: Pens
Expected closing stock: 70
Recorded closing stock: 68
Status: Discrepancy of -2
Replenishment needed: 20

Product: Books
Expected closing stock: 45
Recorded closing stock: 45
Status: Matched
Replenishment needed: 15

Product: Files
Expected closing stock: 60
Recorded closing stock: 60
Status: Matched
Replenishment needed: 0
Flowchart
Read the flowchart from top to bottom. START/END are terminators, ▱ is input/output, ▭ is a process, and ◇ is a decision.
(START)  Start
▱  Read product stock records
▭  Expected closing = opening + incoming − dispatched
◇  Does recorded stock equal expected stock?
▭  No: report discrepancy; Yes: report matched
▭  Replenishment = max(0, target − expected)
◇  More products?
→  Yes: process next product
(END)  No: display all results and stop

 
Question 15: Smart Parking Fee Management
Problem statement
Calculate parking charges using entry and exit times, vehicle category, overnight duration and a daily charge limit while validating the time inputs.
Algorithm (step by step)
25.	Read entry hour, exit hour and vehicle type.
26.	Validate hours are from 0 through 23 and vehicle type is supported.
27.	Calculate parked hours, treating an exit earlier than entry as next-day exit.
28.	Round any partial hour up to a full hour.
29.	Calculate the hourly fee by vehicle type and apply a daily cap.
30.	Display duration and fee.
Python code
entry = int(input("Entry hour (0-23): "))
exit_time = int(input("Exit hour (0-23): "))
vehicle = input("Vehicle (car/bike): ").lower()

rates = {"car": 30, "bike": 15}
if not (0 <= entry <= 23 and 0 <= exit_time <= 23) or vehicle not in rates:
    print("Invalid time or vehicle type.")
else:
    hours = exit_time - entry
    if hours <= 0:
        hours += 24
    rate = rates[vehicle]
    fee = min(hours * rate, 300)
    print("Parking duration:", hours, "hour(s)")
    print("Parking fee: Rs.", fee)
Sample output
Entry hour (0-23): 20
Exit hour (0-23): 2
Vehicle (car/bike): car
Parking duration: 6 hour(s)
Parking fee: Rs. 180
Flowchart
Read the flowchart from top to bottom. START/END are terminators, ▱ is input/output, ▭ is a process, and ◇ is a decision.
(START)  Start
▱  Input entry hour, exit hour, vehicle type
◇  Are hours and vehicle valid?
→  No: display invalid input → END
▭  Calculate duration; if exit ≤ entry, add 24 hours
▭  Fee = duration × vehicle rate, capped at Rs. 300
▭  Display duration and fee
(END)  Stop

 
Question 16: Multi-Day Water Tank Simulation
Problem statement
Update a tank's water level over several days using inflow and outflow, detect overflow or shortages, and identify when the level first reaches a target.
Algorithm (step by step)
31.	Set tank capacity, initial water level and target level.
32.	Read each day's inflow and outflow.
33.	Calculate new level = old level + inflow − outflow.
34.	If the level is below zero, report shortage and set it to zero; if above capacity, report overflow and set it to capacity.
35.	Print the level each day and record the first day the target is reached.
36.	Stop after all days.
Python code
capacity = 1000
level = 600
target = 800
days = [(250, 100), (200, 50), (100, 250), (300, 100)]
first_day = None

for day, (inflow, outflow) in enumerate(days, start=1):
    level += inflow - outflow
    if level > capacity:
        print("Day", day, ": overflow detected")
        level = capacity
    elif level < 0:
        print("Day", day, ": water shortage detected")
        level = 0

    print("Day", day, "water level:", level)
    if first_day is None and level >= target:
        first_day = day

if first_day is None:
    print("Target not reached.")
else:
    print("Target first reached on day:", first_day)
Sample output
Day 1 water level: 750
Day 2 water level: 900
Day 3 water level: 750
Day 4 water level: 950
Target first reached on day: 2
Flowchart
Read the flowchart from top to bottom. START/END are terminators, ▱ is input/output, ▭ is a process, and ◇ is a decision.
(START)  Initialize capacity, level and target
▱  Read daily inflow and outflow
▭  Update level = level + inflow − outflow
◇  Level above capacity?
▭  Yes: report overflow and set to capacity
◇  Level below zero?
▭  Yes: report shortage and set to zero
▭  Print level; if target first reached, save day
◇  More days?
→  Yes: process next day
(END)  No: print first target day and stop

 
Question 17: Student Performance Trend Analysis
Problem statement
Compare scores across multiple examinations, calculate improvements or declines, identify weak subjects and classify performance using simple criteria.
Algorithm (step by step)
37.	Store subject names and marks from two examinations.
38.	For each subject, calculate change = second exam mark − first exam mark.
39.	Label the trend as improved, declined or unchanged.
40.	Identify subjects with second-exam marks below 40.
41.	Calculate the average of the second examination and classify performance.
42.	Display the report.
Python code
subjects = ["Python", "Maths", "English", "Science"]
exam1 = [65, 72, 48, 55]
exam2 = [78, 68, 35, 60]

for i in range(len(subjects)):
    change = exam2[i] - exam1[i]
    if change > 0:
        trend = "Improved"
    elif change < 0:
        trend = "Declined"
    else:
        trend = "Unchanged"
    weak = " (weak subject)" if exam2[i] < 40 else ""
    print(subjects[i] + ":", trend, f"({change:+d})" + weak)

average = sum(exam2) / len(exam2)
if average >= 75:
    category = "Excellent"
elif average >= 50:
    category = "Satisfactory"
else:
    category = "Needs improvement"

print("Exam 2 average:", round(average, 2))
print("Classification:", category)
Sample output
Python: Improved (+13)
Maths: Declined (-4)
English: Declined (-13) (weak subject)
Science: Improved (+5)
Exam 2 average: 60.25
Classification: Satisfactory
Flowchart
Read the flowchart from top to bottom. START/END are terminators, ▱ is input/output, ▭ is a process, and ◇ is a decision.
(START)  Start
▱  Load subjects and two sets of marks
▭  For each subject calculate exam2 − exam1
◇  Change positive, negative or zero?
▭  Label improved, declined or unchanged; flag mark < 40
▭  Calculate exam 2 average and classification
◇  More subjects?
→  Yes: process next subject
(END)  Display report and stop

 
Question 18: Fuel Consumption and Route Comparison
Problem statement
Calculate fuel required and journey cost for different vehicles using distance, mileage, fuel price and a reserve requirement; choose the lowest-cost feasible vehicle.
Algorithm (step by step)
43.	Read journey distance, fuel price per litre and required reserve.
44.	Store each vehicle's mileage and available fuel.
45.	Calculate journey fuel = distance ÷ mileage.
46.	Calculate required fuel including reserve.
47.	Mark a vehicle feasible if its available fuel is enough; calculate cost for feasible vehicles.
48.	Choose the feasible vehicle with the lowest cost and display the comparison.
Python code
distance = 240
fuel_price = 105
reserve = 2
vehicles = [
    ("Car A", 15, 20),   # name, km/litre, available litres
    ("Car B", 20, 14),
    ("Car C", 12, 25)
]

best = None
for name, mileage, available in vehicles:
    fuel_needed = distance / mileage
    total_required = fuel_needed + reserve
    cost = fuel_needed * fuel_price
    feasible = available >= total_required

    print(name, "- fuel:", round(fuel_needed, 2), "L, cost: Rs.",
          round(cost, 2), ", feasible:", feasible)
    if feasible and (best is None or cost < best[1]):
        best = (name, cost)

if best:
    print("Lowest-cost feasible vehicle:", best[0])
    print("Estimated fuel cost: Rs.", round(best[1], 2))
else:
    print("No vehicle has enough fuel including reserve.")
Sample output
Car A - fuel: 16.0 L, cost: Rs. 1680.0 , feasible: True
Car B - fuel: 12.0 L, cost: Rs. 1260.0 , feasible: True
Car C - fuel: 20.0 L, cost: Rs. 2100.0 , feasible: True
Lowest-cost feasible vehicle: Car B
Estimated fuel cost: Rs. 1260.0
Flowchart
Read the flowchart from top to bottom. START/END are terminators, ▱ is input/output, ▭ is a process, and ◇ is a decision.
(START)  Start
▱  Input distance, fuel price, reserve and vehicle data
▭  For each vehicle: fuel = distance ÷ mileage
▭  Required fuel = fuel + reserve; cost = fuel × price
◇  Available fuel ≥ required fuel?
▭  If feasible and cheaper, update best vehicle
◇  More vehicles?
→  Yes: process next vehicle
(END)  Display lowest-cost feasible option, or none

 
Question 19: Multi-Product Shopping Budget Constraint
Problem statement
Evaluate a shopping basket, apply a discount condition and determine how the basket total compares with a fixed budget.
Algorithm (step by step)
49.	Read the budget and product names, prices and quantities.
50.	Calculate each product subtotal and the basket total.
51.	If the total is at least the discount threshold, apply the stated discount.
52.	Compare the discounted total with the budget.
53.	If over budget, reduce quantities from the last item backward until the total fits, then report changes.
54.	Display the final basket total and remaining budget.
Python code
budget = 1000
items = [
    ["Notebook", 80, 4],
    ["Pen pack", 120, 3],
    ["Folder", 100, 2]
]

def total_cost(basket):
    return sum(price * qty for name, price, qty in basket)

original = total_cost(items)
discount = 0.10 if original >= 1000 else 0
amount = original * (1 - discount)
print("Original total: Rs.", original)
print("Discount:", int(discount * 100), "%")

# Reduce quantities from the last item until the budget is met.
for item in reversed(items):
    while amount > budget and item[2] > 0:
        item[2] -= 1
        original = total_cost(items)
        discount = 0.10 if original >= 1000 else 0
        amount = original * (1 - discount)

print("Final quantities:", [(x[0], x[2]) for x in items])
print("Final total after discount: Rs.", round(amount, 2))
print("Budget remaining: Rs.", round(budget - amount, 2))
Sample output
Original total: Rs. 880
Discount: 0 %
Final quantities: [('Notebook', 4), ('Pen pack', 3), ('Folder', 2)]
Final total after discount: Rs. 880.0
Budget remaining: Rs. 120.0
Flowchart
Read the flowchart from top to bottom. START/END are terminators, ▱ is input/output, ▭ is a process, and ◇ is a decision.
(START)  Start
▱  Input budget and shopping items
▭  Calculate basket total and apply discount if threshold met
◇  Is discounted total over budget?
▭  Yes: reduce quantities and recalculate total
◇  Now within budget?
→  No: continue reducing quantities
▭  Display final quantities, total and remaining budget
(END)  Stop

 
Question 20: University Admission Decision Engine
Problem statement
Evaluate applicants using subject eligibility, aggregate marks and a course threshold, then rank eligible applicants with a deterministic tie-break rule.
Algorithm (step by step)
55.	Store applicants with name, subject marks and attendance.
56.	Calculate aggregate percentage for each applicant.
57.	Check that every subject mark is at least 40, aggregate is at least 70%, and attendance is at least 75%.
58.	Keep only eligible applicants.
59.	Sort eligible applicants by aggregate percentage in descending order, then attendance in descending order.
60.	Print the ranked list or report that no candidate qualifies.
Python code
applicants = [
    ("Asha", [82, 78, 91], 88),
    ("Bharat", [75, 80, 79], 92),
    ("Charan", [35, 90, 88], 95),
    ("Divya", [85, 83, 80], 70)
]

eligible = []
for name, marks, attendance in applicants:
    aggregate = sum(marks) / len(marks)
    subject_ok = all(mark >= 40 for mark in marks)
    if subject_ok and aggregate >= 70 and attendance >= 75:
        eligible.append((name, aggregate, attendance))

eligible.sort(key=lambda item: (item[1], item[2]), reverse=True)

if not eligible:
    print("No eligible applicants.")
else:
    print("Admission ranking:")
    for rank, (name, aggregate, attendance) in enumerate(eligible, start=1):
        print(rank, name, "- aggregate:", round(aggregate, 2),
              "%, attendance:", attendance, "%")
Sample output
Admission ranking:
1 Asha - aggregate: 83.67 %, attendance: 88 %
2 Bharat - aggregate: 78.0 %, attendance: 92 %
Flowchart
Read the flowchart from top to bottom. START/END are terminators, ▱ is input/output, ▭ is a process, and ◇ is a decision.
(START)  Start
▱  Read applicant marks and attendance
▭  Calculate aggregate percentage
◇  All subjects ≥ 40, aggregate ≥ 70%, attendance ≥ 75%?
▭  Yes: add applicant to eligible list; No: exclude
◇  More applicants?
→  Yes: process next applicant
▭  Sort by aggregate descending, then attendance descending
(END)  Print ranked eligible list and stop

 
