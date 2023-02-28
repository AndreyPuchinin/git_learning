from unittest import TestCase, main
import taskO


class TaskOClass1(taskO.TaskOMetaClass):
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
        self.assertEqual(task_o_1.second_max()[1], 10)

    def test_2(self):
        task_o_1 = TaskOClass1([10, 20, 0])
        self.assertEqual(task_o_1.second_max()[1], 10)

    def test_3(self):
        task_o_1 = TaskOClass1([20, 10, 20, 0])
        self.assertEqual(task_o_1.second_max()[1], 20)


if __name__ == '__main__':
    main()
