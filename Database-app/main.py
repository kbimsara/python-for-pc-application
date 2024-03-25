from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QTableWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import QDate
import sys


class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(550, 500)
        self.setWindowTitle("Simple Data Manager")

        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()

        self.add_btn = QPushButton("Add Expense")
        self.delete_btn = QPushButton("Delete Expense")

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        table_header = ["ID", "Date", "Category", "Amount", "Description"]
        self.table.setHorizontalHeaderLabels(table_header)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # desing app
        self.dropdown.addItems(["Food", "Internet", "Electricity", "Bill", "Other"])

        self.setStyleSheet("""
        QWidget{Background-color:yellow}
        """)

        self.master_layout = QVBoxLayout()
        self.row1 = QHBoxLayout()
        self.row2 = QHBoxLayout()
        self.row3 = QHBoxLayout()

        self.row1.addWidget(QLabel("Date :"))
        self.row1.addWidget(self.date_box)
        self.row1.addWidget(QLabel("Category :"))
        self.row1.addWidget(self.dropdown)

        self.row2.addWidget(QLabel("Amount :"))
        self.row2.addWidget(self.amount)
        self.row2.addWidget(QLabel("Description :"))
        self.row2.addWidget(self.description)

        self.row3.addWidget(self.add_btn)
        self.row3.addWidget(self.delete_btn)

        self.master_layout.addLayout(self.row1)
        self.master_layout.addLayout(self.row2)
        self.master_layout.addLayout(self.row3)

        self.master_layout.addWidget(self.table)

        self.setLayout(self.master_layout)

        self.load_table()

        self.add_btn.clicked.connect(self.add_expense)
        self.delete_btn.clicked.connect(self.delete_expense)

        # self.table.currentRow.edit_expense()

    def clear(self):
        self.dropdown.setCurrentIndex(0)
        self.amount.clear()
        self.description.clear()

    # load table/refresh
    def load_table(self):
        self.table.setRowCount(0)

        query = QSqlQuery("SELECT * FROM simpleTest ORDER BY date ASC")
        row = 0
        while query.next():
            res_id = query.value(0)
            res_date = query.value(1)
            res_category = query.value(2)
            res_amount = query.value(3)
            res_description = query.value(4)

            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(res_id)))
            self.table.setItem(row, 1, QTableWidgetItem(str(res_date)))
            self.table.setItem(row, 2, QTableWidgetItem(str(res_category)))
            self.table.setItem(row, 3, QTableWidgetItem(str(res_amount)))
            self.table.setItem(row, 4, QTableWidgetItem(str(res_description)))
            row += 1

    # add data
    def add_expense(self):
        date = self.date_box.date().toString("yyyy-MM-dd")
        category = self.dropdown.currentText()
        amount = self.amount.text()
        description = self.description.text()

        query = QSqlQuery()
        query.prepare(
            """
            INSERT INTO simpleTest (date, category, amount, description)
            VALUES (?, ?, ?, ?)
            """
        )
        query.addBindValue(date)
        query.addBindValue(category)
        query.addBindValue(amount)
        query.addBindValue(description)

        if not query.exec_():
            QMessageBox.critical(self, "Error", "Failed to add expense.")
        else:
            self.load_table()
            self.clear()

    # delete data
    def delete_expense(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(
                self, "No Expense chosen", "Please choose an expense to delete!"
            )
            return
        expense_id = int(self.table.item(selected_row, 0).text())
        confirm = QMessageBox.question(
            self, "Are You sure?", "Delete Expense?", QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.No:
            return
        query = QSqlQuery()
        query.prepare("DELETE FROM simpleTest WHERE id=?")
        query.addBindValue(expense_id)
        query.exec_()

        self.load_table()

    # edit database
    # def edit_expense(self):
    #     selected_row = self.table.currentRow()
    #     if selected_row == -1:
    #         QMessageBox.warning(
    #             self, "No Expense chosen", "Please choose an expense to delete!"
    #         )
    #         return
    #     expense_id = int(self.table.item(selected_row, 0).text())
    #     date = self.table.item(selected_row, 1).text()
    #     category = self.table.item(selected_row, 2).text()
    #     amount = self.table.item(selected_row, 3).text()
    #     description = self.table.item(selected_row, 4).text()

    #     self.date_box.setTime(date)
    #     self.dropdown.setAttribute(category)
    #     self.description.setText(description)
    #     self.amount.setText(amount)


# Database manager
Database = QSqlDatabase.addDatabase("QSQLITE")
Database.setDatabaseName("simpleTest.db")
if not Database.open():
    QMessageBox.critical(None, "Error", "Could not open SQL Database")
    sys.exit(1)

query = QSqlQuery()
create_sql = """
CREATE TABLE IF NOT EXISTS simpleTest(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    category TEXT,
    amount REAL,
    description TEXT
)
"""
query.exec_(create_sql)

# run app
if __name__ == "__main__":
    app = QApplication([])
    main = ExpenseApp()
    main.show()
    sys.exit(app.exec_())
