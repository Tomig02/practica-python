categorias = '''
ptive Technologies
Artistic Software
Communications

    BBS
    Chat
        ICQ
        Internet Relay Chat
        Unix Talk 
    Conferencing
    Email
        Address Book
        Email Clients (MUA)
        Filters
        Mail Transport Agents
        Mailing List Servers
        Post-Office
            IMAP
            POP3 
    FIDO
    Fax
    File Sharing
        Gnutella 
    Ham Radio
    Internet Phone
    Telephony
    Usenet News 

Database

    Database Engines/Servers
    Front-Ends 

Desktop Environment

    File Managers
    GNUstep
    Gnome
    K Desktop Environment (KDE)
    Screen Savers
    Window Managers
        Blackbox
        Fluxbox
        XFCE 

Documentation

    Sphinx 

Education

    Computer Aided Instruction (CAI)
    Testing 

Games/Entertainment

    Arcade
    Board Games
    First Person Shooters
    Fortune Cookies
    Multi-User Dungeons (MUD)
    Puzzle Games
    Real Time Strategy
    Role-Playing
    Side-Scrolling/Arcade Games
    Simulation
    Turn Based Strategy 

Home Automation
Internet

    File Transfer Protocol (FTP)
    Finger
    Log Analysis
    Name Service (DNS)
    Proxy Servers
    WAP
    WWW/HTTP
        Browsers
        Dynamic Content
            CGI Tools/Libraries
            Content Management System
            Message Boards
            News/Diary
            Page Counters
            Wiki 
        HTTP Servers
        Indexing/Search
        Session
        Site Management
            Link Checking 
        WSGI
            Application
            Middleware
            Server 
    XMPP
    Z39.50 

Multimedia

    Graphics
        3D Modeling
        3D Rendering
        Capture
            Digital Camera
            Scanners
            Screen Capture 
        Editors
            Raster-Based
            Vector-Based 
        Graphics Conversion
        Presentation
        Viewers 
    Sound/Audio
        Analysis
        CD Audio
            CD Playing
            CD Ripping
            CD Writing 
        Capture/Recording
        Conversion
        Editors
        MIDI
        Mixers
        Players
            MP3 
        Sound Synthesis
        Speech 
    Video
        Capture
        Conversion
        Display
        Non-Linear Editor 

Office/Business

    Financial
        Accounting
        Investment
        Point-Of-Sale
        Spreadsheet 
    Groupware
    News/Diary
    Office Suites
    Scheduling 

Other/Nonlisted Topic
Printing
Religion
Scientific/Engineering

    Artificial Intelligence
    Artificial Life
    Astronomy
    Atmospheric Science
    Bio-Informatics
    Chemistry
    Electronic Design Automation (EDA)
    GIS
    Human Machine Interfaces
    Hydrology
    Image Processing
    Image Recognition
    Information Analysis
    Interface Engine/Protocol Translator
    Mathematics
    Medical Science Apps.
    Physics
    Visualization 

Security

    Cryptography 

Sociology

    Genealogy
    History 

Software Development

    Assemblers
    Bug Tracking
    Build Tools
    Code Generators
    Compilers
    Debuggers
    Disassemblers
    Documentation
    Embedded Systems
    Internationalization
    Interpreters
    Libraries
        Application Frameworks
        Java Libraries
        PHP Classes
        Perl Modules
        Pike Modules
        Python Modules
        Ruby Modules
        Tcl Extensions
        pygame 
    Localization
    Object Brokering
        CORBA 
    Pre-processors
    Quality Assurance
    Testing
        Acceptance
        BDD
        Mocking
        Traffic Generation
        Unit 
    User Interfaces
    Version Control
        Bazaar
        CVS
        Git
        Mercurial
        RCS
        SCCS 
    Widget Sets 

System

    Archiving
        Backup
        Compression
        Mirroring
        Packaging 
    Benchmark
    Boot
        Init 
    Clustering
    Console Fonts
    Distributed Computing
    Emulators
    Filesystems
    Hardware
        Hardware Drivers
        Mainframes
        Symmetric Multi-processing
        Universal Serial Bus (USB) 
    Installation/Setup
    Logging
    Monitoring
    Networking
        Firewalls
        Monitoring
            Hardware Watchdog 
        Time Synchronization 
    Operating System
    Operating System Kernels
        BSD
        GNU Hurd
        Linux 
    Power (UPS)
    Recovery Tools
    Shells
    Software Distribution
    System Shells
    Systems Administration
        Authentication/Directory
            LDAP
            NIS 

Terminals

    Serial
    Telnet
    Terminal Emulators/X Terminals 

Text Editors

    Documentation
    Emacs
    Integrated Development Environments (IDE)
    Text Processing
    Word Processors 

Text Processing

    Filters
    Fonts
    General
    Indexing
    Linguistic
    Markup
        HTML
        LaTeX
        Markdown
        SGML
        VRML
        XML
        reStructuredText 

Utilities 
'''

def print_con_formato(dict):
    ''' imprime con el formato que pide el ejercicio '''

    divisor = '-' * 25

    print(divisor)
    print('Categoria: ', x)
    print(divisor)
    print('cant: ', dict[x]['cant'])
    print('Subcategorias: ')
    for suc in dict[x]['nombres']:
        print(suc)
    print(divisor)




# decalracion
categorias = categorias.splitlines()
sub_cat = []
dict_cats = {}
ant = ''
cant = 0

# recorre todo el string chequeando si no es una linea vacia, luego
# diferencia las categorias de las subcategorias segun si empiezan 
# con un espacio en blanco y cuenta
for line in categorias:
    if line:
        if not line[0] == ' ':
            if ant:
                dict_cats[ant] = {'cant': cant, 'nombres': sub_cat}
                sub_cat = []
                cant = 0
            ant = line
        else:
            cant += 1
            sub_cat.append(line.strip())

# algo como un menu para poder ver el resultado
x = input('ingrese una categoria: ')
while not x == 'close':
    if x in dict_cats:
        print_con_formato(dict_cats)
    else:
        print('categoria incorrecta')
    x = input('ingrese una categoria: ')



