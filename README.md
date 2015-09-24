Fall 2015 5539 Course Project
=====================

The purpose of the project is to give you the opportunity to interact with some of the datasets and methods discussed in the papers we are reading in class.

In general it takes a lot of time and effort to build these datasets (gathering data, processing with NLP tools, etc...) before you can start doing anything interesting, so we are making several datasets available for you to use for the class project.  You are highly encouraged, though not required to use these datasets.

Freebase Data:
--------------

Unfortunately <a href='https://www.freebase.com/'>Freebase</a> was recently shut down, though we have provided some data in a simplified (easy-to-use) file format in <a href='freebase_data'>freebase_data</a>.  Some examples are below:

	      ['championship', 'super bowl', 'indianapolis colts', u'2007-02-04']
	      ['championship', 'world series', 'boston red sox', u'2007-10-28']
	      ...

	      ['death', 'lynn margulis', 'amherst', u'2011-11-22']
	      ['death', 'hermann zapf', 'darmstadt', u'2015-06-04']
	      ...

	      ['acquired', 'rakuten', 'viber media', u'2014-02-13']
	      ['acquired', 'reliance mediaworks', 'digital domain', u'2012-09-21']
	      ...

In each case, a tuple is listed which consists of a relation, a pair of entities involved, and an associated date.

This data can be used, for example to train weakly supervised relation extractors.

Twitter Data:
--------------

One interesting text datasource to work with is Twitter data.  We have prepared a ~20GB Twitter dataset which is marked up with NLP various annotations (named entities, parts of speech, chunk tags, etc...).
Please email the instructor if you would like to get access to this data for your project.  This dataset will take a while to download, so you will probably want a stable network connection.

The data in the file looks like so (we have included a script to parse this file...):

	73874844944576513       293001188       None ||| None   2011-05-26 22:15:10     NONE    jonesy  band    @femme_italian question of the day , whos driving ? Or we could do the bus ... but I may meet benny ova at jonesy 's house ... hmmmm    DT NN IN DT NN , NNS VBG . CC PRP MD VB DT NN : CC PRP MD VB JJ NN IN NNP POS NN : UH   O O O O O O O O O O O O O O O O O O O O O O O B-ENTITY:1.0023403050300423 O O O O   O O O O O O O O O O O O O O O O O O O B-EVENT:1.523767267512175 O O O O O O O O
	77819992959234048       48505146        N/S Long Beach  ||| Mountain Time (US & Canada) 2011-06-06 12:31:46     201107  cali    person  @djlooneygoham rame was in cali for like a month , he moves back homie in sep . and ill be home in july , lets get it im super ready    USR NN VBD IN NNP IN IN DT NN , PRP VBZ RB VB IN NN . CC PRP VB RB IN NNP , VBP VB PRP PRP JJ JJ    O O O O B-ENTITY:1.8183467735342191 O O O O O O O O O O O O O O O O O O O O O O O O O   O O B-EVENT:1.0007622159164486 O O O O O O O O O O B-EVENT:1.1422257305270844 O O O O O O O O O O O B-EVENT:1.4444396211254773 O O O O
	82643783413534720       280264181       where you want to be ||| Quito  2011-06-19 21:59:48     20110619        thomas  person  @xlaurenjessica random thought .... did i tell u i was watching thomas the train this morning ( don't ask ) and he was doing thriller   USR JJ NN : VBD PRP VBP PRP PRP VBD VBG IN DT NN DT NN ( NNS VBP NN CC PRP VBD VBG NN   O O O O O O O O O O O B-ENTITY:1.7957479935747933 O O O O O O O O O O O O O O O O O B-EVENT:1.0444165745255347 O B-EVENT:1.475778180536863 O O O B-EVENT:1.1211997855839266 O O O O O O O O O O O B-EVENT:2.088356747818362 O O
	84486336219844608       200933015       georgia ||| Central Time (US & Canada)  2011-06-24 23:01:26     NONE    raven   company @theyBElikeBRE raven told sum boy bout the party and he asked where it was and stuff and he thought it was today and he went LMAO !!    USR NNS VBD DT NN IN DT NN CC PRP VBD WRB PRP VBD CC NN CC PRP VBD PRP VBD NN CC PRP VBD UH .   O B-ENTITY:1.353389320634097 O O O O O O O O O O O O O O O O O O O O O O O O O      O O B-EVENT:1.0200540968343 O O O O O O O B-EVENT:1.395541271253109 O O B-EVENT:1.0692245061116836 O O O O B-EVENT:1.689899325069979 O O O O O B-EVENT:1.0051872483557573 O O
	58184041773539328       14480092        New York, NY    2011-04-13 15:05:31     NONE    lolla-  product @monicaobrien re : Lolla- loved it last year- amazing line up . With the 20th anniversary , hopefully they bring some oldies back !     USR NNP : NNP VBD PRP RB DT JJ NN RP . IN DT JJ NN , RB PRP VB DT PRP$ NN .     O O O B-ENTITY:1.1005604301105234 O O O O O O O O O O O O O O O O O O O O   O O O O B-EVENT:1.0021667550708797 O O O O O O O O O O O O O O O O O O O

The fields are as follows:

* tweet id
* user id
* location ||| timezone (from the user’s profile)
* date / time the tweet was written
* Reference date of temporal expression (using TempEx)
* Named entity
* NE type
* tokenized words
* Parts of speech
* Named entity tags
* event phrase tags


One possible project would be to combine these datasets and train a weakly supervised relation (or event) extractor for Twitter.  To give an example of how you might get started doing this, the python script
<a href='match_twitter.py'>match_twitter.py</a> reads in the Freebase data, then iterates through the Twitter data and identifies messages that mention pairs of entities participating in one of the relations.
Example output is <a href='sample_matches'>here</a> (you probably don't want to use this output, but instead modify the script...)
Have a look at this <a href='http://web.stanford.edu/~jurafsky/mintz.pdf'>paper</a> for more details.  A good machine learning package for python is <a href='http://scikit-learn.org/stable/'>scikit-learn</a>.

Annotated Gigaword:
-------------------

Another (newswire) dataset is annotated gigaword: https://catalog.ldc.upenn.edu/LDC2012T21
Email the instructor for access.

Freebase-match NYT dataset
-------------------

If you are not so interested in doing feature extraction steps and want to get directly to implementing algorithms, there is also a relation extraction dataset (Freebase + new york times data) with features already extracted from <a href='http://people.cs.umass.edu/~lmyao/papers/riedel10modeling.pdf'>this paper</a>.

Other Datasets:
----------------------------------

Some other large marked-up text datasets are available here: http://deepdive.stanford.edu/doc/opendata/

You are also encouraged to explore other potential structured data sources as weak supervision as well, for instance <a href='https://www.nlm.nih.gov/research/umls/knowledge_sources/metathesaurus/'>UMLS Metathesaurus</a> for text in the biomedical domain.
