import os
def createfolder(folder):
	if not os.path.exists(folder):
		os.makedirs(folder)

def files_in_folder(folder,files):
	for file in files:
		os.replace(file,f'{folder}/{file}')

files=os.listdir()
files.remove('Foldercleaner.py')

createfolder('images')
createfolder('documents')
createfolder('vedios')
createfolder('others')

imageexts=['.jpg']
images=[file for file in files if os.path.splitext(file)[1].lower() in imageexts]

documentsexts=['.doc','.docx','.pdf']
documents=[file for file in files if os.path.splitext(file)[1].lower() in documentsexts]

vedioexts=['.mp3','.mp4']
vedios=[file for file in files if os.path.splitext(file)[1].lower() in vedioexts]

others=[]
for file in files:
	ext=os.path.splitext(file)[1].lower()

	if (ext not in imageexts) and (ext not in documentsexts) and (ext not in vedioexts) :
		others.append(file)

files_in_folder('images',images)
files_in_folder('documents',documents)
files_in_folder('vedios',vedios)
files_in_folder('others',others)
