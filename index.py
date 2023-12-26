import httpx
import concurrent.futures

# Made by Sphinx (vzrc)

url = 'https://api.discord.gx.games/v1/direct-fulfillment'
headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0'
}

data = '{"partnerUserId":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}'

# Number of requests to make
num_requests = 10000

def make_request(request_num):
    with httpx.Client() as client:
        response = client.post(url, headers=headers, data=data)
        with open('response_content.txt', 'a', encoding='utf-8') as file:
            file.write(f'https://discord.com/billing/partner-promotions/1180231712274387115/{response.json().get('token')}'+ '\n')

        print(f"Request {request_num + 1} completed.")

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(make_request, range(num_requests))

if __name__ == "__main__":
    main()

print("All requests completed.")
