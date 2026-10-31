from blood_unit import BloodUnit

class BloodInventory:
    def __init__(self):
        self.units = []

    def add_unit(self):
        print("\n--- إضافة وحدة دم جديدة ---")
        unit_id = input("أدخل رقم وحدة الدم (Unit ID): ")
        blood_type = input("أدخل فصيلة الدم (مثال: O+, A-): ")
        expiration_date = input("أدخل تاريخ الانتهاء (مثال: 2026-12-30): ")
        
        new_unit = BloodUnit(unit_id, blood_type, expiration_date)
        self.units.append(new_unit)
        print("✅ تم إضافة وحدة الدم بنجاح!")

    def display_all_units(self):
        print("\n--- قائمة وحدات الدم الحالية ---")
        if not self.units:
            print(" لا توجد وحدات دم مسجلة حالياً.")
            return
        for unit in self.units:
            unit.display_unit()

    def search_by_blood_type(self):
        print("\n--- البحث عن فصيلة دم ---")
        target = input("أدخل الفصيلة المطلوبة للبحث: ").strip().upper()
        found = False
        for unit in self.units:
            if unit.blood_type == target:
                unit.display_unit()
                found = True
        if not found:
            print(f"❌ عذراً، لا توجد وحدات مطابقة للفصيلة ({target}).")

    def count_units(self):
        print(f"\n إجمالي عدد وحدات الدم المتوفرة في المخزون: {len(self.units)}")

    def check_expiring_units(self):
        print("\n--- اكتشاف الوحدات التي اقترب انتهاء صلاحيتها ---")
        target_date = input("أدخل التاريخ الحالي أو تاريخ المقارنة (مثال: 2026-11-01): ")
        found = False
        for unit in self.units:
            if unit.expiration_date <= target_date:
                print(f" تنبيه: الوحدة رقم {unit.unit_id} (فصيلة {unit.blood_type}) منتهية أو قاربت على الانتهاء بتاريخ {unit.expiration_date}")
                found = True
        if not found:
            print(" جميع الوحدات صالحة ولا توجد وحدات منتهية مطابقة لهذا التاريخ.")