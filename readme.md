# NYT scapped bilingual corpus MT Evaluation Project

Project integrity disclaimer:

Mr. Wang Yun, "mogita", is a highly skilled full-stack developer based in Singapore and a long-time friend of mine. As the commit history suggests, mogita provided assistance in the development of an ad hoc Python scraper and offered verbal guidance on file organization methodologies. However, it is important to note that**mogita was not involved in any capacity in the corpora processing or the machine translation evaluation tasks.** He has never been asked or expected to do so, nor does he possess the expertise in these tasks.

## Overview

This is a Machine Translation Evaluation project for the June 2023 Exam for the Machine Translation course at University of Bologna.

The project starts with an ad hoc Python scrapper based on Beautifulsoup to obtain body texts from New York Times Chinese bilingual pages, to build a parallel corpus in English and human translated Simplified Chinese.

A parallel corpus of 25k pairs of segments is obtained. Later, 12k pairs of segments are used as the training data, 0.3k paris as tuning, and 0.5k as test data. ModernMT is used to train an adapted MT system to improve the MT translation quality. Later, COMET, BERTScore, and BLEU are used for Automatic Evalution.

Unfortunately, the improvement can only be described as modest according to Automatic Evaluation indicators. A manual evaluation is also done, which demostrates that there is some subtle improvement in the translation output of the Adapted MT, particularly in word order, thus resulting a higher Fluency evalution.

## Folder structure and file description

### Python scrappers

### Corpora

### Evaluation files

## Automatic Evaluation Results

## 

In all 519 segments, there are 79 segments with differences. The improvement is microscopical. 

Manual evaluation
- Some inevitable bias towards Adapted translation, even through the improvement is *microscopical*.
- MT output's fluency is better when the sentences are shorter. However, there isn't much difference between the Fluency between two MT outputs.
- 
#UniBo/MT