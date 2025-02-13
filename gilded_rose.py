# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# Base class for item update strategies
class ItemStrategy:
    def update(self, item):
        pass

# Strategy for normal items
class NormalItemStrategy(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 1
            if item.sell_in < 0:
                item.quality -= 1 


# Strategy for Aged Brie 
class AgedBrieStrategy(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 0 and item.quality < 50:
                item.quality += 1  



# Strategy for Sulfuras (does not change)
class SulfurasStrategy(ItemStrategy):
    def update(self, item):
        pass  # No changes needed


# Strategy for Backstage Passes 
class BackstagePassStrategy(ItemStrategy):
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)


# Main class for updating items
class GildedRose:
    def __init__(self, items):
        self.items = items

    def get_strategy(self, item):
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy()
        elif "Backstage passes" in item.name:
            return BackstagePassStrategy()
        else:
            return NormalItemStrategy()

    def update_quality(self):
        for item in self.items:
            strategy = self.get_strategy(item)
            strategy.update(item)