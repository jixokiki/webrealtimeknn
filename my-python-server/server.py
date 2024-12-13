# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier

# app = Flask(__name__)
# # CORS(app)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     try:
# #         file = request.files['file']
# #         data = pd.read_csv(file)
        
# #         # Tambahkan logging
# #         print('Data received:', data.head())

# #         # Lakukan proses KNN di sini, contoh:
# #         knn_model = KNeighborsClassifier(n_neighbors=3)
# #         # ...

# #         # Hasil KNN
# #         result = {'result': 'Hasil KNN di sini'}

# #         return jsonify(result)
# #     except Exception as e:
# #         # Tambahkan logging untuk error
# #         print('Error:', str(e))
# #         return jsonify({'error': str(e)})

# # @app.route('/upload', methods=['POST'])
# # def upload_file():
# #     try:
# #         file = request.files['file']
# #         data = pd.read_csv(file)
        
# #         # Tambahkan logging
# #         print('Data received:', data.head())

# #         # Lakukan proses KNN di sini, contoh:
# #         knn_model = KNeighborsClassifier(n_neighbors=3)
# #         X = data[['user_id']]  # Sesuaikan dengan kolom-kolom yang ingin Anda gunakan
# #         y = data['message_date']  # Sesuaikan dengan kolom target yang ingin Anda prediksi
# #         knn_model.fit(X, y)

# #         # Prediksi menggunakan KNN (contoh, Anda perlu menyesuaikan ini)
# #         prediction = knn_model.predict([[new_user_id_value]])

# #         # Hasil KNN
# #         result = {'result': 'Hasil KNN di sini', 'prediction': prediction.tolist()}

# #         return jsonify(result)
# #     except Exception as e:
# #         # Tambahkan logging untuk error
# #         print('Error:', str(e))
# #         return jsonify({'error': str(e)})

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         file = request.files['file']
#         data = pd.read_csv(file)
        
#         # Tambahkan logging
#         print('Data received:', data.head())

#         # Lakukan proses KNN di sini, contoh:
#         knn_model = KNeighborsClassifier(n_neighbors=3)
        
#         # Contoh: Ambil kolom 'user_id' sebagai fitur (X)
#         X = data[['user_id']]
        
#         # Contoh: Ambil kolom 'message_date' sebagai target (y)
#         y = data['message_date']

#         knn_model.fit(X, y)

#         # Contoh: Prediksi menggunakan KNN (gantilah sesuai dengan kebutuhan Anda)
#         new_user_id_value = 123  # Gantilah dengan nilai yang sesuai
#         prediction = knn_model.predict([[new_user_id_value]])

#         # Hasil KNN
#         result = {'result': 'Hasil KNN di sini', 'prediction': prediction.tolist()}

#         return jsonify(result)
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)



# # server.py
# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import pandas as pd
# from sklearn.neighbors import KNeighborsClassifier
# import matplotlib.pyplot as plt
# from io import BytesIO

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         file = request.files['file']
#         data = pd.read_csv(file)

#         # Tambahkan logging
#         print('Data received:', data.head())

#         # Lakukan proses KNN di sini, contoh:
#         knn_model = KNeighborsClassifier(n_neighbors=3)
#         X = data[['user_id']]  # Sesuaikan dengan kolom-kolom yang ingin Anda gunakan
#         y = data['message_date']  # Sesuaikan dengan kolom target yang ingin Anda prediksi
#         knn_model.fit(X, y)

#         # Contoh: Prediksi menggunakan KNN (gantilah sesuai dengan kebutuhan Anda)
#         new_user_id_value = 123  # Gantilah dengan nilai yang sesuai
#         prediction = knn_model.predict([[new_user_id_value]])

#         # Hasil KNN
#         result = {'result': 'Hasil KNN di sini', 'prediction': prediction.tolist()}

#         # Visualisasi Histogram
#         data['user_id'].plot(kind='hist')
#         plt.title('Histogram User ID')
#         plt.savefig('histogram.png')
#         plt.clf()

#         # Visualisasi Scatter Plot
#         data.plot.scatter(x='user_id', y='message_date')
#         plt.title('Scatter Plot')
#         plt.savefig('scatter.png')
#         plt.clf()

