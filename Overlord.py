from Base.Recognition import Recognition


class Overlord(Recognition):
    def __init__(self, **kwargs):
        # -------------------------------------------
        model_flag = None
        # -------------------------------------------
        super().__init__(**kwargs)
        # -------------------------------------------

        while True:
            print('Использовать модель?')
            while model_flag is None:
                text = self.listen_one_msg()
                if 'да' in text:
                    model_flag = 1
                    print('Система распознавания: модель')
                elif 'нет' in text:
                    model_flag = 0
                    print('Система распознавания: словарь')

            try:
                self.Recognition_start(model_flag=model_flag)
                print('Система "Overlord" готова к работе')
                if model_flag == 0:
                    for text in self.listen():
                        print(f'>>> {text}')
                        text = self.merge_text(text)
                        print(f'>>> {text}')
                        self.list_recognition(text)
                elif model_flag == 1:
                    for text in self.listen():
                        print(f'>>> {text}')
                        text = self.merge_text(text)
                        print(f'>>> {text}')
                        self.model_recognition(text)

            except OSError as E:
                print(E)

if __name__ == "__main__":
    devices = {}
    devices_name = ["fifine", "Petlya"]  # , "Webcam"]
    for i in devices_name:
        devices[i] = [None, None, None]
    Overlord(devices=devices)
