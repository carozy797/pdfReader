import PySimpleGUI as sg
import threading
import pyttsx3, PyPDF2
import webbrowser

speaker = pyttsx3.init()


def readerPdf(path, pagenum):
    file = path
    if file != "":
        try:
            # print(file)
            # file = easygui.fileopenbox()
            webbrowser.open_new(file)
            # book = open('oop.pdf','rb')
            book = open(file, 'rb')
            reader = PyPDF2.PdfFileReader(book)
            totalPages = reader.numPages
            # getting a page to read fro the user
            # pagenum = int(input("enter the page you want to read from : "))
            for i in range((int(pagenum)-1), totalPages - 1):
                page = reader.getPage(i)
                # extracting the text from that page
                text = page.extractText()
                # reading from the pdf
                voice = speaker.getProperty('voices')
                speaker.setProperty('rate', 120)
                speaker.setProperty('voice', voice[0].id)
                speaker.say(text)
                speaker.runAndWait()
                print("running..")
        except Exception as e:
            print(e)
            pass
    else:
        print("nothing")


sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Select a pdf file: "), sg.Input(key="") , sg.FileBrowse(key="-IN-")], [sg.T("")], [sg.Text("Page number:", justification="left"),sg.InputText(key="pnumb", justification="left")] ,[sg.Button("Read PDF", ),], [sg.Button("cancel"),]]

#Building Window
window = sg.Window(' Fausford PDF Reader', layout,icon="organiser.ico", size=(600, 300), element_justification="center")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Read PDF":
        # start = threading.Thread(target=readerPdf(values["-IN-"]), )
        # start.start()
        speak1 = threading.Thread(target=readerPdf, args=(values["-IN-"], values["pnumb"]))
        speak1.start()

    elif event == "cancel":
        print("cancelling...")
        # window.close()


        def stop():
            print("stopping...")

            speaker.stop()
            print("stopped")
        close = threading.Thread(target=stop, )
        close.start()
        print("closing..")
        exit(0)

        # speaker.stop()
        # print("nice")