#         # Visualisasi Line Plot
#         data.plot(x='user_id', y='message_date')
#         plt.title('Line Plot')
#         plt.savefig('line_plot.png')
#         plt.clf()

#         # Visualisasi Box Plot
#         data.boxplot(column='user_id')
#         plt.title('Box Plot User ID')
#         plt.savefig('box_plot.png')
#         plt.clf()

#         # Visualisasi Pair Plot
#         import seaborn as sns
#         sns.pairplot(data)
#         plt.title('Pair Plot')
#         plt.savefig('pair_plot.png')
#         plt.clf()

#         return send_file('histogram.png', mimetype='image/png')
#         # return jsonify(result)
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)





# # server.py
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# import os
# from sklearn.neighbors import KNeighborsRegressor  # Menggunakan KNeighborsRegressor karena targetnya numerik

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         file = request.files['file']
#         data = pd.read_csv(file)

#         # Tambahkan logging
#         print('Data received:', data.head())

#         # Lakukan proses KNN di sini, contoh:
#         knn_model = KNeighborsRegressor(n_neighbors=3)
        
#         # Contoh: Ambil kolom 'user_id' sebagai fitur (X)
#         X = data[['user_id']]
        
#         # Contoh: Ambil kolom 'duration' sebagai target (y)
#         y = data['duration']

#         knn_model.fit(X, y)

#         # # Contoh: Prediksi menggunakan KNN (gantilah sesuai dengan kebutuhan Anda)
#         # new_user_id_value = 123  # Gantilah dengan nilai yang sesuai
#         # prediction = knn_model.predict([[new_user_id_value]])


#         # Contoh: Prediksi menggunakan KNN
#         # (Ambil nilai dari data yang diunggah, misalnya ambil nilai dari baris pertama)
#         new_user_id_value = data['user_id'].iloc[0]
#         prediction = knn_model.predict([[new_user_id_value]])

#         # Hasil KNN
#         result = {'result': 'Hasil KNN di sini', 'prediction': prediction.tolist()}

#         return jsonify(result)
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# # # Tambahkan endpoint untuk visualisasi
# # @app.route('/visualizations', methods=['GET'])
# # def get_visualizations():
# #     # Dalam kasus nyata, Anda akan menghasilkan visualisasi dan memberikan URL gambar
# #     # Di sini kita memberikan URL dummy untuk keperluan contoh
# #     visualization_url = 'https://example.com/visualization.png'
# #     return jsonify({'url': visualization_url})

# @app.route('/visualizations', methods=['GET'])
# def get_visualizations():
#     try:
#         # Menghasilkan dan menyimpan visualisasi
#         # (Gantilah dengan kode yang sesuai untuk menghasilkan visualisasi dari data)
#         visualization_path = 'path/to/your/visualization.png'

#         # Pastikan file visualisasi ada
#         if os.path.exists(visualization_path):
#             # Dapatkan URL gambar visualisasi
#             visualization_url = f'http://example.com/{visualization_path}'  # Gantilah dengan URL yang sesuai
#             return jsonify({'url': visualization_url})
#         else:
#             return jsonify({'error': 'Visualisasi tidak ditemukan'})

#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True)




# # server.py
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# from sklearn.neighbors import KNeighborsRegressor

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         file = request.files['file']
#         data = pd.read_csv(file)

#         # Tambahkan logging
#         print('Data received:', data.head())

#         # Ambil semua kolom kecuali yang merupakan target
#         feature_columns = data.columns.difference(['duration'])

#         # Ambil kolom 'duration' sebagai target
#         target_column = 'duration'

#         # Ambil kolom 'user_id' sebagai fitur (X)
#         X = data[feature_columns]

#         # Ambil kolom 'duration' sebagai target (y)
#         y = data[target_column]

#         # Lakukan proses KNN di sini, contoh:
#         knn_model = KNeighborsRegressor(n_neighbors=3)
#         knn_model.fit(X, y)

#         # Ambil contoh nilai untuk prediksi (sesuaikan dengan data yang diunggah)
#         new_data_for_prediction = data[feature_columns].iloc[[0]]  # Ambil baris pertama sebagai contoh
#         prediction = knn_model.predict(new_data_for_prediction)

#         # Hasil KNN
#         result = {'result': 'Hasil KNN di sini', 'prediction': prediction.tolist()}

