import pvporcupine
from pvrecorder import PvRecorder
from const import ACCESS_KEY


def start_wake():
    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keywords=['porcupine'],
        sensitivities=[1]
    )
    recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    recorder.start()
    result = False
    while True:
        pcm = recorder.read()
        keyword_index = porcupine.process(pcm)
        if keyword_index == 0:
            result = True
            porcupine.delete()
            recorder.delete()
            return result

            

    


