if __name__ == "__main__":
    # -------------------------------------------
    from Base.Record import *
    from Base.Recognition import *
    # -------------------------------------------
    model_flag = None
    devices = {}
    devices_name = ["fifine", "Petlya", "Webcam"]
    for i in devices_name:
        devices[i] = [None, None, None]
    # -------------------------------------------
    Record = Record(devices=devices)
    Recognition = Recognition()
    # -------------------------------------------

    while True:
        print('Использовать модель?')
        while True:
            # text = str(input(">>> "))
            text = Record.listen_one_msg()
            print(f'>>> {text}')
            if 'да' in text:
                model_flag = 1
                break
            elif 'нет' in text:
                model_flag = 0
                break

        print('Система для распознавания команд установлена')
        try:
            OverlordControlIR.search_com()
            print('Система "Overlord" готова к работе')
            for text in Record.listen():
                print(f'>>> {text}')
                text = Recognition.merge_text(text)
                print(f'>>> {text}')
                if model_flag == 0:
                    Recognition.list_recognition(text)
                elif model_flag == 1:
                    Recognition.model_recognition(text)

        except OSError as E:
            print(E)