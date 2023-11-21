class Stakeholder:
    def __init__(self,name, classification):
        self.name= name
        self.classification= classification
        pass
    def __str__(self) :
        return "f{self.name}-{self.classification}"

#Create Stakeholders
students = Stakeholder("student", "user")
faculty = Stakeholder("Faculty/Instructors", "User")
admin = Stakeholder("University Administrators", "Owner")
registrar_office = Stakeholder("Registrar's Office", "Owner, Analyst")
developers = Stakeholder("System Developers/Programmers", "Builder, Designer")
advisors = Stakeholder("Course Advisors/Counselors", "User, Analyst")

stakeholders = [students, faculty, admin, registrar_office, developers, advisors]
    
for stakeholder in stakeholders :
    print(stakeholder)