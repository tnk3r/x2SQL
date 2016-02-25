#!/usr/bin/env python

import re, os, sys, time, csv, string
import hashlib, mysql.connector
from Tkinter import *
from PIL import Image, ImageTk
import xml.etree.ElementTree as ET
from tkFileDialog import *
import ttk

# TO DO:
    #Mov to Qt Framework
    # When searchRoll activate (event), so when import csv, roll is queried.
    # export XMl pretty
    #Make buttons for Import/Insert/Export/Show XML
    #Fix tree view box and align with top one.
    #Fix insert for each UID in DB not in Camera Report
    #Create exceptions for SQl errors to track down the problems.##
    #Scrollbars and grid layout ... yet again...
    #hide ASCCDL / Camera Attributes ie extra Columns in Metadata Tree,
    #fix errors in loading too many clips ( index error in the metatree insert line [u] & [x] )

    # try /except for show columns?? If Camera report inserted or not, to hide/show extra fields
            # Query if Roll exists, if not for each clip then show = standard.

    # add handler for if false start, if on roll, but not on camera report. put in Notes, false Start for clip/
    # Fix look-up for other cameras, Start with Arri, Red, Phantom, F55
    # search roll/scene  for shots table metadata to be displayed?
                    # Timecode
                    # duration
    # Add search field for notes, For when you dont know scene or Roll.
    # Add ColorSpace / Gamut
    # Add Scene/Take above CDL info?
    # Remove ASC CDL From Tree View, Or have option for Show all Fields. Menu Preference?
    #Test CDl export feature in exd 2014, consider new placement for highres frames
    # Query for Camera format in Shots table to have correct element for ET when pulling Gamma
    # update cdl export filename so it matches Scene # exactly
    # handle cancel event on file import
    # Fix columns shown.... If first column has list its is used for all clips. Must change
    # #---------Give Columns whole list metadata+Camreport
    #   #fields and omit entires that do not exist in db from report.
    # Roll searching must have letter index to increment, change to optional regex??+




    # -- DONE --

    # Fix switching between Roll search and Scene Search

    # Increment buttons up/ down for Roll and Scene, numerically +1 / -1
    # Fix option menu when searching for new scene, "doesnt change when new scene typed in"
    # Get Filename via Shots table? I guess its fine from mediadb or shots.
        # ---    #regex for filename ---
        # fix Filename column ordering, perhaps line by line? Regex for 'C0\d+\d+'
                # always want Filename first on metatree.




main = Tk()
main.title('x2Sql')
main.wm_geometry('1700x850')
main.config(bg='gray10')
#main.resizeable(FALSE,FALSE)
#layout = Frame(main, bg='gray10', bd=0, highlightthickness=0)
#layout.config(width=400, height=500)
#layout.grid(column=1,row=1)

treeFrame = Canvas(main, bg='gray10', highlightthickness=0, width=100, height=100, relief=SUNKEN)
treeFrame.place(x=20,y=60)
importFrame = Canvas(main, bg='gray10', highlightthickness=0, width=800, height=50)
importFrame.place(x=0,y=0)
metatreeFrame = Canvas(main, bg='gray10', highlightthickness=0, relief=SUNKEN, scrollregion=(0,0,1000,1000))
metatreeFrame.place(x=20,y=620)
emptyTable = []



for i in range(15):
    emptyTable.append(i)
tree = ttk.Treeview(treeFrame, columns=emptyTable)
#hsb = ttk.Scrollbar(treeFrame, orient="horizontal")
#vsb = ttk.Scrollbar(treeFrame, orient="vertical")
#tree.config(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
for i in range(len(emptyTable)):
    tree.column(i, anchor='center',width=96, stretch=FALSE)
tree.grid(column=0, row=0, sticky='nswe')
#hsb.config(command=tree.xview)
#vsb.config(command=tree.yview)
#treeFrame.config(scrollregion=(0, 800, 800, 700))
#vsb.grid(column=1, row=0, sticky='ns')
#hsb.grid(column=0, row=1, sticky='ew')
treeFrame.grid_columnconfigure(0, weight=1)
treeFrame.grid_rowconfigure(0, weight=1)
treeFrame.create_window(20, 100)

