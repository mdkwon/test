from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests_html import HTMLSession
from time import sleep
import itertools

def rockauto(part_input_query, make_query, year_query, model_query):
    master_list = []
    session = HTMLSession()
    driver = webdriver.Chrome("C:/Users/Kwon/Downloads/chromedriver.exe")
    driver_autozone = webdriver.Chrome("C:/Users/Kwon/Downloads/chromedriver.exe")
    driver_ebay = webdriver.Chrome("C:/Users/Kwon/Downloads/chromedriver.exe")
    driver_partsgeek = webdriver.Chrome("C:/Users/Kwon/Downloads/chromedriver.exe")
    driver_google_shopping = webdriver.Chrome("C:/Users/Kwon/Downloads/chromedriver.exe")
    r = session.get('http://google.com/search?q=' + part_input_query)
    sleep(1)
    corrected_query = r.html.find('#fprsl')
    if not corrected_query:
        google_corrected_query = part_input_query
    else:
        google_corrected_query = corrected_query[0].text
    driver.get('http://rockauto.com/en/catalog' + make_query)
    driver_autozone.get('https://cse.google.com/cse?cx=007564039463339945667:uilu0za88tz')
    driver_ebay.get('https://www.google.com/search?tbm=shop&psb=1&q=' + year_query + '+' + make_query + '+' + model_query + '+' + google_corrected_query + '&tbs=vw:l,mr:1,merchagg:g6296794')
    driver_partsgeek.get('https://www.google.com/search?tbm=shop&psb=1&q=' + year_query + '+' + make_query + '+' + model_query + '+' + google_corrected_query + '&tbas=0&tbs=vw:l,mr:1,merchagg:m4169763')
    driver_google_shopping.get('https://www.google.com/search?tbm=shop&psb=1&q=' + year_query + '+' + make_query + '+' + model_query + '+' + google_corrected_query)

    rockauto_search_box = driver.find_element_by_id("topsearchinput[input]")
    rockauto_search_box.send_keys(year_query + '+' + make_query + '+' + model_query + '+' + google_corrected_query)
    rockauto_search_box.send_keys(Keys.ENTER)
    google_cs_searchbox = driver_autozone.find_element_by_id('gsc-i-id1')
    google_cs_searchbox.send_keys(year_query + '+' + make_query + '+' + model_query + '+' + google_corrected_query)
    google_cs_searchbox.send_keys(Keys.ENTER)
    google_cs_result_link_selector = driver_autozone.find_elements_by_css_selector('a.gs-title')
    for i in google_cs_result_link_selector:
        if i.get_attribute('textContent').lower() == year_query.lower() + ' ' + make_query.lower() + ' ' + model_query.lower() + ' ' + google_corrected_query.lower():
            autozone_link = i.get_attribute('href')
            driver_autozone.get(autozone_link)
            sleep(2)
            autozone_items = driver_autozone.find_elements_by_css_selector('div.shelfItem.categorizedShelfItem ')
            if autozone_items:
                for i in autozone_items:
                    temp_dict = {}
                    price_element = i.find_element_by_css_selector('strong').get_attribute('textContent')
                    temp_dict['price'] = price_element

                    image_link_element = i.find_element_by_css_selector('img.lazy').get_attribute('src')
                    temp_dict['image_link'] = image_link_element

                    manufacturer = i.find_element_by_css_selector('span.prodName').get_attribute('textContent')

                    list_text = ' '.join(
                        i.find_element_by_css_selector('li.prodNotes').get_attribute('textContent').split())
                    temp_dict['list_text'] = list_text

                    part_href = i.find_element_by_css_selector('.prodImg').get_attribute('href')
                    temp_dict['part_href'] = part_href

                    part_number = i.find_element_by_xpath(
                        '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[6]/div[1]/div[2]/ul/li[2]/em/span').get_attribute(
                        'textContent')
                    temp_dict['manufacturer+part_number'] = manufacturer + ' ' + part_number

                    temp_dict['website'] = 'autozone'

                    temp_dict['corrected_query'] = year_query + ' ' + make_query + ' ' + model_query + ' ' + google_corrected_query

                    master_list.append(temp_dict)

            break


    container_row1 = driver.find_elements_by_css_selector('tbody.listing-inner.altrow-a-1')
    container_row0 = driver.find_elements_by_css_selector('tbody.listing-inner.altrow-a-0')
    if container_row1 or container_row0:
        for i in itertools.chain(container_row1, container_row0):
            temp_dict = {}
            price_element = i.find_element_by_css_selector('span.ra-formatted-amount.listing-total').get_attribute(
                'textContent')
            temp_dict['price'] = price_element

            image_link_element = i.find_element_by_css_selector(
                'img.listing-inline-image.listing-inline-image-thumb.listing-inline-image-border').get_attribute('src')
            temp_dict['image_link'] = image_link_element

            manufacturer = i.find_element_by_css_selector('span.listing-final-manufacturer').get_attribute('textContent')

            list_text = i.find_element_by_css_selector('div.listing-text-row').get_attribute('textContent')
            temp_dict['list_text'] = list_text

            part_number = i.find_element_by_css_selector(
                'span.listing-final-partnumber.as-link-if-js.buyers-guide-color').get_attribute('textContent')
            temp_dict['manufacturer+part_number'] = manufacturer + ' ' + part_number

            part_href = i.find_element_by_css_selector('.ra-btn.ra-btn-moreinfo').get_attribute('href')
            temp_dict['part_href'] = part_href

            temp_dict['website'] = 'rockauto'

            temp_dict[
                'corrected_query'] = year_query + ' ' + make_query + ' ' + model_query + ' ' + google_corrected_query

            master_list.append(temp_dict)

    ebay_result_elements = driver_ebay.find_elements_by_css_selector('.sh-dlr__list-result')
    partsgeek_result_elements = driver_partsgeek.find_elements_by_css_selector('.sh-dlr__list-result')
    google_shopping_elements = driver_google_shopping.find_elements_by_css_selector('.sh-dlr__list-result')

    for i in itertools.chain(ebay_result_elements, partsgeek_result_elements, google_shopping_elements):
        temp_dict = {}
        price_element = i.find_element_by_css_selector('.Nr22bf').get_attribute('textContent')[:-1]
        temp_dict['price'] = price_element

        image_link_element = i.find_element_by_css_selector('.TL92Hc').get_attribute('src')
        temp_dict['image_link'] = image_link_element

        manufacturer_part_number = i.find_element_by_css_selector('.mASaeb').get_attribute('textContent')
        temp_dict['manufacturer+part_number'] = manufacturer_part_number

        list_text = i.find_element_by_css_selector('.hBUZL').get_attribute('textContent')
        temp_dict['list_text'] = list_text

        part_href = i.find_elements_by_css_selector('.mASaeb').get_attribute('href')
        temp_dict['part_href'] = part_href

        website = i.find_element_by_css_selector('.shntl.hy2WroIfzrX__merchant-name').get_attribute('textContent')
        temp_dict['website'] = website

        temp_dict['corrected_query'] = year_query + ' ' + make_query + ' ' + model_query + ' ' + google_corrected_query

        master_list.append(temp_dict)

    return master_list
