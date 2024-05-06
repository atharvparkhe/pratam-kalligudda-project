import io, librosa
import numpy as np
import tensorflow as tf


def preprocess_audio_mfcc(audio_file, target_length=50000, noise_level=0.001):
    audio, sr = librosa.load(audio_file, sr=16000)
    audio_smoothed = np.convolve(audio, np.ones(3) / 3, mode='same')
    audio_normalized = audio_smoothed / np.max(np.abs(audio_smoothed))
    if len(audio_normalized) < target_length:
        audio_normalized = np.pad(audio_normalized, (0, target_length - len(audio_normalized)))
    else:
        audio_normalized = audio_normalized[:target_length]
    mfccs = []
    mfcc = librosa.feature.mfcc(y=audio_normalized, sr=sr, n_mfcc=13)
    mfccs.append(mfcc)
    mfccs = np.array(mfccs)
    return mfccs


def predict_result(aud):
    # file_path = aud
    # with open(file_path, 'rb') as file:
    #     audio_data = file.read()
    # audio_stream = io.BytesIO(audio_data)
    # print("######")
    # print(audio_stream)
    # print("######")
    mfcc = preprocess_audio_mfcc(audio_file=aud)
    model = tf.keras.models.load_model('prediction_accuracy.keras')
    predicted_accuracy_scores = model.predict(mfcc)
    # audio_stream = io.BytesIO(audio_file)
    # print(predicted_accuracy_scores[0][0])
    return predicted_accuracy_scores[0][0]

res = float(predict_result("audio.mp3"))
print(type(res))
print(res)