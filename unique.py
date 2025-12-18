class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.items)
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item


if __name__ == '__main__':
    data = [1, 1, 2, 2, 3]
    for i in Unique(data):
        print(i)

    from gen_random import gen_random
    for i in Unique(gen_random(10, 1, 3)):
        print(i)

    data = ['a', 'A', 'b', 'B', 'a']
    for i in Unique(data):
        print(i)

    for i in Unique(data, ignore_case=True):
        print(i)
