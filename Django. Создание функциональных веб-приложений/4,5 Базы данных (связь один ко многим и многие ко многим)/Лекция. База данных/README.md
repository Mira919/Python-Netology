
# База данных

## Основные измнениния в файлах:
* settings.py, urls.py (Добавлен DebugToolBar, в urls.py - добавлено хэширование)
### Приложение app (владелец автомобиля и автомобиль):
* models.py (добавление модели Person - владелец автомобиля, Car - автомобиль)

* admin.py (добавление таблиц владелец автомобиля и автомобиль и студентов в админку)
 
### Приложение students (связь многие ко многим, курсы и студенты):
* list.html (HTML шаблон, у каждого студента выводятся курсы на которые он записан)

* admin.py (добавление курсов и студентов в админку)

* models.py (создание моделей курсов и студентов для БД)

* views.py (основная функция которая возвращает HTML страницу и данные в ней, хэширование в функции)


