from flask import Flask, render_template
import llm

app = Flask(__name__)
obj = llm.Lmm()


@app.route('/')
def index():
    citations = obj.mapping_function()
    return render_template('index.html', citations=citations)


if __name__ == '__main__':
    app.run(debug=True)