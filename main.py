from datetime import datetime, timedelta

# مدة الصلاحية
expiry_days = {
    "milk": 3,
    "egg": 7,
    "tomato": 5,
    "bread": 4,
    "chicken": 2,
    "cheese": 6,
    "apple": 10,
    "juice": 5
}

fridge = []

# 🤖 AI Recipe System
def ai_recipe(items):
    if "milk" in items and "egg" in items:
        return "🥞 Pancakes (milk + eggs)"
    elif "egg" in items and "tomato" in items:
        return "🍳 Omelette with tomatoes"
    elif "bread" in items:
        return "🥪 Sandwich"
    elif "chicken" in items:
        return "🍗 Chicken Meal"
    else:
        return "💡 Mix ingredients into a simple meal"

# ➤ إضافة مكونات
def add_items():
    print("\n➕ Add items (type 'done' to finish)")

    while True:
        item = input("Enter item: ").lower()

        if item == "done":
            break

        if item not in expiry_days:
            print("⚠ Unknown item → default expiry = 5 days")
            days = 5
        else:
            days = expiry_days[item]

        fridge.append((item, datetime.now(), days))
        print(f"✔ Added {item}")

# ➤ عرض الثلاجة
def show_fridge():
    print("\n📦 YOUR FRIDGE ITEMS:")
    for item, date, days in fridge:
        print(f"- {item} | expiry: {days} days")

# ➤ التحليل الذكي (المهم)
def analyze():
    print("\n🧊 SMART FRIDGE ANALYSIS")
    print("=" * 45)

    today = datetime.now()

    items_only = []
    urgent_items = []
    status_list = []

    for item, date_added, days in fridge:
        expire_date = date_added + timedelta(days=days)
        days_left = (expire_date - today).days

        items_only.append(item)
        status_list.append((item, days_left))

        # 🔥 تنبيهات واضحة
        if days_left <= 0:
            print(f"❌ {item.upper()} → EXPIRED")
        elif days_left <= 1:
            print(f"⚠ {item.upper()} → EXPIRES TOMORROW")
            urgent_items.append(item)
        elif days_left <= 2:
            print(f"🟠 {item} → Use soon ({days_left} days left)")
        else:
            print(f"✔ {item} → safe ({days_left} days left)")

    # 📊 ترتيب حسب الأقرب انتهاء
    print("\n📊 PRIORITY LIST (Most urgent first):")
    status_list.sort(key=lambda x: x[1])

    for item, days in status_list:
        print(f"- {item} ({days} days left)")

    # 🤖 AI suggestion
    print("\n🤖 AI RECIPE SUGGESTION:")
    if urgent_items:
        print(ai_recipe(urgent_items))
    else:
        print(ai_recipe(items_only))

    print("\n💡 Tip: Use urgent items first to reduce food waste!")

# ➤ MENU
while True:
    print("\n" + "=" * 45)
    print("🧊 SMART FRIDGE AI SYSTEM")
    print("=" * 45)
    print("1 - Add Items")
    print("2 - Show Fridge")
    print("3 - Analyze AI System")
    print("4 - Exit")

    choice = input("\nChoose: ")

    if choice == "1":
        add_items()
    elif choice == "2":
        show_fridge()
    elif choice == "3":
        analyze()
    elif choice == "4":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid option")
