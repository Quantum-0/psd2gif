# psd2gif

Данный скрипт представляет из себя консольное приложение для Linux, для быстрого экспортирования слоёв из PSD-файла и преобразования последовательности изображений в GIF-анимацию

## Установка

Для установки достаточно просто запустить скрипт под рутом

Скрипт предложить автоматически установит используемые библиотеки, а затем скопирует себя в /usr/bin для использования в терминале

## Использование

> psd2gif --psd SOURCE \[--gif DESTINATION] \[--delay DELAY] [--onlyvisible]

или

> psd2gif SOURCE \[DESTINATION] \[DELAY] [ONLYVISIBLE]

Где:
* SOURCE - исходный PSD-файл
* DESTINATION - конечный файл GIF-анимации, если не указан, сохраняется как SOURCE с изменением расширения на GIF
* DELAY - задержка между кадрами в милисекундах, если не указано - 10мс
* ONLYVISIBLE - параметр, указывающий, что нужно использовать только видимые слои, невидимые же игнорируются, если не указано - используются все слои

## Примеры использования

> psd2gif test1.psd
>
> psd2gif /home/quantum/Desktop/test2.psd test3.gif
>
> psd2gif test4.psd /home/quantum/Desktop/test5.gif
>
> psd2gif test6.psd test7.gif 2
>
> psd2gif test8.psd --delay 4
>
> psd2gif test9.psd --onlyvisible
>
> psd2gif /home/quantum/Desktop/test10.psd --delay 15 --onlyvisible

## Зависимости

В данном проекте используются:
* Python3
* pip3
* [Fire](https://github.com/google/python-fire)
* [Pillow](https://github.com/python-pillow/Pillow)
* [Psd_tools](https://github.com/psd-tools/psd-tools)

## Цель

Данный скрипт был написан мной с целью получения опыта работы с языком Python, а так же для автоматизации процесса создания анимаций из PSD файлов без использования Adobe Photoshop

## Лицензия

[MIT License](./LICENSE)
