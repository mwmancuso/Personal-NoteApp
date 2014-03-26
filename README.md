Notesapp
========
First thing's first, **Notesapp is a placeholder name** for this project. Though descriptive, this project should have a better, complete name by v1.0.0. For that reason, the rest of this document will **refer to Notesapp as "this project"** for mobility.

The master branch of this Git project is available at https://dev.notes.xpandismo.com/.

What Is It?
-----------
This project is meant to be a new take on note-taking. Simple, linear pages of unorganized notes is old-school and helps much *less* than what is expected. However, there have been few to no advancements in this field since paper notes caught on. Sure, maybe we have a few different maps and other types of visual organizers, but how much do they *really* contribute to our learning? The majority of notes are still taken in a linear fashion.

###What It Isn't
This project is *not* a simple note-taking app. It is not an app like Evernote, Google Keep or anything else that exists currently. Typical note-taking apps use the same linear methodology as paper notes, just in a slightly more organized manner. Take the following:

|Line Number|Text|
|----------:|:---|
|1|**George Washington**|
|2|Born: February 22nd, 1732|
|3|Died: December 14th, 1799|
|4|Party: Federalist*|
|5|In office: April 30, 1789 – March 4, 1797|
|6|* technically not, but supported views|
|7|Etc...|

This is not very useful. The information is there, but it is in an unorganized form and the important information is mixed in with the unimportant information. Furthermore, the important information may *change* depending on the topic at hand. Suppose your teacher informs you that you will be tested on the ages of presidents at their death (they have their reasons). You will most likely end up going through your list of presidents, finding the birth and death dates and calculating their age at death. That information will end up appended to line 3 in your notes. Add a few more bits of information and you have a mess at your hands. Then later come, there is a test on presidents and their parties. You'll then have to search through all of your *messy* notes and find the parties. That information is surrounded by other information that you don't need at the time. Organized notes, such as Evernote or Google Keep, help by allowing you to edit information inline and use a text search tool, but many of the other problems still persist.

Another issue is that the trivial information—birth date and death date—take *valuable time* to research and insert. You may never use that information. Finding and writing the birth date and death date for that example alone took three or four tab-switches to do while writing this. It is also subject to inaccuracies if done multiple times for multiple people. This project is not a place for inserting useless information. **Information supplied to this service should be useful and meaningful**.

This project is also not meant to be another flash card-type memorization service, such as Quizlet (although integration is a possibility). Though sometimes memorization may be a scenario for which this service can be used for, the main purpose of this app is not as such. Simple memorization is what many schools and teachers force us to do. However, **memorization of facts is not the best learning technique for most people**. Although such a method may help somebody in a simple trivia, even Jeopardy requires a lot of analysis along with memorization.

###What It Is
This project is much more than a place to glob together information. It is rather a service that takes your information, along with information from outside sources, and organizes it. It encourages *separability* in information, while *linking* it all together in different ways. Most pieces of information will be stored in a node. That node will be extensible to outside sources of information depending upon the information you supply it with in the first place. As a new notebook is created, nodes will simply be recorded as facts. However, after time, the nodes will begin to multiply and connect. In the end, it is expected that a user's account be filled with many notebooks and nodes all connected together. Cross-notebook nodes will be possible and encouraged to save duplication of information.

Even more, all nodes and notebooks will be **sharable**. Shares will be specifically marked as shared and information may be checked for differences and similarities and given scores of originality. This is to prevent plagiarism and simple copying—defeating the purpose of the app. This project is expected to expand big enough to start using **computer learning** to find matches of information and try to connect people learning about the same thing. Collaboration and conversation is one of the most important aspects of learning.

All of that seems like it could get *very messy* very quickly. That is most likely an accurate assumption. However, the concern of this project is to help people learn; not to make them more confused. All of the messy globs of information will be handled on the server. The information that the user sees should be sorted, streamlined, useful and relevant. Computer learning may be implemented to find the best possible combination of nodes to display to the user at certain times. Without proper mechanisms, nodes could be displayed connected to other nodes that are in turn connected to themselves. It is of utmost important to allow the user to sort and filter nodes as often and as freely as they desire. It is the job of this project to manage those nodes and display only what is *relevant* to the learner.