#         return jsonify(result)
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# # Tambahkan endpoint untuk visualisasi
# @app.route('/visualizations', methods=['GET'])
# def get_visualizations():
#     # Dalam kasus nyata, Anda akan menghasilkan visualisasi dan memberikan URL gambar
#     # Di sini kita memberikan URL dummy untuk keperluan contoh
#     visualization_url = 'https://example.com/visualization.png'
#     return jsonify({'url': visualization_url})

# if __name__ == '__main__':
#     app.run(debug=True)






# # server.py
# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import pandas as pd
# import os
# from sklearn.neighbors import KNeighborsRegressor
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# # def generate_and_save_histogram(data, column_name, output_path):
# #     plt.figure(figsize=(10, 6))
# #     sns.histplot(data[column_name], bins=20, color='skyblue', edgecolor='black')
# #     plt.title(f'Histogram of {column_name}')
# #     plt.xlabel('Values')
# #     plt.ylabel('Frequency')
# #     plt.savefig(output_path)
# #     plt.close()

# def generate_and_save_histogram(data, column_name, output_path):
#     # Menyiapkan plot di utas utama
#     # plt.switch_backend('Agg')  # Menggunakan Agg untuk mode non-interaktif
#     fig, ax = plt.subplots(figsize=(10, 6))

#     # Menggambar histogram
#     sns.histplot(data[column_name], bins=20, color='skyblue', edgecolor='black', ax=ax)
#     ax.set_title(f'Histogram of {column_name}')
#     ax.set_xlabel('Values')
#     ax.set_ylabel('Frequency')

#     # Menyimpan gambar ke path
#     plt.savefig(output_path)
#     # plt.close()
#     plt.close('all')
#     plt.switch_backend('Agg')


#     # # Mengembalikan kembali ke mode interaktif (jika sebelumnya dalam mode interaktif)
#     # plt.switch_backend('TkAgg')  # Gantilah dengan backend yang sesuai jika tidak menggunakan TkAgg


# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         file = request.files['file']
#         data = pd.read_csv(file)

#         # Lakukan proses KNN di sini, contoh:
#         knn_model = KNeighborsRegressor(n_neighbors=3)
        
#         # Ambil kolom 'user_id' sebagai fitur (X)
#         X = data[['user_id']]
        
#         # Ambil kolom 'duration' sebagai target (y)
#         y = data['duration']

#         # knn_model.fit(X, y)
        
#         #UserWarning: X does not have valid feature names, but KNeighborsRegressor was fitted with feature names
#         #Kesalahan ini muncul karena model KNeighborsRegressor Anda tidak mendapatkan nama fitur saat dilatih. Ini adalah peringatan dan umumnya tidak mempengaruhi hasil prediksi. Untuk mengatasi peringatan ini, Anda dapat memberikan nama fitur saat melatih model. Contoh:
#         knn_model.fit(X, y, feature_name=X.columns)

#         # Ambil contoh nilai untuk prediksi (ambil nilai dari data yang diunggah)
#         new_user_id_value = data['user_id'].iloc[0]
#         prediction = knn_model.predict([[new_user_id_value]])

#         # Hasil KNN
#         result = {'result': 'Hasil KNN di sini', 'prediction': prediction.tolist()}

#         # Buat dan simpan histogram Glucose
#         histogram_path = 'path/to/your/histogram.png'  # Ganti dengan path yang sesuai
#         generate_and_save_histogram(data, 'Glucose', histogram_path)

#         return jsonify(result)
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# @app.route('/visualizations', methods=['GET'])
# def get_visualizations():
#     try:
#         # Dapatkan URL gambar visualisasi histogram Glucose
#         histogram_url = generate_histogram_url()
#         return jsonify({'histogram_url': histogram_url})
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# def generate_histogram_url():
#     # # Gantilah dengan path yang sesuai
#     # histogram_path = 'path/to/your/histogram.png'

#     #Pastikan Anda memberikan path yang valid di mana Anda memiliki izin untuk menulis file. Misalnya, jika Anda ingin menyimpannya di direktori yang sama dengan skrip Python Anda, Anda dapat menggunakan:
#     histogram_path = 'histogram.png'
    
#     # # Pastikan file visualisasi ada
#     # if os.path.exists(histogram_path):
#     #     return f'http://example.com/{histogram_path}'  # Gantilah dengan URL yang sesuai
#     # else:
#     #     return None

