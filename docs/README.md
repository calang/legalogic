# Docs

## Development Approach

### Recommendations from LLM Systems

#### Prompt
I want to develop a system that reads legal text in Spanish, for Costa Rica law and derives  a series of facts and rules that can layer be used by a symbolic reasoning system using Logic Programming, to answer questions related to the text. Some example question may a form such as "are there any contradictions in this body of laws?", or "is it legal or allowed to do such and such".

Act as an AI expert in Natural Language Processing and Understanding and either a) recommend a fully open source system that has the described capability, or b) describe the main components and steps to build such a system, using open source frameworks only. 

#### Meta AI's answer

##### Initial answer
[4/26, 05:53] Meta AI: Developing a system to extract facts and rules from legal text in Spanish and apply symbolic reasoning is a challenging task. I'll outline the main components and steps to build such a system using open-source frameworks.

*System Overview*

The proposed system consists of the following components:

1. *Natural Language Processing (NLP)*: to analyze and understand the legal text.
2. *Information Extraction (IE)*: to extract relevant facts and rules from the text.
3. *Knowledge Representation (KR)*: to represent the extracted knowledge in a structured format.
4. *Symbolic Reasoning (SR)*: to apply logical rules and answer questions.

*Component 1: NLP*

For Spanish NLP tasks, you can use:

- *spaCy*: a popular open-source NLP library with support for Spanish. It provides tokenization, entity recognition, language modeling, and more.
- *Stanza*: another powerful NLP library with support for Spanish, providing high-performance, streamlined processing of text data.

*Component 2: IE*

For extracting facts and rules, you can use:

- *Rule-based approach*: define regular expressions or use libraries like *spaCy's Matcher* to extract specific patterns from the text.
- *Machine Learning-based approach*: train models using annotated datasets to extract relevant information. Libraries like *spaCy's EntityRuler* or *Stanza's NER* can be fine-tuned for this purpose.

*Component 3: KR*

To represent the extracted knowledge, you can use:

- ** triples (subject-predicate-object)**: a simple, widely-used format for representing knowledge graphs.
- ** ontologies**: more complex knowledge representation frameworks that define concepts, relationships, and rules.

For implementing KR, you can use libraries like *RDFlib* (for RDF triples) or *OWLAPI* (for ontologies).

*Component 4: SR*

For symbolic reasoning, you can use:

- *Prolog*: a logic programming language that's well-suited for implementing rule-based systems. *SWI-Prolog* is a popular open-source implementation.
- *Answer Set Programming (ASP)*: another logic programming paradigm that can be used for knowledge representation and reasoning. *Clingo* is a popular open-source ASP solver.

*System Steps*

1. *Text Preprocessing*: clean and normalize the legal text using NLP libraries.
2. *Fact Extraction*: apply IE techniques to extract relevant facts and entities.
3. *Rule Extraction*: extract rules and regulations using IE techniques or manual annotation.
4. *Knowledge Representation*: represent the extracted knowledge in a structured format (e.g., triples or ontologies).
5. *Symbolic Reasoning*: implement a rule-based system using Prolog or ASP to apply logical rules and answer questions.

*Open-Source System Recommendation*

While there isn't a single, fully open-source system that meets all your requirements, you can combine the above components to build a system that suits your needs. Some projects that might be worth exploring are:

- *The OASIS project*: an open-source framework for legal knowledge representation and reasoning.
- *LegalRuleML*: an XML-based language for representing legal rules and regulations.

*Example Implementation*

Here's a high-level example of how you could implement the system using spaCy, RDFlib, and SWI-Prolog:
```
import spacy
from rdflib import Graph
import subprocess

Load Spanish NLP model
nlp = spacy.load("es_core_news_sm")

Process legal text
text = "Artículo 1. La ley establece..."
doc = nlp(text)

Extract facts and rules
facts = []
for ent in doc.ents:
    facts.append((ent.text, ent.label_))

Represent knowledge in RDF triples
g = Graph()
for fact in facts:
    g.add((fact[0], fact[1], fact[2]))

Serialize RDF graph
g.serialize("knowledge_graph.ttl")

Call SWI-Prolog to apply logical rules
subprocess.run(["swipl", "-f", "rules.pl", "-g", "consult('knowledge_graph.ttl')"])
```
This example is a starting point, and you'll need to develop a more comprehensive system to meet your specific requirements.

