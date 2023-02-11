import requests

headers = \
{'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

for date in range(62, 32, -1): 
      url = 'https://www.todayhumor.co.kr/board/view.php?table=bestofbest&no=4652{0}&s_no=4652{0}&page=1'.format(date)
      site = requests.get(url, headers=headers)
      source_data = site.text

      count = source_data.count('subject"><a href="')

      for i in range(count):
            pos1 = source_data.find('subject"><a href="')+ len('subject"><a href="')
            source_data = source_data[pos1:]

            pos2 = source_data.find('=1" target="')
            a_data = source_data[: pos2]

            pos3 = source_data.find('=1" target="_top">')+ len('=1" target="_top">')
            sourve_dara = source_data[pos3:]

            pos4 = source_data.find('</a><span class=')
            b_data = source_data[: pos4]

            pos5 = source_data.find('<div class="upfile" id="upfile1"> ')+ len('<div class="upfile" id="upfile1"> ')
            source_data = source_data[pos5:]

            pos6 = source_data.find('/></div>')
            c_data = source_data[: pos6].strip()

            source_data = source_data[pos6+1:]
            print(i+1, a_data, b_data, c_data)