Background
----------
This project idea came to me while trying to study for history. This is why many of the examples in this documentation involve history. The project will not only support history, however, it is instead intended to support nearly every subject, and extend into everyday life. Back on point, I could not for the life of me figure out the best way to study for history. I am an analytical person, but none of the current methods of studying, besides simply reading, seemed to help me. My history teacher made us all fill out vocabulary index cards, which do not help me at all. I think it is important to have all of my information connected and for all of it to be seen *many* times to commit it to memory.

Though this idea began to help *myself*, I soon realized that *nearly every learner* could benefit from such an app. Analytical people would have a new tool to help them better analyze and make connections. Those who are not already analytical could benefit by becoming more analytical after being shown how to make connections and continue to make connections. Talking with other people, I also realized that taking notes on a computer is not the most desired or even possible method for some people. I intend to help them by creating printable handouts, and allowing information they fill out on the handouts available for manual input or scanning in using handwriting recognition. To keep me on the right path for this project, I have decided to attempt pursuing it for my graduation project.

I have not yet decided how this project will be licensed, distributed or financed.

Definition of Terms
-------------------
These terms are subject to aliases for marketing or easier understanding in the project. Those aliases will be addressed here, but the underlying terminology will remain.

###User
Starting at the very top, the user is the person with an account on this service. Their credentials will be stored in a database, which will be accessible via a login page, an account page, a mobile phone application, and linked to anything the user authors. The user is just like a user on any other service.

###Notebook
A notebook will be a container for all nodes and information pertaining to a specific topic. Notebooks will may be owned only by a single user. They may be shared either wholly or partially with other users. Only the owner will be allowed to make changes to the notebook or the information in it.<sup>1</sup> However, nodes from a notebook may be transferred via dragging-and-dropping or other methods of transferring. Transferred nodes may be edited by either party, or synced if wished.<sup>1</sup>

Notebooks are intended to be *overall* containers of information. They are **not meant to be many notebooks** per user. Organization is rather intended to be pursued *inside* of the notebook. This may bring up the point of the need for notebooks.

<sup>1</sup>Information sharing is not solid. A Google Docs approach may be taken instead of the single-user sharing approach. This is subject to change.

####Notebook Templates

Notebooks are intended to be specific to a certain topic. For example, every class a user takes in school could be a new notebook. Let us assume a five-period schedule. The student has, in order: History, English, Chemistry, Band and Photography. Notebooks will have categories for use depending on the subject. The notebook a user creates for History would be tailored to history, and would most likely use Wikipedia and other such sources as a backend. It would also have a timeline, maps, and other modules used for history. Modules are *not* subject-specific, there will simply be a template depending on the notebook-type chosen. The user's English notebook, on the other hand, would have a template tailored to English. The modules backends used would most likely be Goodreads, IMDB, and other related services. Another module for vocabulary would be available with possible integration with Quizlet and related services. A chemistry notebook would have backends for chemical compounds and likely some other science-related modules. The user's Band and Photography notebooks would start out as generic templates on which the user could add modules pertaining to his or her class. Perhaps eventually, templates could be published manually by users or teachers, or *automatically* created after a large enough user base creates class-specific notebooks. This project is intended to launch with the following notebook templates:

 * History
 * English
 * Sciences (biology, chemistry, physics, etc.)
 * Math
 * (Maybe) Programming

###Modules

Modules are dockable panels that are deeply integrated with nodes. Modules may be notebook-dependent or not. Modules allow a deeper learning experience and will help with all types of learning. They will allow learners to *visualize*, *organize*, *hear* and *learn* the information. Modules are the basis for notebook templates, as templates are simply be different layouts of modules. All modules are available for use in any notebook, however it is unlikely that a chemical compound viewer will be needed in a History class or a 3D shape viewer will be needed in an English class. Certain modules may be dockable outside of individual notebooks, for example a to-do list or calendar. Modules can also be embedded inside nodes themselves. **Embedded modules** should be mostly text; other types of media should be displayed outside of nodes to not be distracting. Examples of such embedded modules would be a numbered list, to show steps. Modules both make use of the APIs of other services and also will be extensible via APIs of this project. Below is a list of modules that are to be developed.<sup>1</sup>

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
 * Numbered List
 * Time tracker
 * Diagram maker

All of these modules are not meant to be mainly web-based. **Mobile modules should also be developed** with a specialized interface.

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
 * Freebase
 * GIS Files
 * Khan Academy

