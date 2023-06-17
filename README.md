# Transcription Factor Binding Site Prediction using ML
- Apply ML to predict Transcription Factor Binding Site (TFBS)
- Compare different types of neural networks
- Train the models with grainyhead-like 1 (GRHL1) TFBS sequences obtained by HT-SELEX
- Visualize what the model learns from given sequences

<br/>

### Model Architecture
<img src="./IMAGE/architecture.jpg" width="700"><br/>
- Build 5 different neural network models
- Hyperparameter tuning by [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

<br/>

### Result
##### 1. Receiver operating characteristic (ROC) curve and precision-recall (PR) curve and The area under the curve (AUC) of both curves<br/>
<br/>
<img src="./IMAGE/curves.jpg" width="600"> <br/>
<br/>

##### 2. Loss curve of models by each epoch <br/>
<br/>
<img src="./IMAGE/loss.jpg" width="600"><br/>
<br/>

##### Visualization
<img src="./IMAGE/innvestigate.jpg" width="600"><br/>
- Heatmap shows the importance of each nucleotide for determining the class of a given sequence.
- The top of it shows GRHL1 canonical motif from [JASPAR](https://jaspar.genereg.net/matrix/MA0647.1/).
