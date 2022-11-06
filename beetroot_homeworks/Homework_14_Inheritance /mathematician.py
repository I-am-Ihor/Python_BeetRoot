class Mathematician:
    def square_nums(self, list_num: list) -> list:
        list_new = [num**2 for num in list_num]

        return list_new

    def remove_positives(self, list_num: list) -> list:
        list_new = [num for num in list_num if num < 0]

        return list_new

    def filter_leaps(self, list_num: list) -> list:
        list_new = [num for num in list_num if num % 4 == 0]

        return list_new


m = Mathematician()
list_1 = [7, 11, 5, 4]
list_2 = [26, -11, -8, 13, -90]
list_3 = [2001, 1884, 1995, 2003, 2020]

assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]

assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]

assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
