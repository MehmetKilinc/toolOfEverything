import sys
import base64
import codecs
import random
import hashlib
import PyPDF2
import nmap
import socket
import time
import pyttsx3
import sqlite3
import os
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel, QHBoxLayout, QFileDialog,QListWidgetItem,QListWidget,QStackedWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QMovie



class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 800)
        self.setWindowTitle('Ana Pencere')
        self.setStyleSheet("background-color: green")
        pentest = QPushButton('PENTEST' , self)
        pentest.setGeometry(50,50,300,50)
        pentest.setStyleSheet("QPushButton { border-radius: 15px; background-color: black; color: white; }")
        sifrele = QPushButton('ŞİFRELEME | ŞİFRE KIRMA',self)
        sifrele.setGeometry(50,50,300,50)
        sifrele.setStyleSheet("QPushButton { border-radius: 15px; background-color: black; color: white; }")
        dosya = QPushButton("DOSYA İŞLEMLERİ" , self)
        dosya.setGeometry(50,50,300,50)
        dosya.setStyleSheet("QPushButton { border-radius: 15px; background-color: black; color: white; }")
        ingilizce = QPushButton('İNGİLİZCE ÖĞREN',self)
        ingilizce.setGeometry(50,50,300,50)
        ingilizce.setStyleSheet("QPushButton { border-radius: 15px; background-color: black; color: white; }")
        geri = QPushButton('KAPAT',self)
        geri.setGeometry(50,50,200,50)
        geri.setStyleSheet('background-color: #3498db ; color : black ; border-radius: 15px')
        video = QMovie('./gifs/deneme.gif')
        degisken = QLabel(self)
        degisken.setMovie(video)
        degisken.move(800,300)
        video.start()
        dosya.move(1550 , 50)
        pentest.move(50 , 150)
        ingilizce.move(1550 , 150)
        geri.move(1600,900)
        sifrele.move(50,50)
        dosya.clicked.connect(self.dosyaislemler)
        pentest.clicked.connect(self.pentest_islem)
        ingilizce.clicked.connect(self.english)
        geri.clicked.connect(self.kapat)
        sifrele.clicked.connect(self.sifre)

    def sifre(self):
    	self.yeni_pencere = Sifre()
    	self.yeni_pencere.showMaximized()
    def dosyaislemler(self):
        self.yeni_pencere = Dosya_Donusturucu()
        self.yeni_pencere.showMaximized()
    def pentest_islem(self):
        self.yeni_pencere = Pentest()
        self.yeni_pencere.showMaximized()
    def english(self):
    	self.yeni_pencere = English()
    	self.yeni_pencere.showMaximized()
    def kapat(self):
    	self.close()


