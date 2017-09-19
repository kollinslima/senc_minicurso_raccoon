#Criar ambiente virtual python
virtualenv -p python3 env

#Ativar ambiente virtual (para uso)
source env/bin/activate 

#Instalar flask e mongoengine com pip
#Podemos usar pip install -r arquivo.txt, colocando flask e mongoengine em arquivo.txt

#MongoDB

#Rotas do flask
/users - POST,GET
-POST: adiciona colecao
-GET: pega a colecao inteira

/users/<id> - GET, PATCH, DELETE
-GET: pega dados de um usuario
-PATCH: atualiza um usario
-DELETE: remove o usuario

/tasks - POST,GET
/tasks/<id> - GET, DELETE

