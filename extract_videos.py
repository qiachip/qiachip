import re
import csv
from bs4 import BeautifulSoup

def extract_video_info(html_file):
    """
    从HTML文件中提取视频标题和链接
    """
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    videos = []
    
    # 查找所有视频标题元素
    video_elements = soup.find_all('a', id='video-title')
    
    for video in video_elements:
        title = video.get('aria-label')
        edit_link = video.get('href')
        
        # 从编辑链接中提取视频ID
        video_id_match = re.search(r'video/([\w-]+)/edit', edit_link)
        if video_id_match:
            video_id = video_id_match.group(1)
            # 构建公开观看链接
            public_link = f'https://youtube.com/watch?v={video_id}'
            
            videos.append({
                'title': title,
                'link': public_link
            })
    
    return videos

def save_to_csv(videos, output_file):
    """
    将视频信息保存到CSV文件
    """
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['title', 'link'])
        writer.writeheader()
        writer.writerows(videos)

def main():
    html_file = 'd:\\WorkFiles\\qiachipweb\\1.html'
    output_file = 'd:\\WorkFiles\\qiachipweb\\videoLib.csv'
    
    print(f'正在从 {html_file} 提取视频信息...')
    videos = extract_video_info(html_file)
    print(f'共找到 {len(videos)} 个视频')
    
    save_to_csv(videos, output_file)
    print(f'视频信息已保存到 {output_file}')

if __name__ == '__main__':
    main()