showList = ["Scene","Take", "Lens", "Type", "Stop", "Focus", "Tilt","Cam-Height","ShutterSpeedAngle","ColorTemp","CaptureFrameRate", "CameraFormat", "Width", "Height", "Notes"]
def openFile(event):
        global filename, x, tree, Roll, csvMaster, columns, RollList, OrderColumn
        OrderColumn = StringVar()
        filename = askopenfilename(parent=main)
        inputFile.set(filename)
        with open(filename, 'rU') as csvFile:
                readCSV = csv.reader(csvFile, delimiter=',')
                csvMaster = []
                for row in readCSV:
                        csvMaster.append(row)
        columns = csvMaster[0]
        if 'Cam' in columns:
            columns.remove('Cam')
        if 'Order' in columns:
            OrderColumn.set(columns.index("Order"))
            columns.remove('Order')
        tree = ttk.Treeview(treeFrame, columns= columns)
#        vsb = ttk.Scrollbar(tree, orient="vertical")
#        hsb = ttk.Scrollbar(tree, orient="horizontal")
#        tree.config(xscrollcommand=hsb.set)
#        hsb.config(command=tree.xview)
#        vsb.config(command=tree.yview)
        tree.grid(column=0, row=0, sticky='nswe')
#        vsb.grid(column=1, row=0, sticky='ns')
#        hsb.grid(column=0, row=1, sticky='ew')
#        treeFrame.grid_columnconfigure(0, weight=1)
        treeFrame.grid_rowconfigure(0, weight=1)
        treeFrame.create_window(20, 100 )

        for field in columns:
            if field == 'Notes':
                normal = 500
            else:
                normal = 63

            tree.column(field, anchor='center',width=normal, stretch=FALSE)
            tree.heading(field, text=field)
        t = 1
        tree.tag_configure('ttk', background='white', foreground='black')
        print "Report Has "+str(len(csvMaster))+" Entries"
        RollList = []
        for row in range(len(csvMaster) - 1):
            count = t - 1
            previous = csvMaster[count][0]

            currentValues = csvMaster[t]
            c = int(OrderColumn.get())
            currentValues.remove(currentValues[c])

            if csvMaster[t][0] == csvMaster[count][0]:
                tree.insert(previousRoll, 'end', row, tags=('ttk'), values=currentValues)
                t += 1
            else:
                previousRoll = tree.insert("", row, text=csvMaster[t][0],tags=('ttk'), open=True)
                tree.insert(previousRoll, 'end', row, tags=('ttk'), values=currentValues)
                RollList.append(csvMaster[t][0])
                t += 1

        searchRollQuery.set(csvMaster[1][0])
        searchRoll

def insertMediaRoll(event):
    global shotslist, Roll, csvMaster
    Roll = StringVar()
    Roll.set("%"+SearchRollField.get()+"%")
    for roll in RollList:
        print roll
        curs1.execute("SELECT * From `mediametadata` WHERE `name` LIKE 'FileName' AND `value` LIKE '%s'" % (roll))
        result = curs1.fetchall()
        UniqList = []
    for i in result:
        UniqList.append(i)
    w = 1
    # for multi line CSV with more Roll#
    for line in range(len(csvMaster) - 1):
        csvScene = csvMaster[w][1]
        csvTake = csvMaster[w][2]
        curs1.execute("SELECT UniqueID From `shots` WHERE Scene LIKE '%s' AND Take LIKE '%s'" % (csvScene, csvTake))
        result = curs1.fetchone()
        try:
            UniqInsert = str(result[0])
            UniqList.append(result[0])

            if UniqInsert in UniqList:
                print "Scene: "+csvScene+" Take: "+csvTake+" 'In the DB under:'"+UniqInsert
                for f in range(len(csvMaster[w])):
                    name = str(csvMaster[0][f])
                    value = str(csvMaster[w][f])
                    if name == "Height":
                        name = "Cam-Height"
                    if "\'" in value:
                        value = value.replace("\'", "\\'")
                    if "\"" in value:
                        value = value.replace("\"", "\\\"")
                    #print "INSERT VALUES %s, %s, %s" % (UniqInsert, name, value)
                    values = str("'NULL', "+"'"+UniqInsert+"'"+", "+"'"+name+"'"+", "+"'"+value+"'")
                    #print values
                    try:
                        curs1.execute("INSERT INTO `mediametadata` VALUES (%s)" % (values))
                    except mysql.connector.Error as e:
                        #print "Error in "+name+" : "+value+" : "+str(e.msg)
                        print str(e)
                        pass
        except:
            print "not in db"
            pass
        w += 1

