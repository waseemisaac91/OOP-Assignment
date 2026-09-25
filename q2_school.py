"""
Question 2: School Class
- Attributes: name, foundation_year, students (list), teachers (dict)
- Methods: add_new_student, add_new_teacher, view_student_list, view_teacher_list
By Dana
"""

class School:
    """Represents a school with students and teachers."""

    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
        self.students = []     # list of dicts: {"name": ..., "class": ...}
        self.teachers = {}     # dict: {teacher_name: branch}

    # ---------- Add Student ----------
    def add_new_student(self, student_name, class_name):
        """Add a new student to the school."""
        student = {"name": student_name, "class": class_name}
        self.students.append(student)
        print(f"✅ Student '{student_name}' added to class '{class_name}'.")

    # ---------- Add Teacher ----------
    def add_new_teacher(self, teacher_name, branch):
        """Add a new teacher to the school."""
        self.teachers[teacher_name] = branch
        print(f"✅ Teacher '{teacher_name}' added to branch '{branch}'.")

    # ---------- View Students ----------
    def view_student_list(self):
        """Display all students and their classes."""
        if not self.students:
            print("📭 No students enrolled yet.")
            return
        print(f"\n🎓 Students in {self.name}:")
        print("-" * 45)
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student['name']} — Class: {student['class']}")
        print("-" * 45)

    # ---------- View Teachers ----------
    def view_teacher_list(self):
        """Display all teachers and their branches."""
        if not self.teachers:
            print("📭 No teachers hired yet.")
            return
        print(f"\n👨‍🏫 Teachers in {self.name}:")
        print("-" * 45)
        for i, (name, branch) in enumerate(self.teachers.items(), 1):
            print(f"{i}. {name} — Branch: {branch}")
        print("-" * 45)

    # ---------- Representation ----------
    def __str__(self):
        return (
            f"{self.name} (Founded: {self.foundation_year}) — "
            f"{len(self.students)} students, {len(self.teachers)} teachers"
        )

    def __repr__(self):
        return (
            f"School(name={self.name!r}, foundation_year={self.foundation_year}, "
            f"students={len(self.students)}, teachers={len(self.teachers)})"
        )

# ---------- Testing ----------
if __name__ == "__main__":
    # Create a school
    school = School("Al-Noor High School", 1995)
    print(f"🏫 {school}")

    # Add students
    school.add_new_student("Ahmed Ali", "Grade 10A")
    school.add_new_student("Sara Mohammed", "Grade 10B")
    school.add_new_student("Khalid Hassan", "Grade 11A")

    # Add teachers
    school.add_new_teacher("Mr. Youssef", "Mathematics")
    school.add_new_teacher("Ms. Layla", "Physics")
    school.add_new_teacher("Mr. Omar", "English")

    # View lists
    school.view_student_list()
    school.view_teacher_list()

    # Summary
    print(f"\n📊 Summary: {school}")