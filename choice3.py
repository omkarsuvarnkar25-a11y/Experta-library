from experta import *

class StudentFacts(Fact):
    pass


class CareerExpertSystem(KnowledgeEngine):

    def __init__(self):
        super().__init__()
        self.matched = False

    @Rule(StudentFacts(likes='maths'),
          StudentFacts(likes='programming'))
    def computer(self):
        self.matched = True
        print("Suggested Career Path: Computer Engineering")

    @Rule(StudentFacts(likes='mechanics'),
          StudentFacts(likes='maths'))
    def mechanical(self):
        self.matched = True
        print("Suggested Career Path: Mechanical Engineering")

    @Rule(StudentFacts(likes='anatomy'),
          StudentFacts(likes='pharmacology'))
    def mbbs(self):
        self.matched = True
        print("Suggested Career Path: MBBS")

    @Rule(StudentFacts(likes='circuits'),
          StudentFacts(likes='maths'))
    def electronics(self):
        self.matched = True
        print("Suggested Career Path: Electronics Engineering")

    @Rule(StudentFacts(likes='legal writing'),
          StudentFacts(likes='constitutional law'))
    def law(self):
        self.matched = True
        print("Suggested Career Path: LLB")

    @Rule(StudentFacts(likes='digital media'),
          StudentFacts(likes='advertising'))
    def media(self):
        self.matched = True
        print("Suggested Career Path: Journalism")

    @Rule(StudentFacts(likes='architectural design'),
          StudentFacts(likes='urban planning'))
    def architecture(self):
        self.matched = True
        print("Suggested Career Path: B.Arch")


def main():
    engine = CareerExpertSystem()
    engine.reset()

    print("Welcome to the Career Path Expert System!")

    print("\nAvailable interests:")
    print("1. maths \n 2. programming \n 3. mechanics \n 4. anatomy \n 5. pharmacology \n 6. ciruits \n 7. legal writing \n 8. constitutional law \n 9. advertising \n 10. digital media \n 11. urban planning \n 12. architechtural design")

   

    interests = input("\nEnter your interests separated by commas: ").lower().split(',')

    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))

    engine.run()

    if not engine.matched:
        print("No suitable career path found based on the given interests.")


if __name__ == "__main__":
    main()
