import PySimpleGUI as sg

PLAYER_ONE = "X"
PLAYER_TWO = "O"

current_player = PLAYER_ONE

player_one_track = []
player_two_track = []

button_size = (7, 3)

winner_plays = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7]]

layout = [[
    sg.Button("", key="-0-", size=button_size),
    sg.Button("", key="-1-", size=button_size),
    sg.Button("", key="-2-", size=button_size)
    ],
    [
        sg.Button("", key="-3-", size=button_size),
        sg.Button("", key="-4-", size=button_size),
        sg.Button("", key="-5-", size=button_size)
    ],
    [
        sg.Button("", key="-6-", size=button_size),
        sg.Button("", key="-7-", size=button_size),
        sg.Button("", key="-8-", size=button_size)
    ],
    [sg.Button("Revancha", key="-RE-")],
    [sg.Button("Cerrar", key="-OK-")]]

game_end = False
close_app = False


def close(event):
    if event == sg.WIN_CLOSED or event == "-OK-":
        close_app = True
        return close_app


def rematch(event, window):
    if event == "-RE-":
        window.Element("-0-").Update(text="")
        window.Element("-1-").Update(text="")
        window.Element("-2-").Update(text="")
        window.Element("-3-").Update(text="")
        window.Element("-4-").Update(text="")
        window.Element("-5-").Update(text="")
        window.Element("-6-").Update(text="")
        window.Element("-7-").Update(text="")
        window.Element("-8-").Update(text="")
        replay = True
        return replay


def winner(deck):
    for winner_play in winner_plays:
        if deck[winner_play[0]] == deck[winner_play[1]] == deck[winner_play[2]] != 0:
            if deck[winner_play[0]] == PLAYER_ONE:
                sg.Popup("Ha ganado el jugador 1")
            else:
                sg.Popup("Ha ganado el jugador 2")
            game_end = True
            return game_end


def not_place(deck):
    if 0 not in deck:
        sg.Popup("¡Os habeis quedado sin lugar!")
        game_end = True
        return game_end


def gameplay(event, current_player, window, deck):
    index = int(event.replace("-", ""))
    deck[index] = current_player
    window.Element(event).Update(text=current_player)

    finish = not_place(deck), winner(deck)
    return finish


def structure(game_end, current_player):

    deck = [0, 0, 0,
            0, 0, 0,
            0, 0, 0]

    window = sg.Window("Tic Tac Toe", layout)

    while not close_app:
        event, values = window.read()
        close_event = close(event)
        if close_event:
            break

        replay = rematch(event, window)
        if replay:
            current_player = PLAYER_ONE
            deck = [0, 0, 0,
                    0, 0, 0,
                    0, 0, 0]

        if window.Element(event).ButtonText == "" and not game_end:
            gameplay(event, current_player, window, deck)

        if current_player == PLAYER_ONE:
            current_player = PLAYER_TWO
        else:
            current_player = PLAYER_ONE

    window.close()


def main():
    structure(game_end, current_player)


if __name__ == "__main__":
    main()
