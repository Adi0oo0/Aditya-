import csv

#Day,ScreenTime,NetEffectiveWork,SkillDev.(hrs.),Other,Feedback,Description

class Handler:
    """
    
    This class handles the csv file
    It has methods to write to the csv file and take inputs from the user
    It also has a method to read the file.

    """
    def __init__(self, file_name):
        self.file_name = file_name
    
    def write(self, contents):
        with open(self.file_name, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(contents)

    def take_inputs(self):
        """
        Returns:
            list: csv data
        """
        day = input('Enter Day: ')
        scrt = input('Enter ScreenTime: ')
        neffwork = input('Enter Net Effective Work: ')
        skilldev = input('Enter Skill Development hours: ')
        other = input('Enter Other activities: ')
        feedback = input('Enter Feedback: ')
        description = input('Enter Description: ')
        
        return [day, scrt, neffwork, skilldev, other, feedback, description]

def main():
    """
    This is the main function
    It creates an instance of the Handler class and calls the take_inputs method
    It then calls the write method to write the data to the csv file

    """
    handler = Handler('daily_data.csv')
    data = handler.take_inputs()
    handler.write(data)

if __name__ == "__main__":
    main()