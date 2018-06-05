NO_STUDENTS = "There is no students for this teacher"


class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is %s" % self.name


class Student(Person):
    def __init__(self, name, group):
        super(Student, self).__init__(name)
        self.group = group

    def __str__(self):
        return "My name is %s and I'm from %s group" % (self.name, self.group)

    def print_group(self):
        return "My group is %s" % self.group


class Teacher(Person):
    def __init__(self, name):
        super(Teacher, self).__init__(name)
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        for current_student in self.students:
            if student.name == current_student.name:
                self.students.remove(current_student)

    def __str__(self):
        return "My name is %s and my students are:\n%s" % (self.name, self.get_all_students())

    def get_all_students(self):
        if self.students:
            return "\n".join("%s" % st for st in self.students)
        else:
            return NO_STUDENTS


if __name__ == "__main__":
    alice_student = Student("Alice", "12")
    bob_student = Student("Bob", "12")
    alex_teacher = Teacher("Alex")
    assert alex_teacher.get_all_students() == NO_STUDENTS
    alex_teacher.add_student(alice_student)
    assert alex_teacher.get_all_students() == "%s" % alice_student
    alex_teacher.add_student(bob_student)
    print(alex_teacher)
    alex_teacher.remove_student(alice_student)
    assert alex_teacher.get_all_students() == "%s" % bob_student
