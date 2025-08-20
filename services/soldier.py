class Soldier:
    def __init__(self, ID = None, first_name = '', last_name = '', phone_number = '', rank = ''):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.rank = rank

    @staticmethod
    def from_dict(data: dict) -> "Soldier":
        return Soldier(
            _id=data.get("_id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            phone_number=data.get("phone_number"),
            rank=data.get("rank")
        )

    def to_dict(self) -> dict:
        return {
            "_id": str(self._id) if self._id is not None else None,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "rank": self.rank
        }