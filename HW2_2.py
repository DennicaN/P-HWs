el_count = int(input('Укажите количество эллементов в списке'))
m_list = []
i = 0
el = 0
while i < el_count:
    m_list.append(input('Добавьте элементв в список'))
    i += 1

for elem in range(int(len(m_list)/2)):
        m_list[el], m_list[el + 1] = m_list[el + 1], m_list[el]
        el += 2
print(m_list)