def selectDatabase(event):
    global filedatabase, projectDirectory, today, projectMetaData
    curs1.execute("USE "+ str(db.get()))
    filedatabaseRead = open("/MediaDatabase/.currentproject.txt", 'r')
    filedatabase.set(filedatabaseRead.read().strip())
    todayRead = open("/MediaDatabase/.today.txt", 'r')
    today.set(todayRead.read().strip())
    projectDirectoryRead = open("/MediaDatabase/"+str(filedatabase.get())+"/.dest.txt", "r")
    projectDirectory.set(projectDirectoryRead.read().strip())
    print "Project : "+filedatabase.get()+"  Today : "+today.get()+"  Directory = "+projectDirectory.get()
    curs1.execute("SELECT value FROM `settings` WHERE param = 'MetadataPath'")
    result = curs1.fetchone()
    print "Project metadatapath = "+str(result[0])
    projectMetaData.set(result[0])

def autoscroll(sbar, first, last):
        #"""Hide and show scrollbar as needed."""
        first, last = float(first), float(last)
        if first <= 0 and last >= 1:
                sbar.grid_remove()
        else:
                sbar.grid()
        sbar.set(first, last)

def setNewScene(event):
    searchQuery.set(shot.get())
    searchScene(event)

def getAllShotsinScene():
    global shotslist
    shot.set(SearchField.get())
    scene.set(str("%"+str(scene.get())+"%"))
    curs1.execute("SELECT Scene From `shots` WHERE `Scene` LIKE '%s'" % (scene.get()))
    shotResult = str(curs1.fetchall())
    shotResult = shotResult.split()
    shotsList = []
    for item in shotResult:
        m = re.search("\w+\w+", item)
        if m.group(0) in shotsList:
            pass
        else:
                shotsList.append(m.group(0))
    shotsListMenu = OptionMenu(main, shot, command=setNewScene, *shotsList)
    shotsListMenu.config(bd=0,bg='gray10')
    shotsListMenu.place(x=400,y=ymid)
def PRINT():
    print "pressing Label at the Top?"

def getinfobyUID():
    global metatree, sceneUID, UniqueIDList, metadataFields, metatreeFrame, fileColumn
    curs1.execute("SELECT * From `mediametadata` WHERE UniqueID LIKE '%s'" % (Uniq.get()))
    result = curs1.fetchall()
    metadataFields = []
    FullList = ['ASCCDL1', 'ASCCDL10', 'ASCCDL2',
    'ASCCDL3', 'ASCCDL4', 'ASCCDL5', 'ASCCDL6',
    'ASCCDL7', 'ASCCDL8', 'ASCCDL9', 'Cam-Height',
    'CameraAttributes', 'CameraFormat', 'CaptureFrameRate',
    'ColorTemp', 'Date', 'ExposureIndex', 'FileName',
    'Filter', 'Focus', 'GammaForCDL', 'Height',
    'ImageSensorReadoutMode', 'ISOSensitivity', 'Lens',
    'NeutralDensityFilterWheelSetting', 'Notes', 'Roll',
    'Scene', 'Shutter', 'ShutterSpeedAngle', 'Stop',
    'Take', 'Tilt', 'Type', 'VFX', 'WB', 'WhiteBalance',
    'Width']
    EditedList = ['Roll','Scene', 'Take','CameraFormat',
    'CaptureFrameRate','ColorTemp', 'ExposureIndex', 'FileName',
    'Filter', 'Focus', 'Lens', 'Type',
    'Shutter','Stop','Tilt',  'VFX', 'WB', 'Notes',]
    for i in result:
        metadataFields.append(i[2])
    fileColumn = StringVar()
    print metadataFields
    metatree = ttk.Treeview(main, columns= FullList, displaycolumns=EditedList,  selectmode='browse')
