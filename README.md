Task_1. 
- Судя по документации, если формат не указан в параметрах, то по умолчанию ответ на запрос в формате html. 
Тест "test_format_default_html" выполняет на это проверку, но получает формат xml. Бага в документации или в реализации.
https://nominatim.org/release-docs/develop/api/Reverse/#output-format

Task_3.
- Требуемая OS: Unix подобная. 
- На ней должен присутствовать Python 3 или имя исполняемого файла требуется передать в тест через параметр python3.
- Логирование из потока посылки не осуществляется, т.к, согласно документации, Robot framework для этого не предназначен.
