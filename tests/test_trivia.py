from unittest import TestCase

from trivia import Players


class TestPlayers(TestCase):

    def test_by_default_the_players_object_has_no_players(self):
        assert (Players().count() == 0)

    def test_after_adding_a_player_we_have_one_player(self):
        players = Players()
        players.add_player("John")

        count = players.count()

        assert (count == 1)

    def test_by_default_the_first_player_is_always_zero(self):
        players = Players()
        players.add_player("jj")

        assert(players.get_current() == "jj")

    def test_then_the_next_player_is_the_second(self):
        players = Players()
        players.add_player("first")
        players.add_player("second")

        players.next()

        assert(players.get_current() == "second")

    def test_wrap_the_players_when_going_past_the_last_one_when(self):
        players = Players()
        players.add_player("first")
        players.add_player("second")

        players.next()
        players.next()

        assert (players.get_current() == "first")
