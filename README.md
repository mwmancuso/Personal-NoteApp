Notesapp
========
First thing's first, Notesapp is a placeholder name for this project. Though descriptive, this project should have a better, complete name by v1.0.0. For that reason, the rest of this document will refer to Notesapp as "this project" for mobility.

What Is It?
-----------
This project is meant to be a new take on note-taking. Simple, linear pages of unorganized notes is old-school and helps much less than what is expected. However, there have been few to no advancements in this field since paper notes caught on. Sure, maybe we have a few different maps and other types of visual organizers, but how much do they really contribute to our learning? The majority of notes are still taken in a linear fashion.

###What It Isn't
This project is not a simple note-taking app. It is not an app like Evernote, Google Keep or anything else that exists currently. Typical note-taking apps use the same linear methodology as paper notes, just in a slightly more organized manner. Take the following:

|Line Number|Text|
|----------:|:---|
|1|**George Washington**|
|2|Born: February 22nd, 1732|
|3|Died: December 14th, 1799|
|4|Party: Federalist*|
|5|In office: April 30, 1789 – March 4, 1797|
|6|* *technically not, but supported views*|
|7|Etc...|

This is not very useful. The information is there, but it is in an unorganized form and the important information is mixed in with the unimportant information. Furthermore, the important information may change depending on the topic at hand. Suppose your teacher informs you that you will be tested on the ages of presidents at their death (they have their reasons). You will most likely end up going through your list of presidents, finding the birth and death dates and calculating their age at death. That information will end up appended to line 3 in your notes. Add a few more bits of information and you have a mess at your hands. Then later come, there is a test on presidents and their parties. You'll then have to search through all of your messy notes and find the parties. That information is surrounded by other information that you don't need at the time. Organized notes, such as Evernote or Google Keep, help by allowing you to edit information inline and use a text search tool, but many of the other problems still persist.

Another issue is that the trivial information—birth date and death date—take valuable time to research and insert. You may never use that information. Finding and writing the birth date and death date for that example alone took three or four tab-switches to do while writing this. It is also subject to inaccuracies if done multiple times for multiple people. This project is not a place for inserting useless information. Information supplied to this service should be useful and meaningful.

This project is also not meant to be another flash card-type memorization service, such as Quizlet (although integration is a possibility). Though sometimes that may be a scenario for which this service can be used for, the main purpose of this app is not as such. Simple memorization is what many schools and teachers force us to do. However, memorization of facts is not the best learning technique for most people. Although such a method may help somebody in a simple trivia, even Jeopardy requires a lot of analysis along with memorization.

###What It Is
This project is much more than a place to glob together information. It is rather a service that takes your information, along with information from outside sources, and organizes it. It encourages separability in information, while linking it all together in different ways. Every piece of information will be stored in a node. That node will be extensible to outside sources of information depending upon the information you supply it with in the first place. As a new notebook is created, nodes will simply be recorded as facts. However, after time, the nodes will begin to multiply and connect. In the end, it is expected for a user's account to be filled with many notebooks and nodes all connected together. Cross-notebook nodes will be possible and encouraged to save duplication of information.

Even more, all nodes and notebooks will be sharable. All shares will be specifically marked as shared and information will be checked for differences and similarities and given scores of originality. This is to prevent plagiarism and simple copying—defeating the purpose of the app. This project is expected to expand big enough to start using computer learning to find matches of information and try to connect people learning about the same thing. Collaboration and conversation is one of the most important aspects of learning.

All of that seems like it could get very messy very quickly. That is most likely an accurate assumption. However, the concern of this project is to help people learn; not to make them more confused. All of the messy globs of information will be handled on the server. The information that the user sees should be sorted, streamlined, useful and relevant. Computer learning will have to be implemented to find the best possible combination of nodes to display to the user at certain times. Without proper mechanisms, nodes could be displayed connected to other nodes that are in turn connected to themselves. It is of utmost important to allow the user to sort and filter nodes as often and as freely as they desire. It is the job of this project to manage those nodes and display only what is relevant to the learner.

