from flask import Flask,request,jsonify
import mongoengine as me

database_name = 'todo_app'
me.connect(database_name)

#Definir campos para banco de dados (modelos)
class User(me.Document):
    name = me.StringField()
    email = me.StringField(nullable=False) #nao permite campo nulo

#None eh o null do python

class Task(me.Document):
    description = me.StringField()
    deadline = me.DateTimeField()
    title = me.StringField()
    finished = me.BooleanField()
    tags = me.ListField(me.StringField()) #Lista de Strings
    added = me.DateTimeField()
    user = me.ReferenceField(User)
    color = me.StringField()

#instancia objeto Flack
app = Flask(__name__)

#Define rota raiz
@app.route("/users", methods=['GET'])
def get_users():
    users = User.objects.all()
    array = []

    #Cria o lista de dicionario com dados do banco de dados
    #Esse vetor sera retornado para o front-end
    for user in users:
        array.append({
            'id':str(user._id), #id eh criado automaticamente
            'name':user.name,
            'email':user.email
        })

    #return json.dumps(array) #Transforma em json
    return jsonify(array) #Transforma em json (funcao do flask)

#Roda servidor web
if __name__ == "__main__":
    app.run()
