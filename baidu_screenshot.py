from playwright.sync_api import sync_playwright
import os

def capture_baidu_screenshot():
    # 确保截图目录存在
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    
    with sync_playwright() as p:
        # 启动浏览器
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 导航到百度首页
        page.goto("https://www.baidu.com")
        
        # 等待页面加载完成
        page.wait_for_load_state("networkidle")
        
        # 截图并保存
        screenshot_path = "screenshots/baidu_homepage.png"
        page.screenshot(path=screenshot_path, full_page=True)
        
        # 关闭浏览器
        browser.close()
        
        print(f"截图已保存至: {os.path.abspath(screenshot_path)}")
        return os.path.abspath(screenshot_path)

if __name__ == "__main__":
    capture_baidu_screenshot()