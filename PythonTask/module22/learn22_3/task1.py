import os
file_out = open(os.path.join('task', 'group_1.txt'), 'r', encoding='utf8')
sym_count = []
for i_line in file_out:
    sym_count.append(str(len(i_line)))
file_out.close()

file_in = open(os.path.join('task', 'result.txt'), 'w', encoding='utf8')
file_in.write('\n'.join(sym_count))
file_in.close()