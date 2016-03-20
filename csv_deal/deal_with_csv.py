# coding:utf-8
import csv


def add_bom():
    filename = 'pool1xcf电器池1_.csv'
    with open('{filename}'.format(filename=filename), 'r+b') as file:
        file.write('\xef\xbb\xbf')


def create_csv():
    with open('pipilo.csv', 'wb') as csv_file:
        csv_writer = csv.writer(csv_file, dialect='excel')
        csv_writer.writerow(["\xef\xbb\xbf"])
        csv_writer.writerow(["哈哈出现中文会怎么样", "1/3/09 14:44", "'Product1'", "1200''", "Visa", "Gouya"])
        csv_writer.writerow(["哈哈出现中文会怎么样", "1/3/09 14:44", "'Product1'", "1200''", "Visa", "Gouya"])
        csv_writer.writerow(["哈哈出现中文会怎么样", "1/3/09 14:44", "'Product1'", "1200''", "Visa", "Gouya"])
        csv_writer.writerow(["哈哈出现中文会怎么样", "1/3/09 14:44", "'Product1'", "1200''", "Visa", "Gouya"])


def format_csv():
    filename = 'pool1xcf电器池1.csv'
    write_filename = 'pool1xcf电器池1_.csv'
    with open('{filename}'.format(filename=filename), 'rb') as csv_file:
        csv_reader = csv.reader(csv_file)
        with open('{write_filename}'.format(write_filename=write_filename), 'w+b') as file:
            csv_writer = csv.writer(file, dialect='excel')
            csv_writer.writerow(["\xef\xbb\xbf"])
            csv_writer.writerow(["sku_id", "价格", "商品名称"])
            for line in csv_reader:
                csv_writer.writerow(line[:2]+[''.join(line[2:])])

if __name__ == '__main__':
    add_bom()
    # format_csv()
    # read_format_csv()
