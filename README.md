
# 3d brain tumor scanner

## requirements
Preinstalled software
 * Anaconda 
 * python 3.9.** 
 * cuda 11.2 
 * cdnn 8.1.0

Installing dependencies :

```console
conda create --name env python=3.9
```

```console
conda activate env
```
```console
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
```
```console
pip install tensorflow-gpu==2.10.0
```
```console
pip install numpy==1.21.0
```
```console
conda install anaconda::pandas
```
```console
pip install tqdm
```
```console
conda install anaconda::scikit-learn
```
```console
conda install scikit-image
```
```console
conda install conda-forge::matplotlib
```
```console
conda install anaconda::jupyter
```

Testing gpu enable

```console
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```
## configuring trainnig dataset
```python
python dataGen.py
```
## running segmentation.ipynb
 * Output model_v2.keras
 * training weights (per epoche)
