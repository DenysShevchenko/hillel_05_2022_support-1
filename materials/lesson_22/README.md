## <span style="color:green">Materials</span>
- [Indian guy](https://www.youtube.com/watch?v=o4wGagkfWoY)
- [Serializer relations](https://www.django-rest-framework.org/api-guide/relations/)
- [Nested serializers in DRF](https://blog.devgenius.io/nested-serializers-in-django-rest-framework-6b36bf011074)
- [Many-to-many nested serializers](https://stackoverflow.com/questions/17256724/include-intermediary-through-model-in-responses-in-django-rest-framework/17263583#17263583)
- [Another example of nested serializers](https://testdriven.io/tips/70e2a285-5f58-4358-a151-1b445b192e9a/)


### Lesson example

```python
from dataclasses import asdict, dataclass
from enum import Enum
from pprint import pprint as print


# NOTE: Create an Enum class instead of using dict
class Mealplan(str, Enum):
    AI = "AI"
    BO = "BO"
    BL = "BL"
    BD = "BD"
    RO = "RO"
    RR = "RR"

    @classmethod
    def values(cls) -> list[str]:
        return [el for el in cls]


@dataclass
class Coordinates:
    lat: float
    lng: float

    def __post_init__(self):
        self._validate_lat()
        self._validate_lng()

    def _validate_lng(self):
        if -90 <= self.lng <= 90:
            return
        raise ValueError("Longitude must be in range (-90, 90) ")

    def _validate_lat(self):
        if -180 <= self.lat <= 180:
            return
        raise ValueError("Latitude must be in range (-180, 180) ")


@dataclass
class AddressInfo:
    country: str
    city: str
    address: str
    coordinates: Coordinates


@dataclass
class LuxaryInfo:
    spa_exist: bool
    pool_exist: bool
    rest_exist: bool


@dataclass
class Hotel:
    name: str
    code: int
    rate: int
    phone: str
    mealplan: str
    square: float
    address: AddressInfo
    luxary_info: LuxaryInfo

    def __post_init__(self):
        self._validate_rate()
        self._validate_mealplan()

    def _validate_mealplan(self) -> None:
        allowed_values: list[str] = Mealplan.values()
        if self.mealplan not in allowed_values:
            raise ValueError(f"mealplan could be a value from list: {allowed_values}")

    def _validate_rate(self) -> None:
        if self.rate > 5:
            raise ValueError("Rate could be 5 or less")


# NOTE: Create hotel data model
# grant_dolphin = Hotel(
#     name="Grant dolphin",
#     code=123,
#     address=AddressInfo(
#         country="USA",
#         city="New York",
#         address="Bla bla street 2",
#         coordinates=Coordinates(
#             lat=180,
#             lng=-80,
#         ),
#     ),
#     luxary_info=LuxaryInfo(
#         spa_exist=True,
#         pool_exist=True,
#         rest_exist=False,
#     ),
#     rate=4,
#     phone="+11232431432",
#     mealplan="AI",
#     square=500.5,
# )

# NOTE: Payload for future deserealization
data = {
    "address": {
        "address": "Bla bla street 2",
        "city": "New York",
        "coordinates": {"lat": 180, "lng": -80},
        "country": "USA",
    },
    "code": 123,
    "luxary_info": {"pool_exist": True, "rest_exist": False, "spa_exist": True},
    "mealplan": "AI",
    "name": 12,
    "phone": "+11232431432",
    "rate": 4,
    "square": 500.5,
}

# NOTE: Create hotel model base on dict payload (use unpack here)
new_hotel = Hotel(**data)

print(new_hotel)
```
