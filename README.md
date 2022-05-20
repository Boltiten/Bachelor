# Bachelor

There are 3 main steps for running the model.

First you need data.
Then you must process the data.
Finally you train on the data.



Filedownloader
______________________________________________________________________________________________
You start off by running the rssreader.py located in the filedownloader folder.
rssreader.py takes 3 arguments
  1. url of the rss feed you found
  2. language of the podcast you are downloading, we just shorthands like nor for Norwegian og de for Deutsch
  3. name of the podcast
2. and 3. is used to name the files you download, so its easy to recognize what files you have.
There is an variable named download location which currently goes to my ssd, but that can be changed to whatever place you want.
_______________________________________________________________________________________________



Conversion
_______________________________________________________________________________________________
Run massAudioDif.py to segment the audio into ads and podcasts
Run ConvertToWav.py to convert segments into wave format, this better for the data later.

Both massAudioDif.py and ConvertToWav.py needs the location of the podcasts as an argument, for example:

python3 ConvertToWav.py "D:/Podcasts"

This is an important break, here you will have to balance the dataset such that you do not have a over representation of podcast compared to advertisements.
The data can be up to 95% podcast, so you will have to chose some to remove from the training set.
You can also chose very spesific data to keep here, for example only all the english advertisements, this is useful for checking generalization.

Run ConvertToData.py to futher convert these files to readable data for the model, this will store the data in a .npy.
You will get two files from the previous step, one will be the x_train dataset, which is the sounddata itself, and one which is the y_train set,
which consists of the information about the data if it is an advertisement or if it is a podcast.
You can also chose if you want to convert using mel-spectrograms or mfcc, we recommend using mel-spectrograms.

_______________________________________________________________________________________________


Train the model
_______________________________________________________________________________________________
You can now train the model. If you are not doing spesific tests, we reccomend using the model_v2_folding.ipynb,
as that model allowes for folding of the datasets, giving more results.

If you are testing for spesific data, f.eks. holding out the norwegian advertisements, use Model_v3.

Finished. Hope you had cool results. :)
