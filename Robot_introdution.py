class robot:
    def __init__(self, name):
        self.name = name
    def introduction(self):
        print("Hi, I am a robot and my name is {}". format(self.name))

tom = robot('Tom')
jerry = robot('Jerry')

tom.introduction()
jerry.introduction()