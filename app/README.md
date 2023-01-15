# python-simple-api
API Simples escrita em python para uso em POCs.



## Executando

Usando um terminal, faça o git clone do projeto, entre na pasta e utilize o seguinte comando para executar:

```
/bin/python3 app/src/controller.py
```


## Testando...

Ao acessar http://localhost:8000/hello/1 passando o header codigo com algum valor, o sistema irá retornar a resposta no formato json com o id e o código enviado.

```
curl -H "codigo: 123" http://localhost:8000/hello/1

```

Se o servidor estiver rodando corretamente, esse comando deve retornar uma resposta no formato json com o id e o código enviado:

```
{
  "id": "1",
  "codigo": "123",
  "host_response": "note-oliver"
}
```

# Gerando a imagem

Usando um terminal, entre na pasta 'app' e digite:

```
docker build -t python-simple-api -f docker/Dockerfile .
```

docker run -d -p 8282:8000 python-simple-api


curl -H "codigo: 123" http://localhost:8282/hello/1


## Tagueando a imagem e publicando..

```
docker tag python-simple-api nettooe/python-simple-api:1.1.0
```

```
docker push nettooe/python-simple-api:1.1.0
```