####Module API and Directory

Note: API stands for Application Programming Interface. APIs allow different services to interact with each other, in the simplest sense.

APIs drive the Web today. This project will have both external and internal APIs. External APIs will be available so that other projects can integrate data from this project. Internal APIs will be available for developers to build modules for this project and integrate them with users' data. Also, an internal API will be available for those learning programming to toy with this project itself in their learning. Or even just a techy student who gets lazy and puts their computer to work for them.

A directory will be available for users to add custom modules or find outside services that can integrate with this project. All of the general security measures will be taken to ensure data safety and control.

An open API is not planned for development until *during or after the beta phase*. The open API will be a project of its own. It may be developed in tandem with the mobile applications. A closed API for in-built modules will be developed from the beginning.

###Containers

Containers are the next-biggest thing under Notebooks. Notebooks can contain nodes directly, however this will most often not be the case. Instead, *containers will typically contain nodes*. Containers are simply wrappers for nodes that put them in a more organized fashion. They can be used to sort nodes depending on how they are learned about. Obviously, a subject is not learned all at once. Most subjects are taught in sections. Many classes are taught chapter by chapter from a textbook. Ding ding, perfect use-case for a container. Having a container for each chapter would be an excellent organizational practice. Units are also another candidate for containers.

However, the point of this project is to help learners make connections. Following the dogma of this project, containers are not all-inclusive. Nodes may be *shared between containers* for better relationship definitions. In a U.S. History class, you may learn about political parties. In your first unit, you may learn about Federalists and Antifederalists. Later on in the course, you will be introduced to even more political parties. Even though the nodes with each political party are contained in a unit or chapter container, you may consider making a new container for political parties. A drag-and-drop interface will allow you to quickly add all of the political parties to their own category. If in every node that was a political party, you wrote "political party," a simple search would allow you to find everything you need. This could also be done automatically if proper computer learning techniques were utilized.

Note that categories may seem a lot like tags in other note-taking applications. In a way, they are, but not completely. In simple terms, tags would be *added to nodes* to classify them. Categories, adversely, are *what nodes are added to*. This way, categories must already exist, or be created on the fly, for nodes to be added to them. Though a tag-like interface may be used on nodes, in the end, categories are a better way of organizing the nodes.

Categories are expected to be used for review and establishing connections. Viewing categories by themselves creates a space for a learner to study a particular topic. Using modules, a **quiz** may be generated using the categories to single in on a topic. If a node is part of multiple categories, and multiple reviews are completed with each of those categories, nodes will be seen time and time again and linked with topics inside a learner's memory. This will also signify more important information. If a node is in more categories, there is a better chance that that node is more important.

###Nodes

The all-mighty node. Nodes in themselves are quite simple. They contain information. However, the way nodes in this project work is very useful. The structure of a node is broken down into different sections: the **title**, the **information**, and the **category** of the node. Node categories will be addressed in another sub-topic.

The **title** of the node is just like the title of anything else. It classifies the node and also helps modules and backends get a grip on what your node will be able. Titles in addition to node categories are very important, but that will be explained shortly. The title may also be seasoned with a **picture**. Pictures other than a main picture will have to fall in a module overflow. Nodes may also be color-coded for better distinction on modules like maps and a timeline.

The **information** for a node is all of the facts, statistics, opinions, and whatever else can be listed about the title. It is like bullets in typical note-taking applications. However, every **node entry**—bullet—is separable. They may be rearranged and manipulated individually. It is important to create multiple entries for each topic of information. This allows everything to flow more smoothly. For example, a multiple choice quiz may be generated using a node. Let's take this into example:

Node **A** has three node entries: *1*, *2* and *3*.
Node **B** has four entries: *4*, *5*, *6* and *7*.
Node **C** has three entries: *8*, *9* and *10*.

A multiple choice question is generated, which asks:

```
Which of the following is true about B?
A. 1
B. 3
C. 5
D. 9
```

The correct answer would be **C**. *5* is the node entry from Node **B**, so, unless there is overlap, *5* would be the true about Node **B**. In the long run, computer learning may take guesses at multiple choice entries that may have overlap and either remove those questions or make multiselect answers.

This brings up another point: what about information that isn't very useful on its own? Such as a person's age, birth-place, or things of the sort. Entries that contain this information may be flagged as insignificant. These types of facts are intended to be *imported* from a node backend, to save valuable research time.

