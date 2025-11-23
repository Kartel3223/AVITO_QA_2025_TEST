import random
import pytest
import requests

# Базовый адрес сервиса
BASE_URL = "https://qa-internship.avito.com"

# Пути к ручкам API v1 из Postman-коллекции
ITEM_PATH = "/api/1/item"
STAT_PATH = "/api/1/statistic"


@pytest.fixture
def base_url():
    """Базовый URL сервиса."""
    return BASE_URL


@pytest.fixture
def seller_id():
    """Генерирует sellerID в допустимом диапазоне."""
    return random.randint(111111, 999999)


@pytest.fixture
def default_headers():
    """Стандартные заголовки, как в Postman."""
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


@pytest.fixture
def create_item(base_url, default_headers):
    """
    Фикстура-хелпер для создания объявления.
    Использование в тесте:
        resp = create_item(payload)
    """
    def _create_item(payload: dict):
        url = base_url + ITEM_PATH
        response = requests.post(
            url,
            json=payload,           # ВАЖНО: json=payload, а не data=...
            headers=default_headers,
            timeout=5,
        )
        return response

    return _create_item


def test_create_item_success(seller_id, create_item):
    """
    Позитивный тест:
    создаём объявление и проверяем, что вернулся 200 и нужные поля.
    """
    payload = {
        "sellerID": seller_id,
        "name": "Autotest item",
        "price": 1000,
        "statistics": {
            "likes": 0,
            "viewCount": 0,
            "contacts": 0
        }
    }

    response = create_item(payload)

    assert response.status_code == 200, (
        f"Ожидался 200, а пришло {response.status_code}. Body: {response.text}"
    )

    body = response.json()

    assert "id" in body
    assert "sellerId" in body
    assert "name" in body
    assert "price" in body
    assert "statistics" in body

    assert body["sellerId"] == seller_id
    assert body["name"] == payload["name"]
    assert body["price"] == payload["price"]


def test_get_item_by_id(base_url, seller_id, create_item):
    """
    Создаём объявление, потом получаем его по id.
    """
    payload = {
        "sellerID": seller_id,
        "name": "Autotest get-by-id",
        "price": 2000,
        "statistics": {
            "likes": 1,
            "viewCount": 2,
            "contacts": 3
        }
    }

    create_response = create_item(payload)
    assert create_response.status_code == 200, (
        f"Создание объявления не удалось: {create_response.status_code}, {create_response.text}"
    )

    created_body = create_response.json()
    item_id = created_body["id"]

    get_url = base_url + ITEM_PATH + "/" + str(item_id)
    get_response = requests.get(get_url, timeout=5)

    assert get_response.status_code == 200, (
        f"Ожидался 200 при GET, а пришло {get_response.status_code}. Body: {get_response.text}"
    )

    body = get_response.json()

    if isinstance(body, list):
        assert len(body) > 0
        item = body[0]
    else:
        item = body

    assert item["id"] == item_id
    assert item["sellerId"] == seller_id
    assert item["name"] == payload["name"]
    assert item["price"] == payload["price"]


def test_get_items_by_seller(base_url, seller_id, create_item):
    """
    Создаём несколько объявлений для одного sellerID,
    потом забираем список объявлений по этому sellerID.
    """
    created_ids = []

    for i in range(3):
        payload = {
            "sellerID": seller_id,
            "name": f"Autotest seller items {i}",
            "price": 3000 + i,
            "statistics": {
                "likes": i,
                "viewCount": i * 10,
                "contacts": i * 2
            }
        }

        response = create_item(payload)
        assert response.status_code == 200, (
            f"Создание объявления {i} не удалось: {response.status_code}, {response.text}"
        )

        body = response.json()
        created_ids.append(body["id"])

    get_url = base_url + f"/api/1/{seller_id}/item"
    get_response = requests.get(get_url, timeout=5)

    assert get_response.status_code == 200, (
        f"Ожидался 200 при GET /api/1/{seller_id}/item, а пришло {get_response.status_code}. Body: {get_response.text}"
    )

    body = get_response.json()
    assert isinstance(body, list), f"Ожидался список, а пришло: {type(body)}"

    returned_ids = [item["id"] for item in body]
    for cid in created_ids:
        assert cid in returned_ids, f"Объявление с id {cid} не найдено в списке продавца"

    for item in body:
        assert item["sellerId"] == seller_id


def test_get_statistics_for_item(base_url, seller_id, create_item):
    """
    Создаём объявление, потом запрашиваем статистику по его id.
    """
    payload = {
        "sellerID": seller_id,
        "name": "Autotest statistics",
        "price": 4000,
        "statistics": {
            "likes": 5,
            "viewCount": 10,
            "contacts": 2
        }
    }

    create_response = create_item(payload)
    assert create_response.status_code == 200, (
        f"Создание объявления не удалось: {create_response.status_code}, {create_response.text}"
    )

    created_body = create_response.json()
    item_id = created_body["id"]

    stat_url = base_url + STAT_PATH + "/" + str(item_id)
    stat_response = requests.get(stat_url, timeout=5)

    assert stat_response.status_code == 200, (
        f"Ожидался 200 при GET статистики, а пришло {stat_response.status_code}. Body: {stat_response.text}"
    )

    body = stat_response.json()

    assert isinstance(body, list), f"Ожидался список, а пришло: {type(body)}"

    if len(body) > 0:
        stat = body[0]
        assert "likes" in stat
        assert "viewCount" in stat
        assert "contacts" in stat
