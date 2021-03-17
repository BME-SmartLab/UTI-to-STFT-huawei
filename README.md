# UTI-to-STFT experiment with Atlas 800 9010(Ubuntu 18.04)

Tamás Gábor Csapó, Csaba Zainkó, László Tóth, Gábor Gosztolya, and Alexandra Markó, ,,Ultrasound-based Articulatory-to-Acoustic Mapping with WaveGlow Speech Synthesis'', Interspeech 2020. arXiv:2008.03152


## Original Network Link

https://github.com/BME-SmartLab/UTI-to-STFT

## Pre-trained Model Link

Download the keras model file 
- http://smartlab.tmit.bme.hu/csapo/huawei/UTI_to_STFT_CNN_model.h5

Download the sample ultrasound file
- http://smartlab.tmit.bme.hu/csapo/huawei/20180223_spkr048_1432.ult128

## keras-to-tensorflow .pb
- https://github.com/amir-abdi/keras_to_tensorflow

```
keras_to_tensorflow.py --input_model=UTI_to_STFT_CNN_model.h5  --output_model=UTI_to_STFT_CNN_model.pb
```

## Convert model To Ascend om file