Nodes may also have embedded **modules**. These modules will allow different types of information to be inputted. Some of such modules may be a numbered list, for ordering the steps of something. Another example could be a formula builder. Most of these embedded modules should be mostly text or glorified text. Other types of media should be stored outside of the node in other modules. The reason for embedded modules instead of simple embedded functionality is that modules can be developed independently. For things like a numbered list, this may seem like a simple function that should be native to nodes. However, the information in a node can be used elsewhere in a variety of different ways. A module for a numbered list separates the list from the node entries. This way, if a practice quiz or something related were to be generated, a special type of question could be tailored to the numbered list.

####Node Categories

Node categories are incredibly important in defining the function and relationships of a node. They also classify which modules and backends will be usable with said node. A node category is a very *broad classification* of the node title. For example, Mahatma Gandhi is a person. Japan is a geographical place. Harry Potter is a film. The Wrights brothers' flight is an event. A political party is a body of people. Many of these categories are too broad for useful classification. Sub-categories are available to further refine a categorization. Without further ado, a list of preliminary node categories:<sup>1</sup>

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
* Process

As the user base of this project grows, categories will be able to be automatically defined via a crowd-sourcing method.

<sup>1</sup>Note that this list is in need of major revisions and is subject to significant change. Much still needs to be added. Modules may be able to add custom categories to the list.

####Node Backends

Automatic definition of *known statistical facts* is implemented via node backends. The node backends used will depend on the node category chosen. Upon creating a node and defining a category and title, the service will use a backend to research the title. Relevant information will be presented near the node itself and may be added with a simple click. Insignificant information will automatically be defined and marked as insignificant, though that flag may be removed by the user if deemed inaccurate. Node backends will most likely be deeply integrated with module backends. Modules may be launched with relevant information about the specific node in addition to the pop-up info. As this project expands, the project itself may be used as a backend, pulling information from loads of other users. If all information is found *independently* of each other, it is more than likely accurate. Algorithms and software will be needed to verify this, however, and a voting system will be implemented.

All modules and backends used either automatically or manually will be linked to the node it was used with. This will allow nodes to become containers for deeper information. A Wikipedia article, for example, may be linked to a specific node. Or a picture library may help get a visual feel for the information. A video may clarify some of the information. Links and references may be added, as well, for a research project. This makes every node more extensible. ""Visual indicators** may be used on nodes to clarify which modules are linked to it before selecting the node.
 
####Node Links

Nodes may not only be linked to modules, but *internode connections may be established*. These links may be established automatically or manually via a click and drag interface. Users of graphic editing software may be familiar with node connections. However, node links in this project are not one-way. The benefits of node links may not be immediately noticeable. However, once it comes time to review information, node links will become life-savers. Let's say that you are learning about presidents. You find George W. Bush and see that he is a Republican. You need a refresher on the Republican Party. Good news for you, your node for the Republican Party is already floating next to Bush with a line indicating linkage. So you read what you have listed about the party. Then you find yourself wondering what other presidents are Republicans. So you click on the node and find 17 other Republican presidents. You can then see when parties were in office on the timeline, since the parties are color-coded.

Node links are obviously a powerful tool for reviewing information. Node links may be created automatically via backends, however manual creation is required. A good strategy for linking nodes from the start will pay off exponentially in the end. However, like everything else in this project, node-linkage is not a static property. Nodes links can be added, removed, or modified at any time. Node links can also be classified. To keep it simple, only a few link classifications are available:

 * Synonymous relationship
 * Antonymous relationship
 * Positive relationship
 * Negative relationship
 * Neutral relationship
 * Member-of relationship (a one way connection)
 
###Presentations

Presentations are an important part of learning and teaching alike. With so much information at hand, this project would be perfect for creating presentations. Different types of presentations may be created. Presentations could be exported or imported to backends, such as Powerpoints, Google Docs, or Prezi. Videos could also be created with a video editing module.

Presentations are a better method of conveying and sharing information than sharing nodes directly. Though node sharing will be possible, this project will always recommend creating and sharing presentations. **Presentations are not expected to be available at v1.0.0**.

####Presentation builder

