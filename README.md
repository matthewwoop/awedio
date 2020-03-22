# Awedio

A signal processing toolbox made to sound nice.

## Things to keep in mind

#### WAV file encoding

The python `wave.open` will barf on a `wav` file with an encoding greater than
16 bits.

When exporting from Ableton however, my default encoding is 24 bits, so to
convert the encodings you can turn to `sox` or `ffmpeg`

```bash
brew install sox

sox ./wav_samples/F.M3.wav -b 16 -e signed-integer ./wav_samples/16bit.F.M3.wav
```

```bash
sudo apt update
sudo apt install ffmpeg

ffmpeg -i ./wav_samples/F.M3.wav --audio_rate 44100 --audio_channels 1 --audio_codec pcm_s16le ./wav_samples/16bit.F.M3.wav
```
