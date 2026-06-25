Używane
- CDE - cosinus distance of embeddings
- EF - entities found
- CDEF
- CDE **measure
- EF **measure**
- CDEF **metric**
- named entity **task** - an information extraction sub-task, that involves identifying the names of all the people, organizations, and geographic locations in a text https://aclanthology.org/C96-1079/
	- !!!ALE w http://www.lrec-conf.org/proceedings/lrec2002/pdf/120.pdf named entities są definiowane jako "the names of particular things or classes and numeric expressions", 
	- definicja z wikipedii: a real-world **object**, such as a person, location, organization, product, etc., that can be denoted with a proper name. It can be abstract or have a physical existence, 
	- A named entity is, roughly speaking, anything that can be referred to with a propernamed entity name: a person, a location, an organization https://web.stanford.edu/~jurafsky/slp3/ed3book_jan26.pdf
	- "A specific word or phrase that represents a unique and indentifiable information in the conversation or can be assigned to a category with well defined semantics" https://link.springer.com/book/10.1007/978-3-031-88566-2
- entity - In the context of entity extraction, an "entity" refers to a specific piece of information or an object within a text that holds particular significance. These are often real-world concepts or specific mentions that systems can identify and categorize. https://cloud.google.com/discover/what-is-entity-extraction
- named - In the expression “Named Entity”, the word “Named” aims to restrict the task to only those entities for which one or many rigid designators, as defined by S. Kripke (1982), stands for the referent. For instance, the automotive company created by Henry Ford in \1903 is referred to as Ford or Ford Motor Company. Rigid designators include proper names as well as certain natural kind terms like biological species and substances. https://nlp.cs.nyu.edu/sekine/papers/li07.pdf
- entity class/type/category - eg. person, location, organization, name
	- https://aclanthology.org/W03-0419.pdf type of named entity, named entity category
	- https://nlp.cs.nyu.edu/sekine/papers/li07.pdf type, category, sub-category, subcategory
	- https://web.stanford.edu/~jurafsky/slp3/ed3book_jan26.pdf (strona 214 - w ramach type People, there are sample categories: people, characters)
	- "typical labeling schemes include entity classes such as PER (person), GPE (geopolitical entity), ..."  https://link.springer.com/book/10.1007/978-3-031-88566-2
- tradycyjnie: entity = type + span
- u mnie: entity = type + name/value (problem with name: named entity and entity name can confuse)
- named entity recognition
- predicted entity - ja będę używać generated entity https://arxiv.org/abs/2409.00369
- reference entity https://arxiv.org/abs/2409.00369
- target information




Zbędne

-  tagging scheme/labeling scheme (zastanów się czy potrzebujesz, skoro odnosi się to BIO itp.)
- tag/label (zastanów się czy potrzebujesz, skoro odnosi się to do B-PER, B-LOC itp.)
- span - a sequence of one or more consecutive words https://www.sciencedirect.com/science/article/abs/pii/S1568494624006185