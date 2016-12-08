# ADS Final Project

Term: Fall 2016

+ Team Name: Data Kings
+ Projec title: Music Genius
+ Team members
	+ Guanzhong You (gy2224)
	+ Yinxiang Gao (yg2424)
	+ Chencheng Jiang (cj2451)
	+ Wenhang Bao (wb2304)
	+ Chang Liu (cl3388)

+ Project summary: This project is the last project of Applied Data Science. The objective is to generate a melody with RNN-LSTM model, with or without specifying the starting part of the wanted melody. 
	+ Data: 
	1. Hand-made data: We got the melody data from [public website](http://www.popiano.org/big5/piano/). The raw data is in .ove format, which contains music score information. We first transformed them into MID format, then into ABC notation format. 
	2. Ripe data: In [ABC notation](http://http://abcnotation.com/), we used R crawler to get the data. In [Notingham Music](http://abc.sourceforge.net/NMD/) We copied and pasted them together. 
	
		+ ABC notation is our input. It's a shorthand form of musical notation, which uses the letters A through G to represent the given notes, with other elements used to place added value on these - sharp, flat, the length of the note, key, ornamentation. To know more about [ABC notation](https://en.wikipedia.org/wiki/ABC_notation). A typical ABC notation is like: 
	![screenshot]()
	
	+ Model: We used Recurrent Neural Network to generate("predict") the melody. We chose this method because it creates an internal state of the network. Unlike feedforward neural networks, RNNs can use their internal memory to process arbitrary sequences of inputs. We chose the LSTM, a kind of recurrent neural network to train the model because it can well capture the notation dependency. A simple demo is:
	![screenshot](https://github.com/TZstatsADS/Fall2016-proj5-proj5-grp1/blob/master/doc/RNN.png)
	
	+ Model setting and training: We used Long Short-Term Memory (LSTM) RNN model with 2 hidden layers, 128 nodes in each hidden layer, 100 epoch and 50 chars memory. The logistic function as our loss function. 
	![screenshot](https://github.com/TZstatsADS/Fall2016-proj5-proj5-grp1/blob/master/doc/loss_function.png)
	
	+ Generation: We generated the melody based on a given piece of melody(which could be empty though). Users are also allowed to choose the music style. We offered four chioces: Nottingham, Chinese Pop, Chinese Shange and ACG. Each generator is a RNN-LSTM model trained with the musics from that style. 
	
	+ Result: Here are some examples we generated. If you want to listen more, please look at the output folder.
	
	+ Further improvement: In order to predict a more beautiful melody, we could improve by: 
		+ Add more data and styles in the training step, and select better music.
		+ Adjust the parameter in the training model----with more data we can allow a larger network
		
**Contribution statement**: ([default](doc/a_note_on_contributions.md)) All team members contributed equally in all stages of this project. All team members approve our work presented in this GitHub repository including this contributions statement. 

Following [suggestions](http://nicercode.github.io/blog/2013-04-05-projects/) by [RICH FITZJOHN](http://nicercode.github.io/about/#Team) (@richfitz). This folder is orgarnized as follows.

```
proj/
├── lib/
├── data/
├── doc/
├── figs/
└── output/
```

Please see each subfolder for a README file.
