from turtle import Turtle, Screen
import pandas as pd

class IndiaStatesGame(Turtle):
    def __init__(self, image_path, csv_path):
        super().__init__()
        self.screen = Screen()
        self.screen.title("India States Game")
        self.image_path = image_path
        self.screen.addshape(image_path)
        self.csv_path = csv_path
        self.data = pd.read_csv(csv_path)
        self.data = self.data.rename(columns={'X': 'X'})
        self.states = self.data["State"].tolist()
        self.corrected_guess = []

    def game_over(self):
        not_guessed = list(set(self.states) - set(self.corrected_guess))
        print(not_guessed)
        if not_guessed != []:
            dataframe = pd.DataFrame(not_guessed, columns=["State To Learn"])
            dataframe.to_csv("States_not_guessed.csv")
        else:
            with open("States_not_guessed.csv","w") as file:
                file.write("You WON")

    def play(self):
        game_is_on = True
        while game_is_on:
            if len(self.corrected_guess) == len(self.states):
                self.penup()
                self.home()
                self.write("YOU WON ALL STATES CORRECT", align="center", font=("Courier", 36, "normal"))
                self.game_over()
                break

            guessed_city = self.screen.textinput(title="INPUT", prompt=f"Enter The State Name {len(self.corrected_guess)}/{len(self.states)}").lower()

            if guessed_city.lower() == "exit":
                self.game_over()  # Call game_over() before breaking the loop
                game_is_on = False
                break

            for state in self.states:
                if state.lower() == guessed_city:
                    point = Turtle()
                    self.corrected_guess.append(state)
                    state_xcor = int(self.data[self.data.State == state].X.iloc[0])
                    state_ycor = int(self.data[self.data.State == state].Y.iloc[0])
                    point.goto(state_xcor, state_ycor)
                    point.write(state)

    def start(self):
        self.shape(self.image_path)
        self.penup()
        self.play()
        self.screen.mainloop()

if __name__ == "__main__":
    image_path = "image.gif"
    csv_path = "India Coords turtle.csv"
    game = IndiaStatesGame(image_path, csv_path)
    game.start()