#     #Jika Anda ingin memberikan URL file visualisasi ke client (React) dari server Flask, yang biasanya dilakukan adalah memberikan URL lokal ke file tersebut, bukan URL eksternal http://example.com/.
#     # Pastikan file visualisasi ada
#     if os.path.exists(histogram_path):
#         # Menghasilkan URL lokal ke file visualisasi di server
#         visualization_url = f'http://127.0.0.1:5000/{histogram_path}'  # Gantilah dengan URL yang sesuai
#         return jsonify({'url': visualization_url})
#     else:
#         return jsonify({'error': 'Visualisasi tidak ditemukan'})


# if __name__ == '__main__':
#     app.run(debug=True)




# # server.py
# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import pandas as pd
# import os
# from sklearn.neighbors import KNeighborsRegressor
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# def generate_and_save_histogram(data, column_name, output_path):
#     plt.figure(figsize=(10, 6))
#     sns.histplot(data[column_name], bins=20, color='skyblue', edgecolor='black')
#     plt.title(f'Histogram of {column_name}')
#     plt.xlabel('Values')
#     plt.ylabel('Frequency')
#     plt.savefig(output_path)
#     plt.close()

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         file = request.files['file']
#         data = pd.read_csv(file)

#         # Lakukan proses KNN di sini, contoh:
#         knn_model = KNeighborsRegressor(n_neighbors=3)
        
#         # Ambil kolom 'user_id' sebagai fitur (X)
#         X = data[['user_id']]
        
#         # Ambil kolom 'duration' sebagai target (y)
#         y = data['duration']

#         knn_model.fit(X, y)

#         # Ambil contoh nilai untuk prediksi (ambil nilai dari data yang diunggah)
#         new_user_id_value = data['user_id'].iloc[0]
#         prediction = knn_model.predict([[new_user_id_value]])

#         # Hasil KNN
#         result = {'result': 'Hasil KNN di sini', 'prediction': prediction.tolist()}

#         # # Buat dan simpan histogram Glucose
#         # histogram_path = 'path/to/your/histogram.png'  # Ganti dengan path yang sesuai
#         # Buat dan simpan histogram Glucose
#         histogram_path = 'histogram.png'  # Ganti dengan path yang sesuai
#         generate_and_save_histogram(data, 'Glucose', histogram_path)

#         return jsonify(result)
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# @app.route('/visualizations', methods=['GET'])
# def get_visualizations():
#     try:
#         # # Dapatkan URL gambar visualisasi histogram Glucose
#         # histogram_path = 'path/to/your/histogram.png'  # Ganti dengan path yang sesuai
        
#         # Dapatkan URL gambar visualisasi histogram Glucose
#         histogram_path = 'histogram.png'  # Ganti dengan path yang sesuai
#         return send_file(histogram_path, mimetype='image/png')
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})
    

# def generate_histogram_url():
#     # # Gantilah dengan path yang sesuai
#     # histogram_path = 'path/to/your/histogram.png'

#     #Pastikan Anda memberikan path yang valid di mana Anda memiliki izin untuk menulis file. Misalnya, jika Anda ingin menyimpannya di direktori yang sama dengan skrip Python Anda, Anda dapat menggunakan:
#     histogram_path = 'histogram.png'
    
#     # # Pastikan file visualisasi ada
#     # if os.path.exists(histogram_path):
#     #     return f'http://example.com/{histogram_path}'  # Gantilah dengan URL yang sesuai
#     # else:
#     #     return None

#     #Jika Anda ingin memberikan URL file visualisasi ke client (React) dari server Flask, yang biasanya dilakukan adalah memberikan URL lokal ke file tersebut, bukan URL eksternal http://example.com/.
#     # Pastikan file visualisasi ada
#     if os.path.exists(histogram_path):
#         # Menghasilkan URL lokal ke file visualisasi di server
#         visualization_url = f'http://127.0.0.1:5000/{histogram_path}'  # Gantilah dengan URL yang sesuai
#         return jsonify({'url': visualization_url})
#     else:
#         return jsonify({'error': 'Visualisasi tidak ditemukan'})

# if __name__ == '__main__':
#     app.run(debug=True)






