from socketio import Server

import application.usecase.player as player_usecase
import application.usecase.watch as watch_usecase
import application.utils.room as room_util


def set(socket_io: Server):
    @socket_io.on("watch_room")
    def on_watch_room(socket_id: str, player_name: str, room_number_str: str):
        room_number = int(room_number_str)
        player = player_usecase.register_player(player_name, socket_id)
        room = room_util.get_room_by_room_number(room_number)

        watch_usecase.enter_watch(socket_io, room, player)
