#
# :author:   Polusummator
# :date:     07.09.2020 18:43
# :filename: run_tests.py
# :team:     Little PyPy Squad
#
import natsort
import os

data = 'C:/systestdata'
cur_dir = 'C:/systestdata/cur_dir'
cur_prog = 'C:/systestdata/cur_prog'
out = 'C:/systestdata/output'
# data = '/mnt/windows/Alexandr/systestdata'
# cur_dir = '/mnt/windows/Alexandr/systestdata/cur_dir'
# cur_prog = '/mnt/windows/Alexandr/systestdata/cur_prog'
# out = '/mnt/windows/Alexandr/systestdata/output'
if os.path.isdir(data):
    with open(cur_dir) as d:
        path_to_tests = d.readline().strip()
    with open(cur_prog) as p:
        path_to_program = p.readline().strip()
else:
    path_to_tests = 'Nothing'
    path_to_program = 'Nothing'
print('Your current directory with tests is: {dir}'.format(dir=path_to_tests))
create_d = False
if os.path.isdir(data):
    mode_d = input('Change directory? (y/n) ')
else:
    create_d = True
    mode_d = 'y'
if mode_d == 'y':
    z = False
    while not z:
        new_dir = input('Test directory (absolute path): ')
        new_dir.replace('\\', '/')
        new_dir = new_dir[:-1] if new_dir[-1] == '/' else new_dir
        if os.path.isdir(new_dir):
            if not os.path.isdir(data):
                os.mkdir(data)
            with open(cur_dir, 'w') as d:
                d.write(new_dir)
            print('Ok\n')
            z = True
        else:
            print('Directory not found! Try again')
print('\n')
print('Your current program is: {pro}'.format(pro=path_to_program))
if not create_d:
    mode_p = input('Change program? (y/n) ')
else:
    mode_p = 'y'
if mode_p == 'y':
    z = False
    while not z:
        new_prog = input('Program (absolute path): ')
        new_prog.replace('\\', '/')
        new_prog = new_prog[:-1] if new_prog[-1] == '/' else new_prog
        if os.path.isfile(new_prog):
            with open(cur_prog, 'w') as p:
                p.write(new_prog)
            print('Ok\n')
            z = True
        else:
            print('File not found! Try again')
with open(cur_dir) as d:
    path_to_tests = d.readline().strip()
with open(cur_prog) as p:
    path_to_program = p.readline().strip()
tests_list = natsort.natsorted(os.listdir(path_to_tests))
test = 1
is_nice = True
print('\n')
for i in range(0, len(tests_list), 2):
    os.system('python {solution} < {input} > {output}'.format(solution=path_to_program, input=path_to_tests + '/' + tests_list[i], output=out))
    with open(path_to_tests + '/' + tests_list[i + 1]) as f:
        right = f.readlines()
    with open(out) as f:
        test_me = f.readlines()
    if right == test_me:
        print('TEST {test}: OK'.format(test=test))
        print('------------------------------')
    else:
        print('TEST {test}: WRONG'.format(test=test))
        print('------------------------------')
        is_nice = False
    test += 1
if is_nice:
    print('\nAccepted')
else:
    print('\nWrong Answer')

# /mnt/windows/Alexandr/CLion/AutoTests/Tests
# /home/srez/Загрузки/1z.py
