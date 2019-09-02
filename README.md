# Sentiment-Analysis

This repository contains the data that was used in support of the HCC 2019 paper [Analyzing Sentiments of German Job References](XXXXXXXXXXXXXXXXXXX).

Authors: Finn Folkerts, Vanessa Schreck, Shirin Riazy and Katharina Simbeck

Published at: more information will follow

For more information on our research group, please go to https://iug.htw-berlin.de/. 

Content of the Repository
-------------------------

We compiled a test corpus with typical German job reference letter sentences from German books on how to write job reference letters. We combined those template sentences with subjects of varying gender, origin and nobility.
To find suitable surnames for our experiment, we looked up the lists of members of the German state parliaments. Then we mapped the names to their origins and randomly picked ten German surnames, ten German surnames with nobiliary
particle and ten Turkish surnames. Following a literature review, we collected 843 different sentences that are commonly used in German job references.To compile the German Job Reference Corpus, we combined each template sentence with each of the 30 different surnames and both gender specific titles. This yields 60 distinct sentences originating from the same template. Additionally,
we altered each template sentence by replacing the title and surname with the corresponding male or female pronoun, thus adding another two sentences per template to the corpus.
Eventually, the corpus consists of 52,266 sentences in total, out of which 1,686 sentences are formed with a pronoun instead of a name.



Literature
----------

The literature from which we took the sentences which we then transformed into template sentences are:

* H.-G. Dachrodt and V. Engelbert, _Zeugnisse richtig formulieren: Mit
vielen Mustern und Analysen_. Wiesbaden: Springer Gabler, 2013.

* G. Huber and W. Müller, _Das Arbeitszeugnis in Recht und Praxis:
Rechtliche Grundlagen, Textbausteine, Musterzeugnisse, Zeugnisanalysen_,
16th ed. Haufe-Lexware GmbH & Co. KG, 2016.

* S. Schustereit and J. Welscher, _Arbeitszeugnisse für den öffentlichen
Dienst_, 2nd ed. München: Haufe-Lexware GmbH & Co. KG, 2013.

* T. Knobbe, M. Leis, and K. Umnuß, _Arbeitszeugnisse für
Führungskräfte_, 5th ed. Freiburg, Br.: Haufe, 2010.

* T. Knobbe, M. Leis, and K. Umnuß, _Arbeitszeugnisse: Textbausteine und Tätigkeitsbeschreibungen_,
6th ed. München: Haufe-Lexware GmbH & Co. KG, 2011.


Project
-------

The present research was done as part of the project [*Diskriminiert durch Künstliche Intelligenz* (Discriminated by Artificial Intelligence)](https://iug.htw-berlin.de/?page_id=92 "Discriminated by Artificial Intelligence - Website")
at Hochschule für Technik und Wirtschaft (University of Applied Sciences) Berlin under the direction of [Katharina Simbeck](https://iug.htw-berlin.de/?page_id=230 "Katharina Simbeck - Website").
This research project was funded by [Hans-Böckler-Stiftung](https://www.boeckler.de/ "Hans-Böckler-Stiftung - Website").

#### Hochschule für Technik und Wirtschaft
HTW Berlin,
10313 Berlin (Postfach)

#### Hans-Böckler-Stiftung
Hans-Böckler-Straße 39,
40476 Düsseldorf 


Authors
-------

* **Finn Folkerts** - *HTW Berlin* - [Email](mailto:folkerts@htw-berlin.de)
* **Vanessa Schreck** - *HTW Berlin* - [Email](mailto:schreckv@htw-berlin.de)
* **Shirin Riazy** - *HTW Berlin* - [Email](mailto:riazys@htw-berlin.de)
* **Katharina Simbeck** - *HTW Berlin* - [Email](mailto:simbeck@htw-berlin.de)


License
-------

Please refer to our LICENSE file for this information.


Citing
------

If you found this repository or our paper helpful please consider citing us with this bibtex.  

```

@inproceedings{folkerts2019,
  author =       {Folkerts, Finn and Schreck, Vanessa and Riazy, Shirin and Simbeck, Katharina},
  title =        {Analyzing Sentiments of German Job References},
  crossref =     {hcc2019},
  pages =        {??--??},
  doi =          {???},
}

@proceedings{hcc2019,
  editor =       {???},
  title =        "???",
  booktitle =    "???(gleich wie title)",
  publisher =    {???}
  venue =        {Laguna Hills, California, USA},
  month =        sep,
  year =         {2019},
  isbn =         {???},
}

```
