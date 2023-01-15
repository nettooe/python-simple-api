# python-simple-api
API Simples escrita em python para uso em POCs.


# Subindo o ambiente de forma completa


## Criando o cluster com k3d

```
k3d cluster create --api-port 6550 -p "8081:80@loadbalancer" --agents 2 --servers 3
```

## Instalando o ArgoCD

```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Descubra a senha atribuída ao usuário 'admin' do seu ArgoCD desta forma:
```
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```


## Iniciando as aplicações usando o ArgoCD

Entre na pasta `k8s` e digite:

```
kubectl apply -f application.yaml
```

Agora, abra uma janela do seu terminal e faça um port-fowarding para poder acessar a interface gráfica do ArgoCD:
```
kubectl port-forward service/argocd-server 9091:80 -n argocd
```

No seu navegador, acesse: http://localhost:9091


## Instalando o Prometheus

```
helm install prometheus prometheus-community/prometheus --namespace monitoramento --create-namespace --set server.service.type=LoadBalancer
```

Agora, abra uma janela do seu terminal e faça um port-fowarding para poder acessar a interface gráfica do Prometheus:
(nenhuma configuração adicional é necessária)

```
kubectl port-forward service/prometheus-server 9092:80 -n monitoramento
```

No seu navegador, acesse: http://localhost:9092


## Instalando o Grafana

```
helm install grafana grafana/grafana --namespace monitoramento --create-namespace --set server.service.type=LoadBalancer
```

Para obter a senha do admin:

```
kubectl get secret --namespace monitoramento grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
```

Agora, abra uma janela do seu terminal e faça um port-fowarding para poder acessar a interface gráfica do Grafana:

```
kubectl port-forward service/grafana 9093:80 -n monitoramento
```

No seu navegador, acesse: http://localhost:9093

Vá até Configuração > Datasources. Adicione um novo datasource com:
Nome: Prometheus (opcional)
URL: http://prometheus-server

Vá até o site do grafana e pesquise por um código de dashboard que lhe interesse.
O código '10000' oferece um interessante dashboard para Kubernets.
Para importar um novo dashboard, vá até: Dahboard > Browse > clique em 'new' > Import. Em seguida informe o código como "10000" (sem as aspas).


# Destruindo todo o ambiente


Entre na pasta `k8s` e digite:

```
kubectl delete -f application.yaml
```


## Eliminando o cluster

```
k3d cluster delete k3s-default
```