#    metavsb = ttk.Scrollbar(metatree, orient="vertical")
#   metahsb = ttk.Scrollbar(metatree, orient="horizontal")
#    metatree.config(yscrollcommand=metavsb.set, xscrollcommand=metahsb.set)
    metatree.place(x=20,y=620)
    metatree.bind("<<TreeviewSelect>>", searchSelection)
#    metahsb.config(command=metatree.xview)
#    metavsb.config(command=metatree.yview)
#    metavsb.grid(column=1, row=0, sticky='ns')
#    metahsb.grid(column=0, row=1, sticky='ew')
#    metatreeFrame.grid_columnconfigure(0, weight=1)
#    metatreeFrame.grid_rowconfigure(0, weight=1)
    for m in metadataFields:
        if m == "FileName":
            fileColumn.set(metadataFields.index("FileName"))
        metatree.column(m, anchor='center',width=70, minwidth=50, stretch=False)
        metatree.heading(m, text=m, anchor='w', command=PRINT)
    metatree.tag_configure('ttk', background='white', foreground='black')
    u = 0
    if len(UniqueIDList) <= 1:
        metarow = []
        curs1.execute("SELECT * From `mediametadata` WHERE UniqueID LIKE '%s'" % (Uniq.get()))
        result = curs1.fetchall()
        ID = Uniq.get()
        for i in result:
            metarow.append(i[3])
        for field in metarow:
            m = re.search("[A-Z][0-9]+[C][0].._\w+..", field)
            if m:
                filename = m.group(0)
        metatree.insert("", 'end',ID, tags=('ttk'), text=filename,values=metarow)
    else:
        for i in range(len(UniqueIDList)):
            metarow = []
            i = Uniq.get()
            curs1.execute("SELECT * From `mediametadata` WHERE UniqueID LIKE '%s'" % (UniqueIDList[u]))
            result = curs1.fetchall()
            for i in result:
                metarow.append(i[3])
            for field in metarow:
                m = re.search("[A-Z][0-9]+[C][0].._\w+..", field)
                if m:
                    filename = m.group(0)
            metatree.insert("", 'end',UniqueIDList[u], tags=('ttk'), text=filename,values=metarow)
            u += 1
        UniqueIDList = []

def getimg():
    global openThumb, Thumb
    projectThumbs = projectMetaData.get()+"/grade/"
    openThumb = Image.open(str(projectThumbs+"thumbs/"+Uniq.get()+".tif"))
    Thumb = openThumb.resize((500, 300), Image.ANTIALIAS)
    Thumb = ImageTk.PhotoImage(Thumb)
    Thumbnail.config(image=Thumb)



