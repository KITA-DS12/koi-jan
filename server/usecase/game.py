import random

from model.room import Game
from model.round import WINDS
import repository.game
import repository.tile
import repository.wall
import repository.room
import repository.round


def setup_game(room_id: int) -> Game:
    game = repository.game.create_game(room_id)
    tiles = repository.tile.fetch_all_tiles()
    random.shuffle(tiles)
    wall = repository.wall.create_wall(tiles)
    players = repository.room.fetch_players_in_room(room_id)
    random.shuffle(players)
    dealer = players[0]
    round = repository.round.create_round(game.id, 1, "east", dealer.id, wall)

    for wind, player in zip(WINDS, players):
        seat_wind = repository.round.set_seat_wind(round.id, player.id, wind)
        round.seat_winds.append(seat_wind)

    game.rounds.append(round)

    return game


# def next_round(room: Room):
#     usecase.table.next_round(room.table, room.players)
#     room.votes = 0
#     room.skip_players = []
#     room.flag = Flag()
#     room.waiter = Waiter()
#     room.wait_event = RoomWaitEvent()
#     room.tmp_tiles = TileFromPlayer()
#     for player in room.players:
#         usecase.player.next_round(player)
#     usecase.table.update_seat_winds(room.table)
#     dealer = next((p for p in room.players
#                    if p.id == room.table.seat_winds.east))
#     room.table.dealer = dealer.id
#     room.current_player = dealer.id
#     deal_tiles(room)
#
#
# def deal_tiles(room: Room):
#     for player in room.players:
#         NUM_TILES = 13
#         for _ in range(NUM_TILES):
#             tile = usecase.wall.draw_tile(room.table.wall)
#             player.hand.tiles.append(tile)
#
#
# def update_next_current_player(room: Room, player_id: int):
#     room.current_player = usecase.table.update_next_current_player(
#         room.table,
#         player_id
#     )
#
#
# def tsumo(room: Room):
#     room.flag.tsumo = False
#     player: Player = usecase.utils.find_player_by_id(
#         room.players, room.current_player
#     )
#     tile = usecase.wall.draw_tile(room.table.wall)
#     player.hand.tsumo = tile
#
#     hand_tiles = usecase.hand.get_all_tiles(player.hand)
#     shanten = usecase.score.shanten(hand_tiles)
#     if player.hand.calls == [] and shanten <= 0:
#         player.action.riichi = True
#
#     agari = usecase.score.agari(player.hand,
#                                 player.hand.tsumo,
#                                 [],
#                                 room.table.round_wind,
#                                 player.seat_wind,
#                                 True,
#                                 player.is_riichi)
#     if shanten == -1 and agari.__dict__["yaku"] != []:
#         player.action.tsumo = True
#
#
# def dead_tsumo(room: Room):
#     player: Player = usecase.utils.find_player_by_id(
#         room.players, room.current_player
#     )
#     tile = usecase.wall.draw_dead_tile(room.table.wall)
#     player.hand.tsumo = tile
#
#     hand_tiles = usecase.hand.get_all_tiles(player.hand)
#     shanten = usecase.score.shanten(hand_tiles)
#     if player.hand.calls == [] and shanten <= 0:
#         player.action.riichi = True
#
#     agari = usecase.score.agari(player.hand,
#                                 player.hand.tsumo,
#                                 [],
#                                 room.table.round_wind,
#                                 player.seat_wind,
#                                 True,
#                                 player.is_riichi)
#     if shanten == -1 and agari.__dict__["yaku"] != []:
#         player.action.tsumo = True
#
#
# def discard_tile(room: Room, player: Player, tile_id: int):
#     remove_tile = usecase.hand.update_hand(player.hand, tile_id)
#     player.discarded_tiles.append(remove_tile)
#     player.action = Action()
#     room.waiter = Waiter()
#     room.tmp_tiles = TileFromPlayer(remove_tile, player.id)
#     for p in room.players:
#         if p.id != player.id:
#             if usecase.player.can_pon(p, remove_tile):
#                 p.action.pon = True
#                 room.waiter.pon = p
#             if usecase.player.can_kan(p, remove_tile):
#                 p.action.kan = True
#                 room.waiter.kan = p
#             if usecase.player.can_ron(p, remove_tile, room.table.round_wind):
#                 p.action.ron = True
#                 room.waiter.ron.append(p)
#
#
# def pon(room: Room, player: Player):
#     call: CallTiles = CallTiles()
#     call.tile_type = "pon"
#     call.tiles = [t for t in player.hand.tiles
#                   if t.name == room.tmp_tiles.tile.name][:2]
#     call.tiles.append(room.tmp_tiles.tile)
#     call.from_tile = room.tmp_tiles
#     player.hand.calls.append(call)
#     for tile in call.tiles:
#         player.hand.tiles = list(filter(lambda t: t.id != tile.id,
#                                         player.hand.tiles))
#     player.action = Action()
#     room.tmp_tiles = TileFromPlayer()
#
#
# def dai_min_kan(room: Room, player: Player):
#     call: CallTiles = CallTiles()
#     call.tile_type = "dai_min_kan"
#     call.tiles = [t for t in player.hand.tiles
#                   if t.name == room.tmp_tiles.tile.name][:3]
#     call.tiles.append(room.tmp_tiles.tile)
#     call.from_tile = room.tmp_tiles
#     player.hand.calls.append(call)
#     for tile in call.tiles:
#         player.hand.tiles = list(filter(lambda t: t.id != tile.id,
#                                         player.hand.tiles))
#     player.action = Action()
#     room.tmp_tiles = TileFromPlayer()
#
#
# def ron_agari(room: Room, player: Player) -> Score:
#     player.hand.tiles.append(room.tmp_tiles.tile)
#     score_info: Score = usecase.score.agari(
#         player.hand,
#         room.tmp_tiles.tile,
#         room.table.wall.dora[:room.table.wall.dora_num],
#         room.table.round_wind,
#         player.seat_wind,
#         False,
#         player.is_riichi
#     )
#     player.round_score += score_info.cost
#     player.action = Action()
#     room.skip_players.append(player.id)
#     room.flag.agari_num += 1
#
#     return score_info
#
#
# def tsumo_agari(room: Room, player: Player) -> Score:
#     dora = room.table.wall.dora[:room.table.wall.dora_num]
#     if player.is_riichi:
#         dora.extend(room.table.wall.ura_dora[:room.table.wall.dora_num])
#     score_info: Score = usecase.score.agari(
#         player.hand,
#         player.hand.tsumo,
#         dora,
#         room.table.round_wind,
#         player.seat_wind,
#         True,
#         player.is_riichi
#     )
#     player.round_score += score_info.cost
#     player.action = Action()
#     room.skip_players.append(player.id)
#     room.flag.agari_num += 1
#
#     return score_info
