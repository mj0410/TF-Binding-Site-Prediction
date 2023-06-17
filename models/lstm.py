# -*- coding: utf-8 -*-
"""LSTM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pebx7CqkANtCHxMPF1q9LY5Tzx750IE5
"""

from keras.metrics import Precision, Recall, TruePositives

!pip install Biopython

import tarfile
import pandas as pd
import numpy as np
import re
from datetime import datetime

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from keras.wrappers.scikit_learn import KerasClassifier

from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dropout, Activation, Flatten
from keras.layers import Embedding, LSTM, Dense, Bidirectional

from matplotlib import pyplot as plt

from Bio.Seq import Seq
from Bio import SeqIO

"""### Read data"""

filename = "training_data_v2.tar.gz"

data = tarfile.open(filename, "r:gz")
data.extractall()
data.close()

b = open('GRHL1_TCCAAC20NTA_Q_3.fasta','r')
bind = b.readlines()
b.close()

u = open('GRHL1_TCCAAC20NTA_Q_3_shuffled.fasta','r')
unbind = u.readlines()
u.close()

"""### Data preprocessing"""

bind = [v for v in bind if '>' not in v]
bind = [s.replace('\n', '') for s in bind]
bind = [x.upper() for x in bind]

unbind = [v for v in unbind if '>' not in v]
unbind = [s.replace('\n', '') for s in unbind]
unbind = [x.upper() for x in unbind]

print(len(bind), len(unbind))

"""Reverse Complement"""

bind_rev = list(range(len(bind)))

for i in range(len(bind)):
  seq = Seq(bind[i])
  rev = seq.reverse_complement()
  bind_rev[i] = str(rev)

unbind_rev = list(range(len(unbind)))

for i in range(len(unbind)):
  seq = Seq(unbind[i])
  rev = seq.reverse_complement()
  unbind_rev[i] = str(rev)

bind_fb = bind + bind_rev
unbind_fb = unbind + unbind_rev

bind_label = [1 for i in range(len(bind_fb))]
unbind_label = [0 for i in range(len(unbind_fb))]

bind_dict = {"seq":bind_fb, "label":bind_label}
unbind_dict = {"seq":unbind_fb, "label":unbind_label}

bind_df = pd.DataFrame(bind_dict)
unbind_df = pd.DataFrame(unbind_dict)

df = pd.concat([bind_df, unbind_df])

"""##### split the dataset"""

from sklearn.utils import shuffle

new_df = shuffle(df)
new_df = new_df.reset_index()

x = new_df.seq
y = new_df.label

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=40)

"""##### One-hot Encoding"""

LE = LabelEncoder()
LE.fit(['A', 'C', 'G', 'T', 'N'])

start = datetime.now()

for index, row in x_train.items():
  x_train[index] = LE.transform(list(row))

for index, row in x_test.items():
  x_test[index] = LE.transform(list(row))

x_train = to_categorical(x_train.values.tolist())
x_test = to_categorical(x_test.values.tolist())

y_train = to_categorical(y_train.values.tolist())
y_t = to_categorical(y_test.values.tolist())

end = datetime.now()
print("encoding running time : "+str(end-start))

"""### RNN model

LSTM
"""

model = Sequential()
model.add(LSTM(64, return_sequences=True))
model.add(LSTM(64, return_sequences=True))
model.add(LSTM(64))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(2, activation='sigmoid'))

from keras.metrics import Precision, Recall, TruePositives
model.compile(optimizer='adam', loss="binary_crossentropy", metrics=[TruePositives(name='tp'), 'accuracy'])

history = model.fit(x_train, y_train, epochs = 10, validation_split = 0.2)

"""##### Evaluation

Accuracy
"""

score = model.evaluate(x_test, y_t)
print("accuracy = " + str(round(score[2],4)))

"""loss-epoch curve"""

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('LSTM Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['train', 'val'], loc='upper right')
plt.show()

"""precision-recall curve"""

probs = model.predict(x_test)[:,1]

precision, recall, thresholds = precision_recall_curve(y_test.values, probs)

from sklearn.metrics import auc
pr_auc = auc(recall, precision)

plt.plot(recall, precision)

plt.title('LSTM Precision-Recall Curve (AUC = ' + str(round(pr_auc,4)) + ')')

plt.xlabel('Recall')
plt.ylabel('Precision')

plt.show()

"""ROC curve & AUC"""

auc = roc_auc_score(y_test.values, probs)
fpr, tpr, _ = roc_curve(y_test.values, probs)

plt.plot(fpr, tpr)
plt.title('LSTM ROC Curve (AUC = ' + str(round(auc,4)) + ')')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()

"""save the result"""

result_dict = {'accuracy': score[2], 'loss': history.history['loss'], 'val_loss': history.history['val_loss'],
               'precision': precision, 'recall': recall, 'tpr': tpr, 'fpr': fpr, 'auc': auc, 'pr_auc': pr_auc}
result_df = pd.DataFrame({ key:pd.Series(value) for key, value in result_dict.items() })
result_df.head()

result_df.to_csv ('LSTM_result.csv', index = False, header=True)