At the heart of presentations is the presentation builder. The presentation builder will allow a user to pull in information to a presentation and apply visual effects to it to make it more appealing. Music, videos and other media may be imported. If a module is compatible with presentations, it can be used, as well. Since a node contains all relevant information, modules and links, creating a presentation can **move at an accelerated pace**. A user can focus more time on making the presentation appealing and understandable than researching and importing information.

As mentioned earlier, different types of presentations can be made. A few examples are a video, a slideshow, or a web. In each of these presentations, nodes can take different forms, links can be mapped to different slides or frames, and information can be organized to emphasize specific points. If so inclined, a simple web can be made of nodes, and a specific order of nodes can be presented. Linkages and other node data will persist.

###Print-out

Though this project is digital, it is important to take into consideration that some learners feel more comfortable taking notes on paper. Others may have no choice but to take notes on paper. Although it is the author's opinion that all schools should be providing some type of technology to students for their disposal, that decision is left to individual schools and is unfortunately not reflected in many of them. That is why this project will support print-outs and scan-ins.

Print-outs are simply papers with node boxes in them, where information can be written into. All of the necessary tools will be available, with the ability to show the scan-in processor what exactly the user wants done. The writer can specify their notebook of choice, whether or not a node is to be extended for more space, show links between nodes, assign nodes to categories (a sheet will be available for all available categories) and group nodes in containers.

Print-outs can also be filled out for review. A user may create a print-out, similar to the way he or she prepares a presentation, and print it out for review. Links will be preserved, and modules capable of print out will be printed with it. Custom settings will allow automatic formatting of modules (or lack thereof). A custom setting for number of pages may be employed, in case the user has limited resources. The more pages specified, the more information and modules may be listed. The pre-filled print-out system is expected to come out between v1.0.0 and v2.0.0.

####Scan-in

Once a user has everything filled out and has a chance to access a computer or phone, they can then scan in their papers. This can be done with a scanner or a photo. Naturally, photos will have to be high enough quality to be accurately interpreted. The scan-in processor will then have to use *pattern recognition* to read the handwriting, use other methods to interpret linkages and other informative marks, and pass the information to the user's account. The server will then attempt to automatically generate missed links and information, and apply applicable modules to the nodes. The print-out can then be discarded and replaced with a print-out with printed data. The print-out/scan-in system is not expected to be completed until many versions have passed. A great amount of research and testing must be observed firstly.

Interface
---------

The interface of this project is perhaps one of the most important aspects. A poorly designed interface would render this project useless. This project includes some complicated tasks. Those tasks ought to pay off in the end. However, if it is too complicated to complete these tasks, users may not opt to complete them. The interface of this project is designed with simplicity and functionality in mind.

###Design Principles

####Simplicity

The interface in this project must be simplistic as possible. Text will be used where necessary, but icons will also be used sparingly. Padding will be plentiful, and everything must be spaced correctly to **not be confusing**. To the same extent, the screen must not be filled with too much at any given time. The device being used and the resolution of the device will all have to be taken into consideration. To avoid distractions, this app must suggest (on computers) or force (on mobile devices) full screen as much as possible. Unimportant parts of the design must be either hidden or miniscule when not used. The user should not feel overwhelmed at any time while using this app.

####Functionality

Though the design is meant to be *simple*, the underlying functionality should be *heavy*. Functions should be hidden, and revealed to the user in intervals. Different functions should be accessible via different methods. Those methods should include mouse-specific and keyboard-specific functions. Methods on mobile devices should make use of mobile characteristics, such as accelerometers. Some learners are graphically oriented. They will want to use their mouse as much as possible. Functions should be available via mouse at all times, especially for beginners. Those same functions should be offered via keyboard commands, as well. Keyboard shortcuts should be compatible with other standard keyboard shortcuts. These should be revealed to the user in tip-form, so as not to overwhelm the user. However, for those who are naturally keyboard-oriented, an entire keyboard command list should be offered.

####Color and Layout

The default color and layout should be neutral and neutrally appealing. Notice the keyword, "default." Customizability will be discussed shortly. The theme must be textured, but not overly so, and should make use of colors and effects to show functions and events. Contrast should be employed, and emphasis should be put on what the user is currently working on. Distracting colors and layouts are to be shunned. The layout of this project must be **logical**. Nodes, modules and system functions should be placed in logical places throughout the interface. Their placements should be specifically linked to their functions.

####Customizability

