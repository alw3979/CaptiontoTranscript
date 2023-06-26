# author: anna williams
# date: 06.14.2022
# program file: convertCaption.py
# description: Given an srt, create a .txt without timestamps and remove any extra whitespace lines.

import os

def main():
  path='/Users/Anna/Documents/codingPractice/CaptiontoTranscript/srt'
  os.chdir(path)
  for file in os.listdir(path):
    filename=file.rstrip('.srt')
    file=open(filename+'.srt', 'r', encoding='utf-8')
    transcript=open(filename+'.txt','x', encoding='utf-8')
    numLines=1

    for line in file:
      numLines=int(line.rstrip())
      timestamp=file.readline().rstrip()
      line1=file.readline().rstrip()
      transcript.write('{} '.format(line1))
      line2=file.readline().rstrip()
      if line2 == (''):
        pass
      else:
        transcript.write('{} '.format(line2))
        skipspace=file.readline()

    file.close()
    transcript.close()
main() 