Background
----------
This project idea came to me while trying to study for history. This is why many of the examples in this documentation involve history. The project will not only support history, however, it is instead intended to support nearly every subject, and extend into everyday life. Back on point, I could not for the life of me figure out the best way to study for history. I am an analytical person, but none of the current methods of studying, besides simply reading, seemed to help me. My history teacher made us all fill out vocabulary index cards, which do not help me at all. I think it is important to have all of my information connected and for all of it to be seen many times to commit it to memory.

Though this idea began to help myself, I soon realized that nearly every learner could benefit from such an app. Analytical people would have a new tool to help them better analyze and make connections. Those who are not already analytical could benefit by becoming more analytical after being shown how to make connections and continue to make connections. Talking with other people, I also realized that taking notes on a computer is not the most desired or even possible method for some people. I intend to help them by creating printable handouts, and allowing information they fill out on the handouts available for manual input or scanning in using handwriting recognition. To keep me on the right path for this project, I have decided to attempt pursuing it for my graduation project.

I have not yet decided how this project will be licensed, distributed or financed.

Definition of Terms
-------------------
These terms are subject to aliases for marketing or easier understanding in the project. Those aliases will be addressed here, but the underlying terminology will remain.

###User
Starting at the very top, the user is the person with an account on this service. Their credentials will be stored in a database, which will be accessible via a login page, an account page, a mobile phone application, and linked to anything the user authors. The user is just like a user on any other service.

###Notebook
A notebook will be a container for all nodes and information pertaining to a specific topic. Notebooks will may be owned only by a single user. They may be shared either wholly or partially with other users. Only the owner will be allowed to make changes to the notebook or the information in it.<sup>1</sup> However, nodes from a notebook may be transferred via dragging-and-dropping or other methods of transferring. Transferred nodes may be edited by either party, or synced if wished.<sup>1</sup>

Notebooks are intended to be overall containers of information. They are not meant to be many notebooks per user. Organization is rather intended to be pursued inside of the notebook. This may bring up the point of the need for notebooks.

<sup>1</sup>Information sharing is not solid. A Google Docs approach may be taken instead of the single-user sharing approach. This is subject to change.

####Notebook Templates

Notebooks are intended to be specific to a certain topic. For example, every class a user takes in school could be a new notebook. Let us assume a five-period schedule. The student has, in order: History, English, Chemistry, Band and Photography. Notebooks will have categories for use depending on the subject. The notebook a user creates for History would be tailored to history, and would most likely use Wikipedia and other such sources as a backend. It would also have a timeline, maps, and other modules used for history. Modules are not subject-specific, there will simply be a template depending on the notebook-type chosen. The user's English notebook, on the other hand, would have a template tailored to English. The modules backends used would most likely be Goodreads, IMDB, and other related services. Another module for vocabulary would be available with possible integration with Quizlet and related services. A chemistry notebook would have backends for chemical compounds and likely some other science-related modules. The user's Band and Photography notebooks would start out as generic templates on which the user could add modules pertaining to his or her class. Perhaps eventually, templates could be published manually by users or teachers, or automatically created after a large enough user base creates class-specific notebooks. This project is intended to launch with the following notebook templates:

 * History
 * English
 * Sciences (biology, chemistry, physics, etc.)
 * Math
 * (Maybe) Programming

###Modules

Modules are dockable panels that are deeply integrated with nodes. Modules may be notebook-dependent or not. Modules allow a deeper learning experience and will help with all types of learning. They will allow learners to visualize, organize, hear and learn the information. Modules are the basis for notebook templates, as templates are simply be different layouts of modules. All modules are available for use in any notebook, however it is unlikely that a chemical compound viewer will be needed in a History class or a 3D shape viewer will be needed in an English class. Certain modules may be dockable outside of individual notebooks, for example a to-do list or calendar. Modules both make use of the APIs of other services and also will be extensible via APIs of this project. Below is a list of modules that are to be developed.<sup>1</sup>

 * Maps (both historic and current)
 * Timeline
 * Vocab list
 * Vocab tests/games
 * Chemical viewer
 * Researcher
 * Research tracker
 * Animations/video player
 * Simulations
 * Image viewer/editor
 * Audio viewer/editor
 * Programming tester
 * Presentation helper
 * Equation builder/solver
 * Advanced calculator
 * 2D/3D shape viewer and manipulator
 * Document editor
 * File manager
 * Share dialog
 * Audio/video recorder
 * Text to speech reader
 * Notebook information
 * Node information
 * Assignment manager
 * To-do list
 * Calendar
 * Weather

