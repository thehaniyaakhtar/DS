# Data Leakage
# Training dataset is used to create a model
# same dataset is not going to be available when the model is used 
# Target Leakage
# future data (not in test dataset) is included in training data
# eg: if someone has taken an antibiotic, it must mean they might have pneumonia
# Train Test Contamination
# Happens when validation data is accidentally used during training 
