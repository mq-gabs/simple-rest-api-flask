# Simple RestAPI with Flask

This is a simple RestAPI made with Flask. Currently it is just a CRUD for products. I made it applying concepts of Clean Architecture. It is structured as Entity, Service, Repository and Controller. The Repository has abstraction to allow any DB to be implemented. I also implemented test with 'unittest' for entity, repository and service.

## Product

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "id": {
      "type": "string",
      "format": "uuid"
    },
    "created_at": {
      "type": "string",
      "format": "date-time"
    },
    "updated_at": {
      "type": "string",
      "format": "date-time"
    },
    "deleted_at": {
      "type": ["string", "null"],
      "format": "date-time"
    },
    "name": {
      "type": "string",
      "maxLength": 64
    },
    "description": {
      "type": "string",
      "maxLength": 1500
    },
    "price": {
      "type": "integer",
      "minimum": 0,
      "description": "Price in cents"
    },
    "status": {
      "type": "string",
      "enum": ["AVAILABLE", "UNAVAILABLE"]
    }
  }
}
```

## Endpoints

### POST - `/products`

Register product

#### Body

Requires the properties of [Product](#product) down below:

- name
- description
- price

#### Response

[Product](#product)

### GET - `/products`

List all products

#### Query

```json
{
  "page": {
    "type": "integer",
    "minimum": 0
  },
  "pageSize": {
    "type": "integer",
    "minimum": 0
  }
}
```

#### Response

```json
{
  "list": {
    "type": "array",
    "items": { "type": Product }
  },
  "total": { "type": "integer" }
}
```

### GET - `/products/:id`

Get one product by id

#### Params

- id - UUID

#### Response

[Product](#product)

### PATCH - `/products/:id`

Update product data

#### Params

- id - UUID

#### Body

These are the properties available for update [Product](#product):

- name
- description
- price
- status

#### Response

[Product](#product)

### DELETE - `/products/:id`

Softdelete product

#### Params

- id - UUID

#### Response

```json
{
  "success": { "type": "boolean" },
  "message": { "type": "string" }
}
```

### Error

#### Response

```json
{
  "status_code": { "type": "integer" },
  "message": { "type": "string" },
  "details": { "type": ["string", "object"] }
}
```
