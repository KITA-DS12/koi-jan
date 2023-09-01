from db.database import execute_query
from db.database import fetch_data

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

def get_watching_players(room_id: int):
    query = (
        "SELECT p.id, pd.name "
        "FROM enter_watch AS ew "
        "JOIN player AS p ON ew.player_id = p.id "
        "JOIN player_detail AS pd ON p.id = pd.player_id "
        "WHERE ew.room_id = %s "
        "AND NOT EXISTS ("
        "    SELECT 1 "
        "    FROM leave_watch AS lw "
        "    WHERE lw.room_id = ew.room_id "
        "    AND lw.player_id = ew.player_id "
        ") "
    )
    watching_players = fetch_data(query, (room_id,))
    return watching_players