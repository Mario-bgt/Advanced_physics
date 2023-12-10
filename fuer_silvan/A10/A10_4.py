class Fridge:
    def __init__(self):
        self.items = []

    def store(self, item):
        self.items.append(item)

    def take(self, item):
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            raise Warning("Item not found in fridge.")

    def find(self, name):
        filtered_items = [(date, item_name) for date, item_name in self.items if item_name == name]
        if filtered_items:
            return min(filtered_items, key=lambda x: x[0])
        return None

    def take_before(self, date):
        items_to_remove = [item for item in self.items if item[0] < date]
        for item in items_to_remove:
            self.items.remove(item)
        return items_to_remove

    def __iter__(self):
        sorted_items = sorted(self.items, key=lambda x: x[0])
        return iter(sorted_items)

    def __len__(self):
        return len(self.items)
