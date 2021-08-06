import sys 
from PyQt5 import QtWidgets, uic
from PyQt5.uic.uiparser import WidgetStack
import mysql.connector


tb_imoveis = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd ='',
    database = "cadastroimoveis"
)




def iniciar():

    rua = banco.lineEdit.text ()
    numero = banco.lineEdit_2.text()
    bairro = banco.lineEdit_3.text()
    valor = banco.lineEdit_4.text ()
    prop = banco.lineEdit_5.text()
    tell = banco.lineEdit_6.text()
    descrição = banco.lineEdit_7.text()
    casa_ap = ''

    if banco.radioButton.isChecked():
        print ('casa')
        casa_ap= 'casa'
    elif banco.radioButton_2.isChecked():
        casa_ap='ap'
        
    
    cursor = tb_imoveis.cursor()
    adicionar = "INSERT INTO imoveis (rua,numero,bairro,casa_ap,valor,descrição,prop,tell) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    inf = (str (rua),str(numero),str(bairro),casa_ap,int(valor),str(descrição),str(prop),int(tell))
    cursor.execute(adicionar ,inf )
    tb_imoveis.commit()
    banco.lineEdit.setText('')
    banco.lineEdit_2.setText('')
    banco.lineEdit_3.setText ('')
    banco.lineEdit_4.setText ('')
    banco.lineEdit_5.setText ('')
    banco.lineEdit_6.setText ('')
    banco.lineEdit_7.setText ('')
    
def m_imoveis ():
    imoveis.show()
    cursor = tb_imoveis.cursor()
    adicionar = "SELECT * FROM imoveis "
    cursor.execute(adicionar)
    imoveis_salvos = cursor.fetchall()
    imoveis.tableWidget.setRowCount(len(imoveis_salvos))
    imoveis.tableWidget.setColumnCount(7)
    for i in range (0,len(imoveis_salvos)):
        for c in range (0,7):
            imoveis.tableWidget.setItem(i,c,QtWidgets.QTableWidgetItem(str(imoveis_salvos[i][c])))
    
def deletar ():
    imv = imoveis.tableWidget.currentRow()
    imoveis.tableWidget.removeRow(imv)
    

    cursor = tb_imoveis.cursor()
    cursor.execute("SELECT id FROM imoveis")
    m_imoveis = cursor.fetchall()
    valor_id = m_imoveis[imv][0]
    cursor.execute ('DELETE FROM imoveis WHERE id='+ str (valor_id))
    print (valor_id)
    





app = QtWidgets.QApplication([])
banco = uic.loadUi("banco.ui")
imoveis = uic.loadUi('imoveis.ui')
banco.pushButton.clicked.connect(iniciar)
banco.pushButton_2.clicked.connect(m_imoveis)
imoveis.pushButton.clicked.connect(deletar)



banco.show()
app.exec_()




 