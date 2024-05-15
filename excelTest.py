import xlrd
workbook = xlrd.open_workbook(r"C:\Users\Mengling.Huang\Downloads\Confluence资源清单.xlsx")
sheet = workbook.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)

print(sheet.row(1)[1].value)
title_place = sheet.row(0)[0].value
title_type = sheet.row(0)[1].value
title_id = sheet.row(0)[2].value
title_name = sheet.row(0)[3].value
title_ip = sheet.row(0)[4].value

vm_list = []
for row in range(1, sheet.nrows):
    vm = {}
    vm_place = sheet.row(row)[0].value
    vm_type = sheet.row(row)[1].value
    vm_id = sheet.row(row)[2].value
    vm_name = sheet.row(row)[3].value
    vm_ip = sheet.row(row)[4].value

    vm[title_ip] = vm_ip
    vm[title_name] = vm_name
    vm[title_id] = vm_id
    vm[title_type] = vm_type
    vm[title_place] = vm_place
    vm_list.append(vm)

print(vm_list)
