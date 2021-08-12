import pymysql

class  DB:

    def __init__(self):
        self.con = pymysql.connect(
                    user='root',
                    password='123456',
                    port=3308,
                    database='test'
                    )
        self.cur = self.con.cursor(cursor=pymysql.cursors.DictCursor)

    def select_data(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def update_data(self, sql):
        self.cur.execute(sql)
        self.con.commit()

class books(DB):

    def add_book(self):

        id = input('请输入编号')
        book_name = input("请输入书名：")
        book_location = input("请输入图书存放位置：")
        SQL = 'insert into books(name,position) value ( "{}","{}" )'.format(book_name,book_location)
        self.update_data(SQL)
        print("添加成功")
        n=input("请确认是否继续输入")
        if n=='1':
            self.add_book()

    def update_book(self):
        id=input("请输入要查询的图书")
        res=self.select_data(f"select * from books where id={id}")
        pass
    def delete_book(self):
        pass
    def select_book(self):

        book_name=input("请输入书的编号：")
        sql='select *  from books where id={0}'.format(book_name)
        self.select_data(sql)
    def list_book(self):
        sql = 'select *  from books'
        res = self.select_data(sql)
        for i in res:
            print(f"编号:{i['id']},书名:{i['name']},位置:{i['position']},状态{i['status']},借阅人{i['borrorwer']}")
        # pass
    def lend_book(self):
        pass
    def reback_book(self):
        pass
    def quit(self):
        print("返回主菜单")

    def print_menu(self):
        print('--------------菜单-------------')
        print('【1】：添加图书')
        print('【2】：修改图书')
        print('【3】：删除图书')
        print('【4】：查询图书')
        print('【5】：图书列表')
        print('【6】：出借图书')
        print('【7】：归还图书')
        print('【8】：退出')

    def main(self):
        print("-------------欢迎来到图书管理系统------------")
        while True:
            self.print_menu()
            number=input("请输入你的选项:")
            if number=='1':
                self.add_book()
            if number=='2':
                self.update_book()
            if number=='3':
                self.delete_book()
            if number=='4':
                self.select_book()
            if number=='5':
                self.list_book()
            if number=='6':
                self.add_book()
            if number=='7':
                self.add_book()
            if number=='8':
                self.add_book()


if __name__ == "__main__":

    book = books()
    book.main()