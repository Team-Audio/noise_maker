import argh

from effect_pipeline import EffectPipeline
from wavfile import read_wavfile, write_wavfile
from whitenoise import WhiteNoiseEffect
from noise50hz import FiftyHertz


# def noise_gen(length=1, volume=0.5):
# whitenoise = gen_white_noise_noise(length, volume)
# write_wavfile('noise.wav', whitenoise, 44100)


def renoise(arg: str, *args: str):
    # you can change what is applied here
    pipeline = EffectPipeline([
        WhiteNoiseEffect(),
        FiftyHertz()
    ])

    elements = [arg, *args]

    for elem in elements:
        rate, width, data = read_wavfile(elem)
        data, rate, width = pipeline.run(data, rate, width)
        write_wavfile('modified' + elem, data, rate, width)


if __name__ == '__main__':
    argh.dispatch_command(renoise)
