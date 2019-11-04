from IPython.core.display import display, HTML

css = open('./animation/custom.css', "r").read()

def generate_matrix(file_id, data_matrices, three_dimensional = False):
    matrix = '<div class="array array-{}">'.format(6 if three_dimensional else 5)
    
    for slice_index, label in enumerate(data_matrices): 
        data_matrix = data_matrices[label]
        matrix += empty_element('elem', 2) if three_dimensional else empty_element('elem')
        for i in range(len(data_matrix[0])):
            matrix += '<div class="elem">{}</div>'.format(i)

        for i in range(len(data_matrix)):
            if three_dimensional: 
                if i == len(data_matrix) // 2:
                    matrix += '<div class="elem-wide">Slice {}</div>'.format(slice_index)
                else:
                    matrix += empty_element('elem-wide')
            
            matrix += '<div class="elem">{}</div>'.format(i)
            for j in range(len(data_matrix[0])):
                element = data_matrix[i][j]
                element_id = file_id + label + str(i) + str(j)
                matrix += '<div id="{}" class="elem box">{}</div>'.format(element_id, element)
    
    return matrix + '</div>'

def empty_element(e, count = 1):
    return '<div class="{}"></div>'.format(e) * count

def generate_html(file_id, data_list):
    html = '<div class="array array-11">'
    for data in data_list:
        html = add_html(file_id, html, data)
    return html + '</div>'

def add_html(file_id, html, data):
    for i in range(len(data)):
        array_type, label, numbers = data[i] 
        html += '<div class="elem">{}</div>'.format(label)
        for j in range(10):
            if j < len(numbers):
                element_id = file_id + array_type + str(j)
                html += '<div id="{}" class="elem box">{}</div>'.format(element_id, numbers[j])
            elif i == len(data) - 1:
                html += '<div class="elem extra-vertical-space"></div>'
            else:
                html += '<div class="elem"></div>'
    return html

def generate_javascript(file_id, array_names, instructions):
    javascript = '<script>'
    
    for label in instructions:
        element_id = file_id + label;
        instruction = instructions[label];
        javascript += 'document.getElementById("{}").onmouseover = function() \
            {{mouse({}, "{}", "{}", {}, "#0cf")}};'.format(element_id, array_names, file_id, element_id, instruction)
        javascript += 'document.getElementById("{}").onmouseout = function() \
            {{mouse({}, "{}", "{}", {}, "#fff")}};'.format(element_id, array_names, file_id, element_id, instruction)

    with open('./animation/javascript.txt', 'r') as file:
        javascript += file.read() + '</script>'
    
    return javascript

def display_animation(file_id, data_matrices, data_list, array_names, instructions, three_dimensional = False): 
    matrix = generate_matrix(file_id, data_matrices, three_dimensional)
    html = generate_html(file_id, data_list)
    javascript = generate_javascript(file_id, array_names, instructions)
    display(HTML(css + matrix + html + javascript))