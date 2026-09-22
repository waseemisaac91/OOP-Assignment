"""
OOP Assignment Week 3 - Package Initializer
"""

# Q1
from oop_questions.q1_rectangle import Rectangle

# Q2
from oop_questions.q2_school import School

# Q3
from oop_questions.q3_shape import Shape, Square
from oop_questions.q3_shape import Rectangle as ShapeRectangle

# Q4
from oop_questions.q4_vehicle import Vehicle, OffRoadVehicle, SportsCar

# Q5
from oop_questions.q5_bank_account import Customer, Account

__all__ = [
    "Rectangle",
    "School",
    "Shape",
    "ShapeRectangle",
    "Square",
    "Vehicle",
    "OffRoadVehicle",
    "SportsCar",
    "Customer",
    "Account",
]

__version__ = "1.0.0"
