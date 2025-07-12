from deepspeech import Model

# import numpy as np
# import wave

model_path = 'mozillaDeepSpeech/deepspeech-0.9.3-models.pbmm'
lm_path = 'mozillaDeepSpeech/deepspeech-0.9.3-models.scorer'
beam_width = 500
lm_alpha = 0.75
lm_beta = 1.85

model = Model(model_path)
model.enableExternalScorer(lm_path)
model.setScorerAlphaBeta(lm_alpha, lm_beta)
model.setBeamWidth(beam_width)