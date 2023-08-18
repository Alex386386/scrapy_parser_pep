# ЯП - Спринт 19 - Проект парсинга: асинхронный парсер PEP.

### Описание

Проект Парсера который написанного на scrapy, собирающего данные о документах PEP и парсит их в два csv файла.
Один из документов включает название документа, номер документа и его статус, второй же собирает данные о количествах документов определённого статуса.

## Stack

Python 3.8, Scrapy 2.5.1

### Установка, Как запустить проект:
https://github.com/Alex386386/scrapy_parser_pep
Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:Alex386386/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Для запуска парсинга и получения результатов, введите команду:

```
scrapy crawl pep
```

Автор:
- [Александр Мамонов](https://github.com/Alex386386) 