def getCDL():
    global root
    curs1.execute("SELECT LatestGrade From `latestgrade` WHERE UniqueID LIKE '%s'" % (Uniq.get()))
    result = curs1.fetchone()
    print "Fetching CDL for: "+str(Uniq.get())
    xml = ET.fromstring(result[0])
    cdl = xml.find('CDL1')
    rOffset = cdl.find('ROffset').text
    gOffset = cdl.find('GOffset').text
    bOffset = cdl.find('BOffset').text
    rSlope = cdl.find('RSlope').text
    gSlope = cdl.find('GSlope').text
    bSlope = cdl.find('BSlope').text
    rPower = cdl.find('RPower').text
    gPower = cdl.find('GPower').text
    bPower = cdl.find('BPower').text
    Saturation = cdl.find('Saturation').text
    root = ET.Element("ColorDecisionList")
    colorDecision = ET.SubElement(root, "ColorDecision")
    colorCorrection = ET.SubElement(colorDecision, "ColorCorrection")
    sopNode = ET.SubElement(colorCorrection, "SOPNode")
    satNode = ET.SubElement(colorCorrection, "SatNode")
    saturation = ET.SubElement(satNode, "Saturation")
    offset = ET.SubElement(sopNode, "Offset")
    slope = ET.SubElement(sopNode, "Slope")
    power = ET.SubElement(sopNode, "Power")
    offset.text = rOffset+" "+gOffset+" "+bOffset
    power.text = rPower+" "+gPower+" "+bPower
    slope.text = rSlope+" "+gSlope+" "+bSlope
    saturation.text = Saturation
    offx = 820
    slopex = 1010
    powerx = 940
    ry = 530
    gy = 550
    by = 570
    rOffsetLabel = Label(main, bg='gray10',text="R :    "+rOffset, bd=0, fg='white')
    rOffsetLabel.place(x=offx, y=ry)
    gOffsetLabel = Label(main, bg='gray10',text="G :    "+gOffset, bd=0, fg='white')
    gOffsetLabel.place(x=offx, y=gy)
    bOffsetLabel = Label(main, bg='gray10',text="B :    "+bOffset, bd=0, fg='white')
    bOffsetLabel.place(x=offx, y=by)
    rSlopeLabel = Label(main, bg='gray10',text=rSlope, bd=0, fg='white')
    rSlopeLabel.place(x=slopex, y=ry)
    gSlopeLabel = Label(main, bg='gray10',text=gSlope, bd=0, fg='white')
    gSlopeLabel.place(x=slopex, y=gy)
    bSlopeLabel = Label(main, bg='gray10',text=bSlope, bd=0, fg='white')
    bSlopeLabel.place(x=slopex, y=by)
    rPowerLabel = Label(main, bg='gray10',text=rPower, bd=0, fg='white')
    rPowerLabel.place(x=powerx, y=ry)
    gPowerLabel = Label(main, bg='gray10',text=gPower, bd=0, fg='white')
    gPowerLabel.place(x=powerx, y=gy)
    bPowerLabel = Label(main, bg='gray10',text=bPower, bd=0, fg='white')
    bPowerLabel.place(x=powerx, y=by)
    saturationLabel = Label(main, bg='gray10', text="Saturation:  "+Saturation, bd=0, fg='white')
    saturationLabel.place(x=630,y=570)
    SOPLabel = Label(main, bg='gray10', fg='white', text="Offset           Power         Slope")
    SOPLabel.place(x=855,y=505)

def writeCDL(event):
    print "writing CDL and .tif"
    tree = ET.ElementTree(root)
    tree.write(str(projectDirectory.get())+"/"+str(today.get())+"/looks/"+SearchField.get()+".cdl")
    openThumb.save(str(projectDirectory.get())+"/"+str(today.get())+"/looks/"+SearchField.get()+".tif")

def sideOUT():
    main.geometry("1800x1200")
    sidePanel.set("YES")

def sideIN():
    main.geometry("1800x1200")
    sidePanel.set("NO")

def getgradebyUID():
    curs1.execute("SELECT LatestGrade From `latestgrade` WHERE UniqueID LIKE '%s'" % (Uniq.get()))
    result = curs1.fetchall()
    y, y_coord = 0, 100
    for line in result:
        grade = StringVar()
        grade.set(line[y])
        gradeinfo = Text(main, bg='gray10', fg='white', height=15, bd=0, relief=SUNKEN, highlightthickness=0)
        gradeinfo.insert(INSERT, "COLORFRONT GRADE XML\n")
        gradeinfo.insert(END, grade.get())
        gradeinfo.place(x=20,y=350)
        y += 1
        y_coord += 20

def SHOWXML(event):
    global sidePanel
    if sidePanel.get() == "NO":
        sidePanel = StringVar()
        sideOUT()
    else:
        sidePanel = StringVar()
        sideIN()
