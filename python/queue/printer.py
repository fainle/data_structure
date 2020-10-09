import random

from python.basic.queue_by_list import Queue


class Printer:
    """
    打印机类
    """

    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None  # 当前是否在打印
        self.time_remaining = 0  # 任务时间

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task:
            return True
        return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task:
    """
    打印任务
    """

    def __init__(self, time):
        """
        初始化打印任务
        :param time:
        """
        self.timestamp = time
        self.pages = random.randrange(1, 21)  # 随机产生1-20页打印任务

    def get_stamp(self):
        """
        获取时间戳
        :return:
        """
        return self.timestamp

    def get_pages(self):
        """
        获取总页数
        :return:
        """
        return self.pages

    def wait_time(self, current_time):
        """
        等待时间
        :param current_time:
        :return:
        """
        return current_time - self.timestamp


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if not lab_printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, print_queue.size()))


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    return False


for _ in range(10):
    simulation(3600, 200)
