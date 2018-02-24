# -*- coding: utf-8 -*-

import httplib
import urllib
import csv
import json
import sys
import codecs
import re
import sqlite3
from collections import OrderedDict
from bs4 import BeautifulSoup

formdata = {
    "__VIEWSTATE": "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",
    "__VIEWSTATEGENERATOR": "31A172A6", "__EVENTTARGET": "pagelist", "__EVENTARGUMENT": 2,
    "__EVENTVALIDATION": "/wEWEALIoMyoCgLV5KIqArjloioCl+WiKgL646IqAtHloioCtOaiKgKT5qIqAvbkoioCzeaiKgKw56IqAtXktqUCArjltqUCApfltqUCAvrjtqUCAtHltqUCG65UrNVZMlr/6wwylnP29GVEQRE=",
    "pagelist_input": 1}


def parse_html_to_list(html_data):
    soup = BeautifulSoup(html_data, "lxml")
    table = soup.find("table", attrs={"class": "dataList"})

    data_list = []
    for row in table.find_all("tr")[1:]:
        single_row = []
        col = 0
        for td in row.find_all("td"):
            td_value = td.get_text().strip()
            # Process the first col which is reporter's name
            if col == 0:
                td_value = td.find_all("input", limit=1)[0].get("value")
            single_row.append(td_value)
            col = col + 1
        data_list.append(single_row)
    return data_list


def parse_html_to_page_number(html_data):
    soup = BeautifulSoup(html_data, "lxml")
    page_number_div = soup.find("div", attrs={"class": "pn"})
    page_number_div_content = page_number_div.get_text().strip()
    page_number = int(re.findall('\d+', page_number_div_content)[0])
    return page_number


def json_to_csv(json_input, csv_output, header):
    with open(json_input, 'r') as data_file:
        json_data = json.load(data_file)

    with open(csv_output, 'wb') as file_handler:
        # This is important for unicode data, otherwise csv file is not readable
        file_handler.write(codecs.BOM_UTF8)

        csv_writer = csv.writer(file_handler)
        csv_writer.writerow([item for item in header.values()])  # header row

        for row in json_data:
            csv_writer.writerow([item.encode('utf8') for item in row])


def get_page_number(html_data):
    soup = BeautifulSoup(html_data, "lxml")
    div_content = soup.find("div", attrs={"class": "pn"}).get_text().strip()
    number = div_content
    return number


def __main__():
    host = 'www.dpac.gov.cn'
    proxy_host = "cnproxy.int.nokia-sbell.com"
    proxy_port = "8080"
    is_proxy_needed = True
    url = 'http://' + host + '/cpqxcj/VehicleComplaintPublicity.aspx'
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", 'Accept-Encoding': 'utf-8'}
    formdata['__EVENTARGUMENT'] = 1  # Current Page number
    json_file = "data.json"
    csv_file = "data.csv"
    # db column and description mapping
    db_mapping = OrderedDict([
        ("reporter", "消费者"), ("reporter_location", "所在省市"),
        ("product_producer", "生产者名称"), ("brand_name", "品牌"),
        ("product_model", "车型系列"), ("product_year", "年款"),
        ("product_name", "车型名称"), ("assemble", "所在总成"),
        ("sub_assemble", "所在分总成"), ("submit_time", "缺陷报告时间")
    ])

    db_mapping = OrderedDict([
        ("reporter", "报告人"), ("product_producer", "生产者名称"), ("brand_name", "品牌"),
        ("product_model", "车型系列"), ("product_name", "车型名称"), ("assemble", "所在总成"),
        ("submit_time", "入库时间")
    ])
    db_table = "VehicleComplaint"
    db_name = "VehicleComplaint.db3"

    if is_proxy_needed:
        conn = httplib.HTTPConnection(proxy_host, proxy_port)
    else:
        conn = httplib.HTTPConnection(host)

    # get the first page and find the total page number
    print("Reading page number")
    params = urllib.urlencode(formdata)
    conn.request("POST", url, params, headers)
    data = conn.getresponse().read()
    total_page = parse_html_to_page_number(data)
    print("Total page number: %s" % total_page)
    start_page = 1
    # sys.exit(0)

    if total_page > 1:
        # Store the inserted data and then dump to json and csv file
        inserted_data = []

        # Used to break outer loop
        duplicated_error_count = 0
        max_error_count = 20
        db = sqlite3.connect(db_name)
        cursor = db.cursor()
        columns = ', '.join(db_mapping.keys())
        placeholders = ', '.join('?' * len(db_mapping))
        # start to get all pages one by one
        for page in range(start_page, total_page + 1):
            print("Reading page: %s / %s" % (page, total_page))
            # Changing page number
            formdata['__EVENTARGUMENT'] = page
            params = urllib.urlencode(formdata)
            conn.request("POST", url, params, headers)
            data = conn.getresponse().read()
            list_data = parse_html_to_list(data)

            # Store to DB and break during insert error
            for row in list_data:
                try:
                    sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (db_table, columns, placeholders)
                    cursor.execute(sql, row)
                    db.commit()
                    inserted_data.append(row)
                except sqlite3.Error as e:
                    msg = repr([x.encode(sys.stdout.encoding) for x in row]).decode('string-escape')
                    duplicated_error_count += 1  # Break outer loop, stop to get next page since the data has been collected
                    print("Insert Error: %s for data: %s. Total error: %s" % (e.message, msg, duplicated_error_count))
            if duplicated_error_count > max_error_count:
                print("Insert Error over %s, exit collection process at %s / %s" % (max_error_count, page, total_page))
                break
            print("Done")
        db.close()
        conn.close()

        print("Dumping data to json file: %s" % json_file)
        with codecs.open(json_file, encoding='UTF-8', mode='w') as outfile:
            json.dump(inserted_data, outfile, encoding='UTF-8', ensure_ascii=False)
        print("Done")

        print("Converting %s to csv %s" % (json_file, csv_file))
        json_to_csv(json_file, csv_file, db_mapping)
        print("Done")
    else:
        print("Get page number failed.")


__main__()