Keep in mind that building such a system will require significant development and testing efforts. You may need to adapt and extend existing open-source components to fit your specific use case.

##### Is the above a practical approach for avoiding hallucinations from an NLP system processing legal content?  Are there any more practical and effective approaches?
[4/26, 06:13]

The approach I outlined can help mitigate hallucinations in NLP systems processing legal content, but it may not be the most practical or effective approach for several reasons:

1. *Complexity*: The system requires multiple components, including NLP, IE, KR, and SR, which can lead to complexity and integration challenges.
2. *Domain expertise*: Legal domain expertise is essential for defining rules, annotating data, and validating the system's output.
3. *Data quality*: The system's performance relies heavily on the quality of the training data, which can be challenging to obtain and annotate in the legal domain.

More practical and effective approaches to avoiding hallucinations in NLP systems processing legal content might include:

1. *Constrained generation*: Use techniques like constrained decoding or structured prediction to ensure the generated text adheres to specific formats or templates.
2. *Fact-checking*: Implement fact-checking mechanisms to verify the accuracy of generated text against trusted sources or databases.
3. *Knowledge graph-based approaches*: Represent legal knowledge as a graph and use graph-based algorithms to generate text that is grounded in the graph's structure and content.
4. *Hybrid approaches*: Combine symbolic and neural AI approaches to leverage the strengths of both paradigms. For example, use neural networks for text generation and symbolic reasoning for validation and verification.
5. *Training data curation*: Carefully curate and annotate training data to ensure it is accurate, consistent, and relevant to the legal domain.
6. *Evaluation metrics*: Use evaluation metrics that prioritize factual accuracy, such as fact-based metrics or metrics that assess the system's ability to retrieve relevant information.
7. *Human oversight*: Implement human oversight and review processes to detect and correct hallucinations in generated text.

Some specific techniques that might be useful for avoiding hallucinations in legal NLP systems include:

1. *Named Entity Recognition (NER)*: Use NER to identify and extract specific entities (e.g., laws, regulations, court cases) and ensure they are accurately represented in generated text.
2. *Relation extraction*: Extract relationships between entities and use these relationships to inform generated text.
3. *Dependency parsing*: Analyze the grammatical structure of text to ensure generated text is syntactically correct and semantically meaningful.

Ultimately, the most effective approach will depend on the specific requirements and constraints of your project. It's essential to carefully evaluate different approaches and techniques to determine the best fit for your use case.

