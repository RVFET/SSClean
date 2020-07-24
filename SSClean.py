from colorama import init, Fore, Back, Style
import os
import pyperclip
import datetime
import getpass


init()
now = datetime.datetime.now()



welcome = '''
                                      WELCOME TO SSCLEAN

     .M"""bgd  .M"""bgd   .g8"""bgd `7MMF'      `7MM"""YMM        db      `7MN.   `7MF'
    ,MI    "Y ,MI    "Y .dP'     `M   MM          MM    `7       ;MM:       MMN.    M  
    `MMb.     `MMb.     dM'       `   MM          MM   d        ,V^MM.      M YMb   M  
      `YMMNq.   `YMMNq. MM            MM          MMmmMM       ,M  `MM      M  `MN. M  
    .     `MM .     `MM MM.           MM      ,   MM   Y  ,    AbmmmqMA     M   `MM.M  
    Mb     dM Mb     dM `Mb.     ,'   MM     ,M   MM     ,M   A'     VML    M     YMM  
    P"Ybmmd"  P"Ybmmd"    `"bmmmd'  .JMMmmmmMMM .JMMmmmmMMM .AMA.   .AMMA..JML.    YM  
                                
                                    SIMPLE SYSTEM CLEAN v1.0
                          *WAIT 1 SECOND AND PRESS ANY KEY TO CONTINUE   
                                                                                   '''

def mainmenu():
	os.system('mode con:cols=90 lines=14')
	os.system('title SSCleaner v1.0')
	print(Fore.GREEN+welcome+Fore.WHITE)
	os.system('timeout 1 /nobreak > nul')
	os.system('pause >nul')
	os.system('mode con:cols=70 lines=14')
	os.system('cls')
	print(Fore.YELLOW+' --------------------------------------------------------------------')
	print(Fore.YELLOW+' | [1] '+Fore.WHITE+' Quick Clean                                                 '+Fore.YELLOW+'|')
	print(Fore.YELLOW+' | [2] '+Fore.WHITE+' Full Clean                                                  '+Fore.YELLOW+'|')
	print(Fore.YELLOW+' | [3] '+Fore.WHITE+' Speed Up, System Scan, Virus Removal and System Error Fixer '+Fore.YELLOW+'|')
	print(Fore.YELLOW+' | [4] '+Fore.WHITE+' Run Windows Cleaner                                         '+Fore.YELLOW+'|')
	print(Fore.YELLOW+' | [5] '+Fore.WHITE+' Rename PC                                                   '+Fore.YELLOW+'|')
	print(Fore.YELLOW+' | [6] '+Fore.WHITE+' Uninstall a Program                                         '+Fore.YELLOW+'|')
	print(Fore.YELLOW+' | [7+]'+Fore.WHITE+' Auto Clean at every Boot                                    '+Fore.YELLOW+'|')
	print(Fore.YELLOW+' | [8] '+Fore.WHITE+' Help                                                        '+Fore.YELLOW+'|')
	print(Fore.YELLOW+' | [9] '+Fore.WHITE+' About                                                       '+Fore.YELLOW+'|')
	print(Fore.YELLOW+' | [10]'+Fore.WHITE+' Exit                                                        '+Fore.YELLOW+'|')
	print(Fore.YELLOW+' --------------------------------------------------------------------')
	menuselection = None




	while True:
		try:
			menuselection = int(input('[-] ENTER SELECTION HERE: '))
		except ValueError:
			print(Fore.RED+'[!]'+Fore.WHITE+'Command Not Found!')
			continue
		else:
			break

	if menuselection not in range(0,11):
		print(Fore.RED+'[X]'+Fore.WHITE+'Command Not Found!')
		exit()
	if menuselection == 1:
		quickclean()
	if menuselection == 2:
		fullclean()
	if menuselection == 3:
		speedup()
	if menuselection == 4:
		mscleaner()
	if menuselection == 5:
		rename()
	if menuselection == 6:
		uninstall()
	if menuselection == 7:
		autorun()
	if menuselection == 8:
		help()
	if menuselection == 9:
		about()
	if menuselection == 10:
		exit()

