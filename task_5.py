"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

yandex = ['ping', 'yandex.ru']
ya_p = subprocess.Popen(yandex, stdout=subprocess.PIPE)
print('yandex.ru')
for line in ya_p.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

youtube = ['ping', 'youtube.com']
yo_p = subprocess.Popen(youtube, stdout=subprocess.PIPE)
print('youtube.com')
for line in yo_p.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))