class Sifre(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("şifreleme")
		self.setStyleSheet('background-color:green')
		video = QMovie('./gifs/deneme.gif')
		degisken = QLabel(self)
		degisken.setMovie(video)
		degisken.move(800,300)
		video.start()
		self.md5 = QPushButton('MD5',self)
		self.base64 = QPushButton('BASE64',self)
		self.geri = QPushButton('GERİ',self)
		self.rot13 = QPushButton('ROT13',self)
		self.md5.setStyleSheet('background-color:black;color:white')
		self.base64.setStyleSheet('background-color:black;color:white')
		self.geri.setStyleSheet('background-color:purple;color:black')
		self.rot13.setStyleSheet('background-color:black;color:white')
		self.md5.move(50,50)
		self.base64.move(50,100)
		self.geri.move(1700,900)
		self.rot13.move(50,150)
		self.md5.clicked.connect(self.md5sayfa)
		self.base64.clicked.connect(self.base64sayfa)
		self.geri.clicked.connect(self.kapa)
		self.rot13.clicked.connect(self.rot13sayfa)


	def md5sayfa(self):
		self.yeni_pencere = Md5()
		self.yeni_pencere.showMaximized()
	def base64sayfa(self):
		self.yeni_pencere = Base64Pencere()
		self.yeni_pencere.showMaximized()
	def kapa(self):
		self.close()
	def rot13sayfa(self):
		self.yeni_pencere = Rot()
		self.yeni_pencere.showMaximized()


class Dosya_Donusturucu(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 800)
        self.setWindowTitle('Ana Pencere')
        self.setStyleSheet("background-color: green")
        pdf_birlestir = QPushButton('PDF BİRLEŞTİR', self)
        kapat = QPushButton('GERİ' , self)
        pdf_birlestir.setStyleSheet("background-color: black; color: white;")
        pdf_birlestir.move(100 , 50)
        pdf_birlestir.clicked.connect(self.yeni)
        kapat.clicked.connect(self.kapa)
        kapat.setStyleSheet('background-color: purple ; color : black')
        kapat.move(1700,900)
        video = QMovie('./gifs/deneme.gif')
        degisken = QLabel(self)
        degisken.setMovie(video)
        degisken.move(800,300)
        video.start()        
    def yeni(self):
        self.yeni_pencere = Pdf()
        self.yeni_pencere.showMaximized()
    def kapa(self):
        self.close()

class Base64Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Base64 Pencere')
        layout = QVBoxLayout()
        self.yazi_alani = QTextEdit(self)
        self.yazi_alani.setGeometry(100,100,800,800)
        self.buton2 = QPushButton('base64 şifre kırma' , self)
        self.sifrele = QPushButton('base64 şifreleme')
        self.geri = QPushButton('geri',self)
        self.cevap = QLabel("cevap : ")
        self.kopyala = QPushButton("kopyala",self)
        self.yazi_alani.setStyleSheet('background-color: black; color: green')
        self.buton2.setStyleSheet('background-color:purple; color: black')
        self.sifrele.setStyleSheet('background-color:purple; color: black')
        self.geri.setStyleSheet('background-color:green;color:black')
        self.kopyala.setStyleSheet('background-color:green;color:black')
        self.buton2.setFixedHeight(50)
        self.sifrele.setFixedHeight(50)
        self.geri.setFixedHeight(50)
        self.kopyala.setFixedHeight(50)
        self.cevap.setFixedHeight(150)
        layout.addWidget(self.yazi_alani)
        layout.addWidget(self.buton2)
        layout.addWidget(self.sifrele)
        layout.addWidget(self.geri)
        layout.addWidget(self.cevap)
        layout.addWidget(self.kopyala)
        self.buton2.clicked.connect(self.base64_sifre_kir)
        self.sifrele.clicked.connect(self.base64_sifrele)
        self.geri.clicked.connect(self.geriye)
        self.kopyala.clicked.connect(self.kopyalama)
        self.setLayout(layout)
    def base64_sifre_kir(self):
        yazi = self.yazi_alani.toPlainText()
        metin = base64.b64decode(yazi).decode('utf-8')
        self.cevap.setText(metin)
    def base64_sifrele(self):
        yazi = self.yazi_alani.toPlainText()
        yazi = yazi.encode("utf-8")
        metin = base64.b64encode(yazi)
        self.cevap.setText(metin.decode("utf-8"))
    def geriye(self):
        self.yeni_pencere = AnaPencere()
        self.showMaximized()
        self.close()
    def kopyalama(self):
        self.kopyala.setStyleSheet('background-color: red; color: white')
        QApplication.clipboard().setText(self.cevap.text())
        QTimer.singleShot(2000 , self.guncelle)
    def guncelle(self):
     	self.kopyala.setStyleSheet('background-color:green;color:black')

class Rot(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Base64 Pencere')
        layout = QVBoxLayout()
        self.yazi_alani = QTextEdit(self)
        self.yazi_alani.setGeometry(100,100,800,800)
        self.sifre_kir = QPushButton('rot13 şifre kırma' , self)
        self.sifrele = QPushButton('rot13 şifreleme')
        self.geri = QPushButton('geri',self)
        self.cevap = QLabel("cevap : ")
        self.kopyala = QPushButton("kopyala")
        self.yazi_alani.setStyleSheet('background-color: black ; color: green')
        self.sifre_kir.setStyleSheet('background-color: purple ; color: black')
        self.sifrele.setStyleSheet('background-color: purple ; color: black')
        self.geri.setStyleSheet('background-color: green ; color: black')
        self.kopyala.setStyleSheet('background-color: green ; color: black')
        layout.addWidget(self.yazi_alani)
        layout.addWidget(self.sifre_kir)
        layout.addWidget(self.sifrele)
        layout.addWidget(self.geri)
        layout.addWidget(self.cevap)
        layout.addWidget(self.kopyala)
        self.sifre_kir.clicked.connect(self.rot13_sifre_kir)
        self.sifrele.clicked.connect(self.rot13_sifrele)
        self.geri.clicked.connect(self.geriye)
        self.kopyala.clicked.connect(self.kopyalama)
        self.setLayout(layout)
    def rot13_sifre_kir(self):
        yazi = self.yazi_alani.toPlainText()
        metin = codecs.decode(yazi , 'rot_13')
        self.cevap.setText(metin)
    def rot13_sifrele(self):
        yazi = self.yazi_alani.toPlainText()
        metin = codecs.encode(yazi , 'rot_13')
        self.cevap.setText(metin)
    def geriye(self):
        self.yeni_pencere = AnaPencere()
        self.showMaximized()
        self.close()
    def kopyalama(self):
        self.kopyala.setStyleSheet('background-color: red; color: white')
        QApplication.clipboard().setText(self.cevap.text())
        

class Md5(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Base64 Pencere')
        layout = QVBoxLayout()
        self.yazi_alani = QTextEdit(self)
        self.yazi_alani.setGeometry(100,100,800,800)
        self.md5sifrele = QPushButton('md5 şifreleme')
        self.geri = QPushButton('geri',self)
        self.cevap = QLabel("cevap : ")
        self.kopyala = QPushButton("kopyala")
        self.yazi_alani.setStyleSheet('background-color: black; color: green')
        self.md5sifrele.setStyleSheet('background-color: purple; color: black')
        self.geri.setStyleSheet('background-color: green; color: black')
        self.kopyala.setStyleSheet('background-color: green; color: black')
        layout.addWidget(self.yazi_alani)
        layout.addWidget(self.md5sifrele)
        layout.addWidget(self.geri)
        layout.addWidget(self.cevap)
        layout.addWidget(self.kopyala)
        self.md5sifrele.clicked.connect(self.md5_sifrele)
        self.geri.clicked.connect(self.geriye)
        self.kopyala.clicked.connect(self.kopyalama)
        self.setLayout(layout)
    def md5_sifrele(self):
        yazi = self.yazi_alani.toPlainText()
        md_hash = hashlib.md5()
        md_hash.update(yazi.encode('utf-8'))
        sonuc = md_hash.hexdigest()
        self.cevap.setText(sonuc)
    def geriye(self):
        self.yeni_pencere = AnaPencere()
        self.showMaximized()
        self.close()
    def kopyalama(self):
        self.kopyala.setStyleSheet('background-color: red; color: white')
        QApplication.clipboard().setText(self.cevap.text())

class Pdf(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PDF Birleştirme Uygulaması')
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet('background-color: black')
        self.yazi = QLabel("PDF DOSYALARINI BİRLEŞTİRMEK İÇİN DOSYA SEÇ SEÇENEĞİNE TIKLAYIN...")
        self.dosya_sec = QPushButton('PDF Dosyalarını Seç', self)
        self.geri = QPushButton('GERİ')
        self.dosya_sec.clicked.connect(self.browsePDFs)
        self.dosya_birlestir = QPushButton('PDF Dosyalarını Birleştir', self)
        self.dosya_birlestir.clicked.connect(self.mergePDFs)
        self.geri.clicked.connect(self.kapa)
        self.dosya_sec.setStyleSheet('background-color: purple ; color: black')
        self.dosya_birlestir.setStyleSheet('background-color: purple ; color: black')
        self.geri.setStyleSheet('background-color: green ; color: black')
        self.dosya_sec.setFixedHeight(100)
        self.geri.setFixedHeight(100)
        self.dosya_birlestir.setFixedHeight(100)
        layout = QVBoxLayout()
        layout.addWidget(self.yazi)
        layout.addStretch()
        layout.addWidget(self.dosya_sec)
        layout.addWidget(self.dosya_birlestir)
        layout.addWidget(self.geri)
        self.setLayout(layout)
    def kapa(self):
        self.close()
    def browsePDFs(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        files, _ = QFileDialog.getOpenFileNames(self, "PDF Dosyalarını Seç", "", "PDF Dosyaları (*.pdf);;Tüm Dosyalar (*)", options=options)
        self.selected_files = files
        self.yazi.setText("PDF DOSYALARI SEÇİLDİ . BİRLEŞTİRME İŞLEMİNİ BAŞLATMAK İÇİN BİRLEŞTİR SEÇENEĞİNİ TIKLAYIN")
    def mergePDFs(self):
        if hasattr(self, 'selected_files') and len(self.selected_files) > 1:
            merged_pdf = PyPDF2.PdfFileMerger()
            for pdf_file in self.selected_files:
                merged_pdf.append(pdf_file)
            output_file, _ = QFileDialog.getSaveFileName(self, "Birleştirilmiş PDF Dosyasını Kaydet", "", "PDF Dosyaları (*.pdf);;Tüm Dosyalar (*)")
            if output_file:
                merged_pdf.write(output_file)
                merged_pdf.close()
                self.yazi.setText("BAŞARILI !! : PDF DOSYALARI BİRLEŞTİRİLDİ")
        else:
            self.yazi.setText("UYARI !!! : PDF DOSYALARI SEÇİLMEDİ")

class Pentest(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 800)
        self.setWindowTitle('Ana Pencere')
        self.setStyleSheet("background-color: green")
        nmap_tarama = QPushButton("NMAP TARAMA",self)
        geri = QPushButton("GERİ",self)
        nmap_tarama.setStyleSheet("background-color:black;color:white")
        geri.setStyleSheet("background-color:black;color:white")
        nmap_tarama.move(50,50) 
        geri.move(1700,900)
        video = QMovie('./gifs/deneme.gif')
        degisken = QLabel(self)
        degisken.setMovie(video)
        degisken.move(800,300)
        video.start()
        nmap_tarama.clicked.connect(self.nmap)
        geri.clicked.connect(self.kapat)
    def nmap(self):
        self.yeni_pencere = Nmap()
        self.yeni_pencere.showMaximized()
    def kapat(self):
    	self.close()

class Nmap(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 800)
        self.setWindowTitle('Ana Pencere')
        self.setStyleSheet('background-color: black')
        self.yazi = QLabel("IP ADRESİNİ GİRİNİZ :" , self)
        self.ip = QTextEdit(self)
        self.yazi.setStyleSheet('color : green;font-size:30px')
        self.tamam = QPushButton('TARAMAYI BAŞLAT')
        self.geri = QPushButton('GERİ')
        self.tamam.setFixedHeight(100)
        self.geri.setFixedHeight(100)
        layout = QVBoxLayout()
        layout.addWidget(self.yazi)
        layout.addWidget(self.ip)
        layout.addStretch()
        layout.addWidget(self.tamam)
        layout.addWidget(self.geri)
        self.setLayout(layout)
        self.tamam.setStyleSheet('border-radius : 30px ; background-color: purple;color:black')
        self.geri.setStyleSheet('border-radius : 15px ; background-color:green;color:black')
        self.tamam.clicked.connect(self.tarama_baslat)
        self.geri.clicked.connect(self.kapat)
    def tarama_baslat(self):

    	ip_adres = self.ip.toPlainText()
    	nm = nmap.PortScanner()
    	nm.scan(hosts=ip_adres , arguments=f'-p 1-100')
    	total_hosts = len(nm.all_hosts())
    	current_host = 0
    	liste = list()
    	liste.append("HOST : {}".format(ip_adres))
    	for i in nm.all_hosts():
    		current_host += 1
    		for k in nm[i].all_protocols():
    			ports = nm[i][k].keys()
    			total_ports = len(ports)
    			current_port = 0
    			for port in ports:
    				current_port +=1
    				state = nm[i][k][port]['state']
    				service = nm[i][k][port]['name']
    				liste.append(f" PORT {current_port}/{total_ports}: {port} ({state}) - {service}")
    	liste.append("tarama tamamlandı")

    	sonuc = '\n'.join((liste))
    	self.ip.setPlainText(sonuc)

    def kapat(self):
    	self.close()


class English(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('English')
		self.setStyleSheet('background-color:green')
		video = QMovie('./gifs/deneme.gif')
		degisken = QLabel(self)
		degisken.setMovie(video)
		degisken.move(850,300)
		video.start()
		geri = QPushButton('GERİ',self)
		kelime_ekle = QPushButton('KELİME EKLE',self)
		kelime_sil = QPushButton('KELİME SİL',self)
		kelime_ekle.setStyleSheet('border-radius:15px; background-color:black;color:white')
		kelime_sil.setStyleSheet('border-radius:15px;background-color:black;color:white')
		kelime_oyunu = QPushButton('KELİME OYUNU',self)
		kelime_oyunu.setStyleSheet('border-radius:15px;background-color:black;color:white')
		kelime_ekle.setGeometry(50,50,300,50)
		kelime_sil.setGeometry(50,50,300,50)
		kelime_oyunu.setGeometry(50,50,300,50)
		geri.setStyleSheet('border-radius:15px;background-color:#3498db;color:black')
		geri.setGeometry(50,50,200,50)
		geri.move(1600,900)
		kelime_ekle.move(50,50)
		kelime_sil.move(50,150)
		kelime_oyunu.move(50,250)
		geri.clicked.connect(self.kapat)
		kelime_ekle.clicked.connect(self.kelime_eklee)
		kelime_sil.clicked.connect(self.kelime_sill)
		kelime_oyunu.clicked.connect(self.kelime_oyunuu)
		con = sqlite3.connect("kelime.db")
		cursor = con.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS kelimeler (anahtar TEXT , deger TEXT)')
		con.commit()

	def kelime_oyunuu(self):
		self.yeni_pencere = Oyun()
		self.yeni_pencere.showMaximized()

	def kelime_sill(self):
		self.yeni_pencere = Kelime_sil()
		self.yeni_pencere.showMaximized()
	def kelime_eklee(self):
		self.yeni_pencere = Kelime_ekle()
		self.yeni_pencere.showMaximized()
	def kapat(self):
		self.close()

class Kelime_ekle(QWidget):
	def __init__(self):
		super().__init__()
		self.setStyleSheet('background-color:black')
		self.kelime = QLabel('İNGİLİZCE KELİMEYİ YAZINIZ  :')
		self.kelime_yaz = QTextEdit(self)
		self.anlam = QLabel("KELİMENİN ANLAMINI YAZ  :")
		self.anlam_yaz = QTextEdit(self)
		self.kelime_ekle = QPushButton('KELİME EKLE',self)
		self.geri = QPushButton('GERİ',self)
		self.yazi = QLabel('')
		self.kelime.setStyleSheet('color:green')			
		self.kelime_yaz.setStyleSheet('background-color:black;color:green')
		self.anlam.setStyleSheet('color:green')
		self.anlam_yaz.setStyleSheet('background-color:black;color:green')
		self.kelime_ekle.setStyleSheet('background-color:purple;color:black')
		self.geri.setStyleSheet('background-color:green;color:black')
		self.yazi.setStyleSheet('color:red')
		self.kelime_ekle.setFixedHeight(100)
		self.geri.setFixedHeight(100)		
		layout = QVBoxLayout()
		layout.addWidget(self.kelime)
		layout.addWidget(self.kelime_yaz)
		layout.addWidget(self.anlam)
		layout.addWidget(self.anlam_yaz)
		layout.addWidget(self.yazi)
		layout.addWidget(self.kelime_ekle)
		layout.addWidget(self.geri)
		self.setLayout(layout)
		self.kelime_ekle.clicked.connect(self.kelime_ekleee)
		self.geri.clicked.connect(self.kapat)
		self.kelime_yaz.installEventFilter(self)
	def eventFilter(self,obj,event):
		if obj == self.kelime_yaz:
			if event.type() == 6:
				if event.key() == 16777217:
					self.anlam_yaz.setFocus()
					return True
		return super().eventFilter(obj, event)
	def kelime_ekleee(self):
		con = sqlite3.connect("kelime.db")
		cursor = con.cursor()
		kelime = self.kelime_yaz.toPlainText()
		anlam = self.anlam_yaz.toPlainText()
		cursor.execute('SELECT * FROM kelimeler')
		liste = list()
		veri = cursor.fetchall()
		for i in veri:
			liste.append(i[0])
		if kelime in liste:
			self.yazi.setText('BU KELİME VERİ TABANINDA BULUNMAKTADIR !!!')
		else:
			cursor.execute('INSERT INTO kelimeler VALUES (?,?)',(kelime,anlam))
			con.commit()
			self.yazi.setText('KELİME EKLENDİ')
		self.kelime_yaz.clear()
		self.anlam_yaz.clear()		
		QTimer.singleShot(5000 , self.guncelle)
	def guncelle(self):
		self.yazi.setText('')
	def kapat(self):
		self.close()

class Kelime_sil(QWidget):
	def __init__(self):
		super().__init__()
		self.setStyleSheet('background-color:black')
		self.kelime = QLabel('SİLMEK İSTEDİĞİNİZ İNGİLİZCE KELİMEYİ YAZIN :')
		self.yaz = QTextEdit()
		self.sonuc = QLabel('')
		self.sil = QPushButton('SİL',self)
		self.geri = QPushButton('GERİ',self)
		self.kelime.setStyleSheet('color:green')
		self.yaz.setStyleSheet('background-color:black;color:green')
		self.sil.setStyleSheet('background-color:purple;color:black;font-size:50px')
		self.geri.setStyleSheet('background-color:green;color:black;font-size:50px')
		self.sonuc.setStyleSheet('color:green;font-size:30px')	
		layout = QVBoxLayout()
		layout.addWidget(self.kelime)
		layout.addWidget(self.yaz)
		layout.addWidget(self.sonuc)
		layout.addWidget(self.sil)
		layout.addWidget(self.geri)
		self.setLayout(layout)
		self.sil.setFixedHeight(100)
		self.geri.setFixedHeight(100)
		self.sil.clicked.connect(self.sill)
		self.geri.clicked.connect(self.kapat)
	def sill(self):
		deger = self.yaz.toPlainText()
		con = sqlite3.connect("kelime.db")
		cursor = con.cursor()
		cursor.execute('DELETE FROM kelimeler WHERE anahtar = ? ' , (deger,))
		con.commit()
		self.sonuc.setText('KELİME SİLİNDİ ...')
		self.yaz.clear()
		QTimer.singleShot(5000,self.guncelle)
	def guncelle(self):
		self.sonuc.setText('')

	def kapat(self):
		self.close()

class Oyun(QWidget):
	def __init__(self):
		super().__init__()
		self.setStyleSheet('background-color:black')
		self.kelimeler = QLabel('')
		self.yazi = QTextEdit(self)
		self.sonuc = QLabel('')
		self.cevapla = QPushButton('CEVAPLA',self)
		self.ornek = QPushButton('ÖRNEK CÜMLELER',self)
		self.sonraki = QPushButton('SONRAKİ KELİME',self)
		self.okunus = QPushButton('OKUNUŞ',self)
		self.geri = QPushButton('GERİ',self)
		self.kelimeler.setStyleSheet('background-color:green;  color:black;font-size:30px')
		self.yazi.setStyleSheet('background-color:black;color:green')
		self.cevapla.setStyleSheet('background-color:green;color:black')
		self.sonraki.setStyleSheet('background-color:green;color:black')
		self.okunus.setStyleSheet('background-color:green;color:black')
		self.geri.setStyleSheet('background-color:purple;color:black')
		self.ornek.setStyleSheet('background-color:green;color:black')
		self.sonuc.setStyleSheet('color:green')
		self.cevapla.setFixedHeight(100)
		self.sonraki.setFixedHeight(100)
		self.okunus.setFixedHeight(100)
		self.geri.setFixedHeight(100)
		self.ornek.setFixedHeight(100)
		self.cevapla.clicked.connect(self.cevaplaa)
		self.sonraki.clicked.connect(self.sonrakii)
		self.okunus.clicked.connect(self.okunuss)
		self.geri.clicked.connect(self.kapat)
		self.ornek.clicked.connect(self.ornekler)
		self.stacked_widget = QStackedWidget()
		layout = QVBoxLayout()
		layout.addWidget(self.kelimeler)
		layout.addWidget(self.yazi)
		layout.addWidget(self.sonuc)
		layout.addWidget(self.cevapla)
		layout.addWidget(self.ornek)
		layout.addWidget(self.sonraki)
		layout.addWidget(self.okunus)
		layout.addWidget(self.geri)
		self.setLayout(layout)
		con = sqlite3.connect("kelime.db")
		cursor = con.cursor()
		liste = list()
		cursor.execute('SELECT * FROM kelimeler ORDER BY RANDOM() LIMIT 1')
		self.deger,self.diger = cursor.fetchone()
		self.kelimeler.setText(self.diger)
		self.kel = self.deger
		url = 'https://sentence.yourdictionary.com/' + str(self.kel)
		response = requests.get(url)
		self.liste = list()
		if response.status_code == 200:
			html_icerigi = response.content
			soup = BeautifulSoup(html_icerigi,'html.parser')
			for i in soup.find_all("div",{"class":"sentence-item__wrapper"}):
				self.liste.append(i.text)
			self.result = '\n'.join((self.liste))
	def ornekler(self):
		self.yazi.setPlainText(self.result)
		self.liste.clear()
	def cevaplaa(self):
		son = self.yazi.toPlainText()
		if son != self.deger:
			self.sonuc.setText('YANLIŞ!!!')
		else:
			self.sonuc.setText('DOĞRU')
	def sonrakii(self):
		con = sqlite3.connect("kelime.db")
		cursor = con.cursor()
		cursor.execute('SELECT * FROM kelimeler ORDER BY RANDOM() LIMIT 1')
		self.deger,self.diger = cursor.fetchone()
		self.kelimeler.setText(self.diger)
		self.yazi.clear()
		self.sonuc.setText('')
		self.kel = self.deger
		self.liste.clear()	
	def okunuss(self):
		kelimeeee = self.deger
		import pyttsx3
		nesne = pyttsx3.init()
		nesne.setProperty('rate',130)
		nesne.say(kelimeeee)
		nesne.runAndWait()
	def kapat(self):
		self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ana_pencere = AnaPencere()
    ana_pencere.showMaximized()
    sys.exit(app.exec_())
