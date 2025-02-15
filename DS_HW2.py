class Filter:
    def __init__(self, type: str, wear: float = 0):
        self.type = type
        self.wear = wear


class Solution:
    def __init__(self, concentration: float, purity: float):
        self.concentration = concentration
        self.purity = purity


class CyanideSolution(Solution):
    def __init__(self, concentration: float, purity: float):
        assert 50 <= concentration <= 100, 'Концентрация раствора цианида должна быть от 50 до 100!'
        super().__init__(concentration, purity)


class Catalyst(Solution):
    pass


class Batch:
    def __init__(self, fraction: float, cyanid_processed: CyanideSolution = None, catalyst_processed: Catalyst = None,
                 purity: float = 0):
        self.fraction = fraction
        self.cyanide_processed = cyanid_processed
        self.catalyst_processed = catalyst_processed
        self.purity = purity


class Ore:
    def __init__(self, fraction: float):
        self.fraction = fraction

    def makeBatches(self, n: int):
        """
        Возвращаем список из n батчей
        """
        pass


class FiltrationDepartment:
    def __init__(self, current_filter: Filter):
        self.current_filter = current_filter

    def replace_filter(self, new_filter: Filter):
        self.current_filter = new_filter

    def filter_batch(self, batch: Batch):
        if (self.current_filter.wear >= 80):
            print("Фильтр не в кондиции, замените его!")
            return batch
        # batch.purity = #($&#(@ изменяем чистоту бача
        # self.current_filter.wear += #@# симулируем износ фильтра
        return batch

class CrushingDepartment:
    def __init__(self, fraction : float):
        self.fraction = fraction

    def crush_ore(self, ore : Ore):
        Ore.fraction = self.fraction

class Cyanidation_Department:
    def __init__(self, cyanide : CyanideSolution, catalyst : Catalyst):
        self.cyanide = cyanide
        self.catalyst = catalyst

    def read_parameters(self):
        print(self.catalyst.purity, self.catalyst.concentration)
        print(self.cyanide.purity, self.cyanide.concentration)

    def process_batch(self, batch : Batch):
        batch.cyanide_processed = self.cyanide
        batch.catalyst_processed = self.catalyst
        return batch