##INI KODE FIX UNTUK PENERAPAN KNN
# server.py
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pandas as pd
import os
from sklearn.neighbors import KNeighborsRegressor
import matplotlib
matplotlib.use('Agg')  # Set Matplotlib backend to 'Agg'
import matplotlib.pyplot as plt
import seaborn as sns
import io

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

def generate_and_save_histogram(data, column_name, output_path):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column_name], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column_name}')
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.savefig(output_path)
    plt.close()

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files['file']
        data = pd.read_csv(file)
        print(data.columns)

        # Lakukan proses KNN di sini, contoh:
        knn_model = KNeighborsRegressor(n_neighbors=3)
        
        # Ambil kolom 'user_id' sebagai fitur (X)
        X = data[['Glucose']]
        
        # Ambil kolom 'duration' sebagai target (y)
        y = data['Age']

        # Perbaikan: Hapus parameter yang tidak diperlukan
        knn_model.fit(X, y)

        # Ambil contoh nilai untuk prediksi (ambil nilai dari data yang diunggah)
        new_user_id_value = data['Glucose'].iloc[0]
        prediction = knn_model.predict([[new_user_id_value]])

        # Hasil KNN
        result = {'result': 'Hasil KNN di sini', 'prediction': prediction.tolist()}

        # Buat dan simpan histogram Glucose
        # Perbaikan: Path untuk menyimpan histogram
        histogram_path = '/Users/rizkimaulana/Documents/WebWidya/my-python-server/static/histogram.png'
        generate_and_save_histogram(data, 'Glucose', histogram_path)

        return jsonify(result)
    except Exception as e:
        # Tambahkan logging untuk error
        print('Error:', str(e))
        return jsonify({'error': str(e)})

@app.route('/visualizations', methods=['GET'])
def get_visualizations():
    try:
        # Dapatkan URL gambar visualisasi histogram Glucose
        # Perbaikan: Path untuk menyimpan histogram
        histogram_path = '/Users/rizkimaulana/Documents/WebWidya/my-python-server/static/histogram.png'
        return send_file(histogram_path, mimetype='image/png')
    except Exception as e:
        # Tambahkan logging untuk error
        print('Error:', str(e))
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, threaded=False)




# # # server.py
# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import pandas as pd
# import os
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.cluster import KMeans
# import matplotlib
# matplotlib.use('Agg')  # Set Matplotlib backend to 'Agg'
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# def generate_and_save_histogram(data, column_name, output_path):
#     plt.figure(figsize=(10, 6))
#     sns.histplot(data[column_name], bins=20, color='skyblue', edgecolor='black')
#     plt.title(f'Histogram of {column_name}')
#     plt.xlabel('Values')
#     plt.ylabel('Frequency')
#     plt.savefig(output_path)
#     plt.close()

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         file = request.files['file']
#         data = pd.read_csv(file)
#         print(data.columns)

#         # Lakukan proses KNN di sini, contoh:
#         knn_model = KNeighborsRegressor(n_neighbors=3)
        
#         # Ambil kolom 'Glucose' sebagai fitur (X)
#         X_knn = data[['Glucose']]
        
#         # Ambil kolom 'Age' sebagai target (y) untuk KNN
#         y_knn = data['Age']

#         # Hapus parameter yang tidak diperlukan
#         knn_model.fit(X_knn, y_knn)

#          # Lakukan proses K-Means di sini, contoh:
#         kmeans_model = KMeans(n_clusters=3, random_state=42, n_init=10)
#         X_kmeans = data[['Glucose', 'Age']]
#         data['cluster'] = kmeans_model.fit_predict(X_kmeans)


#         # # Hasil KNN
#         # prediction_knn = knn_model.predict([[data['Glucose'].iloc[0]]])

#         # Hasil KNN
#         prediction = knn_model.predict([[data['Glucose'].iloc[0]]])


#         # Hasil K-Means
#         cluster_centers = kmeans_model.cluster_centers_
#         result = {'result_knn': 'Hasil KNN di sini', 'prediction': prediction.tolist(),
#                   'result_kmeans': 'Hasil K-Means di sini', 'cluster_centers': cluster_centers.tolist(),
#                     'cluster_labels': data['cluster'].tolist()}

