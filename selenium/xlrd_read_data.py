from xlrd import open_workbook

#
# workbook = open_workbook(r"C:\Users\user\Desktop\python\read.xls")
# sheet = workbook.sheet_by_name("Employee")
# rows = sheet.nrows
# cols = sheet.ncols
# print(rows)
# print(cols)

#read header of test case
# def read_headers(sheet_name, test_case_name):
#     workbook = open_workbook(r"C:\Users\user\Desktop\python\python_practice\files\testdata.xls")
#     sheet = workbook.sheet_by_name(sheet_name)
#     used_rows = sheet.nrows
#     for i in range(0, used_rows):
#         rows = sheet.row_values(i)
#         if rows[0] == test_case_name:
#             headers = sheet.row_values(i-1)
#             h = [header for header in headers if header]
#             print(h)
#             break
# read_headers("smoke", "test_registration")


#read locaters

def read_locators(pagename):
    workbook = open_workbook(r"C:\Users\user\Desktop\python\python_practice\files\objects.xls")
    sheet = workbook.sheet_by_name(pagename)
    used_rows = sheet.nrows
    locators = {}
    for i in range(1,used_rows):
        data = sheet.row_values(i)
        locators[data[0]] = (data[1], data[2])
    return locators
print(read_locators("homepage"))

#read actual data
def actual_data(sheetname,test_case_name):
    workbook = open_workbook(r"C:\Users\user\Desktop\python\python_practice\files\testdata.xls")
    sheet = workbook.sheet_by_name(sheetname)
    actual_data = []
    used_rows = sheet.nrows
    for i in range(1, used_rows):
        rows = sheet.row_values(i)
        if rows[0] == test_case_name:
            data = [r for r in rows if r]
            if data[1] == "Yes":
                actual_data.append(data[2::])
    return actual_data
print(actual_data("smoke", "test_login_positive"))


