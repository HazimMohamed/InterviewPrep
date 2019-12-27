class CardList:
    class CardData:
        def __init__(self, card_id, max_level, upgrade_cost, level_power):
            self.card_id = card_id
            self.max_level = max_level
            self.upgrade_cost = {level + 2: cost for level, cost in enumerate(upgrade_cost)}
            self.level_power = {level + 1: power for level, power in enumerate(level_power)}

    def __init__(self, card_info_list):
        self.cards = {card.card_id: card for card in card_info_list}

    def __len__(self):
        return len(self.cards)

    @staticmethod
    def encode_state(values_dict):
        encoded_string = ''
        for key, val in values_dict.items():
            encoded_string += '{}:{};'.format(key, val)
        return encoded_string[:-1]

    @staticmethod
    def upgrade(state, index):
        split_state = state.split(';')
        card_id, card_level = map(int, split_state[index].split(':'))
        new_str = str(card_id) + ':' + str(card_level + 1)
        new_state = ''
        for ind, val in enumerate(split_state):
            if ind == index:
                new_state += new_str + ';'
            else:
                new_state += val + ';'
        return new_state[:-1]

    def can_upgrade(self, state, index):
        relevant_card = state.split(';')[index]
        card_id, card_level = map(int, relevant_card.split(':'))
        return card_level < self.cards[card_id].max_level

    def next_upgrade_cost(self, state, index):
        relevant_card = state.split(';')[index]
        card_id, card_level = map(int, relevant_card.split(':'))
        return self.cards[card_id].upgrade_cost[card_level+1]

    def get_value(self, state):
        value = 0
        split_state = state.split(';')
        for card_pair in split_state:
            card_id, card_level = map(int, card_pair.split(':'))
            value += self.cards[card_id].level_power[card_level]
        return value


def solve(card_data, state, num_coins):
    def max_if_upgraded(card_info, current_state, card_index, remaining_coins):
        if not card_info.can_upgrade(current_state, card_index):
            return -1

        upgrade_cost = card_info.next_upgrade_cost(current_state, card_index)
        if remaining_coins - upgrade_cost < 0:
            return -1

        current_state = card_info.upgrade(current_state, card_index)
        possible_game_states = \
            [max_if_upgraded(card_info=card_data,
                             current_state=current_state,
                             card_index=j,
                             remaining_coins=remaining_coins - upgrade_cost) for j in range(len(card_info))]

        current_val = card_info.get_value(state)
        return max(*possible_game_states, current_val)

    game_states = [max_if_upgraded(card_info=card_data,
                                   current_state=state,
                                   card_index=i,
                                   remaining_coins=num_coins) for i in range(len(card_data))]
    max_power = max(*game_states, 0)
    return max_power


def main():
    num_test_cases = int(input())
    card_data = []
    start_values = {}
    card_id = 0
    for i in range(num_test_cases):
        num_coins, num_cards = map(lambda a: int(a), input().split(' '))
        for j in range(num_cards):
            max_level, current_level = map(lambda a: int(a), input().split(' '))
            level_power = list(map(lambda a: int(a), input().split(' ')))
            upgrade_cost = list(map(lambda a: int(a), input().split(' ')))
            card_data.append(CardList.CardData(card_id = card_id,
                                               max_level=max_level,
                                               upgrade_cost=upgrade_cost,
                                               level_power=level_power))
            start_values[card_id] = current_level
            card_id += 1
        card_data = CardList(card_data)
        state = CardList.encode_state(start_values)
        print('Case #{}: {}'.format(i + 1, solve(card_data, state, num_coins)))


if __name__ == '__main__':
    main()
