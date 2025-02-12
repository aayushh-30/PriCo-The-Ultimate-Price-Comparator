from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def test(request):
    return HttpResponse("This is Testing")

def managing_search(search):
    search = search.strip()
    return search.replace(' ', "%20"), search.replace(' ', "+")

def getting_data(search):
    flipkart_query, amazon_query = managing_search(search)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
    try:
        flipkart_url = f"https://www.flipkart.com/search?q={flipkart_query}"
        amazon_url = f"https://www.amazon.in/s?k={amazon_query}"

        flipkart_response = requests.get(flipkart_url, headers=headers)
        amazon_response = requests.get(amazon_url, headers=headers)
        return flipkart_response.text, amazon_response.text
    except requests.exceptions.RequestException as e:
        return str(e), str(e)

def flipkart_scraping(html):
    soup = BeautifulSoup(html, "lxml")
    Flipkart_Product_Names = soup.find_all("div", class_="KzDlHZ")
    Flipkart_Product_Prices = soup.find_all("div", class_="Nx9bqj _4b5DiR")
    Flipkart_Product_Ratings = soup.find_all("div", class_="XQDdHH")
    Flipkart_Product_Pictures = soup.find_all("img", class_="DByuf4")
    Flipkart_Product_Links = soup.find_all("a", class_="CGtC98")
    
    products = []
    for i in range(len(Flipkart_Product_Names)):
        name = Flipkart_Product_Names[i].text.strip() if i < len(Flipkart_Product_Names) else "N/A"
        price = Flipkart_Product_Prices[i].text.strip() if i < len(Flipkart_Product_Prices) else "N/A"
        rating = Flipkart_Product_Ratings[i].text.strip() if i < len(Flipkart_Product_Ratings) else "N/A"
        image = Flipkart_Product_Pictures[i]['src'] if i < len(Flipkart_Product_Pictures) else "N/A"
        link = "https://www.flipkart.com" + Flipkart_Product_Links[i]['href'] if i < len(Flipkart_Product_Links) else "N/A"
        
        products.append((name, price, rating, image, link))
    return products

def amazon_scraping(html):
    soup = BeautifulSoup(html, "lxml")
    Amazon_Product_Names = soup.find_all("h2", class_="a-size-medium")
    Amazon_Product_Prices = soup.find_all("span", class_="a-price-whole")
    Amazon_Product_Ratings = soup.find_all("span", class_="a-icon-alt")
    Amazon_Product_Pictures = soup.find_all("img", class_="s-image")
    Amazon_Product_Links = soup.find_all("a", class_="a-link-normal s-no-outline")
    
    products = []
    for i in range(len(Amazon_Product_Names)):
        name = Amazon_Product_Names[i].text.strip() if i < len(Amazon_Product_Names) else "N/A"
        price = Amazon_Product_Prices[i].text.strip() if i < len(Amazon_Product_Prices) else "N/A"
        rating = Amazon_Product_Ratings[i].text.strip() if i < len(Amazon_Product_Ratings) else "N/A"
        image = Amazon_Product_Pictures[i]['src'] if i < len(Amazon_Product_Pictures) else "N/A"
        link = "https://www.amazon.in" + Amazon_Product_Links[i]['href'] if i < len(Amazon_Product_Links) else "N/A"
        
        products.append((name, price, rating, image, link))
    return products



def Search(request):
    product_name = request.GET.get("q", "laptop")
    flipkart_html, amazon_html = getting_data(product_name)
    flipkart_results = flipkart_scraping(flipkart_html)
    amazon_results = amazon_scraping(amazon_html)

    return render(request, "results.html", {
        "flipkart_products": flipkart_results,
        "amazon_products": amazon_results,
        "search_query": product_name
    })
