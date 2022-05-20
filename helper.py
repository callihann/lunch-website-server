class Meals():
    def __init__(self, date, main, side1, side2):
        self.date = date
        self.main = main
        self.side1 = side1
        self.side2 = side2

    def __str__(self):
        return(f"{self.date} {self.main} {self.side1} {self.side2}")