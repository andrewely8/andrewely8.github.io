This project involves fine tuning the LLM Qwen2.5-Math-1.5B

Our fine tuning method was LoRA with Unsloth.

Base model link: https://huggingface.co/unsloth/Qwen2.5-Math-1.5B

We explored fine tuning the model to count the number of integer solutions to linear inequalities over a domain.
We found the model had a baseline performance of 25% accuracy on our test set, which improved to 82.5% accuracy after fine tuning.

Also, we explored fine tuning the model to preform better with AIME math problems.
We found the model had a baseline performance of 10% accuracy on AIME 2025, which we were not able to improve after fine tuning.
We highlight the fallbacks of our methods when trying to fine tune for AIME problem solving.

link to project website: https://andrewely8.github.io/


files                              description
---------------------------------------------------------------------------------------------
generateData.py                    Python script to generate our train/val/test data.
test.json                          Test data set containing 40 data points.
train_400.json                     Train data set with 400 data points.
train_2000.json                    Train data set with 2,000 data points.
validation.json                    Validation data set, containing 40 data points.
fineTuning.ipynb                   Notebook file used in Google Colab to fine tune our model.
index.html                         HTML source code for our project website.
paper.pdf                          Our paper writeup for the project.
video.mp4                          A video summarizing our project.
README.txt                         This readme file.