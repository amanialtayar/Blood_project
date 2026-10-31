from inventory_manager import BloodInventory

def main():
    manager = BloodInventory()

    while True:
        print("\n==========================================")
        print(" نظام إدارة وحدات الدم المصغر (Blood Bank) ")
        print("==========================================")
        print("1. إضافة وحدة دم")
        print("2. عرض الوحدات")
        print("3. البحث عن فصيلة")
        print("4. حساب عدد الوحدات")
        print("5. اكتشاف الوحدات التي اقترب انتهاء صلاحيتها")
        print("6. خروج")

        choice = input("اختر العملية (1-6): ").strip()

        if choice == '1':
            manager.add_unit()
        elif choice == '2':
            manager.display_all_units()
        elif choice == '3':
            manager.search_by_blood_type()
        elif choice == '4':
            manager.count_units()
        elif choice == '5':
            manager.check_expiring_units()
        elif choice == '6':
            print("\n👋 تم إغلاق النظام بنجاح. بالتوفيق يا مهندسة!")
            break
        else:
            print("❌ اختيار غير صحيح، يرجى إدخال رقم بين 1 و 6.")

if __name__ == "__main__":
    main()