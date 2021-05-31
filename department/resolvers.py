from typing import Tuple, Type

from django.db.models import Model

from department.exceptions import SubjectException
from department.models import (
    Strazacy, UwagaStrazacy, Sprzet, UwagaSprzet, Uslugi, UwagaUslugi, Pojazdy, UwagaPojazdy,
    PrzegladPojazdy, PrzegladSprzet, UwagaPrzegladSprzet, UwagaPrzegladPojazdy
)


class SubjectResolver:
    SUBJECT_MAPPER = {
        "firefigher": (Strazacy, UwagaStrazacy),
        "equipment": (Sprzet, UwagaSprzet),
        "service": (Uslugi, UwagaUslugi),
        "vehicle": (Pojazdy, UwagaPojazdy),
        "history_vehicle": (PrzegladPojazdy, UwagaPrzegladPojazdy),
        "history_equipment": (PrzegladSprzet, UwagaPrzegladSprzet),
    }

    def resolve(self, name) -> Tuple[Type[Model], Type[Model]]:
        if name not in self.SUBJECT_MAPPER:
            raise SubjectException()
        return self.SUBJECT_MAPPER.get(name)
