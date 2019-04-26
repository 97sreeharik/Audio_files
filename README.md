# Speech_recognition in Malayalam
This is our final year project for our B-tech degree.In this project we tried to make a malayalam interaction module that is trained for college receptionist rorbot.
 The intercation module is capable recognizing malayalam speech from the context and respond to it(in malayalam).

## <a name="team-members"></a>Team Members
* Gokul P
* Ashique
* Sreehari K
* Sandra
## Things to be done before running interaction module
Firstly download the latest libraries of the following:
* [SphinxBase](http://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha)
* [PocketSphinx](http://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha)
* [SphinxTrain](http://sourceforge.net/projects/cmusphinx/files/sphinxtrain/5prealpha)

For more details head over to [CMUSphinx Download](http://cmusphinx.sourceforge.net/wiki/download)
After downloading extract them to corresponding folders, then istall them using:

In a unix-like environment (such as linux, solaris etc):

* ran "autogen.sh" at least once, then compile and install each:

```bash
$ ./autogen.sh
```
```bash
 $ ./configure
 $ make clean all
 $ make check
 $ sudo make install
```
Now, download the zip of this repository, extract and open terminal inside the "response_final" folder which is inside the "output_mapping" folder.

run simple_recognizer.py with python2.7 . (make sure u change the model directory path in the code)

## what are the folders and whats inside them :

* Malayalam_acoustic_model _new_limited	: This folder contains acoustic model files which are made with sphinx tools for limited context audio recordings and transcriptions
* Malayalam_acoustic_model : This folder have acoustic model files generated similarly as before but with large dataset which made by combining our dataset and data set created by [Sreenath](https://github.com/sreecodeslayer/ml-am-lm-cmusphinx#ml-am-lm-cmusphinx)
* Malayalam_language model : It contains Language model which made with tools of sphinx and data collected by Sreenath
* Malayalam_new_language model : This languge model is made with data made by us for our context.
* output_mapping : This folder contains the final acoustic model and language model and python script for interaction module.
* Documentation : This folder contains all the documentation done on the project
