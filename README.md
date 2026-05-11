# سیستم سفارش غذای رستوران

این پروژه با زبان Python و با هدف پیاده‌سازی و درک مفاهیم برنامه‌نویسی شی‌گرا (OOP) و الگوهای طراحی (Design Patterns) توسعه داده شده است.

در این پروژه چند الگوی طراحی مهم به‌صورت عملی پیاده‌سازی شده‌اند:

- Singleton Pattern
- Factory Method Pattern
- Abstract Factory Pattern
- Builder Pattern

---

# قابلیت‌های پروژه

- ساخت انواع غذا با Factory Method
- ساخت پکیج‌های غذایی اقتصادی و لوکس با Abstract Factory
- ساخت مرحله‌ای سفارش‌ها با Builder
- مدیریت مرکزی سفارش‌ها با Singleton
- پشتیبانی از چند روش پرداخت
- پشتیبانی از چند روش اعلان (Notification)
- تست واحد (Unit Test)
- معماری ماژولار و قابل توسعه

---

# ساختار پروژه

```text
food_order_system/
│
├── main.py
├── requirements.txt
├── README.md
│
├── models/
│   ├── __init__.py
│   ├── food.py
│   ├── payment.py
│   ├── notification.py
│   └── order.py
│
├── patterns/
│   ├── __init__.py
│   ├── singleton.py
│   ├── factory_method.py
│   ├── abstract_factory.py
│   └── builder.py
│
└── tests/
    ├── __init__.py
    ├── test_singleton.py
    ├── test_factory.py
    ├── test_abstract_factory.py
    ├── test_builder.py
    └── run_tests.py
```

---

# الگوهای طراحی استفاده‌شده

## 1. Singleton Pattern

### استفاده در:
- RestaurantManager

### هدف:
اطمینان از اینکه فقط یک نمونه از مدیر رستوران در کل برنامه وجود داشته باشد.

### مزایا:
- مدیریت مرکزی سفارش‌ها
- جلوگیری از ساخت نمونه‌های اضافی
- اشتراک داده‌ها بین بخش‌های مختلف سیستم

---

## 2. Factory Method Pattern

### استفاده در:
- ساخت غذاها

### هدف:
جدا کردن منطق ساخت object از بخش استفاده‌کننده.

### مزایا:
- کاهش وابستگی (Coupling)
- توسعه آسان
- اضافه کردن غذاهای جدید بدون تغییر سیستم اصلی

---

## 3. Abstract Factory Pattern

### استفاده در:
- ساخت پکیج‌های غذایی

### هدف:
ایجاد خانواده‌ای از objectهای سازگار.

### مزایا:
- جلوگیری از ترکیب ناسازگار
- حفظ هماهنگی بین اجزای پکیج
- توسعه‌پذیری بالا

---

## 4. Builder Pattern

### استفاده در:
- ساخت سفارش‌ها

### هدف:
ساخت مرحله‌به‌مرحله objectهای پیچیده.

### مزایا:
- خوانایی بهتر
- جلوگیری از constructorهای پیچیده
- انعطاف بالا در ساخت سفارش

---

# کلاس‌های اصلی پروژه

| کلاس | توضیح |
|---|---|
| RestaurantManager | مدیریت سفارش‌ها (Singleton) |
| Food | کلاس انتزاعی غذا |
| Pizza / Burger / Salad | انواع غذا |
| FoodFactory | کارخانه ساخت غذا |
| MealPackageFactory | کارخانه ساخت پکیج |
| OrderBuilder | سازنده سفارش |
| Payment | سیستم پرداخت |
| Notification | سیستم اعلان |

---

# روش‌های پرداخت

پروژه از چند روش پرداخت پشتیبانی می‌کند:

- پرداخت آنلاین
- پرداخت نقدی

---

# روش‌های اعلان

پروژه از چند روش اعلان پشتیبانی می‌کند:

- پیامک (SMS)
- ایمیل (Email)

---

# نحوه اجرای پروژه

ابتدا وارد پوشه پروژه شوید:

```bash
cd food_order_system
```

سپس برنامه را اجرا کنید:

```bash
python main.py
```

---

# اجرای تست‌ها

برای اجرای تمام تست‌ها:

```bash
python -m unittest discover tests
```

یا:

```bash
python tests/run_tests.py
```

---

# نمونه خروجی تست‌ها

```text
Ran 18 tests

OK
```

---

# پیش‌نیازها

- Python 3.10 یا بالاتر

---

# مفاهیم شی‌گرایی استفاده‌شده

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

# مزایای معماری پروژه

- کد تمیز و ماژولار
- توسعه آسان
- قابلیت تست بالا
- کاهش وابستگی بین بخش‌ها
- نگهداری ساده‌تر

---

# نویسنده

پروژه درس سیستم های شی گرا فاطمه الیاسی