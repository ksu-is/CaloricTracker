class Goals:

    def __init__\
    (self, weight=0):
        self.weight = weight

#These are the values that are used in the process of calculating calories for goal

    gain_muscle = [16, 18]
    lose_fat = [10, 12]
    maintain = [14, 15]

    def getUserWeight(self):
        self.weight = int(input('Respectfully, Whats your current weight - Please Enter in "lbs"? '))


#Here is the Formula found to caluclate proper caloric intake for goals!


    def loseWeight(self):
        lose_cals = list(map(lambda x: self.weight * x, self.lose_fat))
        print("The following are the calories you need to stay in between to reach your goal - Lets begin Tracking your Caloric Intake!")
        print(lose_cals)

    def maintainWeight(self):
        maintain_cals = list(map(lambda x: self.weight * x,self.maintain))
        print("The following are the calories you need to stay in between to reach your goal - Lets begin Tracking your Caloric Intake!")
        print(maintain_cals)

    def gainMuscle(self):
        strong_cals = list(map(lambda x: self.weight * x, self.gain_muscle))
        print("The following are the calories you need to stay in between to reach your goal - Lets begin Tracking your Caloric Intake!")
        print(strong_cals)

class User:

    def __init__(self, run=True):
        self.run = run

    yes ='yes'

    import os
    from time import sleep

    msg = "Opening Application.. Please wait"
    for x in range(2):
        msg = msg + "."
        print(msg)
        sleep(1)

    print("%s Thanks for using Calorie Counter as your goal setting application!" % msg)

    goal ='''Weight Input Received - Thanks! 
    Please Enter a Number below corresponding to your number 1 goal!:
                Enter 0 to: Lose Weight
                Enter 1 to: Maintain Weight
                Enter 2 to: Gain Muscle
    '''

    def setRun(self):
        answer = input("Do you need further assistance? ")
        if answer in self.yes:
            self.run = True
        else:
            self.run = False

    def getRun(self):
        return self.run

    def sortCalc(self, obj):
        print(self.goal)
        answer = int(input("Enter your Number here---> "))
        print('\n')
        if answer == 0:
            obj.loseWeight()
        elif answer == 1:
            obj.maintainWeight()
        else:
            obj.gainMuscle()

c1 = Goals()
u1 = User()

c1.getUserWeight()

while u1.run:
    print('\n')
    u1.sortCalc(c1)
    print('\n')
    u1.setRun()

print("Good luck on tracking your Calories towards your goal!")
print("Always Remember to stay focused and never get discouraged :)")


