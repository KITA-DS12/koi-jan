from dataclasses import asdict
from typing import List

from socketio import Server

from model.room import Room


def reconnected(socket_io: Server, to: List[str], new_socket_id: str):
    for socket_id in to:
        socket_io.emit("reconnected", new_socket_id, room=socket_id)


def update_game(socket_io: Server, to: List[str], room: Room):
    for socket_id in to:
        socket_io.emit("update_game", asdict(room), room=socket_id)