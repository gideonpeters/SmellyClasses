class BlackjackGame:
    def __init__(self):
        self.deck = []
        suits = ['S', 'C', 'D', 'H']
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for suit in suits:
            for rank in ranks:
                self.deck.append(rank + suit)

    def calculate_hand_value(self, hand):
        values = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
        total_value = 0
        num_aces = 0
        for card in hand:
            rank = card[:-1]
            total_value += values[rank]
            if rank == 'A':
                num_aces += 1
        while total_value > 21 and num_aces:
            total_value -= 10
            num_aces -= 1
        return total_value

    def check_winner(self, player_hand, dealer_hand):
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)
        if player_value > 21:
            return 'Dealer wins'
        elif dealer_value > 21:
            return 'Player wins'
        elif player_value > dealer_value:
            return 'Player wins'
        elif player_value < dealer_value:
            return 'Dealer wins'
        else:
            return 'Draw'
