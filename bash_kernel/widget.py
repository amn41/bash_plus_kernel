

def should_display_iframe(output):
    return 'iframe' in output

def display_data_for_iframe(url):
    content = {
        'data': {
            'text/html': '<a href="{}" target="_blank"><button class="button">Open UI</button></a>'.format(url)
         },
        'metadata': {}
    }
    return content
