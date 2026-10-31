class BloodUnit:
    def __init__(self, unit_id, blood_type, expiration_date):
        self.unit_id = unit_id
        self.blood_type = blood_type.upper()
        self.expiration_date = expiration_date

    def display_unit(self):
        print(f"رقم الوحدة: {self.unit_id} | الفصيلة: {self.blood_type} | تاريخ الصلاحية: {self.expiration_date}")