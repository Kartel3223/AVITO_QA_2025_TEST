
## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## Reproducer: POST /api/1/item постоянно возвращает 400

Steps to reproduce:
- Отправить POST `https://qa-internship.avito.com/api/1/item` с заголовками `Content-Type: application/json` и `Accept: application/json` и телом (пример):

```json
{
	"sellerID": 901008,
	"name": "Autotest seller items 0",
	"price": 3000,
	"statistics": {"likes": 0, "viewCount": 0, "contacts": 0}
}
```

Observed result:
- HTTP 400. Responses observed include both:
	- {"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}
	- {"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Notes:
- Tests attempted multiple payload variants (raw bytes, `sellerId` key, `sellerID` as string, removing `statistics`, `statistics` as array, statistics values as strings, and requests with/without `charset=utf-8`) — все варианты вернули 400. Логи попыток выше в этом файле.
- Похоже, контракт в API либо неконсистентен, либо сервер ожидает иную форму тела (например, обёртку, multipart или иное), поэтому просьба к бэкенду: проверить валидацию поля `statistics.likes` и формат принимаемого JSON.

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## Create item failed (400)

All POST attempts failed for https://qa-internship.avito.com/api/1/item
Initial status: 400
Initial body: {"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}



-- Request body --
{"sellerID": 589906, "name": "Autotest item", "price": 1000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}



---

## Create item failed (400)

All POST attempts failed for https://qa-internship.avito.com/api/1/item
Initial status: 400
Initial body: {"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}



-- Request body --
{"sellerID": 966195, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}



---

## Create item failed (400)

All POST attempts failed for https://qa-internship.avito.com/api/1/item
Initial status: 400
Initial body: {"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}



-- Request body --
{"sellerID": 628900, "name": "Autotest item", "price": 1000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}



---

## Create item failed (400)

All POST attempts failed for https://qa-internship.avito.com/api/1/item
Initial status: 400
Initial body: {"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}



-- Request body --
{"sellerID": 813229, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}



---

## Create item failed after attempts

Final failure for POST https://qa-internship.avito.com/api/1/item
Attempt 1: request={"sellerID": 313758, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 2: request=raw-json-bytes -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 3: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}, "sellerId": 313758} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 4: request={"sellerID": "313758", "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 5: request={"sellerID": 313758, "name": "Autotest seller items 0", "price": 3000} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 6: request={"sellerID": 313758, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 7: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}, "sellerId": 313758} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}


-- Request body --
{"sellerID": 313758, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## Create item failed after attempts

Final failure for POST https://qa-internship.avito.com/api/1/item
Attempt 1: request={"sellerID": 901008, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 2: request=raw-json-bytes -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 3: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}, "sellerId": 901008} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 4: request={"sellerID": "901008", "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 5: request={"sellerID": 901008, "name": "Autotest seller items 0", "price": 3000} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 6: request={"sellerID": 901008, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 7: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}, "sellerId": 901008} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 8: request={"no_charset": true, "sellerID": 901008, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 9: request={"sellerID": 901008, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": 0, "viewCount": 0, "contacts": 0}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 10: request={"sellerID": 901008, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": "0", "viewCount": "0", "contacts": "0"}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}


-- Request body --
{"sellerID": 901008, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## Create item failed after attempts

Final failure for POST https://qa-internship.avito.com/api/1/item
Attempt 1: request={"sellerID": 711351, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 2: request=raw-json-bytes -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 3: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}, "sellerId": 711351} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 4: request={"sellerID": "711351", "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 5: request={"sellerID": 711351, "name": "Autotest seller items 0", "price": 3000} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 6: request={"sellerID": 711351, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 7: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}, "sellerId": 711351} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 8: request={"no_charset": true, "sellerID": 711351, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 9: request={"sellerID": 711351, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": 0, "viewCount": 0, "contacts": 0}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 10: request={"sellerID": 711351, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": "0", "viewCount": "0", "contacts": "0"}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}


-- Request body --
{"sellerID": 711351, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## Create item failed after attempts

Final failure for POST https://qa-internship.avito.com/api/1/item
Attempt 1: request={"sellerID": 480179, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 2: request=raw-json-bytes -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 3: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}, "sellerId": 480179} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 4: request={"sellerID": "480179", "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 5: request={"sellerID": 480179, "name": "Autotest seller items 0", "price": 3000} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 6: request={"sellerID": 480179, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 7: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}, "sellerId": 480179} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 8: request={"no_charset": true, "sellerID": 480179, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 9: request={"sellerID": 480179, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": 0, "viewCount": 0, "contacts": 0}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 10: request={"sellerID": 480179, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": "0", "viewCount": "0", "contacts": "0"}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 11: request={"item": {"sellerID": 480179, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}} -> status=400 body={"result":{"message":"поле name обязательно","messages":{}},"status":"400"}

Attempt 12: request=multipart-json-file -> status=400 body={"message":"invalid content type","code":400}

Attempt 13: request=form-urlencoded-payload -> status=400 body={"message":"invalid content type","code":400}

Attempt 14: request=text-plain-json -> status=400 body={"message":"invalid content type","code":400}


-- Request body --
{"sellerID": 480179, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## Create item failed after attempts

Final failure for POST https://qa-internship.avito.com/api/1/item
Attempt 1: request={"sellerID": 966357, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 2: request=raw-json-bytes -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 3: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}, "sellerId": 966357} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 4: request={"sellerID": "966357", "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 5: request={"sellerID": 966357, "name": "Autotest seller items 0", "price": 3000} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 6: request={"sellerID": 966357, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 7: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}, "sellerId": 966357} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 8: request={"no_charset": true, "sellerID": 966357, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 9: request={"sellerID": 966357, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": 0, "viewCount": 0, "contacts": 0}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 10: request={"sellerID": 966357, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": "0", "viewCount": "0", "contacts": "0"}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 11: request={"item": {"sellerID": 966357, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}} -> status=400 body={"result":{"message":"поле name обязательно","messages":{}},"status":"400"}

Attempt 12: request=multipart-json-file -> status=400 body={"message":"invalid content type","code":400}

Attempt 13: request=form-urlencoded-payload -> status=400 body={"message":"invalid content type","code":400}

Attempt 14: request=text-plain-json -> status=400 body={"message":"invalid content type","code":400}


-- Request body --
{"sellerID": 966357, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## Create item failed after attempts

Final failure for POST https://qa-internship.avito.com/api/1/item
Attempt 1: request={"sellerID": 778291, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 2: request=raw-json-bytes -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 3: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}, "sellerId": 778291} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 4: request={"sellerID": "778291", "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 5: request={"sellerID": 778291, "name": "Autotest seller items 0", "price": 3000} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 6: request={"sellerID": 778291, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 7: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}, "sellerId": 778291} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 8: request={"no_charset": true, "sellerID": 778291, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 9: request={"sellerID": 778291, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": 0, "viewCount": 0, "contacts": 0}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 10: request={"sellerID": 778291, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": "0", "viewCount": "0", "contacts": "0"}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 11: request={"item": {"sellerID": 778291, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}} -> status=400 body={"result":{"message":"поле name обязательно","messages":{}},"status":"400"}

Attempt 12: request=multipart-json-file -> status=400 body={"message":"invalid content type","code":400}

Attempt 13: request=form-urlencoded-payload -> status=400 body={"message":"invalid content type","code":400}

Attempt 14: request=text-plain-json -> status=400 body={"message":"invalid content type","code":400}


-- Request body --
{"sellerID": 778291, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---

## Create item failed after attempts

Final failure for POST https://qa-internship.avito.com/api/1/item
Attempt 1: request={"sellerID": 937828, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 2: request=raw-json-bytes -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 3: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}, "sellerId": 937828} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 4: request={"sellerID": "937828", "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 5: request={"sellerID": 937828, "name": "Autotest seller items 0", "price": 3000} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 6: request={"sellerID": 937828, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 7: request={"name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": "0", "viewCount": "0", "contacts": "0"}, "sellerId": 937828} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 8: request={"no_charset": true, "sellerID": 937828, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}} -> status=400 body={"result":{"message":"поле likes обязательно","messages":{}},"status":"400"}

Attempt 9: request={"sellerID": 937828, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": 0, "viewCount": 0, "contacts": 0}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 10: request={"sellerID": 937828, "name": "Autotest seller items 0", "price": 3000, "statistics": [{"likes": "0", "viewCount": "0", "contacts": "0"}]} -> status=400 body={"result":{"message":"","messages":{}},"status":"не передано тело объявления"}

Attempt 11: request={"item": {"sellerID": 937828, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}} -> status=400 body={"result":{"message":"поле name обязательно","messages":{}},"status":"400"}

Attempt 12: request=multipart-json-file -> status=400 body={"message":"invalid content type","code":400}

Attempt 13: request=form-urlencoded-payload -> status=400 body={"message":"invalid content type","code":400}

Attempt 14: request=text-plain-json -> status=400 body={"message":"invalid content type","code":400}


-- Request body --
{"sellerID": 937828, "name": "Autotest seller items 0", "price": 3000, "statistics": {"likes": 0, "viewCount": 0, "contacts": 0}}

-- Request headers --
{"Content-Type": "application/json; charset=utf-8", "Accept": "application/json"}

---

## API returned 400 for POST https://qa-internship.avito.com/api/1/item

Request: POST https://qa-internship.avito.com/api/1/item
Status: 400
Body:
{"result":{"message":"","messages":{}},"status":"не передано тело объявления"}



---