def searchSelection(event):
    print "Searching... for selection"
    metaSelect = metatree.selection()[0]
    print metaSelect
    Uniq.set(metaSelect)
    getgradebyUID()
    getimg()
    getCDL()

def DOWNROLL(event):
    print "going down!"
    m = re.search("[A-Za-z]", SearchRollField.get())
    if m:
        camIndex = m.group(0)
    n = re.search("\d+", SearchRollField.get())
    if n:
        rollIndex = n.group(0)
    rollIndex = int(rollIndex) - 1
    searchRollQuery.set(camIndex+str(rollIndex))
    print searchRollQuery.get()
    searchRoll(event)

def UPROLL(event):
    print "going up!"
    m = re.search("[A-Za-z]", SearchRollField.get())
    if m:
        camIndex = m.group(0)
    n = re.search("\d+", SearchRollField.get())
    if n:
        rollIndex = n.group(0)
    print camIndex
    print rollIndex
    rollIndex = int(rollIndex) + 1
    searchRollQuery.set(camIndex+str(rollIndex))
    print searchRollQuery.get()
    searchRoll(event)

def setRoll(event):

        global Roll
        Roll = StringVar()
        Roll.set(SearchRollField.get())
        searchRoll(event)

def searchRoll(event):
        global Roll, UniqueIDList
        searchRollQuery.set(SearchRollField.get())
        curs1.execute("SELECT UniqueID From `shots` WHERE ClipName LIKE '%s'" % ("%"+searchRollQuery.get()+"%"))
        result = curs1.fetchall()
        UniqueIDList = []
        for i in result:
            m = re.search("\w+\w+", i[0])
            UniqueIDList.append(m.group(0))
        try:
            Uniq.set(UniqueIDList[0])
            getinfobyUID()
            getimg()
            getCDL()
            getgradebyUID()
        except IndexError as e:
            print "Roll doesn't exist in DB"

def DOWNSCENE(event):
    print "going down!"
    n = re.search("\d+", SearchField.get())
    if n:
        sceneIndex = n.group(0)
    sceneIndex = int(sceneIndex) - 1
    searchQuery.set(sceneIndex)
    print searchQuery.get()
    searchScene(event)

def UPSCENE(event):
    print "going up!"
    n = re.search("\d+", SearchRollField.get())
    if n:
        sceneIndex = n.group(0)
    print sceneIndex
    sceneIndex = int(sceneIndex) + 1
    searchQuery.set(sceneIndex)
    print searchQuery.get()
    searchScene(event)


def searchScene(event):
        global Uniq, sceneUID, UniqueIDList
        searchQuery.set(SearchField.get())
        curs1.execute("SELECT UniqueID From `shots` WHERE Scene LIKE '%s'" % ("%"+searchQuery.get()+"%"))
            #Uniq.set(curs1.fetchall())
        result = curs1.fetchall()
        UniqueIDList = []

        for i in result:
            m = re.search(("\w+\w+") , i[0])
               # Uniq.set(m.group(0))
            print m.group(0)
            UniqueIDList.append(m.group(0))
        sceneUID = Uniq.get()
        UidLabel.config(bg='red')
        Uniq.set(UniqueIDList[0])
        try:
                getgradebyUID()
        except:
               print "Couldn't get grade"
        getinfobyUID()
        getAllShotsinScene()
        getimg()
        getCDL()

def setScene(event):
        scene.set(SearchField.get())
        searchScene(event)

UniqueIDList = []
sql = mysql.connector.connect(user='root', buffered=True)
curs1 = sql.cursor(buffered=True)
curs1.execute("Select * From `INFORMATION_SCHEMA`.`SCHEMATA`")
databaseDict = curs1.fetchall()
dblist = []
db = StringVar()
RollList = []

for line in databaseDict:
        if line[1] == 'mysql':
                continue
        if line[1] == 'open':
                continue
        if line[1] == 'cdcol':
                continue
        if line[1] == 'copra4server':
                continue
        if line[1] == 'information_schema':
                continue
        if line[1] == 'projects':
                continue
        else:
                dblist.append(line[1])
