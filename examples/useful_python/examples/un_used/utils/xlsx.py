from openpyxl import Workbook


def write_info_to_excel():
    wb = Workbook()
    sheet = wb.active
    sheet.title = "result"
    titles = ["电影名字", "腾讯", "爱奇艺", "优酷", "咪咕", "评分"]
    sheet.append(titles)

    wb.save("豆瓣Top100.xlsx")



if __name__ == "__main__":
    write_info_to_excel()

