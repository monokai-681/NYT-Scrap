# NYT scapped bilingual corpus MT Evaluation Project

Project integrity disclaimer:

Mr. Wang Yun, "mogita", is a highly skilled full-stack developer based in Singapore and a long-time friend of mine. As the commit history suggests, mogita provided assistance in the development of an ad hoc Python scraper and offered verbal guidance on file organization methodologies. However, it is important to note that **mogita was not involved in any capacity in the corpora processing or the machine translation evaluation tasks.** He has never been asked or expected to do so, nor does he possess the expertise in these tasks.

## Overview

This is a Machine Translation Evaluation project for the June 2023 Exam for the Machine Translation course at University of Bologna.

The project starts with an ad hoc Python scraper based on Beautifulsoup to build **a parallel corpus of English and human-translated Simplified Chinese of political news from The New York Times Chinese site.** The date range is from 2020 to June 2023.

**A parallel corpus of 25k pairs of segments is obtained, with 1.1m English words and 2m Chinese characters**. Later, 12k pairs of segments are used as the training data, 0.3k paris as tuning, and 0.5k as test data. ModernMT is used to train an adapted MT system to improve the MT translation quality. Finally, COMET, BERTScore, and BLEU are used for Automatic Evalution, and a manual evalution is also added.

Unfortunately, the improvement can only be described as modest according to Automatic Evaluation indicators. A manual evaluation is also done, which demostrates that there is some subtle improvement in the translation output of the Adapted MT, particularly in word order, thus resulting a higher Fluency evalution.

## Folder structure and file description

### Python scrapers
The Python scraper programme is situated in the root folder:
- `links.py` obtains links according to two regular expressions to obtain political news from The New York Times Chinese site.
- The obtained links are then put in links_china.csv and links_world.csv.
- `articles.py` scrapes the body text from individual pages.
- `sample_page_unminified.html` is a unminifield sample page to aid project development.
- environment.yml provides a dependency list for Python environment configuration

### Corpora


Corpora are in the `corpora` folder. The original obtained corpus are in two formats:
1. `Original_scrap_output_25k.csv`
2. `Original_scrap_output_25k.xlsx`

The original corpus are then divided into:
1. `Corpus_main_12k.xlsx`, which is also converted into `12k main-2358211.tmx` translation memory exchange file and used as the Training Data.
2. `Corpus_Tuning_and_Test_3.6k_marked_with_colours.xlsx`; all other sub-corpora with `Test` and `Tuning` are from this file, whose names are self-explainatory.
3. `Corpus_unused_10k.xlsx`, as a backup resource.


### Evaluation files

Evaluation files are in the `evaluations` folder.
- Four single-language `.txt` files from the `Corpus_Test_0.5k` sub-corpus, with the source, reference (human-translation), Baseline MT output, and Adapted MT output.
- Four Jupyter notebook files from two evalution models.
- `ibleu_2023-06-16_21-47-36` is the BLEU evalution result output file.
- `Manual Evaluation.xlsx` is the 1-4 scale manual evalution of two MT output.
- `diffchecker-exported-pdf` is a report file by DiffChecker app to highlight the discrepancies between the `Baseline` and the `Adapted` text files.

## Automatic Evaluation Results

There is only some modest improvments by the Adapted MT output measured by the Automatic Evaluation methods.

* BERTScore model does not reveal any improvement nor deterioration in the Adatped MT output, as both Baseline and Adapted evaluated `0.873` against the Reference.
* COMET model indicates that the Adapted MT only improved microscopically, as it measures at `0.849` against Baseline's `0.848`.
* BLEU even shows some deterioration, as the Adapted MT measured `5.86` against Baseline's `5.90`.

*I would like to point out that as a native speaker of Chinese, I disagree some of the scorings by BLEU on the individual segment level.*

## Manual Evalution

The manual evalution does give more credit to the Adapted MT output, but the improvement is still insignificant.

The manual evalution is done on a 1 to 4 scoring scale to both outputs, on both Adequacy and Fluency dimensions. In all 519 segments, there are only 78 segments with discrepancies. The other 441 identical segment pairs are removed from the evaluation.

For Adequacy, the the Adapted MT output scores 211 against the Baseline's 208; improvment is slightly more pronounced in the Fluency department, as Adapted MT scores 239 against Baseline's 226.

However, if all segement pairs are considered, and the default evaluation of the identical segments is 2.5, the Adapted MT scores, in the Fluency:

```math
441 * 2.5 + 239 = 1341.5
```
while the Baseline scores:
```math
441 * 2.5 + 226 = 1328.5
```

If we consider the 1-4 scoring scale as linear, the improment is about
```math
1341.5 / 1328.5  - 1 ≈ 1\%
```


---

Manual evaluation
- Some inevitable bias towards Adapted translation, even through the improvement is *microscopical*.
- MT output's fluency is better when the sentences are shorter. However, there isn't much difference between the Fluency between two MT outputs.
- 
#UniBo/MT