class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, worker):
        self._workers.append(worker)


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    def AddWorker(self):
        self.boss.workers = [self.id, self.name, self.company]


boss_1 = Boss(1, "Boss1", "Company 1")
worker_1 = Worker(1, "Name 1", "Company 1", boss_1)
worker_1.AddWorker()
worker_2 = Worker(2, "Name 2", "Company 2", boss_1)
worker_2.AddWorker()
print(boss_1.workers)
