from unittest import TestCase, main


def get_input():
    return input("enter a number: ")



def second_max():
    v = int(get_input())
    # print('one')
    if v == 0:
        return 0, 0
    res = second_max()
    # print('two')
    if v >= res[0]:
        return v, res[0]
    if v >= res[1]:
        return res[0], v
    return res


class TaskOClass1:
    def __init__(self, els):
        self.els = els
        self.n = 0

    def get_input(self):
        self.n += 1
        if self.n <= len(self.els):
            return self.els[self.n-1]
        else:
            raise Exception


def trick(els):
    def trick_decorator(func):
        def _wrapper(*args, **kwargs):
            task_o_1 = TaskOClass1(els)
            global get_input
            foo1 = get_input
            get_input = task_o_1.get_input
            func(*args, **kwargs)
            get_input = foo1
        return _wrapper
    return trick_decorator


class TaskOTest(TestCase):
    @trick([20, 10, 0])
    def test_1(self):
        self.assertEqual(second_max()[1], 10)

    @trick([10, 20, 20, 0])
    def test_2(self):
        self.assertEqual(second_max()[1], 20)

    @trick([0])
    def test_3(self):
        self.assertEqual(second_max()[1], 0)


if __name__ == '__main__':
    main()