#### Perplexity AI's answer
[2025-04-26 13:34](https://www.perplexity.ai/search/i-want-to-develop-a-system-tha-f_U8hvLJST2_wEgdwfMxqQ)

To develop a system that reads Spanish legal texts (specifically Costa Rican law), extracts facts and rules, and enables symbolic reasoning with logic programming to answer questions such as contradictions or legality, you have two main paths: using existing open source resources or building a system from components. Below is a detailed expert recommendation based on open source frameworks and research.

1. Existing Open Source Resources for Spanish Legal Text Processing
* Legal-ES: This is an open source resource kit 
   specifically for Spanish legal text processing. It includes a very large corpus (over 1 billion words) of legislative and administrative documents in Spanish from various jurisdictions, along with pre-trained word embeddings and topic models tailored to legal language. The corpus is preprocessed with SpaCy, and embeddings are generated with Gensim, making it suitable for downstream NLP tasks like information extraction, semantic similarity, and topic navigation in legal texts.
   * [Legal-ES: A Set of Large Scale Resources for Spanish Legal Text Processing](https://aclanthology.org/2020.lt4gov-1.6/)
   * [Legal-ES: A Set of Large Scale Resources for Spanish Legal Text Processing](https://www.academia.edu/67138354/Legal_ES_A_Set_of_Large_Scale_Resources_for_Spanish_Legal_Text_Processing)
   * [Legal-ES: A Set of Large Scale Resources for 
     Spanish Legal Text Processing](https://aclanthology.org/2020.lt4gov-1.6.pdf)
   * [LegalNLP - Natural Language Processing methods for 
     the Brazilian Legal Language](https://www.academia.edu/79909964/LegalNLP_Natural_Language_Processing_methods_for_the_Brazilian_Legal_Language)

* LegalNLP: Although primarily focused on Brazilian 
Portuguese, LegalNLP offers methods and tutorials for legal text manipulation that could inspire similar approaches for Spanish legal texts.
  * [LegalNLP - Natural Language Processing Methods for the Brazilian Legal Language](https://github.com/felipemaiapolo/legalnlp)
  * [LegalNLP - Natural Language Processing methods for the Brazilian Legal Language](https://www.academia.edu/79909964/LegalNLP_Natural_Language_Processing_methods_for_the_Brazilian_Legal_Language)

These resources provide a solid foundation for Spanish legal language understanding and can be adapted or extended for Costa Rican law.

2. Main Components and Steps to Build the System Using Open Source Frameworks

A. Legal Text Preprocessing and Representation
Use SpaCy with Spanish language models to tokenize, lemmatize, and parse legal texts. SpaCy supports custom pipelines and can be extended with domain-specific models.

Apply Legal-ES embeddings or train domain-specific embeddings with Gensim on Costa Rican legal corpora to capture legal semantics.

Optionally, use topic modeling (e.g., LDA) to understand thematic structures in the texts.

B. Legal Information Extraction
Develop or fine-tune named entity recognition (NER) and relation extraction models to identify:

Legal entities (laws, articles, institutions)

Facts (case-specific details)

Rules and conditions stated in the law

This can be done by adapting transformer-based models (e.g., BERT multilingual or BETO for Spanish) fine-tuned on annotated legal datasets or using distant supervision from Legal-ES resources.
    * [Connecting Symbolic Statutory Reasoning with Legal 
Information Extraction](https://aclanthology.org/2023.nllp-1.12.pdf)

Use rule-based patterns to complement statistical models, especially for extracting logical conditions and legal references.

C. Formalization into Logic Programming
Translate extracted facts and rules into a logic programming language such as Prolog or Answer Set Programming (ASP).

Frameworks like PROLEG have been used for formalizing laws and reasoning with legal facts in logic programming, integrating fact extraction with symbolic reasoning.
* [Beyond Logic Programming for Legal Reasoning](https://ceur-ws.org/Vol-3437/paper2LPLR.pdf)

The process involves mapping natural language rules to logical predicates and facts, enabling queries like contradiction detection or legality checks.

D. Symbolic Reasoning and Query Answering
Use a logic programming engine (e.g., SWI-Prolog, Clingo for ASP) to:

Check for contradictions by querying conflicting rules or facts.

Determine legality by evaluating whether certain conditions satisfy legal rules.

Integrate the reasoning engine with the NLP pipeline to allow end-to-end question answering.

E. Optional: Deep Learning Integration
Enhance fact extraction accuracy by fine-tuning deep learning models on legal text queries and their corresponding logical representations.

Explore end-to-end models that combine information extraction and reasoning, though these are still research topics.

Summary Recommendation

Aspect | Tools/Resources | Purpose
----- | ----- | -----
Corpus & Embeddings | Legal-ES (SpaCy, Gensim) | Spanish legal text representation
NLP Pipeline | SpaCy (Spanish models), Transformer models (BETO) | Tokenization, NER, relation extraction
Information Extraction | Fine-tuned deep learning models + rule-based patterns | Extract facts and legal rules
Logic Programming | PROLEG framework, SWI-Prolog, ASP (Clingo) | Formalize and reason about laws/facts
Reasoning & Querying | Logic programming engines | Contradiction detection, legality queries

No fully integrated open source system currently exists that directly performs all these steps for Spanish legal texts and logic-based reasoning out-of-the-box. However, combining Legal-ES for language resources, SpaCy and transformer models for NLP, and PROLEG or other logic programming frameworks for reasoning provides a feasible and fully open source approach to build your system.
* https://aclanthology.org/2020.lt4gov-1.6/
* https://ceur-ws.org/Vol-3437/paper2LPLR.pdf
* https://aclanthology.org/2023.nllp-1.12.pdf

References to Support Development
Legal-ES: Large scale Spanish legal corpus and embeddings.
* https://aclanthology.org/2020.lt4gov-1.6/
* https://www.academia.edu/67138354/Legal_ES_A_Set_of_Large_Scale_Resources_for_Spanish_Legal_Text_Processing
* https://paperswithcode.com/paper/legal-es-a-set-of-large-scale-resources-for
* https://www.academia.edu/79909964/LegalNLP_Natural_Language_Processing_methods_for_the_Brazilian_Legal_Language

PROLEG: Logic programming framework for legal reasoning, integrating fact extraction with symbolic reasoning.
* https://ceur-ws.org/Vol-3437/paper2LPLR.pdf

Recent research on connecting legal information extraction with symbolic statutory reasoning shows high performance is achievable and critical for downstream reasoning tasks.
* https://aclanthology.org/2023.nllp-1.12.pdf


NLP tools like SpaCy and transformer models can be adapted for Spanish legal text processing.

This architecture will allow you to extract structured facts and rules from Costa Rican legal texts and perform symbolic reasoning to answer complex legal queries such as contradictions or legality assessments.

##### How can I integrate Legal-ES with a logic programming framework
To integrate Legal-ES-a large Spanish legal text corpus and embedding resource-with a logic programming framework for symbolic legal reasoning, you need to bridge natural language legal knowledge extraction and formal logic representation. The integration involves several key steps and components, combining NLP and logic programming tools:

1. Use Legal-ES for Legal Text Processing and Fact/Rule Extraction
Preprocessing and Embeddings: Use Legal-ES resources (SpaCy pipelines, word embeddings) to preprocess Costa Rican legal texts, including tokenization, lemmatization, and semantic representation. This step prepares the text for deeper analysis by capturing legal terminology and context in vector form.

Information Extraction: Apply or fine-tune NLP models (NER, relation extraction) on Legal-ES data to extract structured legal facts, entities (laws, articles, actors), and rules expressed in natural language. This can be enhanced by transformer models fine-tuned on Legal-ES or similar corpora.

2. Translate Extracted Facts and Rules into Logic Programming
Mapping to Logic Predicates: Convert extracted legal facts and rules into logical predicates suitable for a logic programming language such as Prolog or Answer Set Programming (ASP). For example, a legal rule expressed in Spanish can be formalized as a Prolog clause.

Frameworks: Use logic programming frameworks like PROLEG or standard Prolog engines (e.g., SWI-Prolog) or ASP solvers (e.g., Clingo). PROLEG is designed for legal reasoning and can integrate facts from text with symbolic reasoning.

3. Neuro-Symbolic Integration (Optional but Recommended)
Recent research advocates a neuro-symbolic approach that combines deep learning (LLMs) with logic programming. You can use LLMs to generate or assist in generating logic encodings of legal text extracted from Legal-ES, then validate and execute these in a logic programming environment to improve accuracy and explainability.
* https://arxiv.org/html/2502.17638v1

This approach can automate the transformation of natural language legal text into logic rules, with iterative correction via logic program execution feedback.

4. Reasoning and Query Answering
Once legal knowledge is encoded in the logic programming system, you can perform queries such as contradiction detection or legality checks by querying the logic engine.

The logic programming system can provide explanations for decisions, supporting transparency and trustworthiness.
* https://ebooks.iospress.nl/doi/10.3233/FAIA230991
* https://ceur-ws.org/Vol-3733/short3.pdf

Summary Workflow

Step | Tools/Resources | Description
----- | ----- | -----
Legal Text Processing | Legal-ES (SpaCy, embeddings) | Preprocess and extract semantic features from text
Information Extraction | Transformer models, rule-based patterns | Extract facts and rules from legal text
Logic Encoding | PROLEG, SWI-Prolog, Clingo | Map extracted info to logic predicates and rules
Neuro-Symbolic Assistance | LLMs + logic programming (e.g., SWISH) | Automate and refine logic encoding from text
Reasoning & Querying | Logic programming engines | Execute queries, detect contradictions, check legality

Practical Integration Tips
Start by preprocessing Costa Rican legal texts with Legal-ES pipelines to obtain clean, semantically rich representations.

Develop or adapt extraction models to identify legal statements and conditions.

Define a clear schema for mapping extracted elements to logic predicates (e.g., permits(action), prohibits(action), contradiction(rule1, rule2)).

Use PROLEG or SWI-Prolog to encode and reason over these predicates.

Consider leveraging LLMs fine-tuned on Legal-ES data to assist in generating logic encodings, then validate them with the logic engine to reduce errors.
* https://arxiv.org/html/2502.17638v1

Build an interface layer that connects NLP output to logic input and allows querying and explanation generation.

By combining Legal-ES’s rich Spanish legal language resources with a logic programming framework and optionally neuro-symbolic methods, you can create a robust system that extracts, formalizes, and reasons over Costa Rican legal texts effectively.

References:
* [Neuro-symbolic integration of LLMs and logic programming for legal reasoning](https://arxiv.org/html/2502.17638v1)
* [LawGiBa: Combining GPT, knowledge bases, and Prolog for legal assistance](https://ebooks.iospress.nl/doi/10.3233/FAIA230991)
* [PROLEG and deep learning integration for legal reasoning](https://arxiv.org/pdf/2306.16632.pdf)
* [ASP-based legal decision explanation systems](https://ceur-ws.org/Vol-3733/short3.pdf)

##### What are the best logic programming frameworks for integrating with Legal-ES

The best logic programming frameworks for integrating with Legal-ES, a Spanish legal text resource, are those that support formalizing legal rules and facts extracted from text, enable symbolic reasoning, and ideally facilitate neuro-symbolic integration with language models. Based on recent research and practical use cases, the following frameworks stand out:

Recommended Logic Programming Frameworks

Framework | Description & Strengths | Notes on Integration with Legal-ES and NLP
---- | ---- | ----
SWI-Prolog | A mature, widely used Prolog environment with extensive libraries and tooling. Supports symbolic reasoning and querying of legal rules. | Proven effective in legal reasoning projects (e.g., CodeX) and can be combined with NLP outputs from Legal-ES for logic encoding and querying. [1](https://arxiv.org/html/2502.17638v1) [4](https://law.stanford.edu/2023/03/10/why-a-logic-programming-approach-works-for-automating-insurance-contracts/) [5](https://openreview.net/forum?id=AsTWBjCvUt). Integrates well with LLMs for neuro-symbolic approaches [1].
Epilog | An extension of Prolog with enhanced expressivity and scope, used in legal automation projects like CodeX. | Provides richer expressivity for complex legal contracts and rules, suitable for detailed Costa Rican law formalization [4].
Answer Set Programming (ASP) (e.g., Clingo) | A declarative logic programming paradigm supporting non-monotonic reasoning, useful for modeling exceptions and conflicting rules. | Used in legal decision modeling and explanation tools (e.g., Italian criminal law modeling) with good support for explainability and inconsistency detection [7](https://ceur-ws.org/Vol-3733/short3.pdf).
s(CASP) | A top-down ASP solver with explanation capabilities, enabling justifications of legal decisions. | Useful for explainable legal reasoning, though with scalability trade-offs. Can complement Legal-ES extracted knowledge [7].
PROLEG | A legal reasoning framework integrating logic programming for formalizing laws and reasoning. | Designed specifically for legal text formalization and reasoning, can be adapted to work with Legal-ES extracted facts and rules [1].
ProSLM | A Prolog-based language model framework validating LLM outputs against domain-specific legal knowledge bases. | Enhances factual accuracy and interpretability by combining LLMs and Prolog for legal question answering [1].
Alda | A newer language integrating logic rules with sets, functions, and objects, supporting concurrent and distributed programming. | Allows seamless integration of logic rules with other programming paradigms, potentially useful for complex legal systems [6](https://www.cambridge.org/core/journals/theory-and-practice-of-logic-programming/article/integrating-logic-rules-with-everything-else-seamlessly/43F7B71F2B4A27FAB6BFF7EFC0C58EF6).

Integration Considerations with Legal-ES
From Legal-ES to Logic Programs: Use Legal-ES’s SpaCy pipelines and embeddings to preprocess and extract structured facts and rules from Spanish legal texts. Then map these extracted elements into logic predicates compatible with the chosen logic programming framework.

Neuro-Symbolic Synergy: Recent work shows prompting LLMs 
to translate legal text into logic programs (e.g., 
Prolog clauses) improves accuracy and reasoning 
consistency. Frameworks like SWI-Prolog and ProSLM 
facilitate this integration by executing and validating 
LLM-generated logic encodings. [1](https://arxiv.org/html/2502.17638v1) [5](https://openreview.net/forum?id=AsTWBjCvUt)

Explainability and Contradiction Detection: ASP solvers 
like Clingo and s(CASP) support non-monotonic reasoning 
and provide explanations for legal decisions, which is 
crucial for detecting contradictions and understanding rule interactions extracted from Legal-ES.[7](https://ceur-ws.org/Vol-3733/short3.pdf)

Scalability and Usability: SWI-Prolog offers robust tooling and community support, making it a practical choice for initial development. Epilog and Alda provide advanced expressivity for more complex legal rule sets.

Summary

Framework | Best Use Case in Legal-ES Integration
--- | ---
SWI-Prolog | General-purpose legal reasoning, neuro-symbolic integration
Epilog | Complex legal contracts requiring enhanced expressivity
ASP / Clingo | Modeling exceptions, contradictions, and explainable reasoning
s(CASP) | Explainable top-down reasoning with justification
PROLEG | Legal-specific logic programming framework
ProSLM | Validating and refining LLM-generated legal logic encodings
Alda | Integrating logic with other programming paradigms

These frameworks provide a solid foundation to formalize and reason over legal knowledge extracted from Legal-ES, enabling you to build a system that answers complex legal queries with symbolic logic and explainability.

References:
* ["Towards Robust Legal Reasoning: Harnessing Logical LLMs in Law" (2024)](https://arxiv.org/html/2502.17638v1)
* [Stanford Law on Logic Programming for Automating Insurance Contracts](https://law.stanford.edu/2023/03/10/why-a-logic-programming-approach-works-for-automating-insurance-contracts/)
* [LawGiBa: Combining GPT, Knowledge Bases, and Prolog for Legal Assistance](https://openreview.net/forum?id=AsTWBjCvUt)
* [Alda: Integrating Logic Rules with Everything Else, Seamlessly](https://www.cambridge.org/core/journals/theory-and-practice-of-logic-programming/article/integrating-logic-rules-with-everything-else-seamlessly/43F7B71F2B4A27FAB6BFF7EFC0C58EF6)
* [XAI-LAW: Logic Programming Tool for Explaining Legal Decisions](https://ceur-ws.org/Vol-3733/short3.pdf)

### Previous Systems to Consider

## Resource Lists

### [Legal Text Analytics](https://github.com/Liquid-Legal-Institute/Legal-Text-Analytics)

### [Legal Natural Language Processing](https://github.com/maastrichtlawtech/awesome-legal-nlp)

## Articles

### [SemEval-2023 Task 6: LegalEval - Understanding Legal Texts](2023.semeval-1.318.pdf)

From https://aclanthology.org/2023.semeval-1.318.pdf

### [Coupling Large Language Models with Logic Programming for Robust and General Reasoning from Text](Coupling Large Language Models with Logic Programming for Robust and General Reasoning from Text 2307.07696v1.pdf)

From: Joohyung Lee
[v1] Sat, 15 Jul 2023 
03:29:59 UTC (2,765 KB)
https://arxiv.org/abs/2307.07696

### [Weakly supervised semantic parsing with abstract examples](Weakly supervised semantic parsing with abstract examples P18-1168.pdf)
Omer Goldman, Veronica Latcinnik, Ehud Nave, Amir
Globerson, and Jonathan Berant. 2018. **Weakly supervised semantic parsing with abstract examples**. In
Proceedings of the 56th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 1809–1819.
https://aclanthology.org/P18-1168/

### [Natural language processing in the era of large language models](Natural language processing in the era of large language models frai-06-1350306.pdf)
SPECIALTY GRAND CHALLENGE article
Front. Artif. Intell. , 11 January 2024
Sec. Natural Language Processing
Volume 6 - 2023 | https://doi.org/10.3389/frai.2023.1350306

### [A Study on the Implementation of Generative AI Services Using an Enterprise Data-Based LLM Application Architecture](A_Study_on_the_Implementation_of_Generative_AI_Ser.pdf)
September 2023
DOI:10.48550/arXiv.2309.01105
LicenseCC BY-NC-ND 4.0

https://www.researchgate.net/publication/373685686_A_Study_on_the_Implementation_of_Generative_AI_Services_Using_an_Enterprise_Data-Based_LLM_Application_Architecture

### [Answer set programming](answer-set-programming-978-3-030-24658-7_compress.pdf)
Vladimir Lifschitz. 2019. Answer set programming. Springer Heidelberg
https://link.springer.com/book/10.1007/978-3-030-24658-7#toc

### [Answer set programming - Wikipedia](https://en.wikipedia.org/wiki/Answer_set_programming)

### [Constraint Answer Set Programming without Grounding](answer-set-programming-978-3-030-24658-7_compress.pdf)
https://www.cambridge.org/core/journals/theory-and-practice-of-logic-programming/article/constraint-answer-set-programming-without-grounding/55A678C618EF54487777F021D89B3FE7

### [Stable model semantics - Wikipedia](https://en.wikipedia.org/wiki/Stable_model_semantics)

### [Retrieval-Augmented Semantic Parsing: Using Large Language Models to Improve Generalization](Retrieval-Augmented Semantic Parsing Using Large Language Models to Improve Generalization 2412.10207v1.pdf)
https://arxiv.org/html/2412.10207v1

### More References
Emilia Oikarinen and Tomi Janhunen. 2006.
_Modular equivalence for normal logic programs_. In 17th European Conference on Artificial Intelligence(ECAI),
pages 412–416.

Joseph Babb and Joohyung Lee. 2012. _Module theorem for 
the general theory of stable models_. Theory and
Practice of Logic Programming, 12(4-5):719–735.

## Frameworks and Libraries

### [Flair](https://github.com/flairNLP/flair)
A very simple framework for state-of-the-art NLP. Developed by Humboldt University of Berlin and friends.

### [TextBlob](https://github.com/sloria/TextBlob)
#### [https://textblob.readthedocs.io/en/dev/](https://textblob.readthedocs.io/en/dev/)
    * TextBlob is a Python library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, and more.

### [spaCy](https://spacy.io)
#### [Usage](https://spacy.io/usage)
#### [Mastering spaCy - Second Edition](https://learning.oreilly.com/library/view/mastering-spacy/9781835880463/)
#### [NLP_APP](https://github.com/sharonreshma/NLP_APP)
#### [NLP Pipeline with SpaCy & TextBlob](https://github.com/AqueeqAzam/Complete-NLP-pipeline-using-SpaCy)

### [FreeLing](https://nlp.lsi.upc.edu/freeling/)
*Could not install it in Ubuntu 24.10 - Oracular Oriole*

FreeLing is a C++ library providing language analysis functionalities (morphological analysis, named entity detection, PoS-tagging, parsing, Word Sense Disambiguation, Semantic Role Labelling, etc.) for a variety of languages (English, Spanish, Portuguese, Italian, French, German, Russian, Catalan, Galician, Croatian, Slovene, among others).

## Knowledge Graphs
### [How to Convert Any Text Into a Graph of Concepts](https://towardsdatascience.com/how-to-convert-any-text-into-a-graph-of-concepts-110844f22a1a/)
### [Text to Knowledge Graph Made Easy with Graph Maker](https://towardsdatascience.com/text-to-knowledge-graph-made-easy-with-graph-maker-f3f890c0dbe8/)


## Systems

The OASIS project: an open-source framework for legal knowledge representation and reasoning.

LegalRuleML: an XML-based language for representing legal rules and regulations.

### ASP in Swi-Prolog
#### [s(CASP) SWISH site](https://swish.swi-prolog.org/example/scasp.swinb)

#### [s(CASP) for SWI-Prolog](sCASP for Swi-Prolog gdeinvited4.pdf)
Jan Wielemaker, Joaquín Arias and Gopal Gupta4
https://ceur-ws.org/Vol-2970/gdeinvited4.pdf





