#Name: Hasin Shadab Rahman                                                             UID:U87513234
from questions import Questions
#Generate a list of trivia question objects.

#Returns:
# list: A list containing trivia question objects.
def generate_questions():
    question_list = [
        Questions("How many days are in a lunar year?", "354", "365", "243", "379", 2),
        Questions("What is the largest planet?", "Mars", "Jupiter", "Earth", "Pluto", 2),
        Questions("What is the largest kind of whale?", "Orca whale", "Humpback whale", "Beluga whale", "Blue whale", 4),
        Questions("Which dinosaur could fly?", "Triceratops", "Tyrannosaurus Rex", "Pteranodon", "Diplodocus", 3),
        Questions("Which of these Winnie the Pooh characters is a donkey?", "Pooh", "Eeyore", "Piglet", "Kanga", 2),
        Questions("What is the hottest planet?", "Mars", "Pluto", "Earth", "Venus", 4),
        Questions("Which dinosaur had the largest brain compared to body size?", "Troodon", "Stegosaurus", "Ichthyosaurus", "Gigantoraptor", 1),
        Questions("What is the largest type of penguins?", "Chinstrap penguins", "Macaroni penguins", "Emperor penguins", "White-flippered penguins", 3),
        Questions("Which children's story character is a monkey?", "Winnie the Pooh", "Curious George", "Horton", "Goofy", 2),
        Questions("How long is a year on Mars?", "550 Earth days", "498 Earth days", "126 Earth days", "687 Earth days", 4)
    ]
    return question_list