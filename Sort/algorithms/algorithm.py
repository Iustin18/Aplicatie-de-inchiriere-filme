from enum import Enum, unique
from Sort.algorithms.bubble_sort import BubbleSort
from Sort.algorithms.shell_sort import ShellSort


@unique
class Algorithm(Enum):
    BUBBLE_SORT = BubbleSort
    SHELL_SORT = ShellSort