All of these modules are not meant to be mainly web-based. Mobile modules should also be developed with a specialized interface.

<sup>1</sup>Note that this is not a definite list. It is subject to additions, removals and changes. Complete list of modules will not be available in v1.0.0.

####Module Backends

Backends and services must be used for many of the modules. Some modules will be developed in-house, but many will be integrations with existing services. These backends may be available via Web APIs, front-end integrations, or SDKs on in-house servers. Financing for some backends is a huge importance for this project. Many collaborations will most likely have to be made for custom APIs. A list of possible backends:

 * Wikipedia
 * Google
 * Goodreads
 * IMDB
 * Google Maps
 * Open Street Maps
 * Quizlet
 * Chemspider
 * NCBI
 * EasyBib
 * Evernote
 * Diigo
 * YouTube
 * McGraw Animations
 * ExploreLearning
 * Pixlr
 * Soundcloud
 * Codecademy
 * Github
 * Prezi
 * Glogster
 * Google Drive
 * Wolfram Alpha
 * Some formula editor (many available)
 * Sketchfab
 * Google Calendar
 * Weather.com
 * OpenWeatherMap
 * Forecast.io

####Module API and Directory

Note: API stands for Application Programming Interface. APIs allow different services to interact with each other, in the simplest sense.

APIs drive the Web today. This project will have both external and internal APIs. External APIs will be available so that other projects can integrate data from this project. Internal APIs will be available for developers to build modules for this project and integrate them with users' data. Also, an internal API will be available for those learning programming to toy with this project itself in their learning. Or even just a techy student who gets lazy and puts their computer to work for them.

A directory will be available for users to add custom modules or find outside services that can integrate with this project. All of the general security measures will be taken to ensure data safety and control.

An API is not planned for development until during or after the beta phase. The API will be a project of its own. It may be developed in tandem with the mobile applications.

###Containers

Containers are the next-biggest thing under Notebooks. Notebooks can contain nodes directly, however this will most often not be the case. Instead, containers will typically contain nodes. Containers are simply wrappers for nodes that put them in a more organized fashion. They can be used to sort nodes depending on how they are learned about. Obviously, a subject is not learned all at once. Most subjects are taught in sections. Many classes are taught chapter by chapter from a textbook. Ding ding, perfect use-case for a container. Having a container for each chapter would be an excellent organizational practice. Units are also another candidate for containers.

However, the point of this project is to help learners make connections. Following the dogma of this project, containers are not all-inclusive. Nodes may be shared between containers for better relationship definitions. In a U.S. History class, you may learn about political parties. In your first unit, you may learn about Federalists and Antifederalists. Later on in the course, you will be introduced to even more political parties. Even though the nodes with each political party are contained in a unit or chapter container, you may consider making a new container for political parties. A drag-and-drop interface will allow you to quickly add all of the political parties to their own category. If in every node that was a political party, you wrote "political party," a simple search would allow you to find everything you need. This could also be done automatically if proper computer learning techniques were utilized.

Note that categories may seem a lot like tags in other note-taking applications. In a way, they are, but not completely. In simple terms, tags would be added to nodes to classify them. Categories, adversely, are what nodes are added to. This way, categories must already exist, or be created on the fly, for nodes to be added to them. Though a tag-like interface may be used on nodes, in the end, categories are a better way of organizing the nodes.

Categories are expected to be used for review and establishing connections. Viewing categories by themselves creates a space for a learner to study a particular topic. Using modules, a quiz may be generated using the categories to single in on a topic. If a node is part of multiple categories, and multiple reviews are completed with each of those categories, nodes will be seen time and time again and linked with topics inside a learner's memory. This will also signify more important information. If a node is in more categories, there is a better chance that that node is more important.

