import pyodbc
from flask import Flask, render_template, request

app = Flask(__name__)


def conexao():
    server = 'SQL'
    database = 'SICAD'
    usernamedb = 'FAISP'
    password = 'faisp'
    cnxn = pyodbc.connect(
        "DRIVER={SQL Server};SERVER=" + server + ';DATABASE=' + database + ';UID=' + usernamedb + '; PWD=' + password)
    return cnxn.cursor()


@app.route('/')
def consultar():
    cursor = conexao()
    cursor.execute('SELECT * FROM T_ALUNO')
    result_set = cursor.fetchall()
    # return render_template('my_list.html', my_list=cursor.fetchall())
    return render_template('my_list.html', my_list=result_set)


@app.route('/cadastro')
def cadastro():
    return render_template("cadastrar.html")


@app.route('/resultado', methods=['POST', 'GET'])
def resultado():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        dt_nasc = request.form['nascimento']
        genero = request.form['genero']
        obj_grad = request.form['obj_grad']
        email = request.form['email']
        usuario = request.form['usuario']
        senha = request.form['senha']

        cursor = conexao()
        cursor.execute("SELECT * FROM T_ALUNO WHERE NOME ='" + nome + "'")
        row = cursor.fetchone()
        if row is not None:
            return "Usuário {} já cadastrado!".format(nome)
        else:
            cursor.execute(
                "INSERT INTO T_ALUNO (NOME,ENDERECO,DT_NASC,GENERO,OBJ_GRAD,EMAIL,USUARIO,SENHA) VALUES ('{}','{}',"
                "'{}','{}','{}','{}','{}','{}');".format(
                    nome, endereco, dt_nasc, genero, obj_grad, email, usuario, senha))
            cursor.commit()
            cursor.close()
        return consultar()


@app.route('/excluir/<idUsr>')
def excluir(idUsr):
    cursor = conexao()
    cursor.execute("delete from T_ALUNO where ID ='" + idUsr + "'")
    cursor.commit()
    cursor.close()
    return consultar()


@app.route('/editaruser/<idUsr>', methods=['GET'])
def editaruser(idUsr):
    cursor = conexao()
    cursor.execute("SELECT * FROM T_ALUNO WHERE ID = " + idUsr)
    result_set = cursor.fetchall()
    return render_template('editar.html', MyUser=result_set)


@app.route('/editar/', methods=['POST'])
def editar():
    nome = request.form['nome']
    endereco = request.form['endereco']
    dt_nasc = request.form['nascimento']
    genero = request.form['genero']
    obj_grad = request.form['obj_grad']
    email = request.form['email']
    usuario = request.form['usuario']
    senha = request.form['senha']
    idUsr = request.form['idUsr']

    cursor = conexao()
    cursor.execute("UPDATE T_ALUNO SET (NOME='{}',ENDERECO='{}',DT_NASC,GENERO='{}',OBJ_GRAD='{}',EMAIL='{}',USUARIO='{}',SENHA='{}') WHERE ID = " + idUsr).format(nome, endereco, dt_nasc, genero, obj_grad, email, usuario, senha)
    cursor.commit()
    cursor.close()
    return consultar()


if __name__ == '__main__':
    import os

    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5000'))
    except ValueError:
        PORT = 5000
    app.run(HOST, PORT)
