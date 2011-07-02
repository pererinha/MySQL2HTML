"""
 This script reads a database (MySQL) and exports all of its tables structure to a HTML file. 
 @pererinha - 02/07/2011
"""

import MySQLdb 

class MysqlToHTML:
 def __init__(self):
  try:
    con = MySQLdb.connect('<HOST>', '<USERNAME>', '<PASSWORD>')
    con.select_db('<DATABASE>')
    cursor = con.cursor() 
    tableData = con.cursor() 
  except MySQLdbError, error:
    print(str(error), "Info")
    exit()
  outfile = open("tabelas.html", "w")
  outfile.write("<style>table{font-family:'Arial';font-size:12px;margin:0 0 40px 0;border:1px solid #000;width:600px;}th{background:#F5F5F5;border:1px solid #000;text-align:left;}td{border:1px solid #000;}td, th{padding:5px;}th.name{border:1px solid #000;background:#CCC;font-weight:bold;font-size:13px;padding:5px;}</style>")
  cursor.execute ("SHOW TABLE STATUS FROM `espiral2base_dev2`;;")
  while (1):
    row = cursor.fetchone()
    if row == None:
      break
    tableName = row[0]
    tableData.execute("DESCRIBE " + tableName + ";")
    tableInfo = ""
    tableInfo += "<table>"
    tableInfo += "<tr><th class=\"name\" colspan=\"6\">" + tableName + "</th></tr>"
    tableInfo += "<tr>"
    tableInfo += "<th>Field</th>"
    tableInfo += "<th>Type</th>"
    tableInfo += "<th>Null</th>"
    tableInfo += "<th>Key</th>"
    tableInfo += "<th>Default</th>"
    tableInfo += "<th>Extras</th>"
    tableInfo += "</tr>"
    while (1):
      tableRow = tableData.fetchone()
      if tableRow == None:
        break
      field = tableRow[0]
      type = tableRow[1]
      isNull = tableRow[2]
      isKey = tableRow[3]
      defaultValue = tableRow[4]
      extras = tableRow[5]
      tableInfo += "<tr>"
      tableInfo += "<td>" + field + "&nbsp;</td>"
      tableInfo += "<td>" + type + "&nbsp;</td>"
      tableInfo += "<td>" + isNull + "&nbsp;</td>"
      tableInfo += "<td>" + isKey + "&nbsp;</td>"
      tableInfo += "<td>"
      if defaultValue != None:
        tableInfo += defaultValue
      tableInfo += "&nbsp;</td>"
      tableInfo += "<td>" + extras + "&nbsp;</td>"
      tableInfo += "</tr>"
    tableInfo += "</tr>"
    tableInfo += "</table><hr/>"
    outfile.write(tableInfo)
  cursor.close()
  con.close()
ap = MysqlToHTML()