from flask import jsonify
from conexao import get_conexao
from psycopg2.extras import RealDictCursor


def buscar_tarefas():
    con = get_conexao()
    cursor = con.cursor(cursor_factory = RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos;"
    )
    #busca os dados e armazena na variavel
    todos = cursor.fetchall()

    #fecha as conexoes
    cursor.close()
    con.close()

    return jsonify(todos)

    
    

def buscar_tarefa(id):
    con = get_conexao()
    cursor = con.cursor(cursor_factory = RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM todos WHERE id = %s;",
        (id,)
    )
    #busca os dados e armazena na variavel
    todo = cursor.fetchall()

    #fecha as conexoes
    cursor.close()
    con.close()

    return jsonify(todo)
