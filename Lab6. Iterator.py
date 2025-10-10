class Student:
    def __init__(self, first_name, last_name, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.average_grade = average_grade

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Средний балл: {self.average_grade}"


class StudentGroupIterator:
    def __init__(self, students, sort_by_grade=False, filter_last_name=None):
        self._students = students

        if filter_last_name:
            self._students = [s for s in self._students if s.last_name == filter_last_name]

        if sort_by_grade:
            self._students.sort(key=lambda s: s.average_grade, reverse=True)

        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._students):
            student = self._students[self._index]
            self._index += 1
            return student
        raise StopIteration


class StudentGroup:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_iterator(self, sort_by_grade=False, filter_last_name=None):
        return StudentGroupIterator(self.students, sort_by_grade, filter_last_name)


group = StudentGroup()
group.add_student(Student("Иван", "Иванов", 4.5))
group.add_student(Student("Мария", "Петрова", 4.8))
group.add_student(Student("Алексей", "Иванов", 4.2))

print("Сортировка по баллу:")
for student in group.get_iterator(sort_by_grade=True):
    print(student)

print("Только Ивановы:")
for student in group.get_iterator(filter_last_name="Иванов"):
    print(student)
