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
                ('OverlordControlIR', 'vol_down'): ["тише"],
                ('OverlordControlIR', 'vol_up'): ["громче"],
                # 'conditioner'
                ('OverlordControlIR', 'off_conditioner'): ["холодно"],
                ('OverlordControlIR', 'set17'): ["жарко"],
                ('OverlordControlIR', 'set18'): ["..."],
                ('OverlordControlZigbee', 'light_on'): ["включить свет", "включи свет"],
                ('OverlordControlZigbee', 'light_off'): ["выключить свет", "выключи свет"],
                #('OverlordControlZigbee', 'light'): ["свет"],
                ('OverlordControlZigbee', 'charger_on'): ["включить розетка", "включи розетку"],
                ('OverlordControlZigbee', 'charger_off'): ["выключить розетка", "выключи розетку"],
                #('OverlordControlZigbee', 'charger'): ["розетка"],
            }
        }
