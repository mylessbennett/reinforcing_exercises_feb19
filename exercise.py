# Exercise 2
class Person:
    """ Discribes how a person is feeling """

    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def __str__(self):
        return

    def feeling(self):
        for i in emotions:
            if emotions[i] == 3:
                print("I'm feeling a high amount of {}.".format(i))
            elif emotions[i] == 2:
                print("I'm feeling a medium amount of {}.".format(i))
            elif emotions[i] == 1:
                print("I'm feeling a low amount of {}.".format(i))



#---------------------------------------------------------------
# Exercise 1
emotions = {'happiness': 3, 'fear': 1, 'sadness': 2}

myles = Person('Myles', emotions)
#---------------------------------------------------------------
# Exercise 3
myles.feeling()


#---------------------------------------------------------------
