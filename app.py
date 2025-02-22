from flask import Flask, render_template

app = Flask(__name__)

# 图片列表，每个图片包含路径、介绍和方向（横向或纵向）
images = [
    {"src": "images/image1.jpg", "description": "乱针绣作品1", "id": 1, "orientation": "landscape", "title": "作品一", "detail": "这是作品一的详细介绍。"},
    {"src": "images/image2.jpg", "description": "乱针绣作品2", "id": 2, "orientation": "portrait", "title": "作品二", "detail": "这是作品二的详细介绍。"},
    {"src": "images/image3.jpg", "description": "乱针绣作品3", "id": 3, "orientation": "landscape", "title": "作品三", "detail": "这是作品三的详细介绍。"},
    {"src": "images/image4.jpg", "description": "乱针绣作品4", "id": 4, "orientation": "portrait"},
    {"src": "images/image5.jpg", "description": "乱针绣作品5", "orientation": "landscape"},
    {"src": "images/image6.jpg", "description": "乱针绣作品6", "orientation": "portrait"},
    {"src": "images/image7.jpg", "description": "乱针绣作品7", "orientation": "landscape"},
    {"src": "images/image8.jpg", "description": "乱针绣作品8", "orientation": "portrait"},
    {"src": "images/image9.jpg", "description": "乱针绣作品9", "orientation": "landscape"},
    {"src": "images/image10.jpg", "description": "乱针绣作品10", "orientation": "portrait"},
    {"src": "images/image11.jpg", "description": "乱针绣作品11", "orientation": "landscape"},
    {"src": "images/image12.jpg", "description": "乱针绣作品12", "orientation": "portrait"},
    {"src": "images/image13.gif", "description": "乱针绣作品13", "orientation": "landscape"},
]


@app.route('/')
def index():
    return render_template('index.html', images=images)


@app.route('/detail1')
def detail1():
    image = next((img for img in images if img["id"] == 1), None)
    return render_template('detail1.html', image=image)


@app.route('/detail2')
def detail2():
    image = next((img for img in images if img["id"] == 2), None)
    return render_template('detail2.html', image=image)


@app.route('/detail4')
def detail4():
    image = next((img for img in images if img["id"] == 4), None)
    return render_template('detail4.html', image=image)


if __name__ == '__main__':
    app.run(debug=True)
