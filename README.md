
# 🧠 OOP Assignment — Week 3

A collection of **5 Object-Oriented Programming exercises** in Python, covering classes, inheritance, composition, and polymorphism.

---

## 📋 Questions Covered

### Q1 — Rectangle Class
- **Attributes:** `width`, `height`
- **Methods:** `area()`, `perimeter()`
- **Demo:** create rectangle `5 x 7` and print area and perimeter.

### Q2 — School Class
- **Attributes:** `name`, `foundation_year`, `students` (list), `teachers` (dict)
- **Methods:**
  - `add_new_student(student_name, class)`
  - `add_new_teacher(teacher_name, branch)`
  - `view_student_list()`
  - `view_teacher_list()`

### Q3 — Shape Inheritance
- **Base:** `Shape` with `width`, `height`
- **Subclasses:** `Rectangle` and `Square`, both with `calculate_area()`

### Q4 — Vehicle Inheritance
- **Base:** `Vehicle` with `make`, `model`, `year`
- **Subclasses:**
  - `OffRoadVehicle` — adds `four_wheel_drive`
  - `SportsCar` — adds `max_speed`

### Q5 — Customer & Account 
- **Customer:** `name`, `surname`, `tc_identification`, `phone`
  - Method: `display_information()`
- **Account:** `customer` (Customer object), `account_number`, `balance`
  - Methods: `deposit(amount)`, `money_check(amount)`, `display_balance()`

  
---

## 🚀 How to Run

```bash
git clone https://github.com/waseemisaac91/OOP-Assignment.git
cd OOP-Assignment

# Run any question individually
python oop_questions/q1_rectangle.py
python oop_questions/q2_school.py
python oop_questions/q3_shape.py
python oop_questions/q4_vehicle.py
python oop_questions/q5_bank_account.py
