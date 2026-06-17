from typing import List

from model.player import Player
import repository.db.watch as watch_repo


def get_watching_players(room_id: int) -> List[Player]:
    watching_players = watch_repo.get_watching_players(room_id)
    return watching_players
