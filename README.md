# API Tests

Запуск автоматизированных тестов для сервиса объявлений.

Требования
- Python 3.8+
- Установлены зависимости из `requirements.txt` (pytest, requests)

Запуск локально (PowerShell):

```powershell
python -m pip install -r requirements.txt
pytest -q -m battle
```

- Чтобы запустить все тесты: `pytest -q`
- Поменять базовый URL: `env:BASE_URL = 'https://qa-internship.avito.com' ; pytest -q`
# AVITO_QA_2025_TEST
Если вы зашли сюда - вероятно вы хотите посмотреть выполнение тестового задания для стажировки в Авито или вы ревьювер. Добро пожаловть.
