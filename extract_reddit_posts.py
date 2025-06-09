import re
import csv
from bs4 import BeautifulSoup

def extract_reddit_posts(html_file):
    """
    从HTML文件中提取Reddit帖子标题和链接
    """
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    posts = []
    
    # 查找所有链接元素
    all_links = soup.find_all('a')
    
    # 定义要过滤的关键词列表（导航链接、按钮等）
    filter_keywords = [
        'Skip to', 'Advertise', 'Create post', 'Open inbox', 'Create Post', 'Get a new',
        'SHOP NOW', 'BUY NOW', 'Click to', 'Original link', 'video', 'Buy', 'Login', 'Sign up',
        'Search', 'Menu', 'Home', 'About', 'Contact', 'Privacy', 'Terms', 'Help', 'FAQ',
        'Settings', 'Profile', 'Messages', 'Notifications', 'Chat', 'More', 'Back', 'Next',
        'has been created', 'Click', 'Shop', 'View', 'Download'
    ]
    
    # 定义Reddit帖子URL的特征模式
    reddit_post_patterns = [
        r'/comments/', r'/r/\w+/comments/', r'/\w+/comments/'
    ]
    
    # 定义可能是帖子标题的关键词
    post_title_keywords = [
        'how to', 'guide', 'tutorial', 'manual', 'instruction', 'qiachip', 'remote control',
        'wireless', 'module', 'receiver', 'transmitter', 'switch', 'controller', 'user manual',
        'performance', 'application', 'DIY'
    ]
    
    for link in all_links:
        # 获取链接文本和URL
        title = link.get_text(strip=True)
        url = link.get('href')
        
        # 跳过空标题或空链接
        if not title or not url:
            continue
            
        # 跳过短标题（可能是导航链接）
        if len(title) < 10:
            continue
            
        # 跳过包含过滤关键词的标题
        if any(keyword.lower() in title.lower() for keyword in filter_keywords):
            continue
            
        # 确保链接是完整的URL
        if not url.startswith(('http://', 'https://')):
            if url.startswith('/'):
                url = f'https://www.reddit.com{url}'
            else:
                url = f'https://www.reddit.com/{url}'
        
        # 检查URL是否符合Reddit帖子的特征
        is_reddit_post = False
        for pattern in reddit_post_patterns:
            if re.search(pattern, url):
                is_reddit_post = True
                break
                
        # 如果URL不符合Reddit帖子特征，但标题看起来像帖子标题，也添加
        if not is_reddit_post:
            if len(title) > 20 and any(keyword.lower() in title.lower() for keyword in post_title_keywords):
                is_reddit_post = True
            
        if is_reddit_post:
            # 清理标题中的多余空格
            clean_title = re.sub(r'\s+', ' ', title).strip()
            
            posts.append({
                'title': clean_title,
                'link': url
            })
    
    # 去除重复项
    unique_posts = []
    seen_titles = set()
    
    for post in posts:
        if post['title'] not in seen_titles:
            seen_titles.add(post['title'])
            unique_posts.append(post)
    
    return unique_posts

def save_to_csv(posts, output_file):
    """
    将帖子信息保存到CSV文件
    """
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'link'])
        writer.writeheader()
        writer.writerows(posts)

def main():
    html_file = 'd:\\WorkFiles\\qiachipweb\\comunityPosts.html'
    output_file = 'd:\\WorkFiles\\qiachipweb\\redditPosts.csv'
    
    print(f'正在从 {html_file} 提取Reddit帖子信息...')
    posts = extract_reddit_posts(html_file)
    print(f'共找到 {len(posts)} 个帖子')
    
    save_to_csv(posts, output_file)
    print(f'帖子信息已保存到 {output_file}')

if __name__ == '__main__':
    main()