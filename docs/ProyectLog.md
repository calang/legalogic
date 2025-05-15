# Proyect Log
Notes about progress made (or not) as the proyect evolved.

**Table of Contents**
<!-- TOC -->
* [Proyect Log](#proyect-log)
  * [2025-05-15 Summary, so far](#2025-05-15-summary-so-far)
    * [Motivation](#motivation)
    * [Architecture](#architecture)
    * [Progress](#progress)
<!-- TOC -->

## 2025-05-15 Summary, so far

### Motivation
The motivation for the proyect, as described in the main 
README.md file, is to
> develop an efficient, 
escalable process to produce logic-based mechanisms to 
answer questions on Costa Rica legislation.

### Architecture
The initial plan, is to use an architecture mostly based 
on logic, while nevertheless use the power of public 
Large Language Models (LLMs) as part of the process to 
ingest and process data.

The overall architecture is this:
```text
Legal Texts (Costa Rica) 
   ↓
Text Extraction (pdfminer, spaCy)
   ↓
Syntactic Parsing (spaCy, CoreNLP)
   ↓
Information Extraction (Rules + Patterns)
   ↓
Logical Form Encoding (Prolog / ASP)
   ↓
Symbolic Reasoner (SWI-Prolog / Clingo)
   ↓
Answers to Questions (GUI or CLI)
```

### Progress
Ran initial trial tests, using `Flair` and 
`spaCy`.

`spaCy` seems to be more complete and produces different 
types of labels on the text, so we focused on it first.

When looking at the first experiments on 
`data/preprocessed/constitucion_sent_cr.txt`, using 
`src/legalogic/sandbox/entity_recog.py`, we found that 
the dependency parse trees often don't show a verb as 
its root node (which we expected to use as part of the 
predicate generation).  Here is an example:

![img.png](images/spaCy_dep_parse_tree.png)

Other items caught our attention, like the fact that 
"es", is 
classified as 
an "AUX" part-of-sentence (POS) and not a verb, despite 
using a Spanish 
language model for the analysis (`es_core_news_lg`).

As an alternative, we decided to look into using 
"Constituency-Based (Phrase Structure) Parse Trees" 
instead of Dependency-Based Parse Trees, as 
distinguished in [here](https://www.perplexity.ai/search/in-a-natural-language-parse-tr-gSlqZxCmTDig_8v4U.N.EQ).

A future challenge might be identifying related entities 
occurring in different sentences, though.

**Note**: Stanza has a [model for entity coreference](https://stanfordnlp.github.io/stanza/coref.html) for Spanish.