###Nodes

The all-mighty node. Nodes in themselves are quite simple. They contain information. However, the way nodes in this project work is very useful. The structure of a node is broken down into different sections: the title, the information, and the category of the node. Node categories will be addressed in another sub-topic.

The title of the node is just like the title of anything else. It classifies the node and also helps modules and backends get a grip on what your node will be able. Titles in addition to node categories are very important, but that will be explained shortly. The title may also be seasoned with a picture. Pictures other than a main picture will have to fall in a module overflow. Nodes may also be color-coded for better distinction on modules like maps and a timeline.

The information for a node is all of the facts, statistics, opinions, and whatever else can be listed about the title. It is like bullets in typical note-taking applications. However, every node entry—bullet—is separable. They may be rearranged and manipulated individually. It is important to create multiple entries for each topic of information. This allows everything to flow more smoothly. For example, a multiple choice quiz may be generated using a node. Let's take this into example:

Node A has three node entries: 1, 2 and 3.
Node B has four entries: 4, 5, 6 and 7.
Node C has three entries: 8, 9 and 10.

A multiple choice question is generated, which asks:

```
Which of the following is true about B?
A. 1
B. 3
C. 5
D. 9
```

The correct answer would be C. 5 is the node entry from Node B, so, unless there is overlap, 5 would be the true about Node B. In the long run, computer learning may take guesses at multiple choice entries that may have overlap and either remove those questions or make multiselect answers.

This brings up another point: what about information that isn't very useful on its own? Such as a person's age, birth-place, or things of the sort. Entries that contain this information may be flagged as insignificant. These types of facts are intended to be imported from a node backend, to save valuable research time.

####Node Categories

Node categories are incredibly important in defining the function and relationships of a node. They also classify which modules and backends will be usable with said node. A node category is a very broad classification of the node title. For example, Mahatma Gandhi is a person. Japan is a geographical place. Harry Potter is a film. The Wrights brothers' flight is an event. A political party is a body of people. Many of these categories are too broad for useful classification. Sub-categories are available to further refine a categorization. Without further ado, a list of preliminary node categories:<sup>1</sup>

* Person
* Geographical Place
 * Planet
 * Continent
 * Country
 * Reference (The West, the East, etc.)
 * State
 * Province
 * City
* Motion Picture
 * Movie
 * Other Video Production
* Text
 * Novel
 * Informative Text
 * Historical Text
 * Governmental Text (Law)
* Object
 * Building
 * Statue/Sculpture
 * Artwork
* Event
 * Dispute (War)
 * Session/Meeting
 * Significant Date
* Body
 * Governmental Body
 * Organization
* Scientific Item
 * Chemical Compound
 * Theory
 * Method
 * Data
 * Anatomical Feature
 * Classification
 * ...
* Mathematical Item
 * Equation
 * Theory
 * Postulate
 * ...

As the user base of this project grows, categories will be able to be automatically defined via a crowd-sourcing method.

<sup>1</sup>Note that this list is in need of major revisions and is subject to significant change. Much still needs to be added. Modules may be able to add custom categories to the list.

####Node Backends

Automatic definition of known statistical facts is implemented via node backends. The node backends used will depend on the node category chosen. Upon creating a node and defining a category and title, the service will use a backend to research the title. Relevant information will be presented near the node itself and may be added with a simple click. Insignificant information will automatically be defined and marked as insignificant, though that flag may be removed by the user if deemed inaccurate. Node backends will most likely be deeply integrated with module backends. Modules may be launched with relevant information about the specific node in addition to the pop-up info. As this project expands, the project itself may be used as a backend, pulling information from loads of other users. If all information is found independently of each other, it is more than likely accurate. Algorithms and software will be needed to verify this, however, and a voting system will be implemented.

All modules and backends used either automatically or manually will be linked to the node it was used with. This will allow nodes to become containers for deeper information. A Wikipedia article, for example, may be linked to a specific node. Or a picture library may help get a visual feel for the information. A video may clarify some of the information. Links and references may be added, as well, for a research project. This makes every node more extensible. Visual indicators may be used on nodes to clarify which modules are linked to it before selecting the node.
 
