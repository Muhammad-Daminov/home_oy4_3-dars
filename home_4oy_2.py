# 1 - masala:



# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id
#         self.__grades = []
#     def add_grade(self, grade: int):
#         if 0 <= grade <=100:
#             self.__grades.append(grade)
          
#         else:
#             print("Xato: Notogri baho")
#     def calculate_average(self):
#         if len(self.__grades) == 0:
#             return 0 
#         return float(sum(self.__grades) / len(self.__grades))
#     def get_status(self):
#         a = self.calculate_average()

#         if 90 <= a <= 100:
#             return "Alo"
#         elif 80 <= a <= 90:
#             return "Yaxshi"
#         elif 70 <= a <= 80:
#             return "Qoniqarli"
#         else: return "Qoniqarsiz"

# student = Student("Nodira", "S123")

# student.add_grade(85)
# student.add_grade(90)

# print(student.calculate_average())
# print(student.get_status())

# student.add_grade(150)


# 2 masala:


# class Employee:
#     def __init__(self, name , employee_id, hourly_rate = 15.0):
#         self.name = name
#         self.employee_id = employee_id
#         self.hourly_rate = hourly_rate
#         self._working_hours = []

#     def log_hours(self, hour: int):
#         if 0 <= hour <= 24:
#             self._working_hours.append(hour)
#             return True
#         else:
#             return False
        
#     def total_hourss(self):
#         return sum(self._working_hours)
    
#     def calculate_alary(self):
#         return self.total_hourss() * self.hourly_rate
    
#     def reset_hours(self):
#         self._working_hours = []


# employee = Employee("Javlon", "E101", 20.0)


# print(employee.log_hours(8))
# print(employee.log_hours(9))
# print(employee.log_hours(10))
# print(employee.log_hours(25))

# print(employee.total_hourss())
# print(employee.calculate_alary())

# employee.reset_hours()

# print(employee.total_hourss())
# print(employee.calculate_alary())



            
# 3 masala:

class Playlist:
    def __init__(self, owner):
        self.owner = owner
        self.track = []
        

    def add_track(self, title, artist):
        
        self.track.append((title, artist))

    def remove_last(self):
        if len(self.track) == 0:
            return None
        return self.track.pop()
    
    def totaltracks(self):
        return len(self.track)
    def unique_tracks(self):
        result = []
        for i in self.track:
            if i not in result:
                result.append(i)
        return result
    
    def search_by_title(self, title):
        result = []
        for i in self.track:
            if i[0] == title:
                result.append(i)
        return result
    def filter_by_artist(self, artist):
        result = []
        for i in self.track:
            if i[1] == artist:
                result.append(i)
        return result



pl = Playlist("Muhammad")

print(pl.totaltracks())  

pl.add_track("Yomg'irlar", "Shahzoda")
pl.add_track("Gulim", "Yulduz Usmonova")
pl.add_track("Yomg'irlar", "Shahzoda")
pl.add_track("Xayr edi", "Lola")
pl.add_track("Kel", "Ulug'bek Rahmatullayev")

print(pl.totaltracks())  

print(pl.unique_tracks())

print(pl.remove_last())  

print(pl.totaltracks())  

print(pl.search_by_title("Yomg'irlar"))

print(pl.filter_by_artist("Yulduz Usmonova"))



        