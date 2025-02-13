# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]

        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(5, sulfuras_item.sell_in)

    def test_aged_brie_exceeds_quality_limit(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        aged_brie = items[0]

        self.assertEqual(50, aged_brie.quality)

    def test_quality_decreases_twice_as_fast_after_sell_in(self):
        items = [Item("Normal Item", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        normal_item = items[0]

        self.assertEqual(8, normal_item.quality)

    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(items)

        all_items = [item.name for item in gilded_rose.items]
        self.assertIsNotNone(all_items)


if __name__ == '__main__':
    unittest.main()

