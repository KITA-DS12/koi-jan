from dataclasses import dataclass, field
from typing import List

from model.wall import Wall


WINDS = ("east", "south", "west", "north")


@dataclass
class SeatWind:
    id: int
    round_id: int
    player_id: int
    wind: str


@dataclass
class Round:
    id: int
    game_id: int
    round_number: int
    round_wind: str
    dealer_id: int
    wall: Wall
    seat_winds: List[SeatWind] = field(default_factory=list)