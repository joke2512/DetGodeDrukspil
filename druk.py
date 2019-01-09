# -*- coding: utf-8 -*-
"""en lang kommentar
dette mesterværk af et drukspil er skabt af patten og Jon (med hjælp fra trines mor)
hej hej
benjamin er en noob der ikke har hjulpet overhovedet
"""
import random as tilfældig
import matplotlib.pyplot as pytonvisning
import numpy as nummerpyton
import time as tid
spillere=["Trine","Jon","Paten"]
et=1
to=2
fem=5
nul=0
grøn="g"
blå="b"
rød="r"
lila="purple"
guiL="y"
trinesjæl="black"
trinesordforåd="cyan"
orange="orange"
trinesmorsfisse="pink"
græs="lawngreen"
graffarver=[rød,grøn,blå,lila,guiL,trinesjæl,trinesordforåd,orange,græs,"magenta",trinesmorsfisse]
antal=len(spillere)
detendeligesvar=nummerpyton.zeros(antal)
pytonvisning.bar(spillere, detendeligesvar)
pytonvisning.show(block=False)
pytonvisning.pause(et)
pytonvisning.close()
for ettal in range(antal*2):
    dettilfældigetal=tilfældig.randint(nul,(antal-et))
    detendeligesvar[dettilfældigetal]+=tilfældig.randint(et,to)
    patens_sexliv="trines mor"
    pytonvisning.bar(spillere,detendeligesvar,color=graffarver[nul:antal])
    pytonvisning.xlabel("Drankerne")
    pytonvisning.ylabel("Tåre")
    pytonvisning.title("Det gode drukspil")
    pytonvisning.fill_between(spillere,detendeligesvar,y2=max(detendeligesvar),color="mediumvioletred")
    pytonvisning.show(block=False)
    pytonvisning.pause(et)
    pytonvisning.close()
dettilfældigetal=tilfældig.randint(nul,(antal-et))
detendeligesvar[dettilfældigetal]+=tilfældig.randint(-fem,fem)
pytonvisning.bar(spillere,detendeligesvar,color=graffarver[nul:antal])
pytonvisning.xlabel("Drankerne")
pytonvisning.ylabel("Tears")
pytonvisning.title("Det gode drukspil")
pytonvisning.fill_between(spillere,detendeligesvar,y2=max(detendeligesvar),color="midnightblue")
pytonvisning.show()