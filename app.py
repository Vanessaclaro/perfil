from flask import Flask,render_template,request,redirect

app = Flask(__name__)
cadastro=[]

@app.route('/')
def index():
    return render_template('index.html',cadastro=cadastro)

@app.route('/cadastrar',methods=['GET'])
def cadastrar():
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



