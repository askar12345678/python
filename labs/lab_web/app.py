import flask

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
)


app = Flask(
    import_name=__name__,
    template_folder='./templates',
    static_folder='./static'
)

old_hobby = ''
    
@app.route('/', methods=['POST'])
def hobby():
    if request.method == 'POST':
        new_hobby = request.form.get('hobby')
        global old_hobby
        old_hobby = new_hobby
        
        return render_template('index.html', hobby = new_hobby)
                        


@app.route('/')
def index():
    return render_template('index.html', hobby = old_hobby)
        

if __name__ == '__main__':
    app.run(debug=True)