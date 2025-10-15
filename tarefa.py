from flask import jsonify

def buscar_tarefas():
    tarefas = [
        {
                'id': 1,
                'nome': 'aprender digitação',
                'descicao': 'Vamos aumentar o zoom para não errar a digitação' ,
                'status': 'Pendente'
        },

        {
            'id': 2,
            'nome': 'Aprender pyhthon',
            'descricao': 'Aprender python para programar JSON',
            'ststus': 'Pendente'
        }
    ]

    return jsonify(tarefas)

def buscar_tarefa():
    tarefa = {
        'id': 1,
        'nome': 'aprender digitação',
        'descicao': 'Vamos aumentar o zoom para não errar a digitação' ,
        'status': 'Pendente'
    }

    return jsonify(tarefa)