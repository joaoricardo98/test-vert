## requisitos
 Docker

## Como Rodar
rode primeiro os sistemas de mensageiria e banco (para evitar qualquer problema)

```sh
docker compose up -d kafka db zookeeper kafka-ui
```
logo depois execute a api e o scheduler
```
docker compose up api scheduler
```
acesse no seu navegador a pagina do kafka-ui
```
http://localhost:8080/
```

e execute as etapas que foram instruídas no teste.