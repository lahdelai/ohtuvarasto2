import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytyy(self):
        player = self.stats.search("Semenko")
        self.assertIsNotNone(player)
        self.assertAlmostEqual(player.name, "Semenko")

    def test_search_ei_loydy(self):
        player = self.stats.search("Teemu")
        self.assertIsNone(player)

    def test_team(self):
        edm_players = self.stats.team("PIT")
        self.assertAlmostEqual(len(edm_players), 1)
        lista = [edm_players]
    
    def test_top(self):
        top_players = self.stats.top(2)
        self.assertAlmostEqual(len(top_players), 3)

        best_player = top_players[0]
        self.assertEqual(best_player.name, "Gretzky")


    