#1
def quickclean():
	os.system('mode con:cols=100 lines=100')
	os.system('cls')
	os.system('echo ^<-------------^| Last Deleted Files (Quick Clean)   Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'   Time: '+str(now.hour)+':'+str(now.minute)+' ^|-----------^> > %userprofile%/desktop/CleanerLog.txt')
	os.system('cd %temp% && del/q/f/s * >> %userprofile%/desktop/CleanerLog.txt')
	os.system('cd C:\Windows\Temp && del/q/f/s * >> %userprofile%/desktop/CleanerLog.txt')
	os.system('cd prefetch && del/q/f/s * >> %userprofile%/desktop/CleanerLog.txt')
	print(Fore.YELLOW+'Press Any Key to Redirect main menu')
	os.system('pause > nul')
	mainmenu()
#2
def fullclean():
	os.system('mode con:cols=100 lines=100')
	os.system('cls')
	os.system('echo ^<-------------^| Last Deleted Files (Full Clean)   Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'   Time: '+str(now.hour)+':'+str(now.minute)+' ^|-----------^> > %userprofile%/desktop/CleanerLog.txt')
	os.system('cd %temp% && del/q/f/s * >> %userprofile%/desktop/CleanerLog.txt')
	os.system('cd C:\Windows\Temp && del/q/f/s * >> %userprofile%/desktop/CleanerLog.txt')
	os.system('cd prefetch && del/q/f/s * >> %userprofile%/desktop/CleanerLog.txt')
	os.system('cd C:\Windows\Prefetch && del/q/f/s * >> %userprofile%/desktop/CleanerLog.txt')
	os.system('cd C:\Windows\Downloaded Program Files del /q/f/s * >> %userprofile%/desktop/CleanerLog.txt')
	os.system('cd C:\Windows\LiveKernelReports del /q/f/s * >> %userprofile%/desktop/CleanerLog.txt')
	os.system('cd C:\Windows.old del /q/f/s * >> %userprofile%/desktop/CleanerLog.txt')
	os.system('Dism.exe /online /Cleanup-Image /StartComponentCleanup')
	os.system('msg %username% Junk File Cleaning Completed But You can Clean More with Windows Clean Manager Tool which already open in your screen.')
	os.system('cleanmgr')
	print(Fore.YELLOW+'Press Any Key to Redirect main menu')
	os.system('pause > nul')
	mainmenu()
#3
def speedup():
	os.system('mode con:cols=100 lines=100')
	os.system('echo ^<-------------^| Last operation (Speed Up, System Error/Crash Fix)   Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'   Time: '+str(now.hour)+':'+str(now.minute)+' ^|-----------^> > %userprofile%/desktop/CleanerLog.txt')
	os.system('cls')
	print('Speed up function works best with low pcs. If your pc is over 8gb ram it won\'t affect that much.')
	wanttospeedup = input('Is Your PC Has less than 8gb Ram? (Y/N): ')
	if wanttospeedup.lower() == 'y':
		os.system('Fsutil behavior set memoryusage 2')
	else:
		print(Fore.RED+'[X]' +Fore.WHITE+' Wrong Command, Skipping.')
	
	os.system('msg %username% Checking and Repairing All System Files. It can Take some time. Be Patient and Don\'t Close the program.')
	#os.system('sfc /scannow')
	os.system('msg %username% System File Check and Repair Process Completed Succesfully. Now Restart Your Machine to take effect.')
	
	wanttorestart = input('Do you Want to restart your computer now? (Y for yes, N for No) : ')
	if wanttorestart.lower() == 'y':
		os.system('shutdown /r')
	else:
		print(Fore.YELLOW+'[!]'+Fore.WHITE+' Manually Restarting Selected.')
	print(Fore.YELLOW+'Press Any Key to Redirect main menu')
	os.system('pause > nul')
	mainmenu()
#4
def mscleaner():
	os.system('mode con:cols=100 lines=100')
	os.system('echo ^<-------------^| Last Operation (MS Clean Manager)   Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'   Time: '+str(now.hour)+':'+str(now.minute)+' ^|-----------^> > %userprofile%/desktop/CleanerLog.txt')
	os.system('cls')
	os.system('cleanmgr')
	print(Fore.GREEN+'[√]'+Fore.WHITE+' MS Cleaner Run Succesfully.')
	os.system('echo ---MS Clean Manager Run Succesfully--- >> %userprofile%/desktop/CleanerLog.txt')
	print(Fore.YELLOW+'Press Any Key to Redirect main menu')
	os.system('pause > nul')
	mainmenu()
#5
def rename():
	os.system('mode con:cols=100 lines=100')
	os.system('echo ^<-------------^| Last Operation (Device Rename)   Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'   Time: '+str(now.hour)+':'+str(now.minute)+' ^|-----------^> > %userprofile%/desktop/CleanerLog.txt')
	os.system('cls')
	os.system('sysdm.cpl >> %userprofile%/desktop/CleanerLog.txt')
	os.system('echo ---Windows Device Rename Dialog Open Succesfully.--- >> %userprofile%/desktop/CleanerLog.txt')
	print(Fore.YELLOW+'Press Any Key to Redirect main menu')
	os.system('pause > nul')
	mainmenu()
#6
def uninstall():
	os.system('mode con:cols=100 lines=100')
	os.system('echo ^<-------------^| Last Operation (Unistall a Program)   Date: '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)+'   Time: '+str(now.hour)+':'+str(now.minute)+' ^|-----------^> > %userprofile%/desktop/CleanerLog.txt')
	os.system('cls')
	os.system('appwiz.cpl')
	os.system('echo ---Control Panel/Remove run Succesfully.--- >> %userprofile%/desktop/CleanerLog.txt')
	print(Fore.YELLOW+'Press Any Key to Redirect main menu')
	os.system('pause > nul')
	mainmenu()
#7
def autorun():
	os.system('mode con:cols=100 lines=100')
	print(Fore.YELLOW+'[1] '+Fore.WHITE+' Eanble AutoRun With Windows')
	print(Fore.YELLOW+'[2] '+Fore.WHITE+' Disable AutoRun With Windows')
	whatyouwant = int(input('[-] ENTER SELECTION HERE: '))
	if whatyouwant == 1:
		USER_NAME = getpass.getuser()
		def add_to_startup(file_path=""):
			if file_path == "":
				file_path = os.path.dirname(os.path.realpath(__file__))
			bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
			with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
				bat_file.write(r'start "" %s' % file_path)
		os.system('msg %username% Program Will Run Itself with every boot.')
	if whatyouwant ==2:
		os.system('cd %AppData%\Microsoft\Windows\Start Menu\Programs\Startup && del SystemCleaner.exe /f/q/s')
		os.system('msg %username% Program Will not Run Itself with boot anymore.')
	print(Fore.YELLOW+'Press Any Key to Redirect main menu')
	os.system('pause > nul')
	mainmenu()
#8
def help():
	os.system('mode con:cols=150 lines=120')
	print(Fore.CYAN+'''This Program is Free and Easy to Use.
		'''+Fore.YELLOW+'''
		\n                                                           ---Quick Clean Tool---'''
		+Fore.WHITE+'''
		\nIt\'s basically deleting some unnecesary temporary files that windows doesn\'t need them.
		'''+Fore.YELLOW+'''
		\n                                                            ---Full Clean Tool---
		'''+Fore.WHITE+'''
		\nIt does almost same thing as Quicl Clean Tool but difference is it\'s more powerfull because it\'s not deleting only temporary files.\nIt\'s Also deleting some advanced Junk files. Don\'t Worry about "Advanced" word,\nit means Full Clean Tool diving more deeper and deleting almost entire junk files that safe to clean.
		'''+Fore.YELLOW+'''
		\n                                             ---SpeedUp, System Repair and Error/crash Fix tool---
		'''+Fore.WHITE+'''
		\nThis Tool Runs several Windows Batch Programming codes that makes your pc run faster and Repair all the damaged windows system files.\nSpeedUp not recommended for computers that has more than 8GB ram cause it makes nosense for those kind of computers.\nOtherwise it\'s a lifesaver function for devices with ram under 8GB.
		'''+Fore.YELLOW+'''
		\n                                                          ---Windows Clean Tool---
		'''+Fore.WHITE+'''
		\nWindows Computers has built-in clean tool. But it\'s not so easy to run.\nFor those who is not so good at computers they can simply open this app select Windows Clean Tool from menu to run this easily.
		'''+Fore.YELLOW+'''
		\n                                                              ---Rename PC---
		'''+Fore.WHITE+'''
		\nThis section is entirely self-explaining. It\'s Just opens a dialog box from "Control Panel" to rename Your PC or Laptop
		'''+Fore.YELLOW+'''
		\n                                                          ---Uninstall Program---
		'''+Fore.WHITE+'''
		\nSame as Rename PC this one is a "Control panel" Shortcut too for make it easy to use.
		'''+Fore.YELLOW+'''
		\n                                                       ---Auto Run With Every Boot---
		'''+Fore.WHITE+'''
		\nJust for make it more easy to use. If You enable this function then this program will run itself at every boot of your device.\nIt\'s Possible to disable it from same menu.
		'''+Fore.YELLOW+'''''')
	print(Fore.YELLOW+'Press Any Key to Redirect main menu')
	os.system('pause > nul')
	mainmenu()
#9
def about():
	os.system('mode con:cols=110 lines=30')
	print(Fore.YELLOW+Style.BRIGHT+'                                             ---------------\n                              "SS" in SSCleaner stands for "Simple System Cleaner"\n    App Makes Log File in Desktop so, you can check What Files deleted by program and What operations done.\n    This App is totally free to use. App Written in Python and Batch Programming Language (Command-Line).\n                       It\'s a very Simple but powerfull as simple as it. Made by Rvfet.\n                                             ---------------')
	print(Fore.YELLOW+Back.BLACK+Style.NORMAL+'Press Any Key to Redirect main menu')
	os.system('pause > nul')
	mainmenu()
#10
def exit():
	os.system('mode con:cols=100 lines=100')
	os.system('echo Dim message, sapi >C:\Windows\Logs\sadtoseeyougone.vbs')
	os.system('echo message=("Sad to See You Gone, Never Forget to Clean Your PC") >>C:\Windows\Logs\sadtoseeyougone.vbs')
	os.system('echo Set sapi=CreateObject("sapi.spvoice") >>C:\Windows\Logs\sadtoseeyougone.vbs')
	os.system('echo sapi.Speak message >>C:\Windows\Logs\sadtoseeyougone.vbs')
	os.system('start C:\Windows\Logs\sadtoseeyougone.vbs')
	os.system('taskkill /im SSClean.exe /f')
	mainmenu()

mainmenu()

#>> %userprofile%/desktop/CleanerLog.txt
#'C:\Users\%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'