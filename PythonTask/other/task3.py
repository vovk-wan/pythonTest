letters_set = set('abcdefghijklmnopqrstuvwxyz')
print('Содержимое файла text.txt:')
total_letters = 0
file_text = open('text.txt', 'r', encoding='utf8')
dict_analysis = dict()
for f_line in file_text:
    for i_letter in letters_set:
        dict_analysis[i_letter] = dict_analysis.get(i_letter, 0) + f_line.lower().count(i_letter)
        total_letters += f_line.lower().count(i_letter)
    print(f_line, end='')
file_text.close()
dict_analysis = {i_key: round(i_val / total_letters, 3) for i_key, i_val in dict_analysis.items() if i_val != 0}
sort_info_tuple = sorted(dict_analysis.items(), key=lambda item: (item[1], item[0]), reverse=True)
text = ''
for i_letter, i_frequency in sort_info_tuple:
    text +=(f'{i_letter} {i_frequency}\n')

file_analysis = open('analysis.txt', 'w', encoding='utf8')
file_analysis.write(text)
file_analysis.close()
print(text)
