# В текстовом файле найти все варианты фамилии Достоевского в единственном экземпляре

import re
with open('dostoevsky.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    reg_name = re.findall(r"Достоевск[ий|ая|ие|ого]+", text)
print((set(reg_name)))
