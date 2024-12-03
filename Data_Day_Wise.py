import csv

#Day,ScreenTime,NetEffectiveWork,SkillDev.(hrs.),Other,Feedback,Description


class Handler:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def write(self, contents):
        with open(self.file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(contents)

    def take_inputs():
        scrt = input('Enter ScreenTime: ')
        neffwork = input