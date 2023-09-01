from db.database import execute_query, fetch_data
from model.player import Player


def enter_watch(room_id: int, player_id: int):
    query = (
        "INSERT INTO enter_watch (room_id, player_id) "
        "VALUES (%s, %s)"
    )
    execute_query(query, (room_id, player_id))


def leave_watch(room_id: int, player_id: int):
    query = (
        "INSERT INTO leave_watch (room_id, player_id) "
        "VALUES (%s, %s)"
    )
    execute_query(query, (room_id, player_id))


def fetch_watching_players(room_id: int):
    query = (
        "SELECT pd.player_id, pd.name pd.socket_id "
        "FROM enter_watch AS ew "
        "JOIN player_detail AS pd ON ew.player_id = pd.player_id "
        "WHERE ew.room_id = %s "
        "AND NOT EXISTS ("
        "    SELECT 1 "
        "    FROM leave_watch AS lw "
        "    WHERE lw.room_id = ew.room_id "
        "    AND lw.player_id = ew.player_id "
        ") "
    )
    result = fetch_data(query, (room_id,))
    watchers = []

    for row in result:
        player_id, name, socket_id = row
        watchers.append(Player(player_id, name, socket_id))

    return watchers
