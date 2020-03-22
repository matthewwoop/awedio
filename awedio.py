import argparse
import wave

import numpy as np


def read_wave(filename):
    '''
        reads a wave file and returns a numpy representation
    '''

    with wave.open(filename, 'rb') as wav:
        n_channels = wav.getnchannels()
        n_frames = wav.getnframes()
        sample_width = wav.getsampwidth()
        frame_rate = wav.getframerate()
        frames = wav.readframes(n_frames)

    print(n_frames, sample_width, type(frames))
    return frames


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-i',
                    '--wav_file',
                    default='./wav_samples/16bit.F.M3.wav',
                    help='Path to input audio file')
    args = ap.parse_args()

    print('Reading {}'.format(args.wav_file))
    frames = read_wave(args.wav_file)
    print(len(frames))