#         # Buat dan simpan histogram Glucose
#         histogram_path = '/Users/rizkimaulana/Documents/WebWidya/my-python-server/static/histogram.png'
#         generate_and_save_histogram(data, 'Glucose', histogram_path)

#         return jsonify(result)
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# @app.route('/visualizations', methods=['GET'])
# def get_visualizations():
#     try:
#         # Dapatkan URL gambar visualisasi histogram Glucose
#         # Perbaikan: Path untuk menyimpan histogram
#         histogram_path = '/Users/rizkimaulana/Documents/WebWidya/my-python-server/static/histogram.png'
#         return send_file(histogram_path, mimetype='image/png')
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# if __name__ == '__main__':
#     app.run(debug=True, threaded=False)



# # server.py
# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import pandas as pd
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.cluster import KMeans
# import matplotlib
# matplotlib.use('Agg')  # Set Matplotlib backend to 'Agg'
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# def generate_and_save_histogram(data, column_name, output_path):
#     plt.figure(figsize=(10, 6))
#     sns.histplot(data[column_name], bins=20, color='skyblue', edgecolor='black')
#     plt.title(f'Histogram of {column_name}')
#     plt.xlabel('Values')
#     plt.ylabel('Frequency')
#     plt.savefig(output_path)
#     plt.close()

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         file = request.files['file']
#         data = pd.read_csv(file)
#         print(data.columns)

#         # Lakukan proses KNN di sini, contoh:
#         knn_model = KNeighborsRegressor(n_neighbors=3)
#         knn_model.fit(data[['Glucose']], data['Age'])
#         prediction = knn_model.predict(data[['Glucose']])

#         # Lakukan proses K-Means untuk analisis tingkat minat dan bakat
#         kmeans_model = KMeans(n_clusters=3, random_state=42)
#         # features_for_kmeans = data[['Feature1', 'Feature2']]  # Ganti dengan fitur yang sesuai
#         features_for_kmeans = data[['Glucose', 'Age']]  # Ganti dengan fitur yang sesuai
#         data['cluster_kmeans'] = kmeans_model.fit_predict(features_for_kmeans)

#         # Hasil KNN dan K-Means
#         result = {
#             'result_knn': 'Hasil KNN di sini',
#             'prediction': prediction.tolist(),
#             # 'result_kmeans': 'Hasil K-Means di sini',
#             # 'cluster_centers': kmeans_model.cluster_centers_.tolist(),
#             # 'cluster_labels': data['cluster_kmeans'].tolist()
#         }

#         # Buat dan simpan histogram Glucose
#         histogram_path = '/Users/rizkimaulana/Documents/WebWidya/my-python-server/static/histogram.png'
#         generate_and_save_histogram(data, 'Glucose', histogram_path)

#         return jsonify(result)
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# # ... (existing code)

# if __name__ == '__main__':
#     app.run(debug=True, threaded=False)




# # server.py
# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import pandas as pd
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.cluster import KMeans
# import matplotlib
# matplotlib.use('Agg')  # Set Matplotlib backend to 'Agg'
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# def generate_and_save_histogram(data, column_name, output_path):
#     plt.figure(figsize=(10, 6))
#     sns.histplot(data[column_name], bins=20, color='skyblue', edgecolor='black')
#     plt.title(f'Histogram of {column_name}')
#     plt.xlabel('Values')
#     plt.ylabel('Frequency')
#     plt.savefig(output_path)
#     plt.close()

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         file = request.files['file']
#         data = pd.read_csv(file)
#         print(data.columns)


#         # # Lakukan proses K-Means untuk analisis tingkat minat dan bakat
#         # kmeans_model = KMeans(n_clusters=3, random_state=42)
#         # # features_for_kmeans = data[['Feature1', 'Feature2']]  # Ganti dengan fitur yang sesuai
#         # features_for_kmeans = data[['Glucose', 'Age']]  # Ganti dengan fitur yang sesuai
#         # data['cluster_kmeans'] = kmeans_model.fit_predict(features_for_kmeans)

#         # # Hasil KNN dan K-Means
#         # result = {
#         #     'result_knn': 'Hasil KNN di sini',
#         #     'prediction': prediction.tolist(),
#         #     # 'result_kmeans': 'Hasil K-Means di sini',
#         #     # 'cluster_centers': kmeans_model.cluster_centers_.tolist(),
#         #     # 'cluster_labels': data['cluster_kmeans'].tolist()
#         # }

