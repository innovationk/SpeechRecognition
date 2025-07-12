A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.2.6 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.

If you are a user of the module, the easiest solution will be to
downgrade to 'numpy<2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.

Traceback (most recent call last):  File "/Users/kim/Dev/InnovationK/SpeechRecognition/whisper/main.py", line 1, in <module>
    import whisper
  File "/Users/kim/.pyenv/versions/3.12.11/lib/python3.12/site-packages/whisper/__init__.py", line 8, in <module>
    import torch
  File "/Users/kim/.pyenv/versions/3.12.11/lib/python3.12/site-packages/torch/__init__.py", line 1477, in <module>
    from .functional import *  # noqa: F403
  File "/Users/kim/.pyenv/versions/3.12.11/lib/python3.12/site-packages/torch/functional.py", line 9, in <module>
    import torch.nn.functional as F
  File "/Users/kim/.pyenv/versions/3.12.11/lib/python3.12/site-packages/torch/nn/__init__.py", line 1, in <module>
    from .modules import *  # noqa: F403
  File "/Users/kim/.pyenv/versions/3.12.11/lib/python3.12/site-packages/torch/nn/modules/__init__.py", line 35, in <module>
    from .transformer import TransformerEncoder, TransformerDecoder, \
  File "/Users/kim/.pyenv/versions/3.12.11/lib/python3.12/site-packages/torch/nn/modules/transformer.py", line 20, in <module>
    device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),
/Users/kim/.pyenv/versions/3.12.11/lib/python3.12/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at /Users/runner/work/pytorch/pytorch/pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)
  device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),
Traceback (most recent call last):
  File "/Users/kim/Dev/InnovationK/SpeechRecognition/whisper/main.py", line 4, in <module>
    model = whisper.load_model("base")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/kim/.pyenv/versions/3.12.11/lib/python3.12/site-packages/whisper/__init__.py", line 159, in load_model
    model.set_alignment_heads(alignment_heads)
  File "/Users/kim/.pyenv/versions/3.12.11/lib/python3.12/site-packages/whisper/model.py", line 282, in set_alignment_heads
    mask = torch.from_numpy(array).reshape(
           ^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: Numpy is not available