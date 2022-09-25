from UI import data_view

def create():
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '            <p{}>Data:{}</p>\n'.format(style, data_view())
    html += '            </body>\n<html>'
    with open('index.html', 'w') as page:
        page.write(html)
    return
