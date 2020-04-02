import animation

data_matrix = {'a': [[6, "", 9, 8], ["", "", "", ""], [5, "", "", 7]]}

data_columns = [('size', 'size', [4])]  
data_rows = [('pos_1', 'pos', [0, 2, 2, 3, 5]),
             ('idx_1', 'idx', [0, 2, 0, 0, 2])]
values = [('vals', 'vals', [6, 5, 9, 8, 7])]

array_names = ['pos_1', 'pos_1', 'idx_1', 'vals']
instructions = {'a00': [0, 1, 0, 0],
                'a20': [0, 1, 1, 1],
                'a02': [2, 3, 2, 2], 
                'a03': [3, 4, 3, 3],
                'a23': [3, 4, 4, 4]}

animation.display_animation('3', data_matrix, [data_columns, data_rows, values], array_names, instructions)