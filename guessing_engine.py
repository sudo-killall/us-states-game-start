import pandas as pd

data = pd.read_csv('50_states.csv', index_col=False)


# y_coordinate = data[data.y == state_guess]


class StateGuess:
    def __init__(self):
        self.states = data['state'].tolist()

    def user_guess(self, state_guess):
        # get the row of the state and extract the x and y coordinates save to a tuple
        state = data[data.state == state_guess]
        x_coord = int(state.x)
        y_coord = int(state.y)
        coordinates = (x_coord, y_coord)
        return coordinates



