# References

These are references compiled during the planning of the 
project.

**Contents**
<!-- TOC -->
* [References](#references)
  * [Recommendations from LLM Systems](#recommendations-from-llm-systems)
  * [Libraries](#libraries)
    * [Flair](#flair)
    * [spaCy](#spacy)
    * [Stanza](#stanza)
    * [Stanford CoreNLP](#stanford-corenlp)
    * [TextBlob](#textblob)
    * [FreeLing](#freeling)
  * [Tools](#tools)
  * [Languages and Frameworks](#languages-and-frameworks)
  * [Knowledge Graphs](#knowledge-graphs)
    * [How to Convert Any Text Into a Graph of Concepts](#how-to-convert-any-text-into-a-graph-of-concepts)
    * [Text to Knowledge Graph Made Easy with Graph Maker](#text-to-knowledge-graph-made-easy-with-graph-maker)
  * [Projects with similar Objectives](#projects-with-similar-objectives)
  * [Articles](#articles)
    * [Support for Logic-based approach](#support-for-logic-based-approach)
    * [Parsing](#parsing)
    * [Simplified NL](#simplified-nl)
    * [ASP](#asp)
    * [Other](#other)
  * [More References](#more-references)
  * [Resource Lists](#resource-lists)
    * [Legal Text Analytics](#legal-text-analytics)
    * [Legal Natural Language Processing](#legal-natural-language-processing)
<!-- TOC -->

## Recommendations from LLM Systems
Compiled [here](Recom_from_LLMs.md).


## Libraries

### Flair
A very simple framework for state-of-the-art NLP. Developed by Humboldt University of Berlin and friends.
* [On Github](https://github.com/flairNLP/flair)
* [Flair Documentation Page](https://flairnlp.github.io/docs/intro) - Initial tutorials.
* [Latest release](https://github.com/flairNLP/flair/releases): 0.15.1, Feb 5 2025

### [spaCy](https://spacy.io)
  * A popular open-source NLP library with 
    support for Spanish. It provides tokenization, entity recognition, language modeling, and more.
    * → POS tagging, dependency parsing.
  * [Usage](https://spacy.io/usage)
  * [Mastering spaCy - Second Edition](https://learning.oreilly.com/library/view/mastering-spacy/9781835880463/)
  * [NLP_APP](https://github.com/sharonreshma/NLP_APP)
    * This Streamlit-based application leverages spaCy, a leading NLP library, to perform advanced text processing tasks. Users can analyze text by tokenizing, visualizing part-of-speech tags, identifying named entities, and performing lemmatization.
  * [NLP Pipeline with SpaCy & TextBlob](https://github.com/AqueeqAzam/Complete-NLP-pipeline-using-SpaCy)
    * This project implements a Natural Language Processing (NLP) pipeline using SpaCy and TextBlob. It covers text processing, named entity recognition (NER), sentiment analysis, rule-based matching, and more, making it useful for chatbots, search engines, sentiment analysis, and text summarization.

### [Stanza](https://stanfordnlp.github.io/stanza)
Another powerful NLP library with support for 
  Spanish, providing high-performance, streamlined processing of text data.

[Universal Dependencies](https://universaldependencies.org/)

### Stanford CoreNLP
Supports Spanish; excellent for 
parsing, dependency analysis (important for logical structure).
  * → Deeper constituency parsing (phrases and clauses).

### [TextBlob](https://github.com/sloria/TextBlob)
  * [https://textblob.readthedocs.io/en/dev/](https://textblob.readthedocs.io/en/dev/)
  * TextBlob is a Python library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, and more.

### [FreeLing](https://nlp.lsi.upc.edu/freeling/)
  * Could not install it in Ubuntu 24.10 - Oracular Oriole*

  FreeLing is a C++ library providing language analysis functionalities (morphological analysis, named entity detection, PoS-tagging, parsing, Word Sense Disambiguation, Semantic Role Labelling, etc.) for a variety of languages (English, Spanish, Portuguese, Italian, French, German, Russian, Catalan, Galician, Croatian, Slovene, among others).


## Tools

* **pdfminer.six** or Apache Tika for extracting text.


## Languages and Frameworks

* **Prolog**: a logic programming language that's well-suited 
for implementing rule-based systems.
  * **SWI-Prolog** is a popular open-source implementation.
* **Answer Set Programming (ASP)**: another logic programming 
  paradigm that can be used for knowledge representation and reasoning.
  * **Clingo** is a popular open-source ASP solver.
  * **ASP in Swi-Prolog**
    * [s(CASP) SWISH site](https://swish.swi-prolog.org/example/scasp.swinb)
    * [s(CASP) for SWI-Prolog](papers/sCASP for Swi-Prolog gdeinvited4.pdf)
      * Jan Wielemaker, Joaquín Arias and Gopal Gupta4 
        https://ceur-ws.org/Vol-2970/gdeinvited4.pdf

* **Datalog** Engines like `LogicBlox` (if you need database integration)
* **RDFlib (for RDF triples)**: a simple, 
widely-used format for representing knowledge graphs.
* **OWLAPI (for ontologies)**: more complex knowledge representation 
  frameworks that define concepts, relationships, and rules.


## Knowledge Graphs
### [How to Convert Any Text Into a Graph of Concepts](https://towardsdatascience.com/how-to-convert-any-text-into-a-graph-of-concepts-110844f22a1a/)
### [Text to Knowledge Graph Made Easy with Graph Maker](https://towardsdatascience.com/text-to-knowledge-graph-made-easy-with-graph-maker-f3f890c0dbe8/)


## Projects with similar Objectives

* **The OASIS project**: an open-source framework for legal 
knowledge representation and reasoning.
* **LegalRuleML**: an XML-based language for representing 
  legal rules and regulations.
* [Legal-ES](papers/Legal-ES-2020.lt4gov-1.6.pdf). This is an open source resource kit 
specifically for Spanish legal text processing
* **LegalNLP**
  * [Article](https://www.academia.edu/79909964/LegalNLP_Natural_Language_Processing_methods_for_the_Brazilian_Legal_Language)
  * [Repo](https://github.com/felipemaiapolo/legalnlp)
* [Connecting Symbolic Statutory Reasoning with Legal 
Information Extraction](https://aclanthology.org/2023.nllp-1.12.pdf)
* Frameworks like **PROLEG** have been used for formalizing laws and reasoning with legal facts in logic programming, integrating fact extraction with symbolic reasoning.
  * [pdf](papers/paper2LPLR.pdf)
  * [Beyond Logic Programming for Legal Reasoning](https://ceur-ws.org/Vol-3437/paper2LPLR.pdf)
* **LeXeMe** (Legal Knowledge Extraction in Multilingual 
  Environments) — EU project, open source, but it's mostly English-focused.


## Articles
### Support for Logic-based approach
* [Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools](https://arxiv.org/abs/2405.20362)
  * Design and report on the first preregistered 
    empirical evaluation of AI-driven legal research 
    tools. We demonstrate that the providers' claims are 
    overstated. While hallucinations are reduced 
    relative to general-purpose chatbots (GPT-4), we 
    find that the AI research tools made by LexisNexis 
    (Lexis+ AI) and Thomson Reuters (Westlaw AI-Assisted 
    Research and Ask Practical Law AI) each 
    **hallucinate between 17% and 33% of the time**, May 
    2024 .
* [Why a Logic Programming Approach Works for Automating Insurance Contracts](https://law.stanford.edu/2023/03/10/why-a-logic-programming-approach-works-for-automating-insurance-contracts/)
* [Towards Robust Legal Reasoning: Harnessing Logical 
  LLMs in Law](https://arxiv.org/html/2502.17638v1), Feb 
  2025 .
  * OpenAI o1 achieved a score of 77.6% on LegalBench 
    Guha et al. (2023); Vals.ai (2025), a benchmark comprising a diverse set of tasks on various legal domains, leaving much room for improvement.
* [Logically Consistent Language Models
via Neuro-Symbolic Integration](https://arxiv.org/pdf/2409.13724)
* [Logic Rules as Explanations for Legal Case Retrieval](https://arxiv.org/abs/2403.01457)
* [Neuro-Symbolic AI in 2024: A Systematic Review]
  (https://arxiv.org/pdf/2501.05435), Apr 2025.  [pdf](papers/NeuSyIn2024-2501.05435v2.pdf).
* [ConceptNet 5.5: An Open Multilingual Graph of General Knowledge](https://arxiv.org/abs/1612.03975)


### Parsing
* [In-Order Transition-based Constituent Parsing](papers/In-Order%20Transition-based%20Constituent%20Parsing-%20Q17-1029.pdf)
  * or from [In-Order Transition-based Constituent Parsing](https://aclanthology.org/Q17-1029/)
  * constituency parser model used by Stanza
  * [code](https://github.com/LeonCrashCode/InOrderParser)
* [NLP with Stanza: Guide to an NLP package for many languages](https://pythonology.eu/guide-to-nlp-with-stanza-stanfordnlp/)
  * Examples of using Stanza for different types of 
    analyses.
* Retrieval-Augmented Semantic Parsing: Using Large Language Models to Improve Generalization
  * [pdf](papers/Retrieval-Augmented Semantic Parsing Using Large Language Models to Improve Generalization 2412.10207v1.pdf)
  * https://arxiv.org/html/2412.10207v1
### Simplified NL
* [Lexpresso: a Controlled Natural Language](papers/Lexpresso-1407.1933v1.pdf) (also: https://arxiv.org/pdf/1407.1933)
* [XAI-LAW Towards a logic programming tool for taking
and explaining legal decisions](https://ceur-ws.org/Vol-3733/short3.pdf)
  * [pdf](papers/XAI-LAW.pdf)
  * Project aiming at producing a semi-automated tool 
    for legal reasoning in the Italian criminal system 
    during the criminal trial stage
  * Criminal _law encoding_ is carried on, currently, _by humans_
* [SemEval-2023 Task 6: LegalEval - Understanding Legal Texts](papers/2023.semeval-1.318.pdf)
  * From https://aclanthology.org/2023.semeval-1.318.pdf
* [Coupling Large Language Models with Logic 
Programming for Robust and General Reasoning from Text](papers/Coupling Large Language Models with Logic Programming for Robust and General Reasoning from Text 2307.07696v1.pdf)
  * From: Joohyung Lee  [v1] Sat, 15 Jul 2023 03:29:59 
    UTC (2,765 KB) https://arxiv.org/abs/2307.07696
* [Weakly supervised semantic parsing with abstract examples](papers/Weakly supervised semantic parsing with abstract examples P18-1168.pdf)
  * Omer Goldman, Veronica Latcinnik, Ehud Nave, Amir
  Globerson, and Jonathan Berant. 2018. **Weakly supervised semantic parsing with abstract examples**. In
  Proceedings of the 56th Annual Meeting of the As-
  sociation for Computational Linguistics (Volume 1:
  Long Papers), pages 1809–1819.
  https://aclanthology.org/P18-1168/

### ASP
* [ASP-based legal decision explanation systems](https://ceur-ws.org/Vol-3733/short3.pdf)
  * Criminal law encoding: this stage is currently carried on by humans
* [Answer set programming](papers/answer-set-programming-978-3-030-24658-7_compress.pdf)
  * Vladimir Lifschitz. 2019. Answer set programming. Springer Heidelberg
  https://link.springer.com/book/10.1007/978-3-030-24658-7#toc
* [Answer set programming - Wikipedia](https://en.wikipedia.org/wiki/Answer_set_programming)
* Constraint Answer Set Programming without Grounding
  * [pdf](papers/answer-set-programming-978-3-030-24658-7_compress.pdf)
  * https://www.cambridge.org/core/journals/theory-and-practice-of-logic-programming/article/constraint-answer-set-programming-without-grounding/55A678C618EF54487777F021D89B3FE7
* [Stable model semantics - Wikipedia](https://en.wikipedia.org/wiki/Stable_model_semantics)
### Other
* [PROLEG and deep learning integration for legal reasoning](https://arxiv.org/pdf/2306.16632.pdf)
* [LawGiBa: Combining GPT, knowledge bases, and Prolog for legal assistance](https://ebooks.iospress.nl/doi/10.3233/FAIA230991)
  * [pdf](papers/FAIA-379-FAIA230991.pdf)
  * A proof-of-concept demonstration system for legal 
    assistance.
  * We demonstrate how incorporating a legal knowledge 
    base and logical reasoning can enhance the accuracy 
    and reliability of legal advice provided by AI models like GPT
* [Alda: Integrating Logic Rules with Everything Else, Seamlessly](https://www.cambridge.org/core/journals/theory-and-practice-of-logic-programming/article/integrating-logic-rules-with-everything-else-seamlessly/43F7B71F2B4A27FAB6BFF7EFC0C58EF6)
  * This paper presents a language, Alda, that supports all of logic rules, sets, functions, updates, and objects as seamlessly integrated built-ins. 
* [Natural language processing in the era of large language models](papers/Natural language processing in the era of large language models frai-06-1350306.pdf)
  * SPECIALTY GRAND CHALLENGE article
Front. Artif. Intell. , 11 January 2024
Sec. Natural Language Processing
Volume 6 - 2023 | https://doi.org/10.3389/frai.2023.1350306



## More References
Emilia Oikarinen and Tomi Janhunen. 2006.
_Modular equivalence for normal logic programs_. In 17th European Conference on Artificial Intelligence(ECAI),
pages 412–416.

Joseph Babb and Joohyung Lee. 2012. _Module theorem for 
the general theory of stable models_. Theory and
Practice of Logic Programming, 12(4-5):719–735.


## Resource Lists

### [Legal Text Analytics](https://github.com/Liquid-Legal-Institute/Legal-Text-Analytics)

### [Legal Natural Language Processing](https://github.com/maastrichtlawtech/awesome-legal-nlp)





