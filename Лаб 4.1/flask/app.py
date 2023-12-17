from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Используем камеру с индексом 0 (обычно это встроенная камера)
cap = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # Захватываем кадр с камеры
        success, frame = cap.read()
        if not success:
            break
        else:
            # Преобразуем кадр в формат JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        # Возвращаем кадр для отображения на веб-странице
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    # Выводим видеопоток на веб-страницу
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
