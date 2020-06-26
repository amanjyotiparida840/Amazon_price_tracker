import requests
from bs4 import BeautifulSoup
import smtplib

URL='https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/dp/B07BS4TJ43/ref=br_msw_pdt-5?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=DZ6QFTAWJ0QBNKM38SNA&pf_rd_t=36701&pf_rd_p=9806b2c4-09c8-4373-b954-bae25b7ea046&pf_rd_i=desktop'

headers={"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def check_price():
  page=requests.get(URL, headers=headers)
  soup=BeautifulSoup(page.content, 'html.parser')
  title = soup.find(id="productTitle").get_text()
  converted_title=title.strip()
  price = soup.find(id="priceblock_ourprice").get_text()
  replace_price = price.replace(",", "")
  converted_price = float(replace_price[2:7])
  print(converted_price)

  if (converted_price < 29990.00) :
   send_mail()
   print(converted_price)
   print(converted_title)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('amanjyotiparida840@gmail.com', 'gnhkavijftylqlga')
    subject = 'price fell down!'
    body = 'check the amazon link https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/dp/B07BS4TJ43/ref=br_msw_pdt-5?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=DZ6QFTAWJ0QBNKM38SNA&pf_rd_t=36701&pf_rd_p=9806b2c4-09c8-4373-b954-bae25b7ea046&pf_rd_i=desktop'

    msg = "Subject:{subject}\n\n{body}"

    server.sendmail(
        'from@gmail.com',
        'to@gmail.com',
        msg
    )
    # from mean here you put your email
    # to mean send your the mail to the specific person

    print("hey Email has been sent!")

    server.quit()

check_price()





