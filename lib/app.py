# Write your code here!
class Member:

    def __init__(self, full_name, introduce):
        self.full_name = full_name
        self.introduce = introduce
      

    def greeting(self,):
        print(self.introduce)
        
        
class Student(Member):
    def __init__(self, reason, full_name, introduce):
        super().__init__(full_name, introduce)
        self.reason = reason
        
    def purpose(self):
        print(self.reason)

        
class Instructor(Member):
    def __init__(self, bio, full_name, introduce):
        super().__init__(full_name, introduce)
        self.bio = bio
        self.skills = []

    def add_skill(self, new_skill ):
        self.new_skill = new_skill
        self.skills.append(self.new_skill)

class Workshop(Member):
    def __init__(self, date, subject):
        self.date = date
        self.subject = subject
        self.instructors = []
        self.roster = []

    def add_participant(self, member):
        self.member = member
        if type(member.reason) == str:
            self.instructors.append(member)





    # def about(self):
    #     print(self.bio)

    # def passion(self)
    #     print(self.skills)

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()