All learners are different. Although some users simply want to stick with the default theme, many will be inclined to customize it to their taste or work styles. A library of themes should be available, as should a theme manager to further refine styles. Color schemes should be employed as opposed to individual color selection to all faster and easier modification of colors and themes. Layouts should be customizable by employing *moveable* and *collapsible* panels. A user should be able to view or hide what they want at any given time during operation. Though some tasks may be automated, options should be given to suppress these automations and replaced with tooltips to perform those tasks manually.

The settings page should be segregated in terms of basic and **advanced settings**. Basic settings should suffice for most users, but users wishing for more control should be allowed to exercise finer control over their interface. Options that can be modified automatically or via the code of the project should also be modifiable by the user. This, in effect, gives users as much freedom as the designers could easily obtain.

####Third-party Principles

All of these principles extend down to third-party modules or backends. Backends must be customized to allow for integration into the interface system. Color schemes and layouts should also affect the backends and third-party modules. Developers of third-party modules should have a document resembling this one with a set of design principles to follow. The module API should allow for integration into the interface system. A review system may need to be employed to enforce compliance.

###Interface Breakdown

This section will describe most parts of the interface. Some parts may be subject to modification and adaptation, but most of these definitions should be followed.

A new user is presented with a very nice page presenting information of the project and its branding. Registration is available on this page directly. The registration/login page is overly simplistic yet informational. Videos and pictures are prominent and exemplify the features of this project. However, links are provided in an easily visible bar to find more information about the project, contact information, prices (if applicable) and more. Registration is *not* required for accessing any of those links. As many of those links as possible do not require loading a new page, rather they move elements to show the information. Also, a new page is not loaded for registration or logging in. This keeps everything simple and concise.

Note: this refers to the default layout. Many of the modules, panels and settings are customizable by the user.

After the user logs in, they will be presented with a notebook canvas and a notebook list on the left. The notebook canvas is populated with the most recent edited notebook if the user isn't new, or is blank for a new user. If no notebooks are available, the notebook list will instead request that the user adds a new notebook. A toolbar is available at the top that has links to user settings, sharing information and user information. Branding for this project is also visible. After a notebook is selected, this toolbar will be made thinner or hide itself, depending on the settings of the user and the screen resolution. A watermark for branding of this project may or may not be visible if the toolbar is hidden. The notebook list is meant to be hidden, as the notebook canvas is pushed to the right rather than shrunken when the list is open. The notebook list is hidden when a notebook is selected. All hidden panels are be accessible either by hovering or clicking on an overlaid pulldown marker.

A new user is presented with a tutorial about how to use the application that is overlaid on the entire interface. The tutorial is preliminary, and shows only the basics of the app. An example notebook will be opened to demonstrate some of the features. The user will be guided through using the application. This tutorial is navigable and may be closed at anytime. It will also be available via a help menu on the toolbar. Most tutorials this app uses are like this one.

The notebook canvas is where the user will spend most of his or her time. The canvas takes up the entire screen once a notebook is selected. The main attractions of the canvas are the nodes. They will take up the entire screen if no modules are opened. Depending on the previous layout, these nodes may be arranged in a linear fashion, a web view, or other layouts defined by modules. The node layout may be changed via a floating selector. Different markers, such as lines or icons, show connections and information about the nodes. Panel pull-out markers are available on the sides of the canvas. These panels are stackable and paginated. The panels may automatically expand when selecting a node that uses a module. Inside the panels are modules. Depending on the type of modules, they may be listed in a scrollable list, they may be paginated, or a module may take up the entire panel. Modules may be dragged, moved, opened or closed. A search box will float in the canvas and allow for searching the information and also modules. The rest of the functionality in the design boils down to the specificities of the node system and the module system. Those specificities will be constantly developed, and will not be listed here.

Development Workflow
--------------------

There are a few central principles that must be defined and points that must be made before getting into the actual development workflow. They are as follows.

###Principles and Points

####Django

Starting this project, Django is used to get a start using Python as a web programming language. Django offers a few features that could benefit this project. However, it is important to realize that a migration away from Django is expected in the future. Django may still be used as a wrapper, but many of its functions will be replaced by home-brewn functions. Development of this project must realize this. Different apps in Django should be replaceable by custom modules one at a time, so that Django can eventually be pushed out. There are no personal vendettas against Django here, however this project may require customization that extend beyond the customization offered by Django.

####Modularity

