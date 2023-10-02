from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()

    for i in range(1, 5):
        queue.enqueue({"qtd_linhas": i * 2})

    assert queue.__len__() == 4
    assert queue.high_priority.__len__() == 2
    assert queue.regular_priority.__len__() == 2

    queue.dequeue()
    assert queue.__len__() == 3
    assert queue.high_priority.__len__() == 1
    assert queue.regular_priority.__len__() == 2

    file = queue.search(0)
    assert file["qtd_linhas"] == 4

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(99999)
