def get_input():
    return input("enter a number: ")


def second_max(get_input_f):
    v = int(get_input_f())
    # print('one')
    if v == 0:
        return 0, 0
    res = second_max(get_input_f)
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


class TaskOMetaClass:
    def get_input(self):
        print('needs reimplementation')


if __name__ == '__main__':
    task_0_obj = TaskOClass1([10, 20, 0])
    print(second_max(task_0_obj.get_input)[1])
    task_0_obj = TaskOClass1([10, 20, 20, 0])
    print(second_max(task_0_obj.get_input)[1])
    task_0_obj = TaskOClass1([0])
    print(second_max(task_0_obj.get_input)[1])