All parts of this project must be developed with the ability to be separated from each other. Though they will communicated via an object oriented approach, the innards of apps (objects) should be able to be rewritten while the rest of the project stays the same. Modularity will allow for ease of maintenance and also an easier migration away from Django.

####Collaboration

This app was designed originally to be developed by one person. That, of course, may change as the project grows. It is for this reason that collaboration must be taken into consideration throughout the development of this project. Code should be properly designed and commented. Git must be used thoroughly and wholly throughout the entire development process. All commits should be labeled and tags should be useful indicators of progress. A central checklist, perhaps this very README, should be employed. The project should be designed so anybody can pick up or leave off the project at any time.

####Databases

The development of this project will use a PostgreSQL database to start. The structure of the database will be defined later and as development progressed, but it is important to note the PostgreSQL is a relational database. Though the database will suffice for user details and other structured data, the storing of nodes is more of a dynamic and unstructured data type. In the future of this project, a graph database is expected to be employed. A graph database will better support the node layout of this project, as they use the same principles: nodes and connections. Just like computers can learn more from a node database, people should be able to learn more from a node note-taking system.

####Error Handling

Error handling was initially an afterthought and then realized to be a very important aspect of development. To have a better understanding of how errors will be handled, a distinction must be made between user and system errors. **User** errors are errors invoked by a user. These errors are to be expected and thrown after a validation fail. **System** errors are errors that the user could not fix. System errors include programming errors and communication errors.

User errors will have their own error handling module that is expected to handle the loading and translation of strings. This is to provide a simple interface for defining what the user will see when causing an error. User errors are to be handled by the UserError exception. A set of error codes is passed to the exception. The exception is not to be caught by any modules other than a view. However, if the catching of an exception is required, the exception should be passed on to the view in order to display valuable information to the user. Exceptions should be thrown only after all validations take place in a definition; the error codes being appended and passed at the end. In high security definitions, such as login authentication, only one error code should be given to prevent distinguishable errors from appearing for malicious users.

System errors must be logged extensively. The user should only receive one error page that gives no information about the error other than an instance number that can be sent to an administrator to debug the issue. That instance error should also be logged alongside the error itself. System errors may in the future have their own string handler, but that would only be for nested views such as a user's module.

###Development Process

The process of development will start simple. Django's features will be used, and data processing will remain simple. As time progresses, however, development will become more complicated. For that reason, organization is of utmost importance from the beginning of development. All aspects of development should be documented and tracked. A checklist of development is provided.

####Checklist

This checklist is to be modified as development proceeds. Development and this checklist are to be meshed. Keys for this checklist:

* **Bold** items indicate **current** development progress.
 * Currently developed items should have sub-items for more specific progress.
* Normal items indicate **incomplete** development progress.
* ~~Crossed out~~ items indicate **complete** development progress.
* [Bracketed] version numbers or number ranges indicate when the development progress is expected to be completed by if the item is normal or **bold**, or was completed if the item is ~~crossed out~~.

The development checklist is intended to be in as much order as it can be. Some pieces of development will depend on others, so many will be developed concurrently, but an effort will be made to keep the checklist in chronological order. The checklist:

* ~~Error handling~~ [v1]
 * ~~User errors~~
 * - ~~Exception class~~
 * - ~~String handler~~
 * ~~System errors~~
 * - ~~Logging system~~
 * ~~Validator methods~~
* ~~Locality~~ [v1]
* **Login/account system** [v1]
 * ~~Database structure~~
 * Login system methods
 * - ~~Password protection (Salt, CSPRNG, bcrypt)~~
 * - ~~Password complexity checking~~
 * -- ~~http://its.ucsc.edu/policies/password.html~~
 * -- ~~May be appended later~~
 * - Password recovery
 * - Connected accounts
 * - Ambiguous error pages
 * Session management
 * Brute force protection
 * Admin section
 * - Admin 2-step (OAUTH)
 * - ~~SSL client authorization~~
 * ~~SSL (StartSSL)~~
