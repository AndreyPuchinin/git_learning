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


class TaskOTest(TestCase):
    def test_1(self):
        task_o_1 = TaskOClass1([20, 10, 0])
        global get_input
        foo1 = get_input
        get_input = task_o_1.get_input
        self.assertEqual(second_max()[1], 10)
        get_input = foo1

    def test_2(self):
        task_o_1 = TaskOClass1([10, 20, 20, 0])
        global get_input
        foo1 = get_input
        get_input = task_o_1.get_input
        self.assertEqual(second_max()[1], 20)
        get_input = foo1

    def test_3(self):
        task_o_1 = TaskOClass1([0])
        global get_input
        foo1 = get_input
        get_input = task_o_1.get_input
        self.assertEqual(second_max()[1], 0)
        get_input = foo1


if __name__ == '__main__':
    main()
