from repository.db.watch import watch_repo
from model.player import Player


def enter_watch(self, room_id: int, player_id: int):
    self.watch_repo.enter_watch(room_id, player_id)


def leave_watch(self, room_id: int, player_id: int):
    self.watch_repo.leave_watch(room_id, player_id)


def get_watching_players(self, room_id: int) -> List[Player]:
    watching_players = self.watch_repo.get_watching_players(room_id)
    return watching_players
