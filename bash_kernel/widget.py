

def should_display_iframe(output):
    return 'iframe' in output

def display_data_for_iframe():
    content = {
        'data': {
            'text/html': '<iframe src="http://localhost:8000/index.html" width=700 height=350></iframe>'
         },
        'metadata': {}
    }
    return content
