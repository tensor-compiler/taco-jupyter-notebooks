import animation

data_matrix = {'a': [[6, "", 9, 8], ["", "", "", ""], [5, "", "", 7]], 'b': [["", 2, "", ""], [3, "", "", 1], ["", "", 6, ""]]}

data_first = [('pos_0', 'pos', [0, 2]),
             ('idx_0', 'idx', [0, 1])]
data_second = [('pos_1', 'pos', [0, 2, 5]),
             ('idx_1', 'idx', [0, 2, 0, 1, 2])]
data_third = [('pos_2', 'pos', [0, 3, 5, 6, 8, 9]),
                ('idx_2', 'idx', [0, 2, 3, 0, 3, 1, 0, 3, 2])]  
values = [('vals', 'vals', [6, 9, 8, 5, 7, 2, 3, 1, 6])]

labels = ['a00', 'a02', 'a03', 'a20', 'a23', 'b01', 'b10', 'b13', 'b22']
array_names = ['pos_0', 'pos_0', 'idx_0', 'pos_1', 'pos_1', 'idx_1', 'pos_2', 'pos_2', 'idx_2', 'vals']
instructions = {'a00': [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                'a02': [0, 1, 0, 0, 1, 0, 0, 1, 1, 1],
                'a03': [0, 1, 0, 0, 1, 0, 0, 1, 2, 2],
                'a20': [0, 1, 0, 0, 1, 1, 1, 2, 3, 3],
                'a23': [0, 1, 0, 0, 1, 1, 1, 2, 4, 4],
                'b01': [0, 1, 1, 1, 2, 2, 2, 3, 5, 5],
                'b10': [0, 1, 1, 1, 2, 3, 3, 4, 6, 6],
                'b13': [0, 1, 1, 1, 2, 3, 3, 4, 7, 7],
                'b22': [0, 1, 1, 1, 2, 4, 4, 5, 8, 8]}

animation.display_animation('4', data_matrix, [data_first, data_second, data_third, values], array_names, instructions, True)