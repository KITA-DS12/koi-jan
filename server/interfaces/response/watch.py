from typing import List

from socketio import Server


def notice_enter_watch(socket_io: Server, to: List[str], room_number: int):
    for socket_id in to:
        socket_io.emit("notice_enter_watch", room_number, room=socket_id)
