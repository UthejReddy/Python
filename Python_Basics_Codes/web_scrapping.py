import bs4 as bs
import urllib.request
sauce = urllib.request.urlopen("https://www.flipkart.com/samsung-galaxy-a21s-black-64-gb/p/itm3f1fa3caa5ac6?pid=MOBFSFMJZVFVNDAG&lid=LSTMOBFSFMJZVFVNDAGCQVA7S&fm=neon%2Fmerchandising&iid=M_87f7ea05-79ca-45b5-8498-5c96896cbdfd_20.NZ5YDRD0C1JU&ppt=hp&ppn=homepage&ssid=1yd4m3m8hc0000001601641667331&otracker=hp_omu_Best%2BBattery%2BPhones_2_11.dealCard.OMU_NZ5YDRD0C1JU_7&otracker1=hp_omu_WHITELISTED_neon%2Fmerchandising_Best%2BBattery%2BPhones_NA_dealCard_cc_2_NA_view-all_7&cid=NZ5YDRD0C1JU").read()
soup=bs.BeautifulSoup(sauce,'lxml')

print(soup.title)