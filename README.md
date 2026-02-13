\# Finance manager loyihasi



Django 6.0.2 asosidagi loyiha. Loyihada Django REST Framework, python-dotenv va bir nechta ilovalar mavjud: `support`, `transactions`, `wallets`.



\## Talablar



\- Python 3.13

\- Django 6.0.2

\- django-cors-headers 4.9.0

\- django-filter 25.2

\- djangorestframework 3.16.1

\- python-dotenv 1.2.1

\- sqlparse 0.5.5

\- tzdata 2025.3



\## Loyiha klonlash



```bash

git clone https://github.com/nijamila/project1.git

cd project1





\## Virtual muhit yaratish



python -m venv venv

\# Windows

.\\venv\\Scripts\\activate

\# Linux/macOS

source venv/bin/activate





\## Talablar paketini o'rnatish



pip install -r requirements.txt





\## .env fayl yaratish



SECRET\_KEY=your-secret-key

DEBUG=True

DATABASE\_URL=sqlite:///db.sqlite3



SECRET\_KEY uchun Django loyihangizdagi maxfiy kalitni ishlating.

DATABASE\_URL misolda SQLite ishlatilgan. Agar boshqa DB bo‘lsa, URL’ni moslashtiring.





\## Ma'lumotlar bazasi migratsiyasi



python manage.py migrate





\## Superuser yaratish



python manage.py createsuperuser





\## Serverni ishga tushirish



python manage.py runserver



Brauzerda admin panelga kirish: http://127.0.0.1:8000/admin/



Admin panel va Support app



apps/support/templates/support ichida HTML shablonlar mavjud.



SupportMessage modeli foydalanuvchi xabarlarini qabul qiladi va javob berish imkonini beradi.



Admin paneldan reply ustunini tahrirlash orqali javob yozish mumkin.



