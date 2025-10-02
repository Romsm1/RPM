class Student:
    def __init__(self, first_name, last_name, average_grade):
        self._first_name = first_name
        self._last_name = last_name
        self._average_grade = average_grade

    def __str__(self):
        return f"Имя и фамилия студента: {self._first_name} {self._last_name} Средний балл: {self._average_grade}"

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
        self._students = []

    def add_student(self, student):
        self._students.append(student)

    def get_iterator(self, sort_by_grade=False, filter_last_name=None):
        return StudentGroupIterator(self._students, sort_by_grade, filter_last_name)