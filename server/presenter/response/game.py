from dataclasses import asdict
from typing import List

from socketio import Server

from model.room import Room
from model.player import Player
from model.tiles import Tiles


def reconnected(socket_io: Server, to: List[str], new_socket_id: str):
    for socket_id in to:
        socket_io.emit("reconnected", new_socket_id, room=socket_id)


def update_game(socket_io: Server, to: List[str], room: Room):
    for socket_id in to:
        socket_io.emit("update_game", asdict(room), room=socket_id)


def update_players(socket_io: Server, to: List[str], players: List[Player]):
    for socket_id in to:
        socket_io.emit("update_players",
                       [asdict(p) for p in players],
                       room=socket_id)


def update_discarded(socket_io: Server,
                     to: List[str],
                     discardeds: List[Tiles]):
    for socket_id in to:
        socket_io.emit("update_discardeds",
                       [asdict(d) for d in discardeds],
                       room=socket_id)


def update_current_player(socket_io: Server,
                          to: List[str],
                          current_player_id: int):
    for socket_id in to:
        socket_io.emit("update_current_player",
                       current_player_id,
                       room=socket_id)


def notice_draw(socket_io: Server, to: List[str]):
    for socket_id in to:
        socket_io.emit("notice_draw", room=socket_id)
