from utius import db
# from flask_login import UserMixin

class Perfil(db.Model):
    __tablename__='usuarios'
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(100))
    email=db.Column(db.String(100))
    bibliogrfia=db.Column(db.String(100))

    def __init__(self,nome,email,bibliografia):
        self.nome=nome
        self.email=email
        self.bibliografia=bibliografia
    
    def __repr__(self):
        return "<Perfil{}>".format(self.nome)
