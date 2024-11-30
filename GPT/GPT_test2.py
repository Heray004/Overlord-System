from g4f.client import Client
import g4f
client = Client()

while True:
    data = f"""
Словарь команд:
    оверлорд, овер, лорд, система, обер, уивер - имена системы

    Вызывается только если упоминаетсмя имя:
        eexit - пользователь попрощался со системой
        restart_PC - перезагружает пк
        off_PC - выключает пк
        hello - пользователь поприветствовал систему
        reload - этим не нужно пользоваться
        open_dota - открывает игру дота

    Вызывается без упоминаниния имени:
        music - включает и выключает музыку (музыка)
        next_music - включает следующую песню (дальше)
        prev_music - включает предыдущую песню (назад)
        vol_down - уменьшает громкость
        vol_up - увеличивает громкость
        off_conditioner - выключает охлаждение комнаты
        set17 - включает охлаждение комнаты

Запрос - "{str(input(">>> "))}"
Ответом на запрос должна быть только команда из словаря. Если нет подходящей функции, напиши NONE и опиши что непонятного.
Скобками обозначены предложения без учета регистра, которые пользователь иногда может использовать.
"""

    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{
            "role": "user",
            "content": data
        }]
    )
    print(response.choices[0].message.content)

# while True:
#     data = f'Запрос - "{str(input(">>> "))}"'
#     response = client.chat.completions.create(
#         model='gpt-4o-mini',
#         messages=[{
#             "role": "user",
#             "content": data
#         }]
#     )
#
#     print(response.choices[0].message.content)
