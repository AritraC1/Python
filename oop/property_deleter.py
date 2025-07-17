# @property.deleter
# Allows you to delete a property via `del` keyword. Used to clean up or reset internal state.

class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.deleter
    def salary(self):
        print("Deleting salary...")
        self._salary = 0


e = Employee(5000)
print("Salary:", e.salary)
del e.salary
print("After delete:", e.salary)
