from django.shortcuts import render


def index(request):
    # Синтетические данные для визуализации (имитация работы паттерна)
    # В реальности эти данные приходили бы из Policy Service и Audit Service
    devices = [
        {
            "name": "Виртуальный сервер БД",
            "ip": "192.168.1.10",
            "status": "Защищен",
            "policy": "Allow: 10.0.0.5, Deny: All",
            "last_audit": "2026-10-02 14:30:00",
            "color": "success",  # Зеленый
        },
        {
            "name": "Виртуальный шлюз",
            "ip": "192.168.1.1",
            "status": "Защищен",
            "policy": "Allow: 10.0.0.0/24, Deny: All",
            "last_audit": "2026-10-02 14:25:00",
            "color": "success",
        },
        {
            "name": "Тестовый стенд",
            "ip": "192.168.1.50",
            "status": "Уязвим (Нет политики)",
            "policy": "Не настроена",
            "last_audit": "2026-10-02 12:00:00",
            "color": "danger",  # Красный
        },
        {
            "name": "Веб-приложение",
            "ip": "192.168.1.20",
            "status": "Защищен",
            "policy": "Allow: 10.0.0.5, Deny: All",
            "last_audit": "2026-10-02 14:35:00",
            "color": "success",
        },
    ]

    # Передаем данные в шаблон
    context = {
        "devices": devices,
        "title": "Мониторинг безопасности виртуальных устройств",
    }
    return render(request, "index.html", context)