####Node Links

Nodes may not only be linked to modules, but internode connections may be established. These links may be established automatically or manually via a click and drag interface. Users of graphic editing software may be familiar with node connections. However, node links in this project are not one-way. The benefits of node links may not be immediately noticeable. However, once it comes time to review information, node links will become life-savers. Let's say that you are learning about presidents. You find George W. Bush and see that he is a Republican. You need a refresher on the Republican Party. Good news for you, your node for the Republican Party is already floating next to Bush with a line indicating linkage. So you read what you have listed about the party. Then you find yourself wondering what other presidents are Republicans. So you click on the node and find 17 other Republican presidents. You can then see when parties were in office on the timeline, since the parties are color-coded.

Node links are obviously a powerful tool for reviewing information. Node links may be created automatically via backends, however manual creation is required. A good strategy for linking nodes from the start will pay off exponentially in the end. However, like everything else in this project, node-linkage is not a static property. Nodes links can be added, removed, or modified at any time.

###Presentations

Presentations are an important part of learning and teaching alike. With so much information at hand, this project would be perfect for creating presentations. Different types of presentations may be created. Presentations could be exported or imported to backends, such as Powerpoints, Google Docs, or Prezi. Videos could also be created with a video editing module.

Presentations are a better method of conveying and sharing information than sharing nodes directly. Though node sharing will be possible, this project will always recommend creating and sharing presentations. Presentations are not expected to be available at v1.0.0.

####Presentation builder

At the heart of presentations is the presentation builder. The presentation builder will allow a user to pull in information to a presentation and apply visual effects to it to make it more appealing. Music, videos and other media may be imported. If a module is compatible with presentations, it can be used, as well. Since a node contains all relevant information, modules and links, creating a presentation can move at an accelerated pace. A user can focus more time on making the presentation appealing and understandable than researching and importing information.

As mentioned earlier, different types of presentations can be made. A few examples are a video, a slideshow, or a web. In each of these presentations, nodes can take different forms, links can be mapped to different slides or frames, and information can be organized to emphasize specific points. If so inclined, a simple web can be made of nodes, and a specific order of nodes can be presented. Linkages and other node data will persist.

###Print-out

Though this project is digital, it is important to take into consideration that some learners feel more comfortable taking notes on paper. Others may have no choice but to take notes on paper. Although it is the author's opinion that all schools should be providing some type of technology to students for their disposal, that decision is left to individual schools and is unfortunately not reflected in many of them. That is why this project will support print-outs and scan-ins.

Print-outs are simply papers with node boxes in them, where information can be written into. All of the necessary tools will be available, with the ability to show the scan-in processor what exactly the user wants done. The writer can specify their notebook of choice, whether or not a node is to be extended for more space, show links between nodes, assign nodes to categories (a sheet will be available for all available categories) and group nodes in containers.

Print-outs can also be filled out for review. A user may create a print-out, similar to the way he or she prepares a presentation, and print it out for review. Links will be preserved, and modules capable of print out will be printed with it. Custom settings will allow automatic formatting of modules (or lack thereof). A custom setting for number of pages may be employed, in case the user has limited resources. The more pages specified, the more information and modules may be listed. The pre-filled print-out system is expected to come out between v1.0.0 and v2.0.0.

####Scan-in

Once a user has everything filled out and has a chance to access a computer or phone, they can then scan in their papers. This can be done with a scanner or a photo. Naturally, photos will have to be high enough quality to be accurately interpreted. The scan-in processor will then have to use pattern recognition to read the handwriting, use other methods to interpret linkages and other informative marks, and pass the information to the user's account. The server will then attempt to automatically generate missed links and information, and apply applicable modules to the nodes. The print-out can then be discarded and replaced with a print-out with printed data. The print-out/scan-in system is not expected to be completed until many versions have passed. A great amount of research and testing must be observed firstly.

Interface
---------

Development Workflow
--------------------

Project Versioning
------------------
