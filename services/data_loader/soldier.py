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
            ID=data.get("_id"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            phone_number=data.get("phone_number"),
            rank=data.get("rank")
        )

    def to_dict(self) -> dict:
        result = {}
        if self.ID:
            result["_id"] = str(self.ID)
        result["first_name"] = self.first_name
        result["last_name"] = self.last_name
        result["phone_number"] = self.phone_number
        result["rank"] = self.rank
        return result
