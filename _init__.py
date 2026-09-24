"""
OOP Assignment - Week 3 -By Waseem
Package Initializer

Exposes all public classes from the 5 questions:
    Q1 - Rectangle
    Q2 - School
    Q3 - Shape, Rectangle, Square
    Q4 - Vehicle, OffRoadVehicle, SportsCar
    Q5 - Customer, Account
"""

# ---------- Question 1: Rectangle ----------
from oop_questions.q1_rectangle import Rectangle

# ---------- Question 2: School ----------
from oop_questions.q2_school import School

# ---------- Question 3: Shape / Rectangle / Square ----------
# NOTE: Q3 also has a "Rectangle" class that conflicts with Q1.
# We import it as "ShapeRectangle" to avoid naming conflicts.
from oop_questions.q3_shape import Shape
from oop_questions.q3_shape import Rectangle as ShapeRectangle
from oop_questions.q3_shape import Square

# ---------- Question 4: Vehicle ----------
from oop_questions.q4_vehicle import Vehicle, OffRoadVehicle, SportsCar

# ---------- Question 5: Customer & Account ----------
from oop_questions.q5_bank_account import Customer, Account


# ---------- Public API ----------
__all__ = [
    # Q1
    "Rectangle",
    # Q2
    "School",
    # Q3
    "Shape",
    "ShapeRectangle",
    "Square",
    # Q4
    "Vehicle",
    "OffRoadVehicle",
    "SportsCar",
    # Q5
    "Customer",
    "Account",
]

__version__ = "1.0.0"
__author__ = "Waseem, Mohammed, Dana"
