# Sentiment-Analysis

This repository contains the data that was used in support of the HCC 2019 paper [Analyzing Sentiments of German Job References](XXXXXXXXXXXXXXXXXXX).

Authors: Finn Folkerts, Vanessa Schreck, Shirin Riazy and Katharina Simbeck

Published at: more information will follow

For more information on our research group, please go to https://iug.htw-berlin.de/. 

Content of the Repository
-------------------------

German Job Reference Corpus: 
We compiled a test corpus of 843 typical German job reference letter sentences from German books on how to write job reference letters. We combined those template sentences with subjects of varying gender, origin and nobility. To create the German Job Reference Corpus, we combined each template sentence with each of the 30 different surnames and both gender specific titles. This yields 60 distinct sentences originating from the same template. Additionally, we altered each template sentence by replacing the title and surname with the corresponding male or female pronoun, thus adding another two sentences per template to the corpus.
Eventually, the corpus consists of 52,266 sentences in total, out of which 1,686 sentences are formed with a pronoun instead of a name.

Sentiment Analysis: 
We have tested the sentiment of all sentences in the corpus using 4 standard, commercially available sentiment analysis APIs: 
Google: https://cloud.google.com/natural-language/
AWS: https://aws.amazon.com/comprehend
IBM: https://www.ibm.com/watson/services/natural-language-understanding/
Azure: https://azure.microsoft.com/en-en/services/cognitive-services/

The sentiments collected from each service in July 2019 are available in /results. 

The scripts used to analyse those sentiment scores are available as python scripts. 


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
