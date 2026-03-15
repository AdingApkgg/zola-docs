import os
import re
import json
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

import time

def get_base_url():
    """从 config.toml 读取 base_url"""
    try:
        with open('config.toml', 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip().startswith('base_url'):
                    # 提取 base_url = "https://..." 中的 URL
                    match = re.search(r'base_url\s*=\s*"([^"]+)"', line)
                    if match:
                        return match.group(1).rstrip('/')
    except Exception as e:
        print(f"Error reading config.toml: {e}")
    return None

def verify_key_accessibility(host, key, max_retries=90, delay=2):
    """验证 Key 文件是否已生效，因为 GitHub Pages 部署有延迟 (默认等待 3 分钟)"""
    url = f"https://{host}/{key}.txt"
    print(f"Verifying key file availability at: {url}")
    
    for i in range(max_retries):
        try:
            # 添加 User-Agent 模拟浏览器，避免被 Cloudflare/GitHub Pages 拦截 (403 Forbidden)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    content = response.read().decode('utf-8').strip()
                    if content == key:
                        print("Key file verification successful!")
                        return True
                    else:
                        print(f"Key file found but content mismatch. Expected {key}, got {content}")
        except urllib.error.HTTPError as e:
            # 只有在第一次和每 5 次重试时打印日志，避免刷屏
            if i == 0 or (i + 1) % 5 == 0:
                print(f"Attempt {i+1}/{max_retries}: Key file not ready yet ({e.code}). Waiting {delay}s...")
        except Exception as e:
            print(f"Attempt {i+1}/{max_retries}: Error checking key file: {e}. Waiting {delay}s...")
        
        time.sleep(delay)
    
    print("Warning: Key file verification timed out. Submitting anyway but might fail.")
    return False

def get_api_key():
    """从 static 目录查找 API Key 文件"""
    static_dir = 'static'
    if not os.path.exists(static_dir):
        print(f"Static directory not found: {static_dir}")
        return None
    
    for filename in os.listdir(static_dir):
        # 查找 32 位 hex 文件名 (IndexNow key 通常是 32 位 hex)
        if filename.endswith('.txt') and len(filename) == 36: # 32 chars + .txt
            key = filename[:-4]
            # 简单验证是否为 hex
            if re.match(r'^[0-9a-fA-F]{32}$', key):
                return key
    return None

def get_urls_from_sitemap(base_url):
    """从 public/sitemap.xml 解析 URL"""
    sitemap_path = 'public/sitemap.xml'
    if not os.path.exists(sitemap_path):
        print(f"Sitemap not found: {sitemap_path}")
        return []
    
    urls = []
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        # namespace usually is http://www.sitemaps.org/schemas/sitemap/0.9
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        
        for url in root.findall('ns:url', namespace):
            loc = url.find('ns:loc', namespace)
            if loc is not None and loc.text:
                url_text = loc.text.strip()
                if url_text.startswith(base_url):
                    urls.append(url_text)
    except Exception as e:
        print(f"Error parsing sitemap: {e}")
    
    return urls

def submit_to_indexnow(host, key, url_list):
    """提交 URL 到 IndexNow"""
    endpoint = "https://api.indexnow.org/indexnow"
    
    data = {
        "host": host,
        "key": key,
        "keyLocation": f"https://{host}/{key}.txt",
        "urlList": url_list
    }
    
    print(f"Submitting {len(url_list)} URLs to IndexNow for host: {host}...")
    
    try:
        json_data = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(endpoint, data=json_data, headers={"Content-Type": "application/json; charset=utf-8"})
        
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print("Success! URLs submitted.")
            else:
                print(f"Failed. Status code: {response.status}")
                print(f"Response: {response.read().decode('utf-8')}")
    except urllib.error.HTTPError as e:
        print(f"HTTP Error submitting to IndexNow: {e.code} {e.reason}")
        print(e.read().decode('utf-8'))
    except Exception as e:
        print(f"Error submitting to IndexNow: {e}")

def main():
    base_url = get_base_url()
    if not base_url:
        print("Could not find base_url in config.toml")
        return

    parsed_url = urlparse(base_url)
    host = parsed_url.netloc

    api_key = get_api_key()
    if not api_key:
        print("Could not find API Key file in static/")
        return
    
    print(f"Found API Key: {api_key}")

    urls = get_urls_from_sitemap(base_url)
    if not urls:
        print("No URLs found in sitemap.")
        return

    # 等待验证文件生效
    verify_key_accessibility(host, api_key)

    # IndexNow limit is 10,000 URLs per request
    submit_to_indexnow(host, api_key, urls)

if __name__ == "__main__":
    main()
