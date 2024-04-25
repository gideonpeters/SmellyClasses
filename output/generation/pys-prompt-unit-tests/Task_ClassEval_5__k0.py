class AutomaticGuitarSimulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def interpret(self, display=False):
        play_list = []
        if self.input_string:
            chords = self.input_string.split()
            for chord in chords:
                tune = chord[1:]
                play_list.append({'Chord': chord[:1], 'Tune': tune})
        else:
            play_list.append({'Chord': '', 'Tune': ''})
        if display:
            return play_list
        return play_list

    def display(self, chord, tune):
        return f"Normal Guitar Playing -- Chord: {chord}, Play Tune: {tune}"
