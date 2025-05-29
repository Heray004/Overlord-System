class WordBase:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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
                ('OverlordControl_Zigbee', 'light_on'): ["включить свет", "включи свет"],
                ('OverlordControl_Zigbee', 'light_off'): ["выключить свет", "выключи свет"],
                #('OverlordControl_Zigbee', 'light'): ["свет"],
                ('OverlordControl_Zigbee', 'charger_on'): ["включить розетка", "включи розетку"],
                ('OverlordControl_Zigbee', 'charger_off'): ["выключить розетка", "выключи розетку"],
                #('OverlordControl_Zigbee', 'charger'): ["розетка"],
            }
        }
