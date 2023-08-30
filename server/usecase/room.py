from typing import List
import random

from model.player import Player
from model.room import Room
import repository.room


def create_room(player_id: int) -> Room:
    def generate_room_number() -> int:
        while True:
            room_number: int = random.randint(1000, 9999)
            # TODO: room_numberを重複しないようにする
            return room_number

    room_number: int = generate_room_number()
    room = repository.room.create_room(room_number, player_id)

    return room


def enter_room(room_number: int, player_id: int):
    # TODO: 部屋がない場合に対応
    # TODO: 満席の場合に対応
    # TODO: 既に同じ名前のプレイヤーが入室している場合に対応
    rooms = repository.room.fetch_open_rooms()
    room = next((room for room in rooms if room.number == room_number))
    repository.room.enter_room(room.id, player_id)


def leave_room(room_id: int, player_id: int):
    repository.room.leave_room(room_id, player_id)


def get_players_in_room(room_number: int) -> List[Player]:
    rooms = repository.room.fetch_open_rooms()
    room = next((room for room in rooms if room.number == room_number))
    players = repository.room.fetch_players_in_room(room.id)

    return players


def reconnect(new_socket_id: str,
              old_socket_id: str) -> Player:
    repository.player.update_player_socket_id(old_socket_id, new_socket_id)


def get_room_by_player_id(player_id: int) -> Room:
    room = repository.room.fetch_open_room_by_player_id(player_id)

    return room


def get_player_ready_info(socket_id: str):
    player = repository.player.fetch_player_by_socket_id(socket_id)
    room = repository.room.fetch_open_room_by_player_id(player.id)
    players = repository.room.fetch_players_in_room(room.id)
    ready_player_id = repository.room.fetch_ready_player_id(room.id) # roomの中のplayer_idを格納
    player_ready_info = {}
    for player in players:
        # player.id が ready_player_idに含まれてる -> ready
        if player.id in ready_player_id:
            player_ready_info[player.name] = True
        # player_ready_info[player.name] = ready(true or false)
        else:
            player_ready_info[player.name] = False
    player_names = [p.id for p in players]

    return player_names


def ready(socket_id: str) -> Player:
    player = repository.player.fetch_player_by_socket_id(socket_id)
    room = repository.room.fetch_open_room_by_player_id(player.id)
    repository.room.ready_room(room.id, player.id)

    return player


def unready(socket_id: str) -> Player:
    player = repository.player.fetch_player_by_socket_id(socket_id)
    room = repository.room.fetch_open_room_by_player_id(player.id)
    repository.room.unready_room(room.id, player.id)

    return player
