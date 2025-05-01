#loading required modules and DeepSpeech
import pandas as pd
import deepspeech
model_path = "path/to/deepspeech-0.9.3-models.pbmm"
scorer_path = "path/to/deepspeech-0.9.3-models.scorer"
ds = deepspeech.Model(model_path)
ds.set_scorer(scorer_path)
audio_path = "path/to/audio.wav"
#speech to text transcription
with open(audio_path, "rb") as audio_file: #insert audio file
    audio_data = audio_file.read()
    text = ds.stt(audio_data)
print("Transcription:", text)
#Lookit all them ambulances
#EMS ambulances (True = in service)
E883 = True
E884 = True
E882 = True
#District ambulances
W840 = True
H823 = True
OP885 = True
OP881 = True
#Token analysis in text transcript (is 884 out/in)
if E884 = True:
    def is_884_out(text, E884, out):

        tokens = text.split()
        index1 = tokens.index(E884) if E884 in tokens else -1
        index2 = tokens.index(out) if out in tokens else -1
        result = index1 != -1 and index2 != -1 and abs(index1 - index2) <= proximity
        return result
    stat_884 = is_884_out(text, E884, out, proximity)
    if stat_884 = True: E884 = False
    text = "placeholder"
    E884 = "884"
    out = "out", "going", "responding", "out of service"
    proximity = 3, 2, 1
else :
    def is_884_in(text, E884, inservice):
        tokens = text.split()
        index3 = tokens.index(E884) if E884 in tokens else -1
        index4 = tokens.index(E884) if inservice in tokens else -1
        stat_884 = index3 != -1 and index4 != -1 and abs(index3 - index4) <= proximity
        return stat_884
    stat_884 = is_884_in(text, E884, inservice, proximity)
    if stat_884 = True: E884 = True
    text = "placeholder"
    E884 = "884"
    inservice = "back in town, available", "back in town available", "in service"
if E883 = True:
    def is_883_in(text, E883, out)
        tokens = text.split()
        index5 = tokens.index(E883) if E883 in tokens else -1
        index6 = tokens.index(out) if out in tokens else -1
        stat_884 = index5 != -1 and index6 != -1 and abs(index5 - index6) <= proximity
        return stat_883
    stat_883 = is_883_in(text, E883, out, proximity)
    if stat_884 = True: E883 = True
    text = "placeholder"
    E883 = "883"
    out = "out", "going", "responding", "out of service"
else:
    def is_883_in(text, E883, inservice):
        tokens = text.split()
        index7 = tokens.index(E883) if E883 in tokens else -1
        index8 = tokens.index(E883) if inservice in tokens else -1
        stat_883 = index7 != -1 and index8 != -1 and abs(index7 - index8) <= proximity
    return stat_883
        stat_883 = is_883_in(text, E883, inservice, proximity)
        if stat_883 = True: E883 = True
    text = "placeholder"
    E883 = "883"
    inservice = "back in town, available", "back in town available", "in service"
