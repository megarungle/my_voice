# <img src="docs/logo.png" alt="Logo" style="width: 30px; height: 30px;"> my_voice

Проект по машинному обучению на хакатон

## TOC

- [Окружение](#окружение)
- [Ручные запуски](#%D1%80%D1%83%D1%87%D0%BD%D1%8B%D0%B5-%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA%D0%B8)
  - [Backend](#backend)
  - [Frontend](#fro)
  - [Infer](#тестовый-инфер)
- [Деплой](#%D0%B4%D0%B5%D0%BF%D0%BB%D0%BE%D0%B9)
- [Инфраструктура](#%D0%B8%D0%BD%D1%84%D1%80%D0%B0%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0)

## Окружение

python3.10  
WSL2 Ubuntu с Docker Desktop

## Ручные запуски

### Backend

```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend

Открыть `index.html` из папки `frontend`

### Тестовый инфер

```bash
cd backend
pip install -r requirements.txt
python views.py
```

## Деплой

Список доступных снаружи сервисов:

- Frontend (через nginx): [localhost:80](localhost:80)
- Backend (behind nginx load balancer): [localhost:8080](localhost:8080)
- Prometheus: [localhost:9090](localhost:9090)
- Grafana: [localhost:3000](localhost:3000)

Список внутренних сервисов недоступных снаружи:

- Alertmanager
- Nginx Exporter

### С мониторингом

Заполни секреты в `infrastructure/prometheus/alertmanager.yml` и запусти:

```bash
  docker-compose -f docker-compose.yaml up
```

### Без мониторинга

Отсутствуют Grafana, Prometheus и связанные с ними внутренний сервисы (алерт менеджер, nginx экспортер)

```bash
  docker-compose -f docker-compose-no-monitoring.yaml up
```

## Инфраструктура

<img src="docs/infrastructure.svg">
