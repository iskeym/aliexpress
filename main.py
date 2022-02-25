import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def link(driver, domen, page, links):
    url = (f'{domen}&page={page}')
    driver.get(url)

    items = driver.find_elements(By.CLASS_NAME, "product-snippet_ProductSnippet__container__mdters")
    for item in items:
        link = item.find_element(By.CLASS_NAME, "product-snippet_ProductSnippet__galleryBlock__mdters").get_attribute('href')
        links.append(link)

        print(link)

def info(driver, links, total):
    for link in links:
        driver.get(link)

        x = []
        try:
            x.append({
                'title': driver.find_element(By.CLASS_NAME, "Product_Name__productTitleText__hntp3").text,
                'price': driver.find_element(By.CLASS_NAME, "product-price-current").text,
                'reviews': driver.find_element(By.XPATH, "//span[@class='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 ali-kit_Label__label__1n9sab ali-kit_Label__size-m__1n9sab']").text,
                'company': driver.find_element(By.XPATH, "//span[@class='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 ali-kit_Label__label__1n9sab ali-kit_Label__size-m__1n9sab StoreBanner_StoreBanner__storeName__1apu4']").text,
                'link': link
            })
        except:
            try:
                x.append({
                    'title': driver.find_element(By.CLASS_NAME, "Product_Name__productTitleText__hntp3").text,
                    'price': driver.find_element(By.XPATH, "//span[@class='Product_UniformBanner__uniformBannerBoxPrice__o5qwb']").text,
                    'reviews': driver.find_element(By.XPATH, "//span[@class='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 ali-kit_Label__label__1n9sab ali-kit_Label__size-m__1n9sab']").text,
                    'company': driver.find_element(By.XPATH, "//span[@class='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 ali-kit_Label__label__1n9sab ali-kit_Label__size-m__1n9sab StoreBanner_StoreBanner__storeName__1apu4']").text,
                    'link': link
                })
            except:
                try:
                    x.append({
                        'title': driver.find_element(By.CLASS_NAME, "Product_Name__productTitleText__hntp3").text,
                        'price': driver.find_element(By.XPATH, "//span[@class='Product_UniformBanner__uniformBannerBoxPrice__o5qwb']").text,
                        'reviews': driver.find_element(By.XPATH, "//span[@class='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 ali-kit_Label__label__1n9sab ali-kit_Label__size-m__1n9sab']").text,
                        'company': 'не известно',
                        'link': link
                    })
                except:
                    x.append({
                        'title': driver.find_element(By.CLASS_NAME, "Product_Name__productTitleText__hntp3").text,
                        'price': driver.find_element(By.CLASS_NAME, "product-price-current").text,
                        'reviews': driver.find_element(By.XPATH, "//span[@class='ali-kit_Base__base__104pa1 ali-kit_Base__default__104pa1 ali-kit_Base__strong__104pa1 ali-kit_Label__label__1n9sab ali-kit_Label__size-m__1n9sab']").text,
                        'company': 'не известно',
                        'link': link
                    })

        print(x)
        total.extend(x)

def save(total):
    with open('parser.csv', 'w', newline='') as ex:
        writer = csv.writer(ex, delimiter=';')
        writer.writerow(['название', 'цена', 'оценка', 'продавец', 'ссылка'])
        for dict in total:
            writer.writerow([dict['title'], dict['price'], dict['reviews'], dict['company'], dict['link']])

def parser():
    domen = input('введите ссылку на Алиэкспресс: ')
    pages = int(input('сколько страниц: '))
    driver = webdriver.Chrome()

    links = []
    for page in range(1, pages + 1):
        link(driver, domen, page, links)

    total = []
    info(driver, links, total)

    save(total)
    os.startfile('parser.csv')

    driver.close()

parser()
