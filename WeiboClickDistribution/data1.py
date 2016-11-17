# coding:utf-8
import xlwt
import pprint

file_in = r"result1.txt"
file_out = r"result1.xls"
map_cates = {'1': '热点', '2': '娱乐', '3': '体育', '4': '军事', '5': '科技', '6': '财经',
             '7': '社会', '8': '教育', '9': '房产', '10': '汽车', '11': '健康', '12': '时尚',
             '13': '旅游', '102': '生活', '1000': '其他', '1001': '城市', '10000': '互联网', '10001': '数码',
             '10002': '家居', '10003': '神总结', '10004': '育儿', '10005': '动漫', '10006': '星座', '10007': '美女',
             '10008': '宠物', '10009': '健身', '10010': '情感', '10011': '搞笑', '10012': '美食', '10013': '历史',
             '10014': '游戏', '10015': '视频', '10016': '养生', '10017': '摄影', '10018': '电影', '10019': '涨知识',
             '10020': '科学', '10021': '国际', '10022': '长微博', '10023': '头条文章', '10025': '奥运', '-1': '其他或未知'}


def sortData(file_in):
    fin = open(file_in, 'r')
    all_data = []
    line_num = 0
    for line in fin:
        all_data.insert(line_num, line.split(';'))
        line_num += 1
    all_data.sort(key=lambda l: (l[1], l[0]))
    new_data = []
    all_data_len = len(all_data)
    all_data_index = 0
    new_data_index = 0

    while all_data_index < all_data_len-1:
        tmp = []
        tmp.append(map_cates.get(all_data[all_data_index][1]))
        tmp.append(all_data[all_data_index][2].strip())
        tmp.append(all_data[all_data_index+1][2].strip())
        tmp.append(round(float(tmp[2])/float(tmp[1]), 2)*100)
        new_data.append(tmp)
        all_data_index += 2

    excel1 = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = excel1.add_sheet("sheet1", cell_overwrite_ok=True)
    sheet.write(0, 0, '领域')
    sheet.write(0, 1, '曝光数')
    sheet.write(0, 2, '点击数')
    sheet.write(0, 3, '点击曝光百分比')
    data_line_num = 1

    for data in new_data:
        for i in range(len(data)):
            sheet.write(data_line_num, i, data[i])
        data_line_num += 1
    excel1.save(file_out)


if __name__ == '__main__':
    sortData(file_in)
