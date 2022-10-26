from asyncio.windows_events import NULL


class Orange:
    def __init__(self, w, orch, d):
        self.weight = w
        self.orchard = orch
        self.date_picked = d

    def pickOrange(self):
        return self

    def squeezeOrange(self):
        