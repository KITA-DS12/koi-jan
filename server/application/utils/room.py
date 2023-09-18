from model.room import Room
import repository.db.room as room_repo


def get_room_by_player_id(player_id: int) -> Room:
    room = room_repo.fetch_open_room_by_player_id(player_id)

    return room


def get_room_by_room_number(room_number: int) -> Room:
    rooms = room_repo.fetch_open_rooms()
    room = next((r for r in rooms if r.number == room_number), None)

    return room
