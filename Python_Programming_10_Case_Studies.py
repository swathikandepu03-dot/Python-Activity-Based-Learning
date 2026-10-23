"""Source code for ten illustrative Python programming case studies."""

# 1. University Scholarship Allocation
# Run each program separately; some cases use their own imports and sample inputs.
applicants = [
    {"name": "Asha", "aggregate": 88, "subjects": [82, 90, 85],
     "attendance": 92, "income": 180000},
    {"name": "Bala", "aggregate": 88, "subjects": [75, 80, 60],
     "attendance": 95, "income": 200000},
    {"name": "Charan", "aggregate": 72, "subjects": [80, 75, 70],
     "attendance": 90, "income": 150000},
    {"name": "Divya", "aggregate": 81, "subjects": [78, 84, 80],
     "attendance": 85, "income": 220000},
]

eligible = []
for a in applicants:
    valid = (0 <= a["aggregate"] <= 100 and
             all(0 <= m <= 100 for m in a["subjects"]) and
             0 <= a["attendance"] <= 100 and a["income"] >= 0)
    if not valid:
        print("Invalid data:", a["name"])
        continue
    if (a["aggregate"] >= 75 and min(a["subjects"]) >= 60
            and a["attendance"] >= 75 and a["income"] <= 250000):
        eligible.append(a)

eligible.sort(key=lambda a: (-a["aggregate"], -a["attendance"], a["income"]))
print("Scholarship Merit List")
if not eligible:
    print("No eligible applicants")
else:
    for rank, a in enumerate(eligible, start=1):
        print(f"{rank}. {a['name']} - Aggregate: {a['aggregate']}%, "
              f"Attendance: {a['attendance']}%, Income: Rs.{a['income']}")

########################################################################

# 2. Progressive Electricity Billing
# Run each program separately; some cases use their own imports and sample inputs.
def energy_charge(units):
    if units <= 100:
        return units * 1.50
    if units <= 200:
        return 100 * 1.50 + (units - 100) * 2.50
    return 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00

monthly_units = [80, 120, 260]
bills = []
for month, units in enumerate(monthly_units, start=1):
    if units < 0:
        raise ValueError("Units cannot be negative")
    energy = energy_charge(units)
    surcharge = energy * 0.05
    rebate = 20 if units <= 100 else 0
    total = energy + 50 + surcharge - rebate
    bills.append(total)
    print(f"Month {month}: {units} units, bill = Rs.{total:.2f}")

print("Monthly comparison")
for i in range(1, len(bills)):
    if bills[i - 1] == 0:
        increase = 0
    else:
        increase = (bills[i] - bills[i - 1]) / bills[i - 1] * 100
    status = "UNUSUAL INCREASE" if increase > 30 else "Normal"
    print(f"Month {i+1}: change = {increase:.1f}% - {status}")

########################################################################

# 3. Hospital Billing and Patient Classification
# Run each program separately; some cases use their own imports and sample inputs.
age = 65
consultation = 500
diagnostics = 1200
treatment = 3000
valid_card = False
amount_paid = 2500

charges = [consultation, diagnostics, treatment, amount_paid]
if age < 0 or any(x < 0 for x in charges):
    raise ValueError("Age and charges must be non-negative")

service_total = consultation + diagnostics + treatment
discount = service_total * 0.10 if age >= 60 or valid_card else 0
subtotal = service_total - discount
tax = subtotal * 0.05
final_bill = subtotal + tax

if amount_paid >= final_bill:
    status = "Paid"
elif amount_paid > 0:
    status = "Partial payment"
else:
    status = "Unpaid"

print("HOSPITAL BILL")
print(f"Service total: Rs.{service_total:.2f}")
print(f"Concession: Rs.{discount:.2f}")
print(f"Tax: Rs.{tax:.2f}")
print(f"Final bill: Rs.{final_bill:.2f}")
print(f"Amount paid: Rs.{amount_paid:.2f}")
print("Payment classification:", status)

########################################################################

# 4. Employee Payroll and Deduction Analysis
# Run each program separately; some cases use their own imports and sample inputs.
basic = 30000
overtime_hours = 8
incentive = 2000

if basic < 0 or overtime_hours < 0 or incentive < 0:
    raise ValueError("Salary inputs must be non-negative")

hra = basic * 0.20
other_allowance = basic * 0.10
overtime_pay = overtime_hours * (basic / 160) * 1.5
gross = basic + hra + other_allowance + overtime_pay + incentive

def progressive_tax(amount):
    tax = 0
    tax += min(amount, 20000) * 0
    tax += min(max(amount - 20000, 0), 20000) * 0.05
    tax += max(amount - 40000, 0) * 0.10
    return tax

