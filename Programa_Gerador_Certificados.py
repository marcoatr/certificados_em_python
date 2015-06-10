import os
# coding: latin-1 
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
import csv

imagem = "./certificados.png" 
def  reconhecer_imagem():
    if not os.path.exists(imagem):
        f = open( imagem, 'w')
        f.write(response.read())
        f.close()
reconhecer_imagem()

def spliter_linhas(tamanho_texto2, texto2 ,*texto2_1):
	if (tamanho_texto2 < 90):
		texto2_1 = texto2
		texto2_2 = ""
	elif (tamanho_texto2 < 110):
		verificador_de_espaco = True
		i = 0
		while verificador_de_espaco == True:
			if texto2[tamanho_texto2 - 20 - i] == " " :
				verificador_de_espaco = False
			i = i + 1
		texto2_1 = texto2[0:tamanho_texto2 - 20 - (i-1)]
		texto2_2 = texto2[tamanho_texto2 - 20 - (i-1): tamanho_texto2]

	else:
		verificador_de_espaco = True
		i = 0
		while verificador_de_espaco == True:
			if texto2[90 - i] == " " :
				verificador_de_espaco = False
			i = i + 1
		texto2_1 = texto2[0:90 - (i-1)]
		texto2_2 = texto2[90 - (i-1):tamanho_texto2]
	return texto2_1, texto2_2

def info_cursos(y, *informacoes):
	if y == 0: #pic
		dias = "18 a 21 de maio"
		horario = "de 07h30min a 12h30min"
		carga_horaria = "20 horas"
		categoria = "Curso"
	elif y == 1: #pdi
		dias = "18 a 22 de maio"
		horario = "de 18h30min a 22h30min"
		carga_horaria = "20 horas"
		categoria = "Curso"
	elif y == 2: #AutoCad
		dias = "18 a 22 de maio"
		horario = "de 07h30min a 10h00min"
		carga_horaria = "10 horas"
		categoria = "Minicurso"
	elif y == 3: #Android
		dias = "18 a 22 de maio"
		horario = "de 20h30min a 22h30min"
		carga_horaria = "10 horas"
		categoria = "Minicurso"
	elif y == 4: #Arduino
		dias = "18 a 22 de maio"
		horario = "de 13h30min a 16h00min"
		carga_horaria = "10 horas"
		categoria = "Minicurso"
	elif y == 5: #confecção
		dias = "18 a 21 de maio"
		horario = "de 20h30min a 22h30min"
		carga_horaria = "10 horas"
		categoria = "Minicurso"
	elif y == 6: #fpga
		dias = "18 a 21 de maio"
		horario = "de 13h30min a 16h00min"
		carga_horaria = "10 horas"
		categoria = "Minicurso"
	elif y == 7: #hp
		dias = "18 a 22 de maio"
		horario = "de 13h30min a 16h00min"
		carga_horaria = "10 horas"
		categoria = "Minicurso"
	elif y == 8: #matlab
		dias = "18 a 22 de maio"
		horario = "de 07h30min a 10h00min"
		carga_horaria = "10 horas"
		categoria = "Minicurso"
	elif y == 9: #msp
		dias = "18 a 22 de maio"
		horario = "de 07h30min a 10h00min"
		carga_horaria = "10 horas"
		categoria = "Minicurso"
	elif y == 10: #shell
		dias = "18 a 22 de abril"
		horario = "de 07h30min a 10h00min"
		carga_horaria = "10 horas"
		categoria = "Minicurso"
	elif y == 11: #solid
		dias = "18 a 22 de abril"
		horario = "de 13h30min a 16h00min"
		carga_horaria = "10 horas"
		categoria = "Minicurso"
	elif y == 12: #galileo
		dias = "19 e 21 de abril"
		horario = "de 13h30min a 16h00min"
		carga_horaria = "5 horas"
		categoria = "Workshop"
	elif y == 13: #latex
		dias = "19 e 21 de abril"
		horario = "de 09h00min a 12h00min"
		carga_horaria = "6 horas"
		categoria = "Workshop"
	elif y == 14: #pda
		dias = "18, 20 e 22 de abril"
		horario = "de 13h30min a 16h00min"
		carga_horaria = "7 horas e 30 minutos"
		categoria = "Workshop"
	elif y == 15: #sist
 		dias = "20 de abril"
		horario = "de 19h30min a 22h30min"
		carga_horaria = "3 horas"
		categoria = "Sistemas Embarcados"
	return dias,horario,carga_horaria,categoria


tipo = input("1 para palestra e 2 para curso: ")

