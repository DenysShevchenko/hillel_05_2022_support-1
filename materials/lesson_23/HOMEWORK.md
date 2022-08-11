## <span style="color:green">Homework</span>

### EN:

Update API function below
```python
@api_view(["GET"])
def get_ticket(request, id_: int):
    tickets = Ticket.objects.get(id=id_)
    data = TicketSerializer(tickets).data
    return Response(data=data)
```

Now it called different and accept more HTTP methods
```python
@api_view(["GET", "PUT", "DELETE"])
retrieve_update_delete_ticket(request, id_: int):
    ...
```

#### TODO:
Realize the body of a new function that can:
- Update ticket's theme or description if customer do a PUT request
- Delete ticket if customer do a DELETE request
- urls.py is updated


### UA:

Оновіть функцію API нижче
```python
@api_view(["GET"])
def get_ticket(request, id_: int):
    tickets = Ticket.objects.get(id=id_)
    data = TicketSerializer(tickets).data
    return Response(data=data)
```

Тепер ф-ція приймає більше методів HTTP
```python
@api_view(["GET", "PUT", "DELETE"])
retrieve_update_delete_ticket(request, id_: int):
    ...
```

#### TODO:
Реалізуйте тіло нової функції, яка:
- Оновлює тему або опис ticket-a, якщо клієнт виконує запит PUT
- Видаляє заявку, якщо клієнт виконує запит DELETE
- urls.py оновлено


