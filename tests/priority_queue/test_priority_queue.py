import pytest
from ting_file_management.priority_queue import PriorityQueue


chapolin = ['Eu, O Chapolin Colorado']
stallone = ['Coma peixe, peixe é bom',
            'Você é a doença, eu sou a cura',
            'Quando eu viro meu boné',
            'Aaadriaan',
            'Ei, tira!',
            'Você veio de tão longe, para ver campos vazios'
            ]


chapolin_file = {
                "nome_do_arquivo": 'chapolin',
                "qtd_linhas": 1,
                "linhas_do_arquivo": chapolin
                }
stallone_file = {
                "nome_do_arquivo": 'stallone',
                "qtd_linhas": 6,
                "linhas_do_arquivo": stallone
                }


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    with pytest.raises(IndexError):
        priority_queue.search(0)
    priority_queue.enqueue(stallone_file)
    assert len(priority_queue) == 1
    priority_queue.enqueue(chapolin_file)
    assert len(priority_queue) == 2
    assert priority_queue.search(0) == chapolin_file
    assert priority_queue.search(1) == stallone_file
    with pytest.raises(IndexError):
        priority_queue.search(-1)
    assert priority_queue.dequeue() == chapolin_file
    assert priority_queue.dequeue() == stallone_file
