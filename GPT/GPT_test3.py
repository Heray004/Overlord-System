from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


# Укажите путь к локальной модели
local_model_path = r"opt-1.3b"

# Загрузка модели и токенизатора
tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model = AutoModelForCausalLM.from_pretrained(local_model_path)

# Генерация текста
def generate_text(prompt, max_length=2500):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs.input_ids, 
        max_length=max_length, 
        num_return_sequences=1, 
        do_sample=True,  # Включение случайности
        temperature=0.9  # Контроль "творчества" модели
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Пример использования
prompt = f"""
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
generated_text = generate_text(prompt)
print(generated_text)