tax = progressive_tax(gross)
pf = basic * 0.08
net = gross - tax - pf

print("EMPLOYEE SALARY STATEMENT")
print(f"Basic pay:          Rs.{basic:,.2f}")
print(f"HRA:                Rs.{hra:,.2f}")
print(f"Other allowance:    Rs.{other_allowance:,.2f}")
print(f"Overtime pay:       Rs.{overtime_pay:,.2f}")
print(f"Incentive:          Rs.{incentive:,.2f}")
print(f"Gross salary:       Rs.{gross:,.2f}")
print(f"Progressive tax:    Rs.{tax:,.2f}")
print(f"PF deduction:       Rs.{pf:,.2f}")
print(f"Net salary:         Rs.{net:,.2f}")

########################################################################

# 5. Multi-Plan Telecommunications Cost Optimization
# Run each program separately; some cases use their own imports and sample inputs.
import math

usage_gb = 18
budget = 500
plans = [
    {"name": "Basic", "price": 199, "data": 10, "extra_rate": 20, "validity": 28},
    {"name": "Smart", "price": 349, "data": 20, "extra_rate": 15, "validity": 30},
    {"name": "Max", "price": 449, "data": 30, "extra_rate": 10, "validity": 56},
]

eligible = []
for p in plans:
    if usage_gb < 0 or budget < 0:
        raise ValueError("Usage and budget must be non-negative")
    excess = max(0, usage_gb - p["data"])
    extra_charge = math.ceil(excess) * p["extra_rate"]
    total = p["price"] + extra_charge
    print(f"{p['name']}: base Rs.{p['price']}, excess Rs.{extra_charge}, total Rs.{total}")
    if p["validity"] >= 30 and total <= budget:
        eligible.append((total, p["name"], p["validity"]))

if eligible:
    eligible.sort()
    total, name, validity = eligible[0]
    print(f"Best eligible plan: {name} | Total Rs.{total} | Validity {validity} days")
else:
    print("No plan satisfies validity and budget constraints.")

########################################################################

# 6. Railway Fare and Reservation Calculator
# Run each program separately; some cases use their own imports and sample inputs.
def distance_fare(km):
    first = min(km, 100) * 0.75
    second = min(max(km - 100, 0), 400) * 0.60
    rest = max(km - 500, 0) * 0.45
    return first + second + rest

distance = 350
travel_class = "AC"
ages = [25, 62, 4]
cancelled = False
multiplier = {"Sleeper": 1.0, "AC": 2.0}

if distance <= 0 or travel_class not in multiplier or any(a < 0 for a in ages):
    raise ValueError("Invalid journey or passenger data")

grand_total = 0
for i, age in enumerate(ages, start=1):
    fare = distance_fare(distance) * multiplier[travel_class]
    if age < 5:
        fare = 0
    elif age >= 60:
        fare *= 0.80
    reservation = 40 if fare > 0 else 0
    total = fare + reservation
    if cancelled and total > 0:
        refund = max(0, fare * 0.75)
        print(f"Passenger {i}: cancellation refund Rs.{refund:.2f}")
    else:
        grand_total += total
        print(f"Passenger {i}, age {age}: fare Rs.{total:.2f}")

if not cancelled:
    print(f"Total booking amount: Rs.{grand_total:.2f}")

########################################################################

# 7. Retail Billing with Multiple Discount Rules
# Run each program separately; some cases use their own imports and sample inputs.
products = [
    {"name": "Headphones", "category": "electronics", "price": 1800, "qty": 2},
    {"name": "Shirt", "category": "clothing", "price": 900, "qty": 2},
    {"name": "Rice", "category": "groceries", "price": 700, "qty": 1},
]
tax_rates = {"electronics": 0.18, "clothing": 0.05, "groceries": 0.00}

for p in products:
    if p["price"] < 0 or p["qty"] <= 0 or p["category"] not in tax_rates:
        raise ValueError("Invalid product details")

subtotal = sum(p["price"] * p["qty"] for p in products)
discount = min(subtotal * 0.10, 1000) if subtotal >= 5000 else 0
total_tax = 0

print("ITEMIZED INVOICE")
for p in products:
    line = p["price"] * p["qty"]
    share = line / subtotal if subtotal else 0
    taxable = line - discount * share
    tax = taxable * tax_rates[p["category"]]
    total_tax += tax
    print(f"{p['name']}: {p['qty']} x Rs.{p['price']} = Rs.{line:.2f}; tax Rs.{tax:.2f}")

final_total = subtotal - discount + total_tax
print(f"Subtotal: Rs.{subtotal:.2f}")
print(f"Discount: Rs.{discount:.2f}")
print(f"Tax: Rs.{total_tax:.2f}")
print(f"Final amount: Rs.{final_total:.2f}")

