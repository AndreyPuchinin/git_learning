class TaskOMetaClass:
    def second_max(self):
        v = self.get_input()
        if v == 0:
            return (0, 0)
        res = self.second_max()
        if v >= res[0]:
            return (v, res[0])
        if v >= res[1]:
            return (res[0], v)
        return res

    def get_input(self):
        print('needs reimplementation')


class TaskOClass1(TaskOMetaClass):
    def get_input(self):
        return int(input())

if __name__ == '__main__':
    taskO_1 = TaskOClass1()
    print(taskO_1.second_max()[1])