import const
import azure.cognitiveservices.speech as speechsdk

class AzureManager():

    def __init__(self,voice,lan) -> None:
        self.speech_config = speechsdk.SpeechConfig(subscription=const.SUBSCRIPTION, region=const.REGION)
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        self.speech_config.speech_synthesis_voice_name=voice
        self.speech_config.speech_recognition_language=lan


    def azure_speak(self, text):
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=self.audio_config)
        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return True
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(cancellation_details.reason))
            
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
            return False

    def azure_listen(self):
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config)
        result = speech_recognizer.recognize_once_async().get()
        return result.text