########################################################################

# 8. Manufacturing Cost and Profitability Analysis
# Run each program separately; some cases use their own imports and sample inputs.
material_qty = 500
unit_material_cost = 12
wastage_percent = 5
labour_cost = 2500
machine_cost = 1800
units_produced = 450
selling_price = 25
target_margin = 20

if (material_qty < 0 or unit_material_cost < 0 or labour_cost < 0
        or machine_cost < 0 or units_produced <= 0 or selling_price < 0
        or not 0 <= wastage_percent <= 100):
    raise ValueError("Invalid production data")

material_cost = material_qty * unit_material_cost
wastage_cost = material_cost * wastage_percent / 100
total_cost = material_cost + wastage_cost + labour_cost + machine_cost
unit_cost = total_cost / units_produced
revenue = units_produced * selling_price
profit = revenue - total_cost
margin = profit / total_cost * 100 if total_cost else 0

print("MANUFACTURING REPORT")
print(f"Material cost: Rs.{material_cost:.2f}")
print(f"Wastage cost: Rs.{wastage_cost:.2f}")
print(f"Labour cost: Rs.{labour_cost:.2f}")
print(f"Machine cost: Rs.{machine_cost:.2f}")
print(f"Total production cost: Rs.{total_cost:.2f}")
print(f"Cost per unit: Rs.{unit_cost:.2f}")
print(f"Revenue: Rs.{revenue:.2f}")
print(f"Profit: Rs.{profit:.2f}; Margin: {margin:.2f}%")
print("Target achieved" if margin >= target_margin else "Target not achieved")

########################################################################

# 9. Multi-Currency Travel Budget Analysis
# Run each program separately; some cases use their own imports and sample inputs.
expenses = [
    {"category": "Accommodation", "amount": 300, "currency": "USD"},
    {"category": "Food", "amount": 120, "currency": "EUR"},
    {"category": "Transport", "amount": 10000, "currency": "INR"},
]
rates_to_inr = {"USD": 83.0, "EUR": 90.0, "INR": 1.0}
budget = 50000
fee_rate = 0.02
converted_expenses = []

for e in expenses:
    if e["amount"] < 0 or e["currency"] not in rates_to_inr:
        raise ValueError("Invalid expense or missing exchange rate")
    converted = e["amount"] * rates_to_inr[e["currency"]]
    fee = converted * fee_rate
    final = converted + fee
    converted_expenses.append((e["category"], final))
    print(f"{e['category']}: INR {final:.2f} including fee")

total = sum(value for _, value in converted_expenses)
largest = max(converted_expenses, key=lambda item: item[1])
print(f"Total travel spending: INR {total:.2f}")
if total <= budget:
    print(f"Budget remaining: INR {budget-total:.2f}")
else:
    print(f"Budget exceeded by: INR {total-budget:.2f}")
print(f"Largest expense category: {largest[0]} (INR {largest[1]:.2f})")

########################################################################

# 10. Campus Event Financial Planning
# Run each program separately; some cases use their own imports and sample inputs.
import math

venue = 12000
equipment = 5000
transport = 3000
catering_per_person = 180
certificate_per_person = 20
sponsorship = 10000
registration_fee = 300
expected_participants = 80

values = [venue, equipment, transport, catering_per_person,
          certificate_per_person, sponsorship, registration_fee,
          expected_participants]
if any(v < 0 for v in values):
    raise ValueError("All costs and counts must be non-negative")

fixed_cost = venue + equipment + transport
variable_per_person = catering_per_person + certificate_per_person
total_cost = fixed_cost + expected_participants * variable_per_person
registration_income = expected_participants * registration_fee
available_funds = registration_income + sponsorship
shortfall = max(total_cost - available_funds, 0)
surplus = max(available_funds - total_cost, 0)

net_per_registration = registration_fee - variable_per_person
if fixed_cost <= sponsorship:
    break_even = 0
elif net_per_registration <= 0:
    break_even = None
else:
    break_even = math.ceil((fixed_cost - sponsorship) / net_per_registration)

print("CAMPUS EVENT BUDGET")
print(f"Fixed costs: Rs.{fixed_cost:.2f}")
print(f"Variable cost per participant: Rs.{variable_per_person:.2f}")
print(f"Total cost for {expected_participants} participants: Rs.{total_cost:.2f}")
print(f"Registration income: Rs.{registration_income:.2f}")
print(f"Sponsorship: Rs.{sponsorship:.2f}")
print(f"Funding shortfall: Rs.{shortfall:.2f}")
print(f"Surplus: Rs.{surplus:.2f}")
print("Break-even registrations:", break_even if break_even is not None else "Not possible at this fee")

########################################################################

