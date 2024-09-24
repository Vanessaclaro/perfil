from flask import Flask,render_template,request,redirect,flash
from utius import db
from flask_migrate import Migrate
from models import Perfil


app = Flask(__name__)

app.secret_key = 'minha chave secreta'
conexao = "sqlite:///meubanco.sqlite"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


migrate = Migrate(app, db)


cadastro=[]

@app.route('/')
def index():
    return render_template('index.html',cadastro=cadastro)

@app.route('/cadastrar',methods=['GET'])
def cadastrar():
    flash('Perfil cadastrado com sucesso!')
    return render_template('cadastrar.html')

@app.route('/cadastrar_enviar',methods=['POST'])
def cadastrar_enviar():
    nome=request.form['nome']
    email=request.form['email']
    bibliografia=request.form['bibliografia']

    cadastro.append({
        'id' :len(cadastro),
        'nome': nome,
        'email': email,
        'bibliografia': bibliografia
    })
    flash('Perfil cadastrado com sucesso!')
    return redirect('perfil')
@app.route('/perfil')
def perfil():
    if cadastro:
        ultimo_cadastro = cadastro[-1]
        return render_template('perfil.html', cadastro=ultimo_cadastro)
    return render_template('perfil.html', cadastro=None)


@app.route('/editar/<int:id_cadastro>')
def editar(id_cadastro):
    # Verificando se o cadastro existe
    dados_cadastro = next((cadastro for cadastro in cadastro if cadastro['id'] == id_cadastro), None)
    if dados_cadastro is not None:
        return render_template('editar.html', dados_cadastro=dados_cadastro)
    return redirect('/')  
@app.route('/editar_enviar', methods=['POST'])
def editar_enviar():
    id_cadastro = int(request.form['id_cadastro'])
    nome = request.form['nome']
    email = request.form['email']
    bibliografia = request.form['bibliografia']

    dados_cadastro = next((cadastro for cadastro in cadastro if cadastro['id'] == id_cadastro), None)
    
    if dados_cadastro:
        dados_cadastro['nome'] = nome
        dados_cadastro['email'] = email
        dados_cadastro['bibliografia'] = bibliografia

    return redirect('/')

@app.route('/excluir/<int:id_cadastro>')
def excluir(id_cadastro):
    global cadastro
    cadastro = [item for item in cadastro if item['id'] != id_cadastro]
    return redirect('/')


if __name__=='__main__':
    app.run()



