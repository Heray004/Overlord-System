class WordBase:
    def __init__(self):
        self.word_base = {
            'name': ["оверлорд", "овер", "лорд", "система", "обер", "опер", "уивер"],
            'commands': {
                ('BaseFunction', 'eexit'): ["пока"],
                ('BaseFunction', 'restart_PC'): ["перезагрузить компьютер", "перезагрузи компьютер"],
                ('BaseFunction', 'off_PC'): ["выключить компьютер", "выключи компьютер"],
                ('BaseFunction', 'hello'): ["привет"],
                ('BaseFunction', 'reload'): ["найди микрофоны", "проверь микрофоны", "инициализация"],
                ('BaseFunction', 'open_dota'): ["открой доту", "открой помойку", "включи помойку", "запусти помойку"]
            },
            'other': {
                # 'player'
                ('BaseFunction', 'music'): ["музыка"],
                ('BaseFunction', 'next_music'): ["дальше"],
                ('BaseFunction', 'prev_music'): ["назад"],
                ('BaseFunction', 'param_vol'): ["параметры звука"],
                ('OverlordControl', 'vol_down'): ["тише"],
                ('OverlordControl', 'vol_up'): ["громче"],
                # 'conditioner'
                ('OverlordControl', 'off_conditioner'): ["холодно"],
                ('OverlordControl', 'set17'): ["жарко"],
                ('OverlordControl', 'set18'): ["..."],
            }
        }