* Graphical interface for accounts [v1]
* Database layout for general node system [v1]
* Graphical interface for general node system [v1]
* In-house module API database layout [v1]
* In-house module API [v1]
* Backend system [v1]
* In-house modules (list should be established at this point) [v1]
* Simple transfer print-out sheets [v1]
* Project name [v1]
* User tutorial [v1]
* In-house alpha modules (list should be established at this point) [v2]
* Prefilled print-out system [v2]
* Presentation system [v2]
* Move to graph database system for nodes [v2]
* Sharing system created [v2]
* In-house beta modules (list should be established at this point) [v3]
* Open module API [v3]
* Complete print-out system with scan-ins [v3]
* Open general API [v3]
* Mobile apps [v3]

Project Versioning
------------------

Note: The lowercase V next to a number indicates a version number. For example, v0 indicates version 0, v1 indicates version 1, etc.
Also note: This section only refers to the website project version. APIs and mobile apps will have their own versioning section.

###Version number breakdown

Version numbers are in the format of vX.Y.Z, except for development progress, which includes another identifier (vX.Y.Z.A):

####vX.y.z.a

*X* refers to major updates to the project. Updates to this number will indicate advanced usability for the project. v0 is the development phase. v1 is the alpha phase. v2 is the beta phase. Finally, v3 is the production phase. All subsequent major updates will be labeled v4 and so on. Major updates are intended to be employed when many number of changes have been made and the project has a new plethora of changes. All new designs should be rolled into a major upgrade. Users may have to become accustomed to major updates, so most major updates should include a "getting started with v**X**.0.0" tutorial. Introduction of a new major release may require down-time, which is important to take into consideration.

####vx.Y.z.a

*Y* refers to minor upgrades to the project. This may be a new modules, a fairly large amount of bug updates, or another task in the checklist completed. In fact, every time a new item in the checklist is completed, the minor number should be incremented. Note that this refers to main items, not sub-items.

####vx.y.Z.a

*Z* refers to bug fixes or minor progress. *Z* should be updated for every sub-item on the checklist that is completed. It should also be updated whenever a major bug fix or many small bug fixes are released. In a production environment, this will be the most frequently updated version number, so it is important not to change this too often. Single small bug fixes should be pushed off until an adequate number of small bug fixes are created.

####vx.y.z.A

*A* refers to the development versioning number. This is likely to be incremented often. *A* should incremented every time a major developmental breakthrough is solidified. Small bug fixes should be included in this version numbering. If a part of development breaks anything else, or if it is unusable, *A* should not be incremented. However, incomplete developments may be included as long as they work and do not break anything else.

*A* will not be used in any production version of this project. However, a user may opt to sign up for developmental testing. Those users would only get updates as long as they made it into an *A* increment. This would mean that undercover developments cannot be included in *A*. Note that the development environment (dev.projectname.com) will reflect intermediary updates between increments of *A*. These updates will not be tagged with version numbers. This is because development may break parts of the project. The development environment should only be used and available to developers of the project.

###Development Phases

####Development (v0)

The development of this project will take place during v0. The development phase is where most of the groundwork will be laid for the project. It will include rapid development and changes. Registration for the project will not be opened to the public. The registration page is to be developed, but it should be locked. Note that as v0 is not considered a production phase, the A versions will be pushed to the production environment. v0.0.0.0 is to be the beginning of this project, at the completion of this README.

####Alpha (v1)

The alpha phase is the first production phase for this project. For that reason, a plethora of bugs is expected to pop up. These must be dealt with before moving onto the beta phase. Also, v1 will be incomplete in terms of usability. Most of the functionality expected will be there, but some features will have to be pushed off until v2. For that reason, the alpha phase should allow only a select number of users in the beginning. Later during the alpha phase, it may be opened up to the public.

The alpha phase is expected to be completed by the time my graduation experience presentation begins.

####Beta (v2)

The beta phase of this project must be able to be opened to the public. Many of the most apparent bugs are to be fixed and all functionality that makes the project what it is should be available. Production during v2 will take place at a rapid pace to get it ready for v3.

####Production (v3)

The production phase is when everything is set in stone and ready for a large user base. During v3, production of the website should slow to focus more development on the mobile apps and APIs for the project. Most bugs should be taken care of, and feature requests will most likely provide the basis for development during v3. Advertising may be employed at this point if the project is expected to yield a profit.

####Massive Upgrades (v4+)

Subsequent upgrades to this project may have names or labels to classify them. They will be used for major upgrades and changes that will directly affect many users. Note that just because this project has reached a stable phase, development should not hault. Innovation is very important and this project should continue to grow version after version to serve the needs of many students, learners and general people.
