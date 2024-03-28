class AutomaticGuitarSimulator:
    def __init__(self, input_string):
        self.input_string = input_string

    def interpret(self, display=False):
        play_list = []
        chords = self.input_string.split()
        for chord in chords:
            if chord:
                chord_name = ''.join(filter(str.isalpha, chord))
                tune = ''.join(filter(str.isdigit, chord))
                play_list.append({'Chord': chord_name, 'Tune': tune})
            else:
                play_list.append({'Chord': '', 'Tune': ''})
        if display:
            return play_list
        return play_list if play_list else None

    def display(self, chord, tune):
        return f"Normal Guitar Playing -- Chord: {chord}, Play Tune: {tune}"
