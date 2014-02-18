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

Notebooks are intended to be specific to a certain topic. For example, every class a user takes in school could be a new notebook. Let us assume a five-period schedule. The student has, in order: History, English, Chemistry, Band and Photography. Notebooks will have categories for use depending on the subject. The notebook a user creates for History would be tailored to history, and would most likely use Wikipedia and other such sources as a backend. It would also have a timeline, maps, and other modules used for history. Modules are not subject-specific, there will simply be a template depending on the notebook-type chosen. The user's English notebook, on the other hand, would have a template tailored to English. The modules used as backends would most likely be Goodreads, IMDB, and other related services. Another module for vocabulary would be available with possible integration with Quizlet and related services. A chemistry notebook would have backends for chemical compounds and likely some other science-related modules. The user's Band and Photography notebooks would start out as generic templates on which the user could add modules pertaining to his or her class. Perhaps eventually, templates could be published manually by users or teachers, or automatically created after a large enough user base creates class-specific notebooks. This project is intended to launch with the following notebook templates:

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

###Nodes

####Node Categories

####Node Backends

####Node Links

###Presentations

####Presentation builder

###Print-out

####Scan-in

Interface
---------

Development Workflow
--------------------

Project Versioning
------------------