if tipo == 2:
	nome = "Carlos Henrique Dos Santos De Carvalho"
	curso = ["PIC","Processamento Digital de Imagem","AutoCad", "Android", "Arduíno", "Confecção de Placas", "FPGA e VHDL", "HP50g", "MatLab", "Msp430", "ShellScript", "SolidWorks","intel Galileo", "LaTeX", "Processamento Digital de Áudio","Sistemas Embarcados"]
	y = input("curso desejado: ")
	
	dias = ""
	horario = ""
	carga_horaria = ""
	categoria = ""
	info_cursos_tupla = info_cursos(y,dias,horario,carga_horaria,categoria)


	c = canvas.Canvas("Certificados/" + nome + "_" + info_cursos_tupla[3] + "_" + curso[y] +".pdf", pagesize=landscape(A4))
	width, height = A4
	c.drawImage(imagem, 0, 0, height,width) 
	
	c.setFont("Times-Roman", 19)
	c.drawString(35,270,"A comissão organizadora da Semana de Atualização em Engenharia Elétrica (SEATEL) certifica que")
	tamanho = len(nome)
	
	if (tamanho < 36):
		c.setFont("Helvetica-Bold", 35)	
		c.drawString(35 + (36 - tamanho)*11  ,230,nome.upper())
	else:
		c.setFont("Helvetica-Bold", 28)	
		c.drawString(45 ,230,nome.upper())


	c.setFont("Times-Roman", 19)
	texto2 = "assitiu ao " + info_cursos_tupla[3] + " de " + curso[y] + " no(s) dia(s) " + info_cursos_tupla[0] + " no período " + info_cursos_tupla[2] + ", " + "totalizando " + info_cursos_tupla[1] + "."
	tamanho_texto2 = len(texto2)
	texto2_1 = ""
	texto2_2 = ""
	tupla1 = spliter_linhas(tamanho_texto2,texto2,texto2_1,texto2_2)
			
	c.drawString(35 + (101 - len(tupla1[0]))*4, 200, tupla1[0])
	c.drawString(35 + (101 - len(tupla1[1]))*4, 180,tupla1[1])

	c.showPage()
	c.save()


if tipo == 1:
	cr = csv.reader(open("tbPalestras.csv","rb"))

	lst_nomes = []	
	for row in cr:		
		indice = 1 
		while indice < 18:
			if (row[indice] != ""): 
				lst_nomes.append(row[indice])
			indice = indice + 1

	nomes_e_qtdes = []
	state = True
	for i in lst_nomes:
		qtde = 0
		for i2 in lst_nomes:
			if i == i2:
				qtde = qtde + 1
		state = True
		for i3 in nomes_e_qtdes:
			if i == i3:
				state = False

		if state == True:
			nomes_e_qtdes.append(i)
			nomes_e_qtdes.append(qtde)

	
	nomes_e_qtdes_arrumados = []
	for i in nomes_e_qtdes:
		tipo = str(type(i))
		if tipo == "<type 'str'>":
			string_correta = i.replace("Ã§","Ç")
			string_correta = string_correta.replace("Ã‡","Ç")
			string_correta = string_correta.replace("Ã£","ããã")
			string_correta = string_correta.replace("Ã­","Í")
			string_correta = string_correta.replace("ããã", "Ã")
			string_correta = string_correta.replace("é","É")		

			nomes_e_qtdes_arrumados.append(string_correta)
		
		else:
			nomes_e_qtdes_arrumados.append(i)
		

	indice_final = 0;
	while indice_final < len(nomes_e_qtdes_arrumados):

		c = canvas.Canvas("Certificados/" + nomes_e_qtdes_arrumados[indice_final] + "_" + "PALESTRA" +".pdf", pagesize=landscape(A4))
		width, height = A4
		c.drawImage(imagem, 0, 0, height,width) 


		c.setFont("Times-Roman", 19)
		c.drawString(35,270,"A comissão organizadora da Semana de Atualização em Engenharia Elétrica (SEATEL) certifica que")
		tamanho = len(nomes_e_qtdes_arrumados[indice_final])
		if (tamanho < 36):
			c.setFont("Helvetica-Bold", 35)	
			c.drawString(35 + (36 - tamanho)*11  ,230,nomes_e_qtdes_arrumados[indice_final].upper())
		else:
			c.setFont("Helvetica-Bold", 28)	
			c.drawString(45,230,nomes_e_qtdes_arrumados[indice_final].upper())

		qtde_palestra = nomes_e_qtdes_arrumados[indice_final + 1]


		c.setFont("Times-Roman", 19)
		texto2 = "assitiu a " + str(qtde_palestra) + " palestra(s) na semana entre 18 a 22 de maio, totalizando " + str(qtde_palestra*1.5) + " horas."
		tamanho_texto2 = len(texto2)
		texto2_1 = ""
		texto2_2 = ""
		tupla1 = spliter_linhas(tamanho_texto2,texto2,texto2_1,texto2_2)
			
		c.drawString(35 + (101 - len(tupla1[0]))*4, 200, tupla1[0])
		c.drawString(35 + (101 - len(tupla1[1]))*4, 180,tupla1[1])

		indice_final = indice_final + 2;

		
		c.showPage()
		c.save()