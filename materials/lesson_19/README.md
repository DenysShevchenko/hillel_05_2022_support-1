## <span style="color:green">Materials</span>

## Databases auto serviceos example

Insert into Hackerdraw

```
Table clients {
  id integer
  first_name varchar
  last_name varchar
  email varchar
  created_at timestamp
}

Table parts {
  id integer
  name str
  price float
}

Table services {
  id integer
  name str
}

Table service_has_parts{
  service_id integer
  part_id integer
  amount integer
}

Table orders {
  id integer
  client_id integer
  price float
}

Table order_has_services {
  id integer
  order_id integer
  service_id integer
}

Ref: order_has_services.order_id > orders.id
Ref: order_has_services.service_id > services.id

Ref: subscriptions.user_id > clients.id

Ref: orders.client_id > clients.id
Ref: orders.service_id > services.id

Ref: service_has_parts.service_id > services.id
Ref: service_has_parts.part_id > parts.id
```

### Django admin panel
[Django School](https://www.youtube.com/watch?v=SZ-kPr4Z38A)
[More django admin panel](https://www.youtube.com/watch?v=Sut1s4LdMG0)
[Moooore](https://www.youtube.com/watch?v=aiMvqNaeylY)

**
[Django custom actions](https://www.youtube.com/watch?v=QhCY_v5jHdQ)

### Migrations
[Django docs](https://docs.djangoproject.com/en/4.0/topics/migrations/)
[The net ninja](https://www.youtube.com/watch?v=aOLrEkpGWDg)
[Gosha Dudar](https://www.youtube.com/watch?v=tG1JTn6gs_Q)