ytop = 10
ymid = 300
searchRollLabel = Label(main, text='Roll :', bg='gray10', fg='white')
searchRollLabel.place(x=50,y=298)
searchRollQuery = StringVar()
SearchRollField = Entry(main, bd=0, width=10,textvariable=searchRollQuery, bg='gray2', fg='white', highlightthickness=0)
SearchRollField.place(x=90,y=ymid)
SearchRollField.bind("<Return>", setRoll)
UP = PhotoImage(file='icons/UP.gif')
DOWN = PhotoImage(file='icons/DOWN.gif')
incrementRollUP = Label(main, image=UP, bg='gray10', bd=0)
incrementRollUP.place(x=180, y=290)
incrementRollUP.bind("<Button-1>", UPROLL)
incrementRollDOWN = Label(main, image=DOWN, bg='gray10', bd=0)
incrementRollDOWN.place(x=180, y=310)
incrementRollDOWN.bind("<Button-1>", DOWNROLL)


global filedatabase, projectDirectory, today
filedatabase = StringVar()
projectDirectory = StringVar()
today = StringVar()
projectMetaData =StringVar()
global Thumb, root, sidePanel
Thumb = PhotoImage()
Thumbnail = Label(main, bd=0, bg='gray10')
Thumbnail.place(x=1110,y=300)
sidePanel = StringVar()
sidePanel.set("NO")
scene = StringVar()
Uniq = StringVar()
UniqLabel = StringVar()
searchLabel = Label(main, text='Scene :', bg='gray10', fg='white')
searchLabel.place(x=210,y=298)
searchQuery = StringVar()
SearchField = Entry(main, bd=0, width=10,textvariable=searchQuery, bg='gray2', fg='white', highlightthickness=0)
SearchField.place(x=265,y=ymid)
SearchField.bind("<Return>", setScene)
incrementSceneUP = Label(main, image=UP, bg='gray10', bd=0)
incrementSceneUP.place(x=355, y=290)
incrementSceneUP.bind("<Button-1>", UPSCENE)
incrementSceneDOWN = Label(main, image=DOWN, bg='gray10', bd=0)
incrementSceneDOWN.place(x=355, y=310)
incrementSceneDOWN.bind("<Button-1>", DOWNSCENE)


dbMenu = OptionMenu(importFrame, db, command=selectDatabase, *dblist)
dbMenu.place(x=20,y=ytop)
dbMenu.config(bg='gray10', bd=0, highlightthickness=0)
shotsList = [""]
shot = StringVar()
UniqueID = Label(main, text='UniqueID: ', bg='gray10', fg='white')
UniqueID.place(x=600,y=ymid)
UidLabel = Entry(main, bg='gray2', fg='white', textvariable=Uniq, bd=0, highlightthickness=0)
UidLabel.place(x=675,y=ymid)
exportCDLButton = Label(main, text="Export CDL", bd=0, highlightthickness=1, bg='gray10',fg='White')
exportCDLButton.place(x=850,y=ymid)
exportCDLButton.bind("<Button-1>", writeCDL)
showXML = Label(main, bg='gray10', fg='white', text='Show XML', bd=1)
showXML.place(x=950,y=ymid)
showXML.bind("<Button-1>", SHOWXML)
insertMediaButton = Label(importFrame, text="InsertData", bd=0,bg='gray10', fg='white', highlightthickness=1)
insertMediaButton.place(x=700,y=ytop)
insertMediaButton.bind("<Button-1>", insertMediaRoll)
importButton = Label(importFrame,bd=0, text="Import", fg='white',  highlightthickness=1)
importButton.place(x=200,y=ytop)
importButton.config(bg='gray10')
importButton.bind("<Button-1>", openFile)
inputFile = StringVar()
inputLabel = Label(importFrame, textvariable=inputFile, bd=0,bg='gray10', fg='white')
inputLabel.place(x=250,y=ytop)

main.bind("q", UPROLL)
main.bind("a", DOWNROLL)



main.mainloop()

