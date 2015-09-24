Fall 2015 5539 Course Project
=====================

The purpose of the project is to give you the opportunity to interact with some of the datasets and methods discussed in the papers we are reading in class.

In general it takes a lot of effort to get (gathering data, processing with NLP tools, etc...) so we are making several datasets available for you to use for the class project.  You are highly encouraged, though not required to use these datasets.

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

One possible project would be to combine these datasets and train a weakly supervised relation (or event) extractor for Twitter.  To give an example of how you might get started doing this, the python script
<a href='match_twitter.py'>match_twitter.py</a> reads in the Freebase data, then iterates through the Twitter data and identifies messages that mention pairs of entities participating in one of the relations.
Have a look at this <a href='http://web.stanford.edu/~jurafsky/mintz.pdf'>paper</a> for more details.

Annotated Gigaword:
-------------------

Another (newswire) dataset is annotated gigaword: https://catalog.ldc.upenn.edu/LDC2012T21

Other Datasets:
----------------------------------

Some other large marked-up text datasets are available here: http://deepdive.stanford.edu/doc/opendata/

You are also encouraged to explore other potential structured data sources as weak supervision as well.

