# Test-case-
Тестовые задание для стажировки
Программа представляет собой консольное приложение, которое обеспечивает удобное управление телефонным справочником. Вот более подробное описание ее функционала:

Вывод записей:
Эта функция позволяет просматривать все записи из справочника. Пользователю предоставляется список всех записей с указанием фамилии, имени, отчества, названия организации, рабочего и личного телефона.

Добавление записи:
При выборе этой опции пользователю предлагается ввести новую запись в справочник. При добавлении новой записи запрашиваются следующие данные:

Фамилия
Имя
Отчество
Название организации
Рабочий телефон
Личный телефон
Перед добавлением данных происходит проверка на корректность ввода имени и номера телефона. В случае некорректного ввода, программа предупреждает пользователя и запрашивает ввод данных заново.

Поиск записей:
Эта функция позволяет найти записи в справочнике по заданной строке поиска. При поиске осуществляется проверка наличия введенной строки в любом из полей записи, включая фамилию, имя, отчество, название организации, рабочий телефон и личный телефон. При совпадении частично введенной строки с любым из полей, программа выводит соответствующую запись.

Выход из программы:
Эта опция позволяет завершить работу программы.

Генерация случайных записей:
В программе также реализована возможность генерации случайных записей для тестовых целей. Это делается с помощью функции populate_directory_with_random_data(), которая генерирует 100 случайных записей с помощью библиотеки Faker и записывает их в файл справочника.

Функционал программы базируется на текстовом интерфейсе, что делает ее удобной для использования в командной строке. Она предоставляет базовые, но важные инструменты для управления телефонным справочником, обеспечивая пользователям простой и эффективный способ управления своими контактами.
Пример работы: поиск ![image](https://github.com/muitiiifruckt/Test-case-/assets/101716836/b0545ab7-1f40-4fb7-83aa-92385df6ce17)
вывод записей: ![image](https://github.com/muitiiifruckt/Test-case-/assets/101716836/52f9f54b-e0f4-4e94-8e72-64e3f43e1fd5)
добавление записи: ![image](https://github.com/muitiiifruckt/Test-case-/assets/101716836/c80a16ab-828e-423c-ba70-cdc659d87687)
![image](https://github.com/muitiiifruckt/Test-case-/assets/101716836/57145bb8-edfc-43fd-9ced-0c35bb5a04a2)
выход: ![image](https://github.com/muitiiifruckt/Test-case-/assets/101716836/6d84fb53-d150-4bb1-8cbe-2d7a7108aa91)
 


