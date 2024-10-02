

class Counter:
    def __init__(self):
        self.count = 0

    def add(self, num):
        self.count += num

    def report(self):
        return f"Counted to {self.count} so far."
    


# class Reminder:
#     def __init__(self, name):
#         self.name = name

#     def remind_me_to(self, task):
#         self.task = task

#     def remind(self):
#         return f"{self.task}, {self.name}!"
    

#     reminder = Reminder("Kay")
#     reminder.remind_me_to("Walk the dog")
#     result = reminder.remind()
#     assert result == "Walk the dog, Kay!"
