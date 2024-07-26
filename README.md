# Task:
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.
При решении тестового задания у вас не должно возникнуть вопросов. Если появляются вопросы, вероятнее всего, у вас недостаточно знаний.
Задание выложить на гитхаб.

# Django Menu Project

This project demonstrates how to create a dynamic, tree-like menu system in Django. The menu is stored in the database, can be edited via the Django admin interface, and is rendered using a custom template tag.

## Features

1. **Template Tag for Menu Rendering**: The menu is rendered using a custom template tag.
2. **Expanded Menu Items**: All items above the active item are expanded, and the first level of nested items under the active item is also expanded.
3. **Database Storage**: Menu items are stored in the database.
4. **Admin Interface**: Menu items can be edited via the standard Django admin interface.
5. **Active Item Detection**: The active menu item is determined based on the current URL.
6. **Multiple Menus**: Supports multiple menus on a single page, identified by name.
7. **URL Handling**: Menu items can have explicit URLs or use named URLs.
8. **Efficient Database Queries**: Only one database query is made per menu rendering.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/django-menu-project.git
   cd django-menu-project
   ```

2. **Set Up Pipenv**:
   ```bash
   pipenv install
   pipenv shell
   ```

3. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

## Project Structure

### Models

The `MenuItem` model is defined in `menu/models.py`. It includes fields for the title, URL, named URL, parent menu item, and menu name.


### Admin Interface

The `MenuItem` model is registered in the admin interface in `menu/admin.py`.


### Template Tag

A custom template tag `draw_menu` is defined in `menu/templatetags/menu_tags.py`. This tag renders the menu based on the menu name.


### Templates

The menu template `menu/menu.html` is used to render the menu items.


### Views and URLs

Basic views and URL patterns are defined in `menu/views.py` and `menu/urls.py`.


### Main Template

The main template `menu/home.html` includes the menu using the `draw_menu` template tag.


## Usage

1. **Add Menu Items**: Log in to the Django admin interface and add menu items under `Menu items`.
2. **Render Menu**: Use the `{% draw_menu 'menu_name' %}` template tag in your templates to render the menu.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or feedback, please contact(mailto:vsirotkin15@gmail.com).
```

This `README.md` file includes instructions for setting up the project using `pipenv`, making it easier for users who prefer this dependency management tool.
