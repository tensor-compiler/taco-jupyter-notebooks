import animation

data_matrix = {'a': [[6, "", 9, 8], ["", "", "", ""], [5, "", "", 7]]}

data_rows = [('size', 'size', [3])]
data_columns = [('pos_1', 'pos', [0, 3, 3, 5]),
                ('idx_1', 'idx', [0, 2, 3, 0, 3])]  
values = [('vals', 'vals', [6, 9, 8, 5, 7])]

array_names = ['pos_1', 'pos_1', 'idx_1', 'vals']
instructions = {'a00': [0, 1, 0, 0],
                'a02': [0, 1, 1, 1],
                'a03': [0, 1, 2, 2], 
                'a20': [2, 3, 3, 3],
                'a23': [2, 3, 4, 4]}

animation.display_animation('2', data_matrix, [data_rows, data_columns, values], array_names, instructions)