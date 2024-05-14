# opinion_mining

Based on the code (fixed and expanded by me) and data of the paper "Bidirectional Machine Reading Comprehension for Aspect Sentiment Triplet Extraction, AAAI 2021" (https://arxiv.org/pdf/2103.07665.pdf)
Based on the data from https://github.com/xuuuluuu/SemEval-Triplet-data/tree/master/ASTE-Data-V1-AAAI2020

Authors: 	Shaowei Chen, Yu Wang, Jie Liu, Yuelin Wang

#### Requirements:

```
  python==3.6.9
  torch==1.2.0
  transformers==2.9.0
```

#### Original Datasets:

You can download the 14-Res, 14-Lap, 15-Res, 16-Res datasets from https://github.com/xuuuluuu/SemEval-Triplet-data.

#### Data Preprocess:

```
  python dataProcess.py
  python makeData_dual.py
  python makeData_standard.py
```

#### How to run:

```
  python main.py --mode train # For training
```

## TBD
1. packaging - Poetry
2. training data
3. model storage
4. code formatting - Black
5. code linting - Flake8
6. logging
7. translate and evaluate more languages

## Most urgent things
1. https://github.com/chiayewken/Span-ASTE - re-write the project in sklearn-style, still sticking to the most up-date library versions as possible
2. Consider alternatives for https://pypi.org/project/allennlp/

## Dockerization
1. docker build -t opinion_mining_api .
2. docker run -d --name opinion_mining_api_container -p 4999:4999 opinion_mining_api
3. docker run -d --restart unless-stopped --name opinion_mining_api_container -p 4999:4999 opinion_mining_api
4. docker logs [XXX]
