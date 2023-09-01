from socketio import Server

from model.player import Player
from model.room import Room
import repository.db.watch as watch_repo
import interfaces.response.watch as emit


def enter_watch(socket_io: Server, room: Room, player: Player):
    watch_repo.enter_watch(room.id, player.id)
    emit.notice_enter_watch(socket_io, [player.socket_id], room.number)


def leave_watch(room_id: int, player_id: int):
    watch_repo.leave_watch(room_id, player_id)
