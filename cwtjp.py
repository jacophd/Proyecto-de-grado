#CONVERSOR WAV JPG
import os
import librosa
import matplotlib.pyplot as plt

def graficar_audio(file_path, save_path):
    # Cargar el archivo de audio
    audio, sr = librosa.load(file_path, sr=None)

    # Obtener los primeros 10 segundos de audio
    audio_10s = audio[:sr*10]

    # Crear el gráfico
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(audio_10s, sr=sr)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Db')
    plt.title('Gráfico de audio')
    
    # Guardar el gráfico como imagen
    plt.savefig(save_path)
    plt.close()

# Carpeta donde se encuentran las grabaciones WAV
folder_path = 'C:/Users/jacop/Desktop/murmur/DATAS4/WAVTRANSITORIO'

# Carpeta donde se guardarán las imágenes
output_folder = 'C:/Users/jacop/Desktop/murmur/DATAS4/IMAGENES JPG'

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Procesar cada archivo en la carpeta de entrada
for filename in os.listdir(folder_path):
    if filename.endswith('.wav'):
        file_path = os.path.join(folder_path, filename)
        save_path = os.path.join(output_folder, filename.replace('.wav', '.jpg'))
        graficar_audio(file_path, save_path)

print("¡Proceso completado!")