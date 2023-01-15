# python-simple-api
API Simples escrita em python para uso em POCs.



# Iniciando o ArgoCD

Entre na pasta `k8s` e digite:

```
kubectl apply -f application.yaml
```

# Intalando o Prometheus

```
helm install prometheus prometheus-community/prometheus --namespace monitoramento --create-namespace --set server.service.type=LoadBalancer
```
