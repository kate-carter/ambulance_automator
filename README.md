#listens to a live audio feed (fire control) and based on token proximity, determines and prints whether a district ambulance
#is needed to complete a call.  DeepSpeech (Mozilla) is the model used for speech -> text due to its performance in noisy
#environments.  ChatGPT 3.5 was used as a copilot for some of the scripting. Intended for use in apparatus tracking for a Vol. fire
#district.  Will print "District Ambulance [insert specific ambulance requested] Requested" if conditions have been met such that
#a volunteer ambulance is needed.
