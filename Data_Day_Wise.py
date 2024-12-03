import csv

#Day,ScreenTime,NetEffectiveWork,SkillDev.(hrs.),Other,Feedback,Description

class Handler:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def write(self, contents):
        with open(self.file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(contents)

    def take_inputs(self):
        day = input('Enter Day: ')
        scrt = input('Enter ScreenTime: ')
        neffwork = input('Enter Net Effective Work: ')
        skilldev = input('Enter Skill Development hours: ')
        other = input('Enter Other activities: ')
        feedback = input('Enter Feedback: ')
        description = input('Enter Description: ')
        
        return [day, scrt, neffwork, skilldev, other, feedback, description]

def main():
    handler = Handler('daily_data.csv')
    data = handler.take_inputs()
    handler.write(data)

if __name__ == "__main__":
    main()