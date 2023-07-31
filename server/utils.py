from typing import List

from tile import Tile


def sort_tiles_by_id(tiles: List[Tile]):
    return sorted(tiles, key=lambda tile: tile.id)
