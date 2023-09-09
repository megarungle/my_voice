# my_voice

Проект по машинному обучению на хакатон

## TOC

  1. [Деплой](#%D0%B4%D0%B5%D0%BF%D0%BB%D0%BE%D0%B9)
  2. [Документация](#%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D1%8F)

## Деплой

Заполни секреты в `infrastructure/prometheus/alertmanager.yml` и запусти:

```bash
  docker-compose up
```

- Frontend: [localhost:80](localhost:80)
- Backend (behind nginx load balancer): [localhost:8080](localhost:8080)
- Prometheus: [localhost:9090](localhost:9090)
- Grafana: [localhost:3000](localhost:3000)


## Документация

https://github.com/anibali/docker-pytorch/tree/master

