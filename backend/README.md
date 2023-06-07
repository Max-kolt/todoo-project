Для запуска:
---
1. Рекомендуется иметь python версии 3.11.1
2. Прописать:
    >   pip install -r requirements.txt 
    
3. В базее данных создать юзера:
   1. name: test_user
   2. пароль: qwerty
4. Создать базу данных:
   1. host: localhost
   2. port: 5432
   3. name: test_db
5. В консоли проекта прописать:
    >alembic revision --autogenerate -m 'Inittial migration'
6. В директории migrations/versions найти новую версию, удостовериться,что сценарии готовы и написать:
   > import sqlmodel
7. В консоли:
   > alembic stamp head
   ---
   > python main.py

Backend готов к работе
---
Переходи по ссылке: http://127.0.0.1:8080/docs#

   
