@echo off
if not exist ".\datafiles\named-20100128" mkdir .\datafiles\named-20100128
java -jar .\programs\enigma-swing-2.0.0-all.jar --jar .\minecraft\in-20100128-2304-intermediary.jar --mappings .\datafiles\named-20100128
