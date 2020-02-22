import telebot
from collections import Counter


def separator(arr):
    return list(map(float, arr.split()))


def average_calc(arr):
    return sum_calc(arr) / len(arr)


def variants_calc(arr):
    variants_arr = []
    for elem in arr:
        if elem in variants_arr:
            continue
        else:
            variants_arr.append(elem)
    return variants_arr


def sum_calc(arr):
    s = 0
    for elem in arr:
        s += elem
    return s


def median_calc(arr):
    if len(arr) % 2 != 0:
        return arr[len(arr) // 2]
    elif len(arr) == 2:
        return (arr[0] + arr[1]) / 2
    else:
        first = arr[len(arr) // 2]
        second = arr[(len(arr) // 2) + 1]
        return average_calc([first, second])


def freq_calc(arr):
    counter = Counter(arr)
    return counter.most_common()


token = "1080937575:AAGXm11nvy6dTHklrDyE6BQuVi3iG21zogg"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "КУ, МЕНЯ СОЗДАЛ ЭМИЛЬ, Я ДЕЛАЮ ЕГО ДОМАШКУ ПО СТАТИСТИКЕ")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Числа отправлять, разделяя пробелом, в качестве разделения целой части и "
                                      "дробной использовать точку. В частоте возвращается кортеж из списков, "
                                      "которые состоят из двух чисел, первое - варианта, второе - ее частота")


@bot.message_handler(content_types=["text"])
def reply(message):
    try:
        array = separator(message.text)
        array.sort()
    except BaseException:
        bot.send_message(message.chat.id, "АЩИПКА")
    else:
        bot.send_message(message.chat.id, "Отсортированный в порядке неубывания список - {0}".format(str(array)))
        bot.send_message(message.chat.id, "Сумма - {0}".format(str(sum_calc(array))))
        bot.send_message(message.chat.id, "Среднее арифметическое - {0}".format(str(average_calc(array))))
        bot.send_message(message.chat.id, "Среднее медианное - {0}".format(str(median_calc(array))))
        bot.send_message(message.chat.id, "Варианты - {0}".format(str(variants_calc(array))))
        bot.send_message(message.chat.id, "Частота - {0}".format(str(freq_calc(array))))


bot.polling()

