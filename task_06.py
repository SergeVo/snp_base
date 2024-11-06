# Разработать методы для программы Камень-Ножницы-Бумага.
# Метод rps_game_winner должен принимать на вход массив следующей структуры
# [ ["player1", "P"], ["player2", "S"] ], где P - бумага, S - ножницы, R - камень, и
# функционировать следующим образом:
# • если количество игроков больше 2 необходимо вызывать исключение
# WrongNumberOfPlayersError
# • если ход игроков отличается от ‘R’, ‘P’ или ‘S’ необходимо вызывать
# исключение NoSuchStrategyError
# • в иных случаях необходимо вернуть имя и ход победителя, если оба
# игрока походили одинаково - выигрывает первый игрок.

class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players=None):
    if players is None or len(players) != 2:
        raise WrongNumberOfPlayersError("Нужно 2 игрока!")

    shown_fingers = {'R', 'P', 'S'}

    player1, figure1 = players[0]
    player2, figure2 = players[1]

    if figure1 not in shown_fingers or figure2 not in shown_fingers:
        raise NoSuchStrategyError("Себе такой палец покажи!")

    if figure1 == figure2:
        return [player1, figure1]
    elif figure1 == 'R' and figure2 == 'S':
        return [player1, figure1]
    elif figure1 == 'P' and figure2 == 'R':
        return [player1, figure1]
    elif figure1 == 'S' and figure2 == 'P':
        return [player1, figure1]
    else:
        return [player2, figure2]


print(rps_game_winner([["player1", "P"], ["player2", "P"]]))
print(rps_game_winner([["player1", "P"], ["player2", "R"]]))
print(rps_game_winner([["player1", "P"], ["player2", "S"]]))
print(rps_game_winner([["player1", "P"], ["player2", "P"]]))
print(rps_game_winner([["player1", "P"], ["player2", "R"]]))
print(rps_game_winner([["player1", "Z"], ["player2", "S"]]))
