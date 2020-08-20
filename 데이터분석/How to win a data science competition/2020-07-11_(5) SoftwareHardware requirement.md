## Software & Hardware Requirement

### Hardware

- Most of competitions (expect image-based) can be solved on :
  - High-level laptop
  - 16+ gb ram
  - 4+ cores
- Quite good setup :
  - Tower PC
  - 32+ gb ram
  - 6+ cores



#### Really import things:

- RAM
  - If you can keep data in memory - everything will be much easier
- Cores
  - More cores you have - more (of faster) experiments you can do
- Storage
  - SSD is crucial if  you work with images or big datasets with a lot of small pieces



#### Cloud resources

Cloud platforms can provide you with a computational resources.

There are several cloud options :

- Amazon AWS (spot option ??)
- Microsoft Azure
- Google cloud



### Software

Most of competitors use Python data science software stack.

- Basic stack : Numpy, Pandas, scikit-learn, matplotlib
- IDE : Jupyter notebook
- Special packages : XGBoost, Keras, LightGBM, tsne
- External tools
  - Vowpal Wabbit : 거대한 데이터셋을 핸들링할 때 유용
  - libfm, libffm : sparce한 CTR 데이터를 다룰 때 유용
  - fast_rgf : 또 다른 tree-based 방법



## Additional Material and Links

## StandCloud Computing:

- [AWS](https://aws.amazon.com/), [Google Cloud](https://cloud.google.com/), [Microsoft Azure](https://azure.microsoft.com/)

## AWS spot option:

- [Overview of Spot mechanism](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
- [Spot Setup Guide](http://www.datasciencebowl.com/aws_guide/)

## Stack and packages:

- [Basic SciPy stack (ipython, numpy, pandas, matplotlib)](https://www.scipy.org/)
- [Jupyter Notebook](http://jupyter.org/)
- [Stand-alone python tSNE package](https://github.com/danielfrg/tsne)
- Libraries to work with sparse CTR-like data: [LibFM](http://www.libfm.org/), [LibFFM](https://www.csie.ntu.edu.tw/~cjlin/libffm/)
- Another tree-based method: RGF ([implemetation](https://github.com/baidu/fast_rgf), [paper](https://arxiv.org/pdf/1109.0887.pdf))
- Python distribution with all-included packages: [Anaconda](https://www.continuum.io/what-is-anaconda)
- [Blog "datas-frame" (contains posts about effective Pandas usage)](https://tomaugspurger.github.io/)