#         # Buat dan simpan histogram Glucose
#         histogram_path = '/Users/rizkimaulana/Documents/WebWidya/my-python-server/static/histogram2.png'
#         generate_and_save_histogram(data, 'Glucose', histogram_path)

#         #    # Perform KNN
#         # knn_model = KNeighborsRegressor(n_neighbors=3)
#         # knn_model.fit(data[['Glucose']], data['Age'])
#         # prediction = knn_model.predict(data[['Glucose']])
#         # # Your existing code...

#         # Save the Excel file
#         excel_path = '/path/to/results.xlsx'
#         data.to_excel(excel_path, index=False)

#         # # Return the Excel file path
#         # result = {
#         #     'result_knn': 'Hasil KNN di sini',
#         #     'prediction': prediction.tolist(),
#         #     'excel_path': excel_path,
#         # }
#         # Perform KNN
#         knn_model = KNeighborsRegressor(n_neighbors=3)
#         knn_model.fit(data[['Glucose']], data['Age'])
#         prediction = knn_model.predict(data[['Glucose']])

#         # Lakukan proses K-Means untuk analisis tingkat minat dan bakat
#         kmeans_model = KMeans(n_clusters=3, random_state=42)
#         features_for_kmeans = data[['Glucose', 'Age']]  # Ganti dengan fitur yang sesuai
#         data['cluster_kmeans'] = kmeans_model.fit_predict(features_for_kmeans)

#         # Hasil KNN dan K-Means
#         result = {
#             'result_knn': 'Hasil KNN di sini',
#             'prediction': prediction.tolist(),
#             'result_kmeans': 'Hasil K-Means di sini',
#             'cluster_centers': kmeans_model.cluster_centers_.tolist(),
#             'cluster_labels': data['cluster_kmeans'].tolist(),
#             'excel_path': excel_path,
#         }


#                 # Save DataFrame to Excel
#         excel_output_path = '/Users/rizkimaulana/Documents/WebWidya/my-python-server/static/results.xlsx'
#         result.to_excel(excel_output_path, index=False)

#         # Return the path to the saved Excel file
#         return jsonify({'excel_path': excel_output_path})

#         return jsonify(result)
#     except Exception as e:
#         # Detailed error logging
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# # ... (existing code)

# if __name__ == '__main__':
#     app.run(debug=True, threaded=False)







# # server.py
# from flask import Flask, request, jsonify, send_file
# from flask_cors import CORS
# import pandas as pd
# from sklearn.cluster import KMeans
# import matplotlib
# matplotlib.use('Agg')  # Set Matplotlib backend to 'Agg'
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# def generate_and_save_histogram(data, column_name, output_path):
#     plt.figure(figsize=(10, 6))
#     sns.histplot(data[column_name], bins=20, color='skyblue', edgecolor='black')
#     plt.title(f'Histogram of {column_name}')
#     plt.xlabel('Values')
#     plt.ylabel('Frequency')
#     plt.savefig(output_path)
#     plt.close()

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     try:
#         file = request.files['file']
#         data = pd.read_csv(file)
#         print(data.columns)

#         # Lakukan proses K-Means untuk analisis tingkat minat dan bakat
#         kmeans_model = KMeans(n_clusters=3, random_state=42)
#         features_for_kmeans = data[['Glucose', 'Age']]  # Ganti dengan fitur yang sesuai
#         data['cluster_kmeans'] = kmeans_model.fit_predict(features_for_kmeans)

#         # Hasil K-Means
#         result = {
#             'result_kmeans': 'Hasil K-Means di sini',
#             'cluster_centers': kmeans_model.cluster_centers_.tolist(),
#             'cluster_labels': data['cluster_kmeans'].tolist()
#         }

#         # Buat dan simpan histogram Glucose
#         histogram_path = '/Users/rizkimaulana/Documents/WebWidya/my-python-server/static/histogram.png'
#         generate_and_save_histogram(data, 'Glucose', histogram_path)

#         return jsonify(result)
#     except Exception as e:
#         # Tambahkan logging untuk error
#         print('Error:', str(e))
#         return jsonify({'error': str(e)})

# # ... (existing code)

# if __name__ == '__main__':
#     app.run(debug